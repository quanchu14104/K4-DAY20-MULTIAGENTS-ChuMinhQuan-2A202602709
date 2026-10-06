"""GUIDE Phần 3 - Người tuyển chọn skill (skill curator): tự viết skill từ các lần chạy thất bại.   >>> SINH VIÊN CÀI ĐẶT curate_skills <<<

Pseudo-code: guides/pseudocode/04_curator.md
Kiểm tra:    pytest tests/test_04_curator.py
Chạy thật:   python -m lab.curator
"""
import re
import json
from pathlib import Path

from .model import make_model
from .tasks import ROOT, eval_markers   # có sẵn: định danh của tác vụ đánh giá, tính lúc chạy

# ---- CÓ SẴN, KHÔNG SỬA: kiểm tra và tách khối skill (phần dễ sai và liên quan bảo mật) ----------------
SAFE_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def validate_skill(text: str, expected_name: str | None = None) -> list[str]:
    """Kiểm tra nội dung một SKILL.md. Trả về danh sách vấn đề (rỗng = hợp lệ).

    Quy tắc: có khối YAML frontmatter; `name` chữ thường/số/gạch ngang (tối đa 64 ký tự) và bằng `expected_name`
    nếu được truyền; có `description` (tối đa 1024 ký tự); phần thân tối đa 80 dòng; không chứa chuỗi nào của
    `eval_markers()`. Quy tắc về `name` cũng là biện pháp bảo mật: tên khối do LLM sinh ra được dùng để tạo
    đường dẫn, nên `../evil` không được lọt qua.
    """
    problems = []
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text.strip() + "\n", re.S)
    if not m:
        return ["missing YAML frontmatter"]
    front, body = m.groups()
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    n = name.group(1).strip() if name else ""
    if not SAFE_NAME.fullmatch(n) or len(n) > 64:
        problems.append("invalid name")
    elif expected_name is not None and n != expected_name:
        problems.append("name differs from the block name")
    if not desc or len(desc.group(1).strip()) > 1024:
        problems.append("missing or too long description")
    if len(body.strip().splitlines()) > 80:
        problems.append("body longer than 80 lines")
    low = text.lower()
    for marker in eval_markers():
        if marker in low:
            problems.append(f"mentions evaluation material: {marker}")
    return problems


def parse_skill_blocks(reply: str) -> list[tuple[str, str]]:
    """Tách câu trả lời của LLM thành danh sách (name, nội dung SKILL.md).

    Khuôn dạng: `=== SKILL: <name> ===` ... `=== END ===`. Một khối kết thúc ở điểm nào đến trước trong ba điểm:
    `=== END ===`, tiêu đề `=== SKILL:` kế tiếp, hoặc cuối văn bản (LLM đôi khi quên dòng END).
    """
    pattern = re.compile(r"^=== SKILL: (\S+) ===[ \t]*\n(.*?)(?=^=== END ===|^=== SKILL: |\Z)", re.S | re.M)
    return [(name, text.strip()) for name, text in pattern.findall(str(reply))]
# --------------------------------------------------------------------------------------------------


