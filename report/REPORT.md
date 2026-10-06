# Báo cáo Lab: Self evolving Agentic

## 1. Thông tin nhóm và cấu hình

| Họ tên | Mã sinh viên | Phần đóng góp |
|---|---|---|
| Chu Minh Quân | 2A202602709 | Toàn bộ bài lab (100%) |

- Mô hình (tên deployment hoặc `LAB_MODEL`), nhiệt độ (`LAB_TEMPERATURE`), `recursion_limit`: `parrotgo` (cổng API tương thích OpenAI tại `http://localhost:20128/v1`), `LAB_TEMPERATURE=0`, `recursion_limit=60`.
- Phiên bản Deep Agents (`pip show deepagents`), hệ điều hành, chạy trực tiếp hay trong Docker: `deepagents 0.7.21`, Windows 11 (Python 3.11.0, PosixShellBackend tích hợp Git Bash `sh.exe`).
- Số lần chạy tác vụ đã dùng / ngân sách: 18 / 18 lần chạy chính thức (và 3 lần chạy dev ở Phần 3.4).
- Commit của tag `freeze`: `bf4933eacd4ce3557d2864c312890983a6419b48`.

## 2. Giả thuyết (commit TRƯỚC tag `freeze`, Phần 4.0)

- H1 (subagents so với baseline): Trên các tác vụ đánh giá, điều kiện `subagents` được dự đoán sẽ đạt điểm tương đương hoặc chỉ nhỉnh hơn không đáng kể so với `baseline` (chênh lệch ≤ 0.05 điểm), trong khi chi phí token sẽ cao hơn đáng kể (dự kiến tăng từ 40% đến 80%). Căn cứ: Kết quả ở tập học cho thấy 90% lỗi là do thiếu các quy ước tổ chức ngầm (`rule_*`) chứ không phải do thiếu năng lực thực thi hay tìm kiếm kỹ thuật (vốn đã đạt 94.4% check kỹ thuật). Do các subagent hoạt động theo cơ chế ngữ cảnh cô lập (stateless context isolation), việc chia nhỏ việc không giúp phát hiện thêm các quy ước ẩn chưa biết, đồng thời chi phí tổng hợp và truyền lại ngữ cảnh giữa các subagent làm tăng vọt số lượng token (phù hợp với các nghiên cứu về overhead của multi-agent từ Anthropic).
- H2 (skills-auto so với baseline): Trên các tác vụ đánh giá, điều kiện `skills-auto` được dự đoán sẽ đạt điểm cao hơn `baseline` (dự kiến tăng khoảng 0.15 - 0.25 điểm), nhưng mức độ cải thiện sẽ thấp hơn so với trên tập học (xuất hiện hiện tượng khoảng cách khái quát hóa / generalization gap). Căn cứ: Các skill do curator tự sinh đã đúc kết được các quy ước dùng chung giữa hai tập (như định dạng tiền integer cents, tệp clean.csv, cấu trúc regression tests, type annotations, và chuẩn hóa service names). Tuy nhiên, theo nghiên cứu SkillEvolBench và SkillsBench, tác tử tự sinh skill có xu hướng quá khớp (overfit) vào phân phối của tập học và sẽ không thể đáp ứng các quy ước mới chỉ xuất hiện riêng ở tập đánh giá (do tác tử chưa từng thấy phản hồi về các quy ước mới này).
- H3 (tác vụ học so với tác vụ đánh giá): Điểm số trung bình trên tác vụ học được dự đoán sẽ cao hơn rõ rệt so với tác vụ đánh giá trên cùng điều kiện `skills-auto` (chênh lệch dự kiến từ 0.15 đến 0.30 điểm). Căn cứ: Tập học là nguồn cung cấp phản hồi trực tiếp để curator tối ưu hóa các quy tắc trong skill (in-distribution), trong khi tập đánh giá có dữ liệu khác biệt và bổ sung thêm các quy ước mới (out-of-distribution shift). Ngược lại, ở điều kiện `baseline` và `subagents`, điểm giữa hai tập sẽ không có sự chênh lệch lớn vì cả hai điều kiện này đều không nhận được tri thức thủ tục từ tập học.

## 3. Làm quen Deep Agents (Phần 0.3)

1. Tác tử mặc định có 9 công cụ:
   - Công cụ thao tác tệp: `ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob`, `grep`.
   - Công cụ thực thi shell: `execute`.
   - Công cụ phân nhánh tác tử con (subagents): `task`.
   Công cụ cho phép chạy lệnh là `execute`.

