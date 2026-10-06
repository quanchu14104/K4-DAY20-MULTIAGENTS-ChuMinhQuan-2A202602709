### Human
The test suite of the `inventory` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: task
{"subagent_type": "explorer", "description": "Use the explorer agent to inspect the workspace, list files in workspace/, read the inventory source code and test files, and run the test suite to see the failures. Return a clear factual summary of the package structure, tests, and current test results."}

### Tool result
Here is a clear, factual summary of the package structure, tests, and current test results:

### 1. Package Structure (`workspace/inventory/`)
The package is named `inventory` and contains four Python modules:
*   `__init__.py`: Empty module init file.
*   `pricing.py`: Price utilities providing:
    *   `parse_price(text)`: Converts price strings (including formatted strings like `"$1,299.50"` or accounting format `"(12.00)"`) to a `Decimal`.
    *   `apply_discount(price, percent)`: Applies a percentage discount and rounds using round-half-up.
*   `export.py`: Export helpers providing:
    *   `to_csv_row(item)`: Formats an item dictionary as a CSV row (`name,price,qty`).
*   `report.py`: Inventory reports providing:
    *   `total_value(items)`: Computes the total inventory value after item discounts.
    *   `low_stock(items, threshold=5)`: Returns a list of item names with a quantity strictly below the threshold, sorted alphabetically ignoring case.

### 2. Test Suite (`workspace/tests/test_report.py`)
The test suite consists of 6 tests covering pricing, total value calculation, discounting, low stock reporting, and CSV export formatting.

### 3. Current Test Results
Running `cd workspace && python -m pytest tests -q` results in **2 failures** out of 6 tests:
1.  `test_total_value_thousands_separator`: Fails because `parse_price` does not remove commas (e.g. `"$1,299.50"` raises `decimal.InvalidOperation`).
2.  `test_discount_rounding_half_up`: Fails because `apply_disco

### Tool call: task
{"description": "Use the explorer agent to read the source files in workspace/inventory/pricing.py, workspace/inventory/export.py, workspace/inventory/report.py, and workspace/tests/test_report.py, and return their exact contents so we can inspect docstrings and implementations.", "subagent_type": "explorer"}

### Tool result
Here are the exact contents of the requested source and test files:

### `workspace/inventory/pricing.py`
```python
"""Price utilities for the inventory package."""
from decimal import Decimal


def parse_price(text):
    """Convert a price string to a Decimal.

    Supported formats:
      "$1,299.50" -> Decimal("1299.50")
      "  12 "     -> Decimal("12")
      "1299.5"    -> Decimal("1299.5")
      "(12.00)"   -> Decimal("-12.00")   # accounting style: parentheses mean negative
    """
    cleaned = text.strip().replace("$", "")
    return Decimal(cleaned)


def apply_discount(price, percent):
    """Return `price` after a percentage discount.

    The result is a Decimal rounded to 2 decimal places using the
    commercial rule "round half up" (0.005 -> 0.01).
    """
    discounted = price * (100 - percent) / 100
    return discounted.quantize(Decimal("0.01"))
```

### `workspace/inventory/export.py`
```python
"""Export helpers."""
from .pricing import parse_price


def to_csv_row(item):
    """Format one item as a CSV row: name,price,qty (price with 2 decimals).

    A name that contains a comma or a double quote is wrapped in double quotes,
    and every double quote inside it is doubled (RFC 4180).
    """
    price = parse_price(item["price"])
    return f'{item["name"]},{price:.2f},{item["qty"]}'
```

### `workspace/inventory/report.py`
```python
"""Inventory reports."""
from decimal import Decimal

from .pricing import apply_discount, parse_price


def total_value

### Tool call: task
{"subagent_type": "implementer", "description": "Use the implementer agent to fix the bugs in workspace/inventory/pricing.py, workspace/inventory/report.py, and workspace/inventory/export.py according to their docstrings and specifications. Ensure that all tests pass and every function adheres strictly to its docstring. Do not modify tests/test_report.py."}

### Tool result
I have successfully fixed the bugs in `workspace/inventory/pricing.py`, `workspace/inventory/report.py`, and `workspace/inventory/export.py` according to their docstrings and specifications:

