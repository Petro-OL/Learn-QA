import pytest

# change group
@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""

# check group
@pytest.mark.check
def test_name(user):
    assert user.name == "Petro"

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Oliinyk"

