from main import encode, decode

def simulate_encode(actual, expected):
    # given
    # actual
    # expected

    # when
    actual = encode(actual)

    # then
    assert actual == expected

def test_encode_dojo():
    # given
    input_str = "DOJO"
    expected = "36665666"

    # when
    simulate_encode(input_str, expected)

def test_encode_pytest():
    input_str = "PYTEST"
    expected = "799983377778"

    simulate_encode(input_str, expected)

def test_encode_tests():
    input_str = "TESTS"
    expected = "833777787777"

    simulate_encode(input_str, expected)

def test_encode_code():
    input_str = "CODE"
    expected = "2226663_33"

    simulate_encode(input_str, expected)

def test_encode_code():
    input_str = "PUZZLE"
    expected = "7889999_999955533"

    simulate_encode(input_str, expected)

def test_encode_sentence1():
    input_str = "I LIKE PYTHON"
    expected = "4440555444553307999844666_66"

    simulate_encode(input_str, expected)

def test_encode_sentence2():
    input_str = "PAIR PROGRAMMING"
    expected = "7244477707_777666477726_6444664"

    simulate_encode(input_str, expected)


def simulate_decode(actual, expected):
    # given
    # actual
    # expected

    # when
    actual = decode(actual)

    # then
    assert actual == expected

def test_decode():
    input_str = "DOJO"
    expected = "36665666"

    simulate_encode(input_str, expected)