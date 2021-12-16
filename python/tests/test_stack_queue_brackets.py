from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_validate_curlies():
    assert True == validate_brackets("{}")

def test_validate_empty():
    assert True == validate_brackets("")

def test_validate_paren_true():
    string = "()"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_paren_true_with_strings():
    string = "(start(middle)also start)end"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_unmatched_brackets():
    string = "((("
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_validate_paren_unmatched():
    string = "(())("
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_validate_curlies_unmatched():
    string = "{words{{tester}}]"
    actual = validate_brackets(string)
    expected = False
    assert actual == expected