def curate_skills(results_dir="results", source_condition="baseline", out_dir=None, model=None, max_skills: int = 3) -> list[Path]:
    """Đọc các lần chạy của TÁC VỤ HỌC (role == "learn") trong `source_condition`, nhờ LLM viết skill, ghi file.

    Các bước: nạp run.json + trace.md -> (nếu không có check nào thất bại: in cảnh báo và trả về [] mà KHÔNG gọi LLM)
    -> dựng prompt -> model.invoke(prompt) -> parse_skill_blocks -> validate_skill(text, expected_name=name)
    -> ghi `<out_dir>/<name>/SKILL.md`. Mặc định `out_dir` = <gốc lab>/skills/auto (dùng `ROOT` từ lab.tasks).
    Giữ tối đa `max_skills` skill hợp lệ; skill không hợp lệ bị bỏ qua.
    Prompt chứa, với mỗi check thất bại, TÊN và trường `detail` (lời nhận xét của bot đánh giá: phát biểu quy tắc bị vi phạm)
    cùng phần cuối của vết (trace). Với tác vụ học, `detail` chỉ phát biểu quy tắc, không chứa đáp án.
    Tuyệt đối KHÔNG đưa dữ liệu của tác vụ đánh giá (role == "eval") vào prompt.
    model mặc định: make_model() (lab.model).
    Trả về: danh sách đường dẫn SKILL.md đã ghi.
    """
    if out_dir is None:
        out_dir = ROOT / "skills" / "auto"
    else:
        out_dir = Path(out_dir)

    source_path = Path(results_dir) / source_condition
    if not source_path.exists():
        print("Cảnh báo: không có check thất bại ở tác vụ học")
        return []

    learning_runs = []
    total_failed_checks = 0

    for d in sorted(source_path.iterdir()):
        if not d.is_dir():
            continue
        run_file = d / "run.json"
        if not run_file.exists():
            continue
        try:
            data = json.loads(run_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        if data.get("role") != "learn":
            continue

        checks = data.get("checks", [])
        failed = [c for c in checks if not c.get("passed", False)]
        if not failed:
            continue

        total_failed_checks += len(failed)
        trace_file = d / "trace.md"
        trace_text = ""
        if trace_file.exists():
            try:
                trace_text = trace_file.read_text(encoding="utf-8")[-6000:]
            except Exception:
                trace_text = ""

        learning_runs.append({
            "task": data.get("task", d.name),
            "failed": failed,
            "trace": trace_text,
        })

    if total_failed_checks == 0 or not learning_runs:
        print("Cảnh báo: không có check thất bại ở tác vụ học")
        return []

    run_summaries = []
    for run in learning_runs:
        failures_desc = "\n".join(
            f"  - Check: {c.get('name', 'unknown')} | Feedback: {c.get('detail', '')}"
            for c in run["failed"]
        )
        summary = (
            f"Task: {run['task']}\n"
            f"Failed checks:\n{failures_desc}\n"
        )
        if run["trace"]:
            summary += f"Recent trace:\n{run['trace']}\n"
        run_summaries.append(summary)

    prompt = (
        "You are an expert software engineer curating procedural skills for an AI agent.\n"
        "Below are failed checks (with checker comments/rules) and execution traces from training tasks.\n"
        f"Identify general procedural mistakes and write up to {max_skills} concise skills to prevent them on new tasks of similar types.\n\n"
        "Rules:\n"
        "- Skills must be general: do not mention specific task IDs, task-specific file names, or specific answers/numbers.\n"
        "- Each skill must have YAML frontmatter with `name` (lowercase, letters/digits/dashes only, max 64 chars) and `description` (one sentence: when to use it, max 1024 chars), followed by max 40 lines of imperative guidance/checklists.\n"
        "- Format each skill exactly as:\n"
        "=== SKILL: <name> ===\n"
        "---\n"
        "name: <name>\n"
        "description: <when to use>\n"
        "---\n"
        "<content>\n"
        "=== END ===\n\n"
        "Failures and traces from learning runs:\n"
        + "\n---\n".join(run_summaries)
    )

    if model is None:
        model = make_model()

    response = model.invoke(prompt)
    reply = getattr(response, "content", str(response))

    written_paths = []
    out_dir.mkdir(parents=True, exist_ok=True)
    blocks = parse_skill_blocks(reply)
    for name, content in blocks:
        if len(written_paths) >= max_skills:
            break
        problems = validate_skill(content, expected_name=name)
        if problems:
            continue
        skill_dir = out_dir / name
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_path = skill_dir / "SKILL.md"
        skill_path.write_text(content.strip() + "\n", encoding="utf-8")
        written_paths.append(skill_path)

    return written_paths


if __name__ == "__main__":
    for p in curate_skills():
        print("wrote", p)
