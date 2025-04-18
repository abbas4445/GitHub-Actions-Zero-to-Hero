# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3, "The sum of 1 and 2 should be s3"
    assert add(1, -1) == 0, "The sum of 1 and -1 should be 0"

