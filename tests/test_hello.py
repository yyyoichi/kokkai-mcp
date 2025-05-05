from src.hello import get_message

def test_get_message():
    assert get_message() == "Hello world"