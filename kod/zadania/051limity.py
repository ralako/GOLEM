from zadanie import *



jazyk = None

def init(jazyk_):
    global jazyk
    jazyk = jazyk_



# ODMOCNINY

class P1(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G,H = super().zvolKoef(8, [[2,5,7,8],[3,4,7,8],[3,5,6,8],[1,3,5,7]])
            if H > 1:
                break
        A = abs(A)
        self.zadanie = super().prepis(r'\sqrt[A]{\left(\cfrac{x^{'+super().texRiesZlomCisla(B,C)[1:-1]+r'}\;x^{'+super().texRiesZlomCisla(D,E)[1:-1]+r'}}{x^{'+super().texRiesZlomCisla(F,G)[1:-1]+r'}}\right)^{H}}',[A,B,C,D,E,F,G,H])
        self.riesenie = r'$x^{'+super().texRiesZlomCisla((B*E*G+C*D*G-C*E*F)*H, C*E*G*A)[1:-1]+r'}$'
        self.neriesenie = r'$x^{'+super().texRiesZlomCisla((B*E*G-C*D*G-C*E*F)*H, C*E*G*A)[1:-1]+r'}$'



class P2(Zadanie):
    def __init__(self):
        super().__init__(fontsize=r'\footnotesize')
        A,B,C = super().zvolKoef(3, [[]])
        A = 1 ; B = abs(B)
        self.zadanie = r'{\scriptsize'+super().prepis(r'\big(A\sqrt{Bx+BCy}+\sqrt{Bx-BCy}\big)^2-\big(A\sqrt{Bx+BCy}-\sqrt{Bx-BCy}\big)^2',[A,B,C])+r'}'
        Z = abs(B) ; Y = C**2 ; X = 4*A*Z
        self.riesenie = super().prepis(r'X\sqrt{x^2-Yy^2}',[X,Y],koefStr=['X','Y'])
        if C == Y and B == Z:
            X = 2*A*Z
        self.neriesenie = super().prepis(r'X\sqrt{x^2-Cy^2}',[X,C],koefStr=['X','C'])
        


# LIMITY

class P3(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[]])
            if abs(B) != abs(D) and E > 0:
                break
        A = E*E
        C = E*E
        self.zadanie = super().prepis(r'\lim\limits_{n\to\infty}\cfrac{n^{-1/2}}{\sqrt{An+B}-\sqrt{Cn+D}}',[A,B,C,D,E])
        self.riesenie = super().texRiesZlomCisla(2*E,B-D)
        neriesenia = [r'$\infty$',r'$-\infty$',r'$0$',super().texRiesZlomCisla(2*E,B+D),super().texRiesZlomCisla(E,B-D)]
        self.neriesenie = choice(neriesenia)


class P4(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G,H = super().zvolKoef(8, [[]])
            if A > 1 and abs(B) != abs(F):
                break
        B = abs(B) ; F = abs(F)
        self.zadanie = r'$\lim\limits_{n\to\infty}'+str(A)+r'n\cfrac{\sqrt{'+super().texRiesPoly([D,C,B*B],premenna='n')[1:-1]+r'}-\sqrt{'+super().texRiesPoly([E,0,B*B],premenna='n')[1:-1]+r'}}{\sqrt{'+super().texRiesPoly([H,G,F*F],premenna='n')[1:-1]+r'}}$'
        self.riesenie = super().texRiesZlomCisla(A*C, 2*B*F)
        self.neriesenie = super().texRiesZlomCisla(A*C, B*F)
        





            


# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), blank(), blank()]

