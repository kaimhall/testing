"""
Most functional tests follow the Arrange-Act-Assert model:

1. Arrange, or set up, the conditions for the test
2. Act by calling some function or method
3. Assert that some end condition is true
"""


def test_always_passes():
    assert True


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