1. **`workspace/inventory/pricing.py`**:
   - Fixed `parse_price` to handle thousands separators (commas) and accounting-style negative numbers wrapped in parentheses (e.g., `"(12.00)"` -> `Decimal("-12.00")`).
   - Fixed `apply_discount` to properly use commercial rounding (`ROUND_HALF_UP`) and handle Decimal precision correctly.

2. **`workspace/inventory/report.py`**:
   - Fixed `low_stock` to check for items *strictly below* the threshold (`qty < threshold` instead of `<=`), and to sort names alphabetically, ignoring case.

3. **`workspace/inventory/export.py`**:
   - Fixed `to_csv_row` to correctly implement RFC 4180 rules for escaping double quotes and wrapping names containing commas or double quotes in double quotes.

All tests (including `tests/test_report.py`) pass successfully.

### Tool call: task
{"description": "Use the reviewer agent to audit the implementation in workspace/inventory/ against task requirements, docstring specifications, edge cases, and house rules. Run pytest via execute. Return a verification report.", "subagent_type": "reviewer"}

### Tool result
# Verification Report: `workspace/inventory/`

**Auditor:** Reviewer Agent  
**Target Package:** `workspace/inventory/`  
**Test Suite:** `workspace/tests/`  

---

## Executive Summary
All tests pass successfully (`9 passed in 0.03s`). The implementation complies with task specifications, docstring requirements, edge cases, and standard Python conventions.

---

## Detailed Component Audit

### 1. `workspace/inventory/pricing.py`
* **Functions:** `parse_price(text)`, `apply_discount(price, percent)`
* **Docstring/Spec Compliance:**
  * Handles standard currency symbols (`$`), thousands separators (`,`), spaces, and accounting format (parentheses for negative numbers like `"(12.00)" -> Decimal("-12.00")`).
  * `apply_discount` properly calculates percentage discounts and rounds using `ROUND_HALF_UP` to two decimal places.
* **Edge Cases & Robustness:**
  * Uses `Decimal` throughout to avoid floating-point inaccuracies.
  * Correctly strips whitespace and handles strings appropriately.

### 2. `workspace/inventory/export.py`
* **Functions:** `to_csv_row(item)`
* **Docstring/Spec Compliance:**
  * Uses `parse_price` to format price to 2 decimal places.
  * Implements RFC 4180 CSV escaping rules: wraps names containing commas or double quotes in double quotes and escapes embedded double quotes by doubling them (`""`).
* **Edge Cases & Robustness:**
  * Tested with complex names containing both quotes and commas (e.g. `Widget "A", Deluxe`).

### 3. `workspace/inventory/report.py`

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import pytest; sys.exit(pytest.main(['workspace/tests']))\""}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_wwu53nob
plugins: anyio-4.15.1, langsmith-0.14.4
collected 9 items

workspace\tests\test_custom.py ...                                       [ 33%]
workspace\tests\test_report.py ......                                    [100%]

============================== 9 passed in 0.03s ==============================

[Command succeeded with exit code 0]

### Assistant
I have successfully fixed and verified the source code in the `inventory` package so that all tests pass and every function strictly adheres to its docstring and specifications.

### Summary of Changes:
1. **`workspace/inventory/pricing.py`**:
   - Updated `parse_price` to correctly handle thousands separators (commas) and accounting-style negative numbers enclosed in parentheses (e.g., `"(12.00)"`).
   - Updated `apply_discount` to ensure accurate percentage calculations using `Decimal` and proper commercial rounding (`ROUND_HALF_UP`) to two decimal places.

2. **`workspace/inventory/report.py`**:
   - Fixed `low_stock` to strictly check quantities below the threshold (`qty < threshold`) and sort item names alphabetically, ignoring case.
   - Ensured `total_value` correctly parses prices, applies optional per-item discounts, and accumulates inventory values.

3. **`workspace/inventory/export.py`**:
   - Fixed `to_csv_row` to properly format item CSV rows in accordance with RFC 4180 (handling double quotes and commas within item names).