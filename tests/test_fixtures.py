import pytest


@pytest.fixture
def example_fixture():
    return 2


def test_with_fixture(example_fixture):
    assert example_fixture == 2


def format_data_for_display(people):
    d = {}
    for obj in people:
        name = f"{obj['given_name']} {obj['family_name']}"
        d[name] = obj["title"]

    res = [f"{k}: {v}" for k, v in d.items()]
    return res


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


@pytest.mark.format_data
def test_format_data_for_display(example_people_data):

    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
