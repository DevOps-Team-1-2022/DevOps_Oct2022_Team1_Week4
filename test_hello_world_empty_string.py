from hello_world import helloWorld

def test_hello_world_empty_string():
    # Empty char
    emptyCharMessage = helloWorld("")
    assert emptyCharMessage == "Input string too long!"