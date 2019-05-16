"""Module with one test which should raise a pylint error."""


def test_pylint_should_find_this_unused_variable():
    """Test without real assertion but with an unused variable"""
    not_used_variable = 1
    assert True
