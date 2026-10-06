---
name: json-schema-and-money-formatting
description: Use when generating data processing outputs or JSON summaries involving monetary values, metadata blocks, and CSV cleanup rules.
---
- Represent all monetary amounts in `answer.json` as integer cents (e.g., 1606.67 USD becomes `160667`), never as floating-point dollars.
- Include the exact required `meta` block object in `answer.json` with keys: `"source"`, `"rows_in"`, and `"rows_used"`.
- Verify output files like `clean.csv` match exact expected header columns, date formats (`YYYY-MM-DDTHH:MM:SSZ`), and canonical spellings.
