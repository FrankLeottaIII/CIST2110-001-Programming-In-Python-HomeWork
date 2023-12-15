import pytest

def test_input_member_id(monkeypatch):
    # Set the input value to be used during the test
    monkeypatch.setattr('builtins.input', lambda _: '12345')
    
    # Call the function that uses input()
    result = input_member_id()
    
    # Assert the expected result
    assert result == '12345'