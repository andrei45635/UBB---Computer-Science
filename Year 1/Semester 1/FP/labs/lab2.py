def problema_sapte(nr):
    p = 1
    i = 2
    while i * i <= nr:
        if nr % i == 0:
            p *= i
            p *= nr // i
        i += 1

    if nr == i * 1:
        p *= i

    return p


def test_problema_sapte():
    assert problema_sapte(1) == 1
    assert problema_sapte(2) == 2
    assert problema_sapte(10) == 10
    assert problema_sapte(12) == 144
    assert problema_sapte(18) == 324


if __name__ == "__main__":
    test_problema_sapte()
    n = int(input())
    p = problema_sapte(n)
    print(p)
