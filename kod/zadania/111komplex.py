from zadanie import *
from random import randint, random


jazyk = None

def init(jazyk_):
    global jazyk
    jazyk = jazyk_


class P21(Zadanie):     # absolutna hodnota
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            if A*B < 0 and abs(A*B) != 1:
                break
        self.zadanie = super().prepis(r'|A+Bi|', [A,B])

        self.riesenie = self.texRiesSqrt(A*A+B*B)
        
        nahoda = random()
        if nahoda < 0.33:
            self.neriesenie = self.texRiesSqrt(abs(A*A-B*B))
        elif nahoda < 0.66:
            self.neriesenie = r'$' + str(abs(A+B)) + r'$'
        else:
           self.neriesenie = self.texRiesSqrt(A*A+B*B+1)





class P22(Zadanie):     # argument
    def __init__(self):
        super().__init__()
        A,C = super().zvolKoef(2, [[]])
        B = A * int(C/abs(C))
        self.zadanie = super().prepis(r'A+Bi', [A,B])
        if A > 0:
            if B > 0:
                self.riesenie = super().texRiesZlomPi(1,4)
                self.neriesenie = super().texRiesZlomPi(5,4)
            else:
                self.riesenie = super().texRiesZlomPi(7,4)
                self.neriesenie = super().texRiesZlomPi(1,4)
        else:
            if B > 0:
                self.riesenie = super().texRiesZlomPi(3,4)
                self.neriesenie = super().texRiesZlomPi(5,4)
            else:
                self.riesenie = super().texRiesZlomPi(5,4)
                self.neriesenie = super().texRiesZlomPi(7,4)



class P23(Zadanie):     # je na im osi
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            if A > 1 and B > 0:
                break
        self.zadanie = super().prepis(r'A\left(\cos{' + self.texRiesZlomPi(B,2)[1:-1] + r'}+i\sin{' + self.texRiesZlomPi(B,2)[1:-1] + r'}\right)', [A,B])
        if B % 2 == 0:
            self.riesenie = super().text(['nie','ne','no'])
            self.neriesenie = super().text(['áno','ano','yes'])
        else:
            self.riesenie = super().text(['áno','ano','yes'])
            self.neriesenie = super().text(['nie','ne','no'])
        
        

class P24(Zadanie):     # zjednodusenie vyrazu
    def __init__(self):
        super().__init__()
        nahoda = random()
        if nahoda < 0.25:
            A = 1
        elif nahoda < 0.5:
            A = -1
        elif nahoda < 0.75:
            A = 3
        else:
            A = -3
        if random() < 0.5:
            B = 1
        else:
            B = -1
    
        self.zadanie = super().prepis(r'A+B\sqrt{3}i', [A,B])

        alpha = [0,2,0,1][abs(A)]   # kolko sestin pi
        alphafake = [0,1,0,2][abs(A)]
        if A > 0:
            if B > 0:
                phi = super().texRiesZlomPi(alpha,6)[1:-1]
                phifake = super().texRiesZlomPi(alphafake,6)[1:-1]
            else:
                phi = super().texRiesZlomPi(12-alpha,6)[1:-1]
                phifake = super().texRiesZlomPi(12-alphafake,6)[1:-1]
        else:
            if B > 0:
                phi = super().texRiesZlomPi(6-alpha,6)[1:-1]
                phifake = super().texRiesZlomPi(6-alphafake,6)[1:-1]
            else:
                phi = super().texRiesZlomPi(6+alpha,6)[1:-1]
                phifake = super().texRiesZlomPi(6+alphafake,6)[1:-1]
                
        self.riesenie = super().texKomplexneCisloGoniometric(super().texRiesSqrt(A*A+3)[1:-1],phi)
        self.neriesenie = super().texKomplexneCisloGoniometric(super().texRiesSqrt(A*A+3)[1:-1],phifake)
        


class P25(Zadanie):     # realna cast
    def __init__(self):
        super().__init__()
        while True:
            A,D = super().zvolKoef(2, [[]])
            if A > 0:
                break
        vyber = randint(0,11)
        B = [1,3,5,7,1,5,7,11,1,2,4,5][vyber]
        C = [4,4,4,4,6,6,6,6,3,3,3,3][vyber]
        cB2 = [2, 2, 2,2,3, 3, 3,3,1, 1, 1,1]
        cC  = [2,-2,-2,2,2,-2,-2,2,2,-2,-2,2]
        sB2 = [2,2, 2, 2,1,1, 1, 1,3,3, 3, 3]
        sC  = [2,2,-2,-2,2,2,-2,-2,2,2,-2,-2]
        
        self.zadanie = super().texKomplexneCisloExp(A,self.texRiesZlomPi(B,C,nicefrac=False,popZnamienko=True)[1:-1])

        re = super().texRiesZlomCisla(A,cC[vyber],pripoj=super().texRiesSqrt(cB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
        im = super().texRiesZlomCisla(A,sC[vyber],pripoj=super().texRiesSqrt(sB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
        self.riesenie = super().texKomplexneCislo(re,im)

        nahoda = random()
        if nahoda < 0.33:
            refake = super().texRiesZlomCisla(-A,cC[vyber],pripoj=super().texRiesSqrt(cB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
            imfake = super().texRiesZlomCisla(A,sC[vyber],pripoj=super().texRiesSqrt(sB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
        elif nahoda < 0.66:
            refake = super().texRiesZlomCisla(A,cC[vyber],pripoj=super().texRiesSqrt(cB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
            imfake = super().texRiesZlomCisla(-A,sC[vyber],pripoj=super().texRiesSqrt(sB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
        else:
            refake = super().texRiesZlomCisla(A*2,cC[vyber],pripoj=super().texRiesSqrt(cB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
            imfake = super().texRiesZlomCisla(A*2,sC[vyber],pripoj=super().texRiesSqrt(sB2[vyber])[1:-1], nicefrac=False,popZnamienko=True)[1:-1]
            
        self.neriesenie = super().texKomplexneCislo(refake,imfake)

        


class P26(Zadanie):     # exponencionalny tvar
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            if B > 2 and B < 7 and abs(A) > 1:
                break

        vyber = random()
        
        if vyber < 0.5:
            self.zadanie = super().prepis(r'x^B=A', [A,B])
            
            if B % 2 == 0:  # parna odmocnina
                self.riesenie = r'$' + str(-A) + '$'
                if random() < 0.5:
                    self.neriesenie = r'$' + str(A) + '$'
                else:
                    self.neriesenie = r'$' + str(-A) + 'i$'
                    
            else:   # neparna odmocnina
                self.riesenie = r'$' + str(A) + '$'
                if random() < 0.5:
                    self.neriesenie = r'$' + str(-A) + '$'
                else:
                    self.neriesenie = r'$' + str(A) + 'i$'
                    
        else:
            self.zadanie = super().prepis(r'x^B=Ai', [A,B])
            
            if B % 2 == 0:  # parna odmocnina
                self.riesenie = r'$' + str(-A) + 'i$'
                if random() < 0.5:
                    self.neriesenie = r'$' + str(A) + 'i$'
                else:
                    self.neriesenie = r'$' + str(-A) + '$'
                    
            else:   # neparna odmocnina
                self.riesenie = r'$' + str(A) + 'i$'
                if random() < 0.5:
                    self.neriesenie = r'$' + str(-A) + 'i$'
                else:
                    self.neriesenie = r'$' + str(A) + '$'

                


###---------


def prikladyLoad():
    return [P21(),P22(),P23(),P24(),P25(),P26()]


