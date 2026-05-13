from project import validate_password
from project import calculate_credit
from project import valid_weight

def test_valid_password():
    assert validate_password("Rohith@123") == (True, "Strong password")

def test_short_password():
    assert validate_password("abc") == (False, "Too short")

def test_no_uppercase():
    assert validate_password("rohith@123") == (False, "Need an uppercase letter")

def test_no_lowercase():
    assert validate_password("ROHITH@123") == (False, "Need a lowercase letter")


def test_no_number():
    assert validate_password("Rohith@abc") == (False, "Need a number")


def test_no_special_character():
    assert validate_password("Rohith123") == (False, "Need a special character")


def test_calculate_credit():
    assert calculate_credit(10, 2) == 20


def test_calculate_credit_zero():
    assert calculate_credit(0, 5) == 0


def test_valid_weight():
    assert valid_weight(5) == True


def test_invalid_weight():
    assert valid_weight(-2) == False
