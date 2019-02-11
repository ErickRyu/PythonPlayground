
def test_loop1():
    i = 0
    for i in range(0, 100):
        a = i
    print(i)


def test_loop2():
    for i in range(0, 100):
        a = i
    print(i)


if __name__ == "__main__":
    test_loop1()
    test_loop2()
