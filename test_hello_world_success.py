from hello_world import helloWorld

def test_hello_world_success():
    # Success message
    successMessage = helloWorld("Team 1")
    assert successMessage == "Hello Team 1! Welcome to Hello World File!"