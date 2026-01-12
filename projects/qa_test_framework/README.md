# QA Test Framework - Pytest Calculator

## Project Overview

This project is a simple QA test framework built using Pytest.  
It demonstrates Python testing fundamentals, test organization, parameterization, skipped tests, and pytest configuration.

The application under test is a basic calculator module.  
The focus of this project is on testing practices rather than application complexity.

---

## What Is Being Tested

The calculator supports the following operations:
- Addition
- Subtraction
- Multiplication
- Division

The test suite includes:
- Positive test cases
- Edge cases (zero, negative numbers, large values)
- Parameterized tests
- Skipped tests for demonstration purposes

---

## Project Structure
qa_test_framework/
├── app/
│ ├── init.py
│ └── calculator.py
├── tests/
│ └── test_calculator.py
├── pytest.ini
├── requirements.txt
└── notes.txt

---

## Setup Instructions

### Create a virtual environment
python -m venv .venv
source .venv/bin/activate

### Install dependencies
pip install -r requirements.txt

---

## Running the Tests
Run all tests:
pytest

Run tests with verbose output:
pytest -v

---

## Testing Techniques Used

### Assertions
assert add(1, 2) == 3

### Parameterized Tests (Tuple-Based)
@pytest.mark.parametrize("a,b,result", [
(0, 4, -4),
(-20, 1, -21),
])
def test_sub_positive(a, b, result):
assert sub(a, b) == result

### Parameterized Tests (Dictionary-Based)
@pytest.mark.parametrize("case", test_cases)
def test_mul_positive(case):
assert mul(case["a"], case["b"]) == case["expected"]

### Skipped Tests
@pytest.mark.skip(reason="Error test")
def test_div_err():
assert div(4, 0)

Skipped tests are useful for known issues, incomplete features, or documentation purposes.

---

## Pytest Configuration

The pytest.ini file is used to:
- Configure import paths
- Register custom markers
- Avoid import errors during test discovery

---

## Dependencies

Main tools used:
- pytest

Dependencies were captured using:
pip freeze > requirements.txt









