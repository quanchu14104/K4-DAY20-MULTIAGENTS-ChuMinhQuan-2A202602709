---
name: python-type-annotations-and-regression-tests
description: Use when writing or fixing Python packages to ensure all code changes satisfy strict style and testing rules (type hints on public functions, regression tests, and changelog updates).
---
- Add type annotations (parameters and return values) to every public function/method (names not starting with `_`).
- Create a dedicated regression test file (e.g., `tests/test_regressions.py`) containing at least one test per fixed bug, and ensure all tests pass.
- Record each fix in `CHANGELOG.md` under the `## Unreleased` heading using the exact format: `- fix(<function name>): <short description>` (at least 3 entries when fixing multiple issues).
- Do not modify existing test files unless explicitly permitted (add new test files instead).