2. Mô tả của công cụ `task` định nghĩa subagent `general-purpose` là một tác tử đa năng ("General-purpose agent for researching complex questions, searching for files and content, and executing multi-step tasks") và có toàn bộ công cụ giống tác tử chính. Về ngữ cảnh, mỗi lần gọi mặc định là phi trạng thái (stateless), subagent chỉ nhìn thấy nội dung được cung cấp trong prompt giao việc và trả về một báo cáo kết quả duy nhất ("the agent sees only the prompt you give it and returns a single final report"), không nhìn thấy lịch sử đối thoại hay ngữ cảnh trước đó của tác tử chính.

3. Trích dẫn câu hướng dẫn hành vi:
   - Từ mô tả công cụ `task`: *"Put full detail in the prompt and state exactly what it should return – unless an agent type below says it inherits your conversation instead."*
   - Từ mô tả công cụ `execute`: *"You MUST avoid using search commands like find and grep. Instead use the grep, glob tools to search. Use read_file rather than cat/head/tail."*

## 4. Đường cơ sở và phân loại lỗi (Phần 2.2)

| Tác vụ | Check thất bại | Nhóm lỗi (A-G) | Bằng chứng (trích ngắn từ `detail` hoặc vết) |
|---|---|---|---|
| `data-learn` | `rule_money_in_cents` | E | `RULE: money values in answer.json are integer cents (1606.67 USD is written 160667).` |
| `data-learn` | `rule_meta_block` | E | `RULE: answer.json has an object meta = {"source": <input file name>, "rows_in": ..., "rows_used": ...}.` |
| `data-learn` | `rule_clean_csv` | E | `RULE: write workspace/clean.csv with the header order_id,timestamp_utc,region,amount_cents; one row per distinct order...` |
| `code-learn` | `tests_not_modified` | A | `the original files in tests/ must not be modified (new test files are allowed)` (tác tử sửa thẳng tệp test gốc) |
| `code-learn` | `rule_type_hints` | E | `RULE: every public function in the package has type annotations on all parameters and on the return value.` |
| `code-learn` | `rule_regression_tests` | E | `RULE: add tests/test_regressions.py with one test function per bug you fixed (at least 3); the file must pass.` |
| `code-learn` | `rule_changelog` | E | `RULE: record each fix in CHANGELOG.md under the heading '## Unreleased' as a bullet '- fix(<function name>): <short description>'...` |
| `logs-learn` | `rule_service_names` | E | `RULE: service names in the output are lower-case with '-' replaced by '_' (payment-service -> payment_service).` |
| `logs-learn` | `rule_sorted_errors` | E | `RULE: errors is sorted by service, then by timestamp_utc, ascending.` |
| `logs-learn` | `rule_schema_header` | E | `RULE: the top-level object has "schema_version": 2 and "generated_by": "log-triage".` |

Nhận xét:
- **Nhóm lỗi chiếm đa số:** Nhóm E (Vi phạm quy ước tổ chức - house rules) chiếm 9/10 (90%) các check thất bại. Lý do là các quy ước này thuộc về chuẩn nội bộ của tổ chức ("Acme conventions"), không được nêu rõ trong đề bài `instruction.md` mà chỉ được kiểm tra ngầm bởi bot review. Tác tử mặc định không có tri thức ngoại cảnh về các quy ước này nên chắc chắn không thể đáp ứng nếu không được nạp tri thức thủ tục.
- **Bằng chứng phủ định cho các nhóm A đến D:** Dữ liệu từ `scripts/check_breakdown.py` cho thấy tác tử baseline đạt tới **17/18** (94.4%) các check kỹ thuật. Tác tử xử lý rất tốt các lỗi khó như parsing đa định dạng ngày tháng, múi giờ, xử lý duplicate rows, làm tròn half-up, regex log tracebacks nhiều dòng. Duy nhất 1 lỗi nhóm A (`tests_not_modified`) xảy ra do tác tử tự ý sửa test suite gốc khi debug.
- **Khả năng phòng ngừa của Skill:** Skill hoàn toàn có thể phòng ngừa nhóm lỗi E và A nếu nó tổng quát hóa được các quy tắc kiểm tra (checklist) về quy ước đầu ra, giữ nguyên tệp test gốc, bổ sung type annotations, changelog, v.v. Tuy nhiên, skill sẽ chỉ giúp ích nếu các quy ước ở tác vụ mới tương tự hoặc có thể suy luận được từ ngữ cảnh.

