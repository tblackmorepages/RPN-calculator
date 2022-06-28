import pytest
from rpn import Calculator



@pytest.mark.parametrize()
def test_rpn_calc(input_exp, result):
    rpn_calc = Calculator()
    output = rpn_calc.evaluate(input_exp)
    assert output == result
