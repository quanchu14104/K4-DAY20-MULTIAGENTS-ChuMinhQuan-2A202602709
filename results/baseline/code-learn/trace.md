### Human
The test suite of the `inventory` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: ls
{"path": "/workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/inventory/', '/workspace/tests/']

### Tool call: glob
{"pattern": "**/*", "path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/inventory/__init__.py', '/workspace/inventory/__pycache__/__init__.cpython-311.pyc', '/workspace/inventory/__pycache__/export.cpython-311.pyc', '/workspace/inventory/__pycache__/pricing.cpython-311.pyc', '/workspace/inventory/__pycache__/report.cpython-311.pyc', '/workspace/inventory/export.py', '/workspace/inventory/pricing.py', '/workspace/inventory/report.py', '/workspace/tests/__pycache__/test_report.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_report.py']

### Tool call: execute
{"command": "pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting workspace/tests/test_report.py _______________
ImportError while importing test module '~\AppData\Local\Temp\lab_sandbox_qbyx8oz3\workspace\tests\test_report.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-learn\workspace\tests\test_report.py:3: in <module>
    from inventory.export import to_csv_row
E   ModuleNotFoundError: No module named 'inventory'
=========================== short test summary info ===========================
ERROR workspace/tests/test_report.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.34s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting workspace/tests/test_report.py _______________
ImportError while importing test module '~\AppData\Local\Temp\lab_sandbox_qbyx8oz3\workspace\tests\test_report.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-learn\workspace\tests\test_report.py:3: in <module>
    from inventory.export import to_csv_row
E   ModuleNotFoundError: No module named 'inventory'
=========================== short test summary info ===========================
ERROR workspace/tests/test_report.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.27s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
_______________ ERROR collecting workspace/tests/test_report.py _______________
ImportError while importing test module '~\AppData\Local\Temp\lab_sandbox_qbyx8oz3\workspace\tests\test_report.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-learn\workspace\tests\test_report.py:3: in <module>
    from inventory.export import to_csv_row
E   ModuleNotFoundError: No module named 'inventory'
=========================== short test summary info ===========================
ERROR workspace/tests/test_report.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.27s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest -o pythonpath=workspace workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 6 items

workspace\tests\test_report.py .FF...                                    [100%]

================================== FAILURES ===================================
____________________ test_total_value_thousands_separator _____________________

    def test_total_value_thousands_separator():
        items = [{"name": "laptop", "price": "$1,299.50", "qty": 2}]
>       assert total_value(items) == Decimal("2599.00")
               ^^^^^^^^^^^^^^^^^^

C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-learn\workspace\tests\test_report.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
workspace\inventory\report.py:14: in total_value
    price = parse_price(item["price"])
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

text = '$1,299.50'

    def parse_price(text):
        """Convert a price string to a Decimal.
    
        Supported formats:
          "$1,299.50" -> Decimal("1299.50")
          "  12 "     -> Decimal("12")
          "1299.5"    -> Decimal("1299.5")
          "(12.00)"   -> Decimal("-12.00")   # accounting style: parentheses mean negative
        """
        cleaned = text.strip().replac

### Tool call: read_file
{"file_path": "workspace/tests/test_report.py"}

### Tool result
@@ lines 1-32 of 32 @@
from decimal import Decimal

from inventory.export import to_csv_row
from inventory.pricing import apply_discount
from inventory.report import low_stock, total_value


def test_total_value_plain():
    items = [{"name": "pen", "price": "$2.50", "qty": 4}]
    assert total_value(items) == Decimal("10.00")


def test_total_value_thousands_separator():
    items = [{"name": "laptop", "price": "$1,299.50", "qty": 2}]
    assert total_value(items) == Decimal("2599.00")


def test_discount_rounding_half_up():
    assert apply_discount(Decimal("10.05"), 10) == Decimal("9.05")


def test_total_value_with_discount():
    items = [{"name": "desk", "price": "100.00", "qty": 1, "discount": 15}]
    assert total_value(items) == Decimal("85.00")


def test_low_stock_basic():
    assert low_stock([{"name": "pen", "qty": 2}, {"name": "ink", "qty": 9}]) == ["pen"]


def test_csv_row_plain_name():
    assert to_csv_row({"name": "pen", "price": "2.5", "qty": 4}) == "pen,2.50,4"

### Tool call: read_file
{"file_path": "workspace/inventory/pricing.py"}

### Tool result
@@ lines 1-25 of 25 @@
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

### Tool call: read_file
{"file_path": "workspace/inventory/report.py"}

### Tool result
@@ lines 1-25 of 25 @@
"""Inventory reports."""
from decimal import Decimal

from .pricing import apply_discount, parse_price


def total_value(items):
    """Total value of `items` after per-item discounts.

    Each item is a dict: {"name": str, "price": str, "qty": int, "discount": percent (optional)}.
    """
    total = Decimal("0")
    for item in items:
        price = parse_price(item["price"])
        price = apply_discount(price, item.get("discount", 0))
        total += price * item["qty"]
    return total


def low_stock(items, threshold=5):
    """Names of the items whose quantity is strictly below `threshold`.

    The names are sorted alphabetically, ignoring case.
    """
    return [item["name"] for item in items if item["qty"] <= threshold]

### Tool call: read_file
{"file_path": "workspace/inventory/export.py"}

### Tool result
@@ lines 1-12 of 12 @@
"""Export helpers."""
from .pricing import parse_price


def to_csv_row(item):
    """Format one item as a CSV row: name,price,qty (price with 2 decimals).

    A name that contains a comma or a double quote is wrapped in double quotes,
    and every double quote inside it is doubled (RFC 4180).
    """
    price = parse_price(item["price"])
    return f'{item["name"]},{price:.2f},{item["qty"]}'

### Tool call: read_file
{"file_path": "workspace/inventory/__init__.py"}

### Tool result
@@ lines 1-1 @@
System reminder: File exists but has empty contents

### Tool call: read_file
{"file_path": "workspace/tests/test_report.py", "offset": 0, "limit": 100}

### Tool result
@@ lines 1-32 of 32 @@
from decimal import Decimal

from inventory.export import to_csv_row
from inventory.pricing import apply_discount
from inventory.report import low_stock, total_value


def test_total_value_plain():
    items = [{"name": "pen", "price": "$2.50", "qty": 4}]
    assert total_value(items) == Decimal("10.00")


def test_total_value_thousands_separator():
    items = [{"name": "laptop", "price": "$1,299.50", "qty": 2}]
    assert total_value(items) == Decimal("2599.00")


def test_discount_rounding_half_up():
    assert apply_discount(Decimal("10.05"), 10) == Decimal("9.05")


def test_total_value_with_discount():
    items = [{"name": "desk", "price": "100.00", "qty": 1, "discount": 15}]
    assert total_value(items) == Decimal("85.00")


def test_low_stock_basic():
    assert low_stock([{"name": "pen", "qty": 2}, {"name": "ink", "qty": 9}]) == ["pen"]


def test_csv_row_plain_name():
    assert to_csv_row({"name": "pen", "price": "2.5", "qty": 4}) == "pen,2.50,4"

### Tool call: glob
{"path": "workspace/tests", "pattern": "*.py"}

### Tool result
['/workspace/tests/test_report.py']

### Tool call: execute
{"command": "python -c \"import pytest; print(pytest.__file__)\""}

### Tool result
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\.venv\Lib\site-packages\pytest\__init__.py

[Command succeeded with exit code 0]

### Tool call: write_file
{"file_path": "workspace/inventory/pricing.py", "content": "\"\"\"Price utilities for the inventory package.\"\"\"\nfrom decimal import Decimal\n\n\ndef parse_price(text):\n    \"\"\"Convert a price string to a Decimal.\n\n    Supported formats:\n      \"$1,299.50\" -> Decimal(\"1299.50\")\n      \"  12 \"     -> Decimal(\"12\")\n      \"1299.5\"    -> Decimal(\"1299.5\")\n      \"(12.00)\"   -> Decimal(\"-12.00\")   # accounting style: parentheses mean negative\n    \"\"\"\n    cleaned = text.strip()\n    is_negative = False\n    if cleaned.startswith(\"(\") and cleaned.endswith(\")\"):\n        is_negative = True\n        cleaned = cleaned[1:-1].strip()\n    \n    cleaned = cleaned.replace(\"$\", \"\").replace(\",\", \"\")\n    val = Decimal(cleaned)\n    return -val if is_negative else val\n\n\ndef apply_discount(price, percent):\n    \"\"\"Return `price` after a percentage discount.\n\n    The result is a Decimal rounded to 2 decimal places using the\n    commercial rule \"round half up\" (0.005 -> 0.01).\n    \"\"\"\n    from decimal import ROUND_HALF_UP\n    discounted = price * (100 - Decimal(str(percent))) / 100\n    return discounted.quantize(Decimal(\"0.01\"), rounding=ROUND_HALF_UP)\n"}

### Tool result
Updated file /workspace/inventory/pricing.py

### Tool call: execute
{"command": "python -m pytest -o pythonpath=workspace workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 6 items

workspace\tests\test_report.py ......                                    [100%]

============================== 6 passed in 0.03s ==============================

[Command succeeded with exit code 0]

### Tool call: read_file
{"file_path": "workspace/inventory/report.py"}

### Tool result
@@ lines 1-25 of 25 @@
"""Inventory reports."""
from decimal import Decimal

from .pricing import apply_discount, parse_price


def total_value(items):
    """Total value of `items` after per-item discounts.

    Each item is a dict: {"name": str, "price": str, "qty": int, "discount": percent (optional)}.
    """
    total = Decimal("0")
    for item in items:
        price = parse_price(item["price"])
        price = apply_discount(price, item.get("discount", 0))
        total += price * item["qty"]
    return total


def low_stock(items, threshold=5):
    """Names of the items whose quantity is strictly below `threshold`.

    The names are sorted alphabetically, ignoring case.
    """
    return [item["name"] for item in items if item["qty"] <= threshold]

### Tool call: read_file
{"file_path": "workspace/inventory/export.py"}

### Tool result
@@ lines 1-12 of 12 @@
"""Export helpers."""
from .pricing import parse_price


def to_csv_row(item):
    """Format one item as a CSV row: name,price,qty (price with 2 decimals).

    A name that contains a comma or a double quote is wrapped in double quotes,
    and every double quote inside it is doubled (RFC 4180).
    """
    price = parse_price(item["price"])
    return f'{item["name"]},{price:.2f},{item["qty"]}'

### Tool call: edit_file
{"file_path": "workspace/inventory/report.py", "old_string": "def low_stock(items, threshold=5):\n    \"\"\"Names of the items whose quantity is strictly below `threshold`.\n\n    The names are sorted alphabetically, ignoring case.\n    \"\"\"\n    return [item[\"name\"] for item in items if item[\"qty\"] <= threshold]", "new_string": "def low_stock(items, threshold=5):\n    \"\"\"Names of the items whose quantity is strictly below `threshold`.\n\n    The names are sorted alphabetically, ignoring case.\n    \"\"\"\n    filtered = [item[\"name\"] for item in items if item[\"qty\"] < threshold]\n    return sorted(filtered, key=lambda s: s.lower())"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/inventory/report.py'

### Tool call: edit_file
{"old_string": "def to_csv_row(item):\n    \"\"\"Format one item as a CSV row: name,price,qty (price with 2 decimals).\n\n    A name that contains a comma or a double quote is wrapped in double quotes,\n    and every double quote inside it is doubled (RFC 4180).\n    \"\"\"\n    price = parse_price(item[\"price\"])\n    return f'{item[\"name\"]},{price:.2f},{item[\"qty\"]}'", "new_string": "def to_csv_row(item):\n    \"\"\"Format one item as a CSV row: name,price,qty (price with 2 decimals).\n\n    A name that contains a comma or a double quote is wrapped in double quotes,\n    and every double quote inside it is doubled (RFC 4180).\n    \"\"\"\n    price = parse_price(item[\"price\"])\n    name = item[\"name\"]\n    if \",\" in name or '\"' in name:\n        name = '\"' + name.replace('\"', '\"\"') + '\"'\n    return f'{name},{price:.2f},{item[\"qty\"]}'", "file_path": "workspace/inventory/export.py"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/inventory/export.py'

### Tool call: write_file
{"content": "\"\"\"Inventory management package.\"\"\"\n", "file_path": "workspace/inventory/__init__.py"}

### Tool result
Updated file /workspace/inventory/__init__.py

### Tool call: execute
{"command": "python -m pytest -o pythonpath=workspace workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 6 items

workspace\tests\test_report.py ......                                    [100%]

============================== 6 passed in 0.05s ==============================

[Command succeeded with exit code 0]

### Tool call: write_file
{"content": "from decimal import Decimal\nfrom inventory.report import low_stock, total_value\nfrom inventory.pricing import parse_price, apply_discount\nfrom inventory.export import to_csv_row\n\ndef test_parse_price_formats():\n    assert parse_price(\"$1,299.50\") == Decimal(\"1299.50\")\n    assert parse_price(\"  12 \") == Decimal(\"12\")\n    assert parse_price(\"1299.5\") == Decimal(\"1299.5\")\n    assert parse_price(\"(12.00)\") == Decimal(\"-12.00\")\n\ndef test_low_stock_threshold_and_sorting():\n    items = [\n        {\"name\": \"Zebra\", \"qty\": 4},\n        {\"name\": \"apple\", \"qty\": 2},\n        {\"name\": \"Banana\", \"qty\": 5},\n    ]\n    # threshold=5 means strictly below 5: \"Zebra\" (4), \"apple\" (2)\n    # Sorted case-insensitively: \"apple\", \"Zebra\"\n    assert low_stock(items, threshold=5) == [\"apple\", \"Zebra\"]\n\ndef test_to_csv_row_escaping():\n    item1 = {\"name\": \"pen, red\", \"price\": \"2.50\", \"qty\": 4}\n    assert to_csv_row(item1) == '\"pen, red\",2.50,4'\n    \n    item2 = {\"name\": 'fancy \"pen\"', \"price\": \"3.00\", \"qty\": 1}\n    assert to_csv_row(item2) == '\"fancy \"\"pen\"\"\",3.00,1'\n", "file_path": "workspace/tests/test_spec.py"}

### Tool result
Updated file /workspace/tests/test_spec.py

### Tool call: execute
{"command": "python -m pytest -o pythonpath=workspace workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 9 items

workspace\tests\test_report.py ......                                    [ 66%]
workspace\tests\test_spec.py ...                                         [100%]

============================== 9 passed in 0.05s ==============================

[Command succeeded with exit code 0]

### Tool call: delete
{"file_path": "workspace/tests/test_spec.py"}

### Tool result
Deleted /workspace/tests/test_spec.py

### Tool call: execute
{"command": "python -m pytest -o pythonpath=workspace workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_qbyx8oz3
plugins: anyio-4.15.1, langsmith-0.14.4
collected 6 items

workspace\tests\test_report.py ......                                    [100%]

============================== 6 passed in 0.02s ==============================

[Command succeeded with exit code 0]

### Assistant
I have fixed the issues in the `inventory` package so that all tests pass and every function conforms strictly to its docstring specification:

1. **`inventory/pricing.py`**:
   - Updated `parse_price` to correctly handle commas in numbers (e.g., thousands separators like `"$1,299.50"`) and negative accounting-style prices enclosed in parentheses (e.g., `"(12.00)"`).
   - Updated `apply_discount` to use `ROUND_HALF_UP` rounding explicitly as specified.

2. **`inventory/report.py`**:
   - Fixed `low_stock` to correctly check for items with quantities *strictly below* the threshold (`< threshold` instead of `<= threshold`) and ensured the returned names are sorted alphabetically, ignoring case.

3. **`inventory/export.py`**:
   - Updated `to_csv_row` to follow RFC 4180 when escaping item names that contain commas or double quotes (wrapping in double quotes and doubling any internal double quotes).

4. **`inventory/__init__.py`**:
   - Added a proper package docstring to satisfy code quality checks.