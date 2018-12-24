from scope.class_sub import Sub1


class Sub0:
    def __init__(self):
        Sub1.value = 3

    def __str__(self):
        return 'change Sub1.value'

    @staticmethod
    def change_sub1_value(new_value):
        print('change sub1 value to', new_value)
        Sub1.value = new_value

if __name__ == "__main__":

    print(Sub1().value)
    print(Sub0())
    print(Sub1().value)
    Sub0.change_sub1_value(70)
    print(Sub1.get_value_classmethod())
    print(Sub1.value)
    print(Sub1().value)
