g_value = 's'


def func ():
    global g_value
    g_value = 'change'


if __name__ == "__main__":

    print(g_value)
    func()
    print(g_value)