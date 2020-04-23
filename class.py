class FourCal:
    def __init__(self, name, age, univ):
        self.name = name
        self.age = age
        self.univ = univ
        self.add_num = 0
        self.sub_num = 0
        self.mul_num = 0
        self.div_num = 0
    def add(self, n1, n2):
        self.add_num += 1
        return n1 + n2
    def sub(self, n1, n2):
        self.sub_num += 1
        return n1 - n2
    def mul(self, n1, n2):
        self.mul_num += 1
        return n1 * n2
    def div(self, n1, n2):
        self.div_num += 1
        if(num2 == 0):
            print('0으로 나눌 수 없습니다')
            return None
        return n1 / n2
    def ShowCount(self):
        print("덧셈: %d" % self.add_num)
        print("뺄셈: %d" % self.sub_num)
        print("곱셈: %d" % self.mul_num)
        print("나눗셈: %d" % self.div_num)

calculator2 = FourCal("정혜인", 22, "Korea")
print(calculator2.name, calculator2.age, calculator2.univ)
print(calculator2.add(2,4), calculator2.mul(3,8))
calculator2.ShowCount()