class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first+self.second
    def mul(self):
        return self.first*self.second
    def sub(self):
        return self.first-self.second
    def div(self):
        return self.first / self.second
    
a = FourCal(1,2)
a.setdata(2,2)
print(a.add())

class MoreFourCal(FourCal):
    def pow(self):
        return self.first**self.second
a = MoreFourCal(4,3)

class SafeFourCal(FourCal):
    def div(self):
            if self.second==0:
                #raise ZeroDivisionError("0으로 나눌 수 없습니다!")
                return 0
            else:
                return self.first/self.second

a = SafeFourCal(4,0)
print(a.pow())
print(a.div())