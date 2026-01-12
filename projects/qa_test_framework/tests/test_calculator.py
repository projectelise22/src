from app.calculator import add, sub, mul, div

def test_add_positive():
    assert add(1, 2) == 3;

def test_sub_positive():
    assert sub(10, 5) == 5;

def test_mul_positive():
    assert mul(3, 20) == 60;

def test_div_positive():
    assert div(6, 3) == 2;