from hello_world import helloWorld

def test_hello_world_too_long():
    # Too long (>10 char)
    tooLongMessage = helloWorld("0123456789A")
    assert tooLongMessage == "Input string too long!"