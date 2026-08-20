from zadanie import *
jazyk = None
def init(jazyk_):
    global jazyk
    jazyk = jazyk_

class P1(Zadanie):     # pocet riešení
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[2,2],[1,3]])
        self.zadanie = super().prepis(r'Ax^2+Bx+C=0', [A,B,C])
        diskriminant = B*B - 4*A*C
        if diskriminant > 0:
            self.riesenie = str(2)
            self.neriesenie = str(choice([0,1]))
        elif diskriminant == 0:
            self.riesenie = str(1)
            self.neriesenie = str(choice([0,2]))
        else:
            self.riesenie = str(0)
            self.neriesenie = str(choice([1,2]))


class P2(Zadanie):     # poloha vrcholu x-os
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[]])
        self.zadanie = super().prepis(r'f(x)=Ax^2+Bx+C', [A,B,C])
        self.riesenie = super().texRiesZlomCisla(-B, 2*A)
        self.neriesenie = super().texRiesZlomCisla(B, 2*A)


class P3(Zadanie):     # poloha vrcholu y-os
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[2,2],[1,3]])
        self.zadanie = super().prepis(r'f(x)=Ax^2+Bx+C', [A,B,C])
        if -B*B+4*A*C == 0:
            self.riesenie = str(0)
            self.neriesenie = super().texRiesZlomCisla(-B*B+2*A*C, 4*A)
        else:
            self.riesenie = super().texRiesZlomCisla(-B*B+4*A*C, 4*A)
            self.neriesenie = super().texRiesZlomCisla(-B*B+2*A*C, 4*A)
        

class P4(Zadanie):     # sucet riešení (lahsie)
    def __init__(self):
        super().__init__()
        while True:
            A,B,C = super().zvolKoef(3, [[1,2,2],[1,2,3],[1,3,3]])
            if B != C and B != -C:
                break
        self.zadanie = super().prepis(r'Ax^2+'+str(A*(B+C))+r'x+'+str(A*B*C)+r'=0', [A,B,C])
        self.riesenie = str(-B-C)
        self.neriesenie = str(-B-C + choice([-3,-2,-1,1,2,3]))


class P5(Zadanie):     # sucet riešení (tazsie)
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[1,1,2,2,5,5],[1,1,2,3,4,5],[1,1,3,3,4,4],[2,4],[3,4],[2,5]])
            if C/B != E/D and C/B != -E/D:
                break
        self.zadanie = super().prepis(str(A*B*D)+r'x^2+'+str(A*(B*E+C*D))+r'x+'+str(A*C*E)+r'=0', [A,B,C,D,E])
        self.riesenie = super().texRiesZlomCisla(-C*D-E*B, B*D)
        self.neriesenie = super().texRiesZlomCisla(-C*D+E*B, B*D)


###---------


def prikladyLoad():
    return [P1(),P1(),P2(),P3(),P4(),P5()]