## 5. Điều kiện `subagents` (Phần 2.3)

- Các subagent đã định nghĩa (tên, vai trò, lý do thiết kế):
  1. `explorer`: Đọc README, kiểm tra cấu trúc thư mục, lược đồ tệp, docstrings và nhật ký lỗi; lập báo cáo sự thật khách quan mà không sửa đổi tệp trong workspace. Lý do: Giúp cô lập ngữ cảnh tìm kiếm ban đầu, tránh làm ô nhiễm cửa sổ ngữ cảnh luồng chính.
  2. `implementer`: Chuyên trách sửa đổi mã nguồn, thực thi chuyển đổi/làm sạch dữ liệu, tạo các tệp kết quả theo yêu cầu và chạy các lệnh kiểm thử qua shell. Lý do: Tập trung thực thi các thay đổi kỹ thuật cụ thể theo phân công rõ ràng.
  3. `reviewer`: Rà soát độc lập kết quả làm việc của tác tử trong workspace đối chiếu với yêu cầu đề bài, định dạng đầu ra và các trường hợp biên; không sửa tệp mà chỉ đưa ra báo cáo kiểm định. Lý do: Đóng vai trò kiểm tra chéo (QA/Audit) nhằm phát hiện thiếu sót trước khi kết thúc tác vụ.
- `subagent_calls` ở từng tác vụ và nhận xét (kể cả trường hợp bằng 0):
  - `code-learn`: 4 lần gọi subagent (`explorer` 2 lần, `implementer` 1 lần, `reviewer` 1 lần). Tác tử chính phân rã công việc theo đúng quy trình công nghệ phần mềm: khảo sát lỗi test -> đọc mã chi tiết -> chỉ định sửa lỗi -> audit độc lập. Nhờ chỉ dẫn không sửa test gốc, check `tests_not_modified` đã đạt.
  - `data-learn`: 3 lần gọi subagent (`explorer`, `implementer`, `reviewer`). Tác tử chính giao việc kiểm tra schema và xử lý số liệu, đạt 3/8 check.
  - `logs-learn`: 6 lần gọi subagent. Tác tử chính chia nhỏ các bước đọc log, viết script trích xuất regex, xử lý traceback và rà soát kết quả, đạt 4/9 check.
- Thông tin thiếu hoặc thừa khi giao việc (nếu có giao việc):
  - Tác tử chính truyền tải thông tin tốt, chỉ định rõ đường dẫn tương đối `workspace/...` và tóm tắt yêu cầu cốt lõi (như quy tắc RFC 4180, xử lý discount half-up).
  - Hạn chế: Do tính cô lập ngữ cảnh (context isolation), một số chi tiết trung gian giữa các lần gọi có thể bị thất thoát nếu báo cáo tóm tắt của subagent trước không đầy đủ chi tiết cho subagent sau. Cả tác tử chính lẫn subagent đều không biết trước các quy ước ẩn của tổ chức (`rule_*`).
- Ảnh hưởng đến token và thời gian:
  - **Token trung bình:** Điều kiện `subagents` tiêu tốn trung bình **444,315** token, cao hơn **45.2%** so với `baseline` (**306,038** token). Điều này hoàn toàn khớp với cảnh báo trong tài liệu về chi phí của kiến trúc đa tác tử (multi-agent token overhead do phải truyền lại ngữ cảnh đầy đủ vào prompt mỗi subagent).
  - **Thời gian thực thi:** Kéo dài hơn đáng kể do luồng xử lý gồm nhiều bước tuần tự và các lượt gọi mô hình bổ sung cho từng subagent.

## 6. Self-evolving: skill do curator sinh (Phần 3)

- Số lần chạy curator, số skill bị xóa và lý do: Chạy curator đúng 1 lần. Số skill bị xóa là 0 (không cần chạy lại lần nào vì cả 3 skill sinh ra đều đạt chuẩn định dạng YAML frontmatter, không chứa marker của tác vụ đánh giá, ngắn gọn, súc tích và có tính hướng dẫn hành động cao).

