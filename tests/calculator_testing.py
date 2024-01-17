import pytest
from calculator import Calculator


# Testing valid expressions
@pytest.mark.parametrize("expression, expected_result", [
    # simple expressions
    ("~5 + ~10.7", -15.7),
    ("5 ! + 3", 123),
    ("123#", 6),
    ("3 ^ 2", 9),
    ("10 % 3", 1),
    ("4 @ 6 @ 8", 6.5),
    ("5 $ 7 $ 2", 7),
    ("1 & 3 & 2", 1),
    ("~4", -4),
    ("5 !", 120),
    ("(2 + 3) * 4", 20),
    ("18 / 3 - 2", 4),
    ("2.5 + 3.5", 6),
    ("9 - 5.5", 3.5),
    ("4 * 2.5", 10),
    ("16 / 4", 4),
    ("(3 + 2) ^ (2 - 1)", 5),
    ("3+-(2+4)", -3),
    ("3+~-3", 6),
    ("~-3!", 6),
    ("-3!", -6),
    ("2---3!", -4),
    ("2 +--3!", 8),
    ("3+-(-1)!", 4),

    # complex expressions
    ("12 + 34.5 - 56 + 78.2", 68.7),
    ("20 * 5.25 / 2 - 30", 22.5),
    ("50.75 % 9 + 70 % 8.25", 9.75),
    ("3 @ 6.5 @ 9 @ 12", 9.4375),
    ("100 $ 200.5 $ 50", 200.5),
    ("1 & 2 & 3.3 & 4", 1),
    ("((2 + 3.3) * 4) ^ 2", 449.44),
    ("(12 + 34.7) / (56 - 45)", 4.245454545454546),
    ("20 - (5 * (3 + 2.5))", -7.5),
    ("((10 + 20.8) * 3) / 2", 46.2),
    ("100 - (5 ^ 2) + 25.5 - 0.5", 100),
    ("(40 $ 30.4) + (20 & 10) + 3!", 56),
    ("(4! - 5 * (4 @ 2)! * 2) + 36 + 2#", 2),
    ("3 ^ 2 ! - 5 * (4 $ 2)! * 2 + 7 @ 9 @ 11", -221.5),
    ("((12.5 + 34.7) / (56 - 45)) ^ 2 - 4 $ 5 $ 6", 12.411900826446281),
    ("10 % 3 + 5 % 2 - 1 & 2 & 3 - ~4 + 10", 15),
    ("(20 - 3) * (2 ^ 3) + 1 + 5.5 @ 6.5", 143),
    ("12.34# + 56.78# - 4 ----- 3", 29),
    ("((4 + 5) * (6 - 3) ^ 2 / 3) @ 5.5 @ 7.5", 11.875),
    ("3 ----- 4 + ~10 & 20 & ~30 - 2.5", -33.5),
    ("4 ^ 3! - 10 + 15.5 $ 20.3 - 12#",  4103.3),
    ("(100 $ 50 $ 25) - (10 & 5 & 3) + ~20", 77),
    ("(5 % 2 + 7 % 3) * 2 - 1 & 4 & 6 - ~5 + 12", 20),
    ("((15 - 4) * (3 ^ 2)) / 2 + 4.5 @ 3.5", 53.5),
    ("23.45# + 67.89# - 6 ----- 4", 34),
    ("((8 + 6) * (9 - 2) ^ 3 / 4) @ 2.5 @ 6.5", 304),
    ("7 ----- 5 + ~15 & 25 & ~35 - 3.5", -36.5),
    ("(9 ^ 2! - 15 + 18 $ 24 - 9#) / 81^0.5", 9),
    ("(200 $ 150 $ 125) - (20 & 10 & 8) + ~30", 162),
    ("((10 + 20) * 3.5) / 2 - 4.5 @ 7.2", 46.65),
    ("(45 % 12 + 8 % 5) * 3 - 2 & 5 & 7 - ~11", 45)

])
def test_valid_expressions(expression, expected_result):
    calc = Calculator()
    assert calc.calculate(expression) == expected_result


# Testing invalid expressions with expected exceptions
@pytest.mark.parametrize("invalid_expression, expected_exception", [
    ("2+/3", SyntaxError),
    ("2++3", SyntaxError),
    ("!2-3", SyntaxError),
    ("2!^2+", SyntaxError),
    ("abc", SyntaxError),
    ("1/0", ZeroDivisionError),
    ("((3.5 + 2.2) * 4.1)! - 20", ValueError),
    ("", SyntaxError),
    ("          ", SyntaxError),
    ("~--3!", ValueError),
    ("--~--3", SyntaxError),
    ("~--~-3", SyntaxError),
    ("~~3", SyntaxError),
    ("2 - - 3!", ValueError),
    ("!4", SyntaxError),
    ("-", SyntaxError),
    ("-~3", SyntaxError),
    ("4**", SyntaxError),
    ("()", SyntaxError),
    (" ", SyntaxError),
    ("(4))", SyntaxError),
    ("4+-3!", ValueError),
    ("4/0", ZeroDivisionError),
    ("3..4", SyntaxError),
    (".", SyntaxError),
    ("", SyntaxError),
    ("~~4", SyntaxError),
    ("(4))", SyntaxError),
    ("4+5-(3)(", SyntaxError),
    ("4+5$", SyntaxError),
    ("~4!", ValueError),
    ("1!!!!2", SyntaxError),

])
def test_invalid_expression(invalid_expression, expected_exception):
    calc = Calculator()
    with pytest.raises(expected_exception):
        calc.calculate(invalid_expression)
