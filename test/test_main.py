from src.main import usual_greeting

def test_func_returns_str():
    result = usual_greeting('hi')
    assert type(result) == str

def test_func_returns_hello_world_when_given_hi():
    result = usual_greeting('hi')
    assert result == 'Hello World'

def test_func_returns_goodbye_earth_when_given_bye():
    result = usual_greeting('bye')
    assert result == 'Goodbye Earth'

def test_func_returns_try_again_when_invalid_input():
    result = usual_greeting('hey')
    assert result == 'Try Again'