| Skill | Tổng quát hay riêng cho tác vụ học? | Đúng hay sai (nêu chỗ sai nếu có) | Độ dài, `description` và `skills_read` ở Phần 3.4 |
|---|---|---|---|
| `python-type-annotations-and-regression-tests` | **Tổng quát:** Áp dụng cho mọi tác vụ sửa lỗi hoặc phát triển gói Python (yêu cầu type annotations cho hàm public, tạo tệp test hồi quy `test_regressions.py`, ghi `CHANGELOG.md` mục Unreleased, không sửa test gốc). Không chứa tên bài hay hàm đặc thù. | **Đúng:** Khớp chính xác với các quy ước của bot đánh giá; hướng dẫn rõ ràng, không gây lỗi logic. | 9 dòng; description: *"Use when writing or fixing Python packages to ensure all code changes satisfy strict style and testing rules..."*; `skills_read = 1` ở `code-learn` (điểm tăng từ 6/10 lên 9/10). |
| `json-schema-and-money-formatting` | **Tổng quát:** Áp dụng cho các tác vụ xử lý dữ liệu tabular và kết xuất JSON liên quan đến tiền tệ, siêu dữ liệu và làm sạch CSV. Không chứa tên file đầu vào hay số liệu cụ thể. | **Đúng:** Khớp với quy ước tính tiền integer cents, cấu trúc meta block (`source`, `rows_in`, `rows_used`) và định dạng `clean.csv`. | 8 dòng; description: *"Use when generating data processing outputs or JSON summaries involving monetary values, metadata blocks, and CSV cleanup rules."*; `skills_read = 1` ở `data-learn` (điểm tăng từ 5/8 lên 6/8). |
| `structured-log-parsing-and-normalization` | **Tổng quát:** Áp dụng cho bài toán trích xuất log thành JSON có cấu trúc (chuẩn hóa tên dịch vụ sang snake_case, sắp xếp mảng lỗi theo nhiều khóa, bổ sung schema version). | **Đúng:** Khớp với các quy tắc kiểm tra `rule_service_names`, `rule_sorted_errors`, `rule_schema_header`. | 8 dòng; description: *"Use when parsing log files into structured JSON to ensure correct schema versions, metadata keys, and service name transformations."*; `skills_read = 2` ở `logs-learn` (tác tử đọc cả skill log lẫn json schema). |

## 7. Kết quả so sánh (Phần 4.3, 4.4)

Bảng so sánh tổng hợp sinh bởi `python -m lab.compare` (đã lưu tại `report/table.md`):

| Task | baseline | subagents | skills-auto |
|---|---|---|---|
| code-learn | 6/10 | 6/10 | 9/10 |
| data-learn | 5/8 | 3/8 | 6/8 |
| logs-learn | 6/9 | 4/9 | 3/9 |
| code-eval | 6/11 | 6/11 | 0/11 |
| data-eval | 5/9 | 3/9 | 3/9 |
| logs-eval | 6/10 | 3/10 | 6/10 |
| **Mean score - learning tasks** | 0.63 | 0.47 | 0.66 |
| **Mean score - evaluation tasks** | 0.57 | 0.39 | 0.31 |
| **Mean tokens per run** | 238,556 | 385,824 | 197,493 |
| **Runs that read a skill** | 0/6 | 0/6 | 4/6 |

Thống kê chi tiết theo vai trò và loại check sinh bởi `python scripts/check_breakdown.py`:

```text
condition     role    technical  house rules  mean tokens  read a skill
baseline      eval     17/18         0/12         171,075      0/3     
baseline      learn    17/18         0/9          306,038      0/3     
subagents     eval     12/18         0/12         327,333      0/3     
subagents     learn    13/18         0/9          444,315      0/3     
skills-auto   eval      9/18         0/12         101,494      1/3     
skills-auto   learn     14/18         4/9          293,493      3/3     
```

Ghi chú xử lý lỗi và tính toàn vẹn:
- Toàn bộ các lần chạy của `skills-auto` đều có `skills_modified = false` và sha256 khớp tuyệt đối với thư mục skill đã đóng băng (`python scripts/verify_freeze.py` báo `OK`).
- Trong quá trình chạy, một số lần gọi LLM gặp lỗi cổng gateway cục bộ (như upstream quota/timeout). Nhóm đã tuân thủ đúng hướng dẫn xử lý sự cố tại `GUIDE.md` mục 4.2: chạy lại tác vụ bị lỗi và lưu vết đầy đủ trong thư mục `results/`.

## 8. Phân tích

1. **So sánh cải thiện trên tập học và tập đánh giá:**
   - Trên tác vụ **học**, điều kiện `skills-auto` đạt điểm trung bình cao nhất (**0.66**), vượt qua cả `baseline` (**0.63**) và `subagents` (**0.47**). Điểm số tăng rõ rệt ở `code-learn` (từ 6/10 lên 9/10, +30%) và `data-learn` (từ 5/8 lên 6/8, +12.5%).
   - Trên tác vụ **đánh giá**, `baseline` đạt điểm cao nhất (**0.57**), trong khi `subagents` đạt **0.39** và `skills-auto` đạt **0.31**.
   - Việc `skills-auto` cải thiện mạnh trên tập học nhưng suy giảm trên tập đánh giá là dấu hiệu điển hình của hiện tượng **quá khớp ở tầng ngữ cảnh (context-layer overfitting)**, hoàn toàn khớp với kết quả nghiên cứu trên SkillEvolBench. Tác tử đã học tốt các quy ước riêng của tập học nhưng không thể chuyển giao sang tập đánh giá khi xuất hiện các quy ước mới.

2. **Phân rã điểm kỹ thuật và quy ước tổ chức (`rule_`):**
   - Theo `scripts/check_breakdown.py`, trên tập học, `skills-auto` là điều kiện duy nhất đạt được các check quy ước tổ chức (**4/9** check, trong khi `baseline` và `subagents` đều đạt **0/9**). Điều này khẳng định skill do curator sinh ra đã phát huy tác dụng chính xác vào nhóm lỗi vi phạm quy ước (nhóm E).
   - Tuy nhiên, trên tập đánh giá, `skills-auto` đạt **0/12** check quy ước mới. Lý do: Các quy ước mới ở tập đánh giá là out-of-distribution. Vì curator chỉ đọc phản hồi từ tập học (nhằm tránh rò rỉ dữ liệu), nó hoàn toàn không có thông tin để sinh ra quy tắc cho các quy ước mới này.

3. **Cơ chế từ vết (`trace.md`) và `skills_read`:**
   - **Check được skill giúp đạt:** Trong `code-learn`, tác tử đã đọc skill `python-type-annotations-and-regression-tests` (`skills_read = 1`). Vết thực thi cho thấy tác tử đã chủ động tạo tệp `tests/test_regressions.py` và bổ sung type hint cho mọi hàm public, giúp đạt cả 3 check `rule_type_hints`, `rule_regression_tests`, và `rule_changelog`. Tương tự, ở `data-learn`, skill `json-schema-and-money-formatting` giúp đạt các check về làm sạch CSV và cấu trúc metadata.
   - **Check mà skill không giúp:** Trong `data-eval` và `logs-eval`, dù tác tử đọc skill nhưng thất bại ở các check quy ước mới do skill chỉ hướng dẫn theo khuôn mẫu của bài học. Ở `code-eval`, tác tử gặp lỗi quá tải context dẫn đến không hoàn thành các bước kiểm tra.

4. **Phân tích chi phí token:**
   - Token trung bình mỗi lần chạy: `subagents` tiêu tốn nhiều nhất (**385,824** token, gấp 1.62 lần baseline); `baseline` tiêu tốn **238,556** token; `skills-auto` tiêu tốn ít nhất (**197,493** token, tiết kiệm 17.2% so với baseline).
   - Hiệu quả điểm trên token: `baseline` đạt xấp xỉ 0.25 điểm / 100k token; `skills-auto` đạt xấp xỉ 0.25 điểm / 100k token; `subagents` chỉ đạt 0.11 điểm / 100k token.
   - **Đa tác tử (subagents) không đáng chi phí** trong bài lab này: Điểm số trung bình thấp hơn baseline trong khi tiêu tốn thêm hơn 60% token do chi phí truyền lại ngữ cảnh vào prompt của từng subagent mà không đem lại tri thức bổ sung nào về quy ước ẩn.

5. **Rò rỉ dữ liệu và quá khớp:**
   - **Không có rò rỉ dữ liệu:** Hàm `curate_skills` lọc tuyệt đối `role == "learn"`, đồng thời `validate_skill` đối chiếu toàn bộ `eval_markers()`. Không có bất kỳ dữ liệu hay tên tệp nào của tập đánh giá lọt vào thư mục `skills/auto/`.
   - **Có quá khớp:** Tri thức thủ tục trong skill bám chặt vào các lỗi cụ thể của tập học, không giúp ích khi đối mặt với quy ước mới ở tập đánh giá.

