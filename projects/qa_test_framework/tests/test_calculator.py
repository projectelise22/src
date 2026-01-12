import pytest
from app.calculator import add, sub, mul, div

def test_add():
    assert add(1, 2)   == 3
    assert add(0, 0)   == 0
    assert add(0, 20)  == 20
    assert add(20, 0)  == 20
    assert add(-20, 1) == -19
    assert add(9, -30) == -21
    assert add(-1, -2) == -3
    assert add(20, -1) == 19
    assert add(-1, 20) == 19
    assert add(1, 9999999) == 10000000 

#simple parameterizing
@pytest.mark.parametrize("a,b,result", [
    (0, 4, -4),
    (4, 0, 4),
    (0, 0, 0),
    (-20, 1, -21),
    (1, -20, 21),
    (-1, -3, 2),
    (-3, -1, -2),
    (-999_999, 1, -1_000_000)
])
def test_sub_positive(a, b, result):
    assert sub(a, b) == result

#paramaterizing using dictionary
test_cases = [
    {"a": 1, "b": 2, "expected": 2},
    {"a": 4, "b": 1, "expected": 4},
    {"a": 1, "b": 0, "expected": 0},
    {"a": 0, "b": 2, "expected": 0},
    {"a": -1, "b": 2, "expected": -2},
    {"a": 2, "b": -2, "expected": -4},
    {"a": -4, "b": -2, "expected": 8},
    {"a": 1_000_000, "b": 20, "expected": 20_000_000},
]
@pytest.mark.parametrize("case", test_cases)
def test_mul_positive(case):
    assert mul(case["a"], case["b"]) == case["expected"]

def test_div_positive():
    assert div(6, 3) == 2

def test_add_fail():
    assert add(4, 0) == 5

# should raise error
@pytest.mark.skip(reason="Error test")
def test_div_err():
    assert div(4, 0)
