

class Sub1:
    value = 0
    def __init__(self):
        Sub1.value += 1

    @classmethod
    def get_value(cls):
        return Sub1.value
