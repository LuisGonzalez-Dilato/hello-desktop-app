from app.main import say_hello, new_test

def test_say_hello():
    assert say_hello() == "Hello, World! Testing that automation test works."

def test_new_test():
    assert new_test() == "New automation test."