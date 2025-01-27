import pytest

from jar import Jar


@pytest.fixture
def jar_capacity():
    return Jar(14)

@pytest.mark.parametrize('amount ,size',[
    (4, 4),
    (2, 2),
    (3, 3)
])
def test_deposit(amount, size, jar_capacity):

    jar_capacity.deposit(amount)

    assert jar_capacity._size == size

@pytest.mark.parametrize('amount, size', [
    (4, 10),
    (5, 9)
])
def test_withdraw(amount, size, jar_capacity):
    jar_capacity.deposit(14)
    jar_capacity.withdraw(amount)
    assert jar_capacity._size == size


@pytest.mark.parametrize('size, cookies', [
    (0, ''),
    (4, '🍪🍪🍪🍪'),
    (2, '🍪🍪'),
    (3, '🍪🍪🍪')
])
def test_jar_str(size, cookies, jar_capacity):
    jar_capacity.size = size
    assert str(jar_capacity) == cookies


def test_jar_raises_value_error(jar_capacity):
    with pytest.raises(ValueError):
        jar_capacity.deposit(30)
    with pytest.raises(ValueError):
        jar_capacity.withdraw(30)

