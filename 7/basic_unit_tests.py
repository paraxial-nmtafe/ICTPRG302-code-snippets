from linear import linear_result
from some_risky_function import risky

def test_equality(expected, actual):
    try:
        assert expected == actual
        print("✅", expected, "was equal to", actual)
    except AssertionError:
        print("Test failed, expected", actual, "to be", expected)


test_equality(10, linear_result(5, 2, 0))
test_equality(14, linear_result(5, 2, 4))
test_equality(12, linear_result(3, 3, 3))
test_equality(0, linear_result(-1, 0, 0))
test_equality(-1, linear_result(-1, 0, -1))
test_equality(5, linear_result(-1, 0, -1))


test_equality(7, risky([]))
test_equality(-1, risky("Hi"))

test_equality(256, risky(12)) # Useless!

test_equality(5, risky(638))
test_equality(256, risky(637))
