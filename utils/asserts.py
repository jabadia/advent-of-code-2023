def assert_equal(a, b):
    if a != b:
        raise AssertionError(f"{a} != {b}")
