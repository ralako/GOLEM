from zadanie import *


jazyk = None

def init(jazyk_):
    global jazyk
    jazyk = jazyk_

# DERIVÁCIE

class P1(Zadanie):     # polynóm
    def __init__(self):
        super().__init__()
        A,B,C,D,E = super().zvolKoef(5, [[]])
        self.zadanie = super().texRiesPoly([E,D,C,B,A])
        self.riesenie = super().texRiesPoly([D,2*C,3*B,4*A])
        self.neriesenie = super().texRiesPoly([D,C,B,A])



class P2(Zadanie):     # zlomok (kvadraticka/linearna)
    def __init__(self):
        super().__init__(maxnum=7)
        A,B,C,D,E = super().zvolKoef(5, [[]])
        self.zadanie = super().texRiesZlom([C,B,A],[E,D])
        self.riesenie = super().texRiesZlom([B*E-C*D, 2*A*E, A*D], [E*E, 2*D*E, D*D])
        self.neriesenie = super().texRiesZlom([B*E-C*D, -2*A*E, A*D], [E*E, 2*D*E, D*D])



class P3(Zadanie):     # sucin 1/x a odmocniny z linearnej
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[]])
        self.zadanie = super().prepis(r'\frac{A}{x}\sqrt{Bx+C}', [A,B,C])
        self.riesenie = super().prepis(r'\frac{'+str(-A*B)+r'x-'+str(2*A*C)+r'}{2x^2 \sqrt{\smash[b]{Bx+C}}}', [A,B,C])
        self.neriesenie = super().prepis(r'\frac{'+str(-A*B)+r'x-'+str(2*A*C)+r'}{x^2 \sqrt{\smash[b]{Bx+C}}}', [A,B,C])
        


class P4(Zadanie):     # exponenciala
    def __init__(self):
        super().__init__()
        A,B,C = super().zvolKoef(3, [[]])
        self.zadanie = super().prepis(r'e^{Ax^2+Bx+C}', [A,B,C])
        self.riesenie = super().prepis(r'('+str(2*A)+r'x+B)e^{Ax^2+Bx+C}', [A,B,C])
        self.neriesenie = super().prepis(r'(Ax+B)e^{Ax^2+Bx+C}', [A,B,C])



class P5(Zadanie):     # logaritmus zo zlomku linearna/linearna
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = super().prepis(r'\ln{\left(\frac{Ax+B}{Cx+D}\right)}', [A,B,C,D])
        self.riesenie = super().prepis(r'\frac{A}{Ax+B}-\frac{C}{Cx+D}', [A,B,C,D])
        self.neriesenie = super().prepis(r'\frac{A}{Ax+B}+\frac{C}{Cx+D}', [A,B,C,D])



class P6(Zadanie):     # exponenciala/linearna
    def __init__(self):
        super().__init__()
        A,B,C,D = super().zvolKoef(4, [[]])
        self.zadanie = super().prepis(r'\frac{e^{Ax+B}}{Cx+D}', [A,B,C,D])
        self.riesenie = super().prepis(r'\frac{ACx+'+str(A*D-C)+r'}{(Cx+D)^2}e^{Ax+B}', [A,B,C,D])
        self.neriesenie = super().prepis(r'\frac{-ACx+'+str(A*D-C)+r'}{(Cx+D)^2}e^{Ax+B}', [A,B,C,D])



            


# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), P5(), P6()]

