import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        tot="%.2f %.2f"%(self.real+no.real,self.imaginary+no.imaginary)
        fin=list(map(float,tot.split()))
        res=Complex(*fin)
        return(res)
        
    def __sub__(self, no):
        tot="%.2f %.2f"%(self.real-no.real,self.imaginary-no.imaginary)
        fin=list(map(float,tot.split()))
        res=Complex(*fin)
        return(res)
        
    def __mul__(self, no):
        rea=self.real*no.real
        rea-=self.imaginary*no.imaginary
        img=(self.imaginary*no.real+self.real*no.imaginary)
        tot="%.2f %.2f"%(rea,img)
        fin=list(map(float,tot.split()))
        res=Complex(*fin)
        return(res)
        
    def __truediv__(self, no):
        temp=no
        temp.imaginary*=-1
        mul_res=self*temp
        den=(no.real**2+no.imaginary**2)
        rea=mul_res.real/den
        img=mul_res.imaginary/den
        tot="%.2f %.2f"%(rea,img)
        fin=list(map(float,tot.split()))
        res=Complex(*fin)
        return(res)
        
    def mod(self):
        tot="%.2f 0.00"%((self.real**2+self.imaginary**2)**0.5)
        fin=list(map(float,tot.split()))
        res=Complex(*fin)
        return(res)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
