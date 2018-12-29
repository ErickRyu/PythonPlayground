

class Sub1:
    value = 0
    value_self = 'Which class value?'

    def __init__(self):
        Sub1.value = 1
        self.value_self = 'this is class value 1'

    def get_value_self(self):
        return self.value_self

    @staticmethod
    def inc_val():
        Sub1.value += 1

    @classmethod
    def inc_cls_val(cls):
        cls.value_self = 'this is class value 2'

    @classmethod
    def get_value_classmethod(cls):
        return cls.value_self

    @staticmethod
    def get_value_staticmethod():
        return Sub1.value

