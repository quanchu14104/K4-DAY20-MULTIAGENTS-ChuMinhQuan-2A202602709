### Human
The test suite of the `bookings` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: ls
{"path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/', '/workspace/tests/']

### Tool call: glob
{"pattern": "**/*", "path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/__init__.cpython-311.pyc', '/workspace/bookings/__pycache__/billing.cpython-311.pyc', '/workspace/bookings/__pycache__/calendar_export.cpython-311.pyc', '/workspace/bookings/__pycache__/schedule.cpython-311.pyc', '/workspace/bookings/__pycache__/timeutil.cpython-311.pyc', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py', '/workspace/tests/__pycache__/test_bookings.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_bookings.py']

### Tool call: execute
{"command": "pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\lab_sandbox_d2ez7nby\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
=========================== short test summary info ===========================
ERROR workspace/tests/test_bookings.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.29s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\lab_sandbox_d2ez7nby\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
=========================== short test summary info ===========================
ERROR workspace/tests/test_bookings.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.27s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"env": {"PYTHONPATH": "workspace"}, "command": "python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\lab_sandbox_d2ez7nby\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
=========================== short test summary info ===========================
ERROR workspace/tests/test_bookings.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.27s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items

============================ no tests ran in 0.00s ============================

[stderr] ERROR: file or directory not found: tests

Exit code: 4
[Command failed with exit code 4]

### Tool call: execute
{"command": "cd workspace && python -m pytest tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby\workspace
plugins: anyio-4.15.1, langsmith-0.14.4
collected 3 items

tests\test_bookings.py FF.                                               [100%]

================================== FAILURES ===================================
______________________ test_total_minutes_mixed_formats _______________________

    def test_total_minutes_mixed_formats():
>       assert total_minutes(["1h30m", "2h"]) == 210
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

C:\VIN_AI_THUC_CHIEN\K4-DAY20-MULTIAGENTS-ChuMinhQuan-2A202602709\tasks\code-eval\workspace\tests\test_bookings.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
bookings\schedule.py:7: in total_minutes
    return sum(parse_duration(d) for d in durations)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bookings\schedule.py:7: in <genexpr>
    return sum(parse_duration(d) for d in durations)
               ^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

text = '2h'

    def parse_duration(text):
        """Convert a duration string to whole minutes (int).
    
        Supported formats:
          "1h30m" -> 90
          "2h"    -> 120
          "45m"   -> 45
          "1:30"  -> 90
          "45"    -> 45    # a bare number means minutes
        Surrou

### Tool call: read_file
{"file_path": "workspace/tests/test_bookings.py"}

### Tool result
@@ lines 1-15 of 15 @@
from bookings.billing import billable_blocks
from bookings.schedule import add_slot, total_minutes


def test_total_minutes_mixed_formats():
    assert total_minutes(["1h30m", "2h"]) == 210


def test_billable_blocks_rounds_up():
    assert billable_blocks(20) == 2
    assert billable_blocks(45) == 3


def test_add_slot_single_call():
    assert add_slot("a") == ["a"]

### Tool call: read_file
{"file_path": "workspace/bookings/billing.py"}

### Tool result
@@ lines 1-11 of 11 @@
"""Billing rules."""


def billable_blocks(minutes, block=15):
    """Number of billable blocks for a booking.

    A partial block is billed as a full block (always round UP):
    16 minutes with 15-minute blocks -> 2 blocks.
    `minutes` must be >= 0; a negative value raises ValueError.
    """
    return round(minutes / block)

### Tool call: read_file
{"file_path": "workspace/bookings/calendar_export.py"}

### Tool result
@@ lines 1-7 of 7 @@
"""Calendar export."""
from .timeutil import parse_duration


def slot_end(start_minute, duration_text):
    """Minute of the day at which a slot ends."""
    return start_minute + parse_duration(duration_text)

### Tool call: read_file
{"file_path": "workspace/bookings/schedule.py"}

### Tool result
@@ lines 1-17 of 17 @@
"""Schedule helpers."""
from .timeutil import parse_duration


def total_minutes(durations):
    """Total minutes of a list of duration strings."""
    return sum(parse_duration(d) for d in durations)


def add_slot(slot, slots=[]):
    """Return a NEW list containing the given slots plus `slot`.

    Separate calls must not share state: calling add_slot("a") and then
    add_slot("b") returns ["a"] and then ["b"].
    """
    slots.append(slot)
    return slots

### Tool call: read_file
{"file_path": "workspace/bookings/timeutil.py"}

### Tool result
@@ lines 1-19 of 19 @@
"""Time helpers for the bookings package."""
import re


def parse_duration(text):
    """Convert a duration string to whole minutes (int).

    Supported formats:
      "1h30m" -> 90
      "2h"    -> 120
      "45m"   -> 45
      "1:30"  -> 90
      "45"    -> 45    # a bare number means minutes
    Surrounding whitespace is ignored.
    """
    m = re.fullmatch(r"(\d+)h(\d+)m", text.strip())
    if not m:
        raise ValueError(f"bad duration: {text!r}")
    return int(m.group(1)) * 60 + int(m.group(2))

### Tool call: read_file
{"file_path": "workspace/README.md"}

### Tool result
@@ lines 1-5 of 5 @@
# bookings

Small package. Run the tests from the `workspace/` folder:

    cd workspace && python -m pytest tests -q

### Tool call: read_file
{"file_path": "workspace/CHANGELOG.md"}

### Tool result
@@ lines 1-6 of 6 @@
# Changelog

## Unreleased

## 1.4.2
- initial import

### Tool call: edit_file
{"old_string": "    return round(minutes / block)", "file_path": "workspace/bookings/billing.py", "new_string": "    import math\n    if minutes < 0:\n        raise ValueError(\"minutes must be >= 0\")\n    return math.ceil(minutes / block)"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/billing.py'

### Tool call: read_file
{"file_path": "workspace/bookings/billing.py"}

### Tool result
@@ lines 1-14 of 14 @@
"""Billing rules."""


def billable_blocks(minutes, block=15):
    """Number of billable blocks for a booking.

    A partial block is billed as a full block (always round UP):
    16 minutes with 15-minute blocks -> 2 blocks.
    `minutes` must be >= 0; a negative value raises ValueError.
    """
    import math
    if minutes < 0:
        raise ValueError("minutes must be >= 0")
    return math.ceil(minutes / block)

### Tool call: edit_file
{"new_string": "def add_slot(slot, slots=None):\n    \"\"\"Return a NEW list containing the given slots plus `slot`.\n\n    Separate calls must not share state: calling add_slot(\"a\") and then\n    add_slot(\"b\") returns [\"a\"] and then [\"b\"].\n    \"\"\"\n    if slots is None:\n        slots = []\n    else:\n        slots = list(slots)\n    slots.append(slot)\n    return slots", "file_path": "workspace/bookings/schedule.py", "old_string": "def add_slot(slot, slots=[]):\n    \"\"\"Return a NEW list containing the given slots plus `slot`.\n\n    Separate calls must not share state: calling add_slot(\"a\") and then\n    add_slot(\"b\") returns [\"a\"] and then [\"b\"].\n    \"\"\"\n    slots.append(slot)\n    return slots"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/schedule.py'

### Tool call: edit_file
{"new_string": "def parse_duration(text):\n    \"\"\"Convert a duration string to whole minutes (int).\n\n    Supported formats:\n      \"1h30m\" -> 90\n      \"2h\"    -> 120\n      \"45m\"   -> 45\n      \"1:30\"  -> 90\n      \"45\"    -> 45    # a bare number means minutes\n    Surrounding whitespace is ignored.\n    \"\"\"\n    text = text.strip()\n    # 1. \"1h30m\" or \"1h\" or \"30m\" etc. Let's make a flexible parser or regex checks.\n    # Supported formats:\n    # \"1h30m\" -> 90\n    # \"2h\"    -> 120\n    # \"45m\"   -> 45\n    # \"1:30\"  -> 90\n    # \"45\"    -> 45\n    \n    # Try HH:MM format first (\"1:30\")\n    m_colon = re.fullmatch(r\"(\\d+):(\\d+)\", text)\n    if m_colon:\n        return int(m_colon.group(1)) * 60 + int(m_colon.group(2))\n\n    # Try bare number format (\"45\")\n    m_bare = re.fullmatch(r\"(\\d+)\", text)\n    if m_bare:\n        return int(m_bare.group(1))\n\n    # Try combined or separate hours/minutes like \"1h30m\", \"2h\", \"45m\"\n    # Let's match optional hours and optional minutes\n    m_hm = re.fullmatch(r\"(?:(\\d+)h)?(?:(\\d+)m)?\", text)\n    if m_hm and text:\n        h_str, m_str = m_hm.groups()\n        if h_str is not None or m_str is not None:\n            hours = int(h_str) if h_str else 0\n            minutes = int(m_str) if m_str else 0\n            # Ensure it actually matched something meaningful and didn't just match empty string if text wasn't empty\n            if hours > 0 or minutes > 0 or text == \"0h\" 

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/timeutil.py'

### Tool call: execute
{"command": "cd workspace && python -m pytest tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby\workspace
plugins: anyio-4.15.1, langsmith-0.14.4
collected 3 items

tests\test_bookings.py ...                                               [100%]

============================== 3 passed in 0.04s ==============================

[Command succeeded with exit code 0]

### Tool call: write_file
{"file_path": "workspace/tests/additional_tests.py", "content": "import pytest\nfrom bookings.billing import billable_blocks\nfrom bookings.schedule import add_slot, total_minutes\nfrom bookings.timeutil import parse_duration\nfrom bookings.calendar_export import slot_end\n\n\ndef test_parse_duration():\n    assert parse_duration(\"1h30m\") == 90\n    assert parse_duration(\"2h\") == 120\n    assert parse_duration(\"45m\") == 45\n    assert parse_duration(\"1:30\") == 90\n    assert parse_duration(\"45\") == 45\n    assert parse_duration(\"  2h  \") == 120\n    with pytest.raises(ValueError):\n        parse_duration(\"invalid\")\n\n\ndef test_billable_blocks_edge_cases():\n    assert billable_blocks(0) == 0\n    assert billable_blocks(15) == 1\n    assert billable_blocks(16) == 2\n    with pytest.raises(ValueError):\n        billable_blocks(-1)\n\n\ndef test_slot_end():\n    assert slot_end(600, \"1h30m\") == 690\n\n\ndef test_add_slot_immutability():\n    s1 = add_slot(\"a\")\n    s2 = add_slot(\"b\", s1)\n    assert s1 == [\"a\"]\n    assert s2 == [\"a\", \"b\"]\n"}

### Tool result
Updated file /workspace/tests/additional_tests.py

### Tool call: execute
{"command": "cd workspace && python -m pytest tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.0, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\lab_sandbox_d2ez7nby\workspace
plugins: anyio-4.15.1, langsmith-0.14.4
collected 3 items

tests\test_bookings.py ...                                               [100%]

============================== 3 passed in 0.02s ==============================

[Command succeeded with exit code 0]

### Tool call: delete
{"file_path": "workspace/tests/additional_tests.py"}

### Tool result
Deleted /workspace/tests/additional_tests.py

### Tool call: execute
{"command": "git status"}

### Tool result
[stderr] fatal: not a git repository (or any of the parent directories): .git

Exit code: 128
[Command failed with exit code 128]

### Tool call: read_file
{"file_path": "workspace/bookings/timeutil.py"}

### Tool result
@@ lines 1-47 of 47 @@
"""Time helpers for the bookings package."""
import re


def parse_duration(text):
    """Convert a duration string to whole minutes (int).

    Supported formats:
      "1h30m" -> 90
      "2h"    -> 120
      "45m"   -> 45
      "1:30"  -> 90
      "45"    -> 45    # a bare number means minutes
    Surrounding whitespace is ignored.
    """
    text = text.strip()
    # 1. "1h30m" or "1h" or "30m" etc. Let's make a flexible parser or regex checks.
    # Supported formats:
    # "1h30m" -> 90
    # "2h"    -> 120
    # "45m"   -> 45
    # "1:30"  -> 90
    # "45"    -> 45
    
    # Try HH:MM format first ("1:30")
    m_colon = re.fullmatch(r"(\d+):(\d+)", text)
    if m_colon:
        return int(m_colon.group(1)) * 60 + int(m_colon.group(2))

    # Try bare number format ("45")
    m_bare = re.fullmatch(r"(\d+)", text)
    if m_bare:
        return int(m_bare.group(1))

    # Try combined or separate hours/minutes like "1h30m", "2h", "45m"
    # Let's match optional hours and optional minutes
    m_hm = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?", text)
    if m_hm and text:
        h_str, m_str = m_hm.groups()
        if h_str is not None or m_str is not None:
            hours = int(h_str) if h_str else 0
            minutes = int(m_str) if m_str else 0
            # Ensure it actually matched something meaningful and didn't just match empty string if text wasn't empty
            if hours > 0 or minutes > 0 or text == "0h" or text == "0m" or text == "0"

### Assistant
I have fixed the issues across the `bookings` package so that all requirements from the docstrings and tests are correctly met:

1. **`bookings/timeutil.py` (`parse_duration`)**: Updated to properly handle all specified duration formats (`"1h30m"`, `"2h"`, `"45m"`, `"1:30"`, and bare numbers like `"45"`).
2. **`bookings/billing.py` (`billable_blocks`)**: Added negative value validation raising `ValueError` and ensured proper rounding up via `math.ceil()`.
3. **`bookings/schedule.py` (`add_slot`)**: Fixed mutable default argument behavior (`slots=[]`) to prevent state sharing across separate function calls.

### Summary of Changed Files:
- `workspace/bookings/timeutil.py`
- `workspace/bookings/billing.py`
- `workspace/bookings/schedule.py`