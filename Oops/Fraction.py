class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        frac2 = Fraction(other.numerator, other.denominator)
        newDenomiator = frac2.denominator * self.denominator
        frac1Numerator = self.numerator * frac2.denominator
        frac2Numerator = frac2.numerator * self.denominator
        totalNumerator = frac1Numerator + frac2Numerator
        return f"{totalNumerator}/{newDenomiator}"

    @staticmethod
    def isValid(numerator, denominator):
        if denominator == 0:
            return False
        else:
            return True

    @classmethod
    def fromString(cls, fractionString):
        num, den = fractionString.split("/")
        return int(num) / int(den)
    
    def multiply(self,*args):
        num = self.numerator
        den = self.denominator
        
        for i in args:
            num = num *i.numerator
            den = den *i.denominator
        return Fraction(num,den)


f = Fraction(2, 2)
f2 = Fraction(4, 4)
print(Fraction.isValid(2, 0))
print(f)
print(f2)
print(f"Multiply: {f.multiply(Fraction(2,3),Fraction(2,3))}")
f3 = f + f2
print(f"{f3}")
print(Fraction.fromString("10/5"))
