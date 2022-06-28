import pytest
from rpn import Calculator

tests = [
    ('856 2023 10 + 70 4 / 9 * % -', 812),
    ('65 94 0 * +', 65),
    ('one million three hundred forty two  eleven  -  six  %  eighty eight  +  nine  /', 10),
    ('two thousand nine hundred  12  seven  * -  thirty  3 % 59 + /', 47),
    ('4 5 -', "Error: result is not a whole number"),
    ('0.5 9 +', "Error: Expression invalid"),
    ('-7 3 *', "Error: Expression invalid"),
    ('81 63 4 /', "Error: Expression invalid"),
    ('12 % /', "Error: Expression invalid"),
    ('hello', "Error: Expression invalid"),
]


@pytest.mark.parametrize("test_input,expected", tests)
def test_rpn_calc(test_input, expected):
    rpn_calc = Calculator()
    number_input = rpn_calc.text_to_numbers(test_input)
    assert rpn_calc.evaluate(number_input) == expected
