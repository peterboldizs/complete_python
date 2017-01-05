class StringUtil:

    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        s = cls._strip_string(s)
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    def _strip_string(s): # _ means private method
        return ''.join(c for c in s if c.isalnum())

    @staticmethod
    def _is_palindrome(s): # _ means private method
        for c in  range(len(s)//2):
            if s[c] != s[-c -1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


print(StringUtil.is_palindrome('Radar'))
# print(StringUtil.is_palindrome('Radar', case_insensitive=False))
str = "Géza kék az ég"
str2 = "happy pahhy happy new year the the day"
print(StringUtil.is_palindrome(str))
print(StringUtil.get_unique_words(str2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)

    @classmethod
    def from_point(cls, point):
        return cls(point.x, point.y)


p = Point.from_tuple((3,7))
print(p.x, p.y)
q = Point.from_point(p)
print(q.x, q.y)


class A:
    def __init__(self, prop1):
        __prop1 = prop1

    def op1(self):
        print("A.op1 with prop1 {}".format(self.__prop1))


class B(A):
    def op2(self, prop1):
        self.__prop1 = prop1
        print("B.op2 with prop1 {}".format(self.__prop1))


obj = B(100)
#obj.op1()
obj.op2(40)
#obj.op1()
print(obj.__dict__.keys())
