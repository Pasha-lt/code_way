import pytest

from calculator import addition

@pytest.mark.parametrize('first_number, second_number, result', (
        pytest.param(2, 3, 5, id='positive numbers'),
        pytest.param(-1, 3, 2, id='negative and positive numbers'),
        pytest.param(4.3, 2.5, 6.8, id='float numbers'),
))
def test_calculator(first_number, second_number, result):
    assert addition(first_number=first_number, second_number=second_number) == result
    
