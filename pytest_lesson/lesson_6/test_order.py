import pytest

# @pytest.mark.run(order=3) outdated 
@pytest.mark.order(3)
def test_DB_disconnect():
    print('DB disconnected')
    assert True

# @pytest.mark.run(order=1) outdated
@pytest.mark.order(1)
def test_DB_connect():
    print('DB connected')
    assert True

# @pytest.mark.run(order=2) outdated
@pytest.mark.order(2)
def test_data_check():
    print('data check')
    assert True

# 'pytest-dependency' is also outdated

