"""GUIDE Phần 1 - Định nghĩa subagent (tác tử con).   >>> SINH VIÊN CÀI ĐẶT <<<

Pseudo-code: guides/pseudocode/02_subagents.md
Kiểm tra:    pytest tests/test_02_agent.py
"""


def get_subagents() -> list[dict]:
    """Trả về danh sách subagent (ít nhất 2, tên khác nhau).

    Mỗi phần tử là một dict có các khóa bắt buộc:
      "name":          tên duy nhất (chữ thường, có thể có dấu gạch ngang)
      "description":   khi nào tác tử chính nên giao việc cho subagent này (viết như một hướng dẫn hành động)
      "system_prompt": chỉ dẫn cho subagent
    Gợi ý vai trò: explorer (đọc và báo cáo), implementer (thực hiện), reviewer (kiểm tra độc lập).
    """
    return [
        {
            "name": "explorer",
            "description": (
                "Use proactively at the beginning of a task to inspect the workspace, "
                "read task instructions, explore file structures, examine schemas, docstrings, "
                "sample data, or error logs. Do not edit files or create artifacts; return a clear, factual summary."
            ),
            "system_prompt": (
                "You are an exploration subagent. Your job is to thoroughly inspect files in workspace/, "
                "read relevant code, data, logs, and docstrings, and report objective findings and facts. "
                "Do not create or edit files in workspace/."
            ),
        },
        {
            "name": "implementer",
            "description": (
                "Use when executing changes, modifying code, generating cleaned data or output files in workspace/, "
                "and executing verification scripts or unit tests."
            ),
            "system_prompt": (
                "You are an implementation subagent. Your job is to implement code fixes or data transformations "
                "in workspace/ strictly following task requirements and conventions. "
                "Verify your work using the shell, run relevant python scripts or tests, and report results."
            ),
        },
        {
            "name": "reviewer",
            "description": (
                "Use after implementation to independently audit results against task requirements, "
                "output schemas, edge cases, and house rules. Do not modify files; return a verification report."
            ),
            "system_prompt": (
                "You are an independent review and QA subagent. Your job is to check the modified workspace/, "
                "verify output file formats, edge cases, and compliance with all instructions and conventions. "
                "Do not edit any files. Report any discrepancies or confirm full compliance."
            ),
        },
    ]

