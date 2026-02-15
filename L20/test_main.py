from main import add

def test_add_positive_number():
    assert add(1, 3) ==5

def test_add_negative_numbers():
    assert add(-1, -4) == -5

def test_add_mixed_number():
    assert add(-2, 5)==3