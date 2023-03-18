import pytest
from unittest.mock import Mock


@pytest.fixture(scope="class")
def setup():
    mock_call = Mock()
    mock_call.return_value = [
        {"id": 0, "value": 0},
        {"id": 1, "value": 1},
    ]
    return mock_call()


@pytest.mark.usefixtures("setup")
class TestOK:
    def test_call_db(self, setup):
        response = setup
        assert response[0]["id"] == 0
        assert response[0]["value"] == 0


@pytest.mark.usefixtures("setup")
class TestFail:
    @pytest.mark.xfail
    def test_call_db_fail(self, setup):
        response = setup
        if response[0]["id"] != 1:
            pytest.xfail(reason="wrong response")