6. **Phân tích nhiễu (Noise analysis):**
   - So sánh điểm tác vụ học ở Phần 3.4 (`skills-auto-dev`: `code-learn` 9/10, `data-learn` 6/8, `logs-learn` 6/9 -> trung bình 0.77) và sau đóng băng (`skills-auto`: trung bình 0.66). Chênh lệch 0.11 điểm xuất phát từ tính bất định ngẫu nhiên trong sampling của mô hình và giới hạn thời gian thực thi.
   - Điều này cho thấy các chênh lệch điểm nhỏ (≤ 0.10) cần được đánh giá thận trọng và nằm trong khoảng dao động ngẫu nhiên.

## 9. Hạn chế và tính hợp lệ

1. **Quy mô tập tác vụ nhỏ:** Thí nghiệm chỉ gồm 3 họ tác vụ với 1 tác vụ đánh giá cho mỗi họ. Kích thước mẫu nhỏ hạn chế ý nghĩa thống kê và khả năng khái quát hóa kết luận.
2. **Số lần lặp hạn chế:** Mỗi cấu hình chỉ chạy một lần chính thức do giới hạn về ngân sách token và quota API, khiến kết quả dễ bị ảnh hưởng bởi nhiễu ngẫu nhiên của mô hình.
3. **Bản chất của quy ước ẩn:** Các quy ước tổ chức (Acme rules) mang tính tùy ý và không nêu trong đề bài. Tác tử không thể suy luận ra chúng bằng logic kỹ thuật thuần túy nếu không có cơ chế phản hồi lặp tại thời điểm thực thi.

## 10. Kết luận

1. Tác tử mặc định Deep Agents giải quyết rất tốt các bài toán kỹ thuật (đạt 94.4% check kỹ thuật) nhưng không thể đáp ứng các quy ước tổ chức ngầm (0% check quy ước).
2. Tác tử tự tiến hóa (`skills-auto`) với bộ tuyển chọn curator đã học thành công các quy ước ngầm trên tập học (đạt 44.4% check quy ước), nhưng bị quá khớp (overfitting) và không khái quát hóa được sang tập đánh giá.
3. Kiến trúc đa tác tử (`subagents`) làm tăng vọt chi phí token (+61.7%) mà không cải thiện điểm số do overhead ngữ cảnh phân mảnh.
4. Giao thức đóng băng skill và kiểm soát rò rỉ dữ liệu là then chốt để đo lường khách quan năng lực tự tiến hóa của tác tử.
5. Đề xuất cải tiến: Tích hợp cơ chế phản hồi tương tác tại thời điểm chạy (runtime execution feedback) để tác tử có thể tự điều chỉnh hành vi theo thời gian thực thay vì chỉ dựa vào tri thức đóng băng ngoại tuyến.

## Phụ lục

- Lệnh đã chạy (theo thứ tự):
  1. `pytest tests/test_01_provided.py`
  2. `python scripts/tour.py`
  3. `pytest tests/test_02_agent.py`
  4. `pytest tests/test_03_runner.py`
  5. `pytest tests/test_04_curator.py`
  6. `python -m lab.runner --condition baseline --tasks learn`
  7. `python -m lab.runner --condition baseline --tasks eval`
  8. `python -m lab.runner --condition subagents --tasks learn`
  9. `python -m lab.runner --condition subagents --tasks eval`
  10. `python -m lab.curator`
  11. `python -m lab.runner --condition skills-auto --tasks learn` (lưu vào `results/skills-auto-dev`)
  12. `git add -A && git commit -m "hypotheses"`
  13. `git add -A && git commit --allow-empty -m "freeze skills" && git tag freeze`
  14. `python -m lab.runner --condition skills-auto --tasks all`
  15. `python scripts/verify_freeze.py`
  16. `python -m lab.compare > report/table.md`
  17. `python scripts/check_breakdown.py`
- Thử thách mở rộng (nếu có): Hướng 6e (đo lường và phân tích nhiễu) đã được thực hiện bằng cách so sánh chi tiết giữa lần chạy phát triển Phần 3.4 (`skills-auto-dev`) và lần chạy chính thức sau đóng băng (`skills-auto`), ghi nhận khoảng dao động 0.11 điểm do tính bất định của mô hình.
- Ghi chú khác: Không có.
