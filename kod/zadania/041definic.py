from zadanie import *
from random import random, choice

jazyk = None
def init(jazyk_):
    global jazyk
    jazyk = jazyk_



class P1(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G = super().zvolKoef(7, [[]])
            B = abs(B)
            if C>1 and A>C:
                break
        if random() < 0.5:
            funkcio = r"\arccos"
        else:
            funkcio = r"\arcsin"
        self.zadanie = super().prepis(r"f(x) = G"+funkcio+r"\!\left( \frac{A-Bx}{C} \right) - \cfrac{e^{Ex+F}}{\sqrt{DBx^2-ADx}}", [A,B,C,D,E,F,G])
        bod1 = super().texRiesZlomCisla(A,B, nicefrac=False)[1:-1]
        bod2 = super().texRiesZlomCisla(A+C,B, nicefrac=False)[1:-1]
        bod3 = super().texRiesZlomCisla(A-C,B, nicefrac=False)[1:-1]
        if D > 0:
            self.riesenie = super().texInterval([[bod1, bod2]],[[False,True]], premenna=False)
            self.neriesenie = super().texInterval([[bod3, bod1]],[[True, False]], premenna=False)
        else:
            self.riesenie = super().texInterval([[bod3, bod1]],[[True,False]], premenna=False)
            self.neriesenie = super().texInterval([[bod1, bod2]],[[False, False]], premenna=False)



class P2(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G = super().zvolKoef(7, [[]])
            A = abs(A)
            if A != 1 and E != F and E+F != 0:
                B = -(E+F)
                C = E*F
                if E > F:
                    G = F - 1
                else:
                    G = F + 1

                if G != 0:
                    break

        self.zadanie = super().prepis(r"g(x) = \frac{1}{A} \ln{\!(x^2+Bx+C)}+\frac{\sqrt[3]{D-x}}{x-G}", [A,B,C,D,E,F,G])
        if E > F:
            self.riesenie = r"{\scriptsize "+super().texInterval([["-inf",F-1], [F-1,F], [E,"inf"]], [[False,False],[False,False],[False,False]], husty=True, premenna=False)+r"}"
            self.neriesenie = r"{\scriptsize "+super().texInterval([["-inf",F-1], [F-1,F], [E,"inf"]], [[False,False],[False,False],[True,False]], husty=True, premenna=False)+r"}"
        else:
            self.riesenie = r"{\scriptsize "+super().texInterval([["-inf",E], [F,F+1], [F+1,"inf"]], [[False,False],[False,False],[False,False]], husty=True, premenna=False)+r"}"
            self.neriesenie = r"{\scriptsize "+super().texInterval([["-inf",E], [F,F+1], [F+1,"inf"]], [[False,False],[True,False],[False,False]], husty=True, premenna=False)+r"}"




class P3(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[]])
            E = abs(E) ; D = abs(D)
            if E != 1 and abs(A) != 1:
                break

        if A > 0:
            C = super().texRiesZlomCisla(-D, A-1, nicefrac=False, popZnamienko=True)[1:-1]
        else:
            C = super().texRiesZlomCisla(-D, A+1, nicefrac=False, popZnamienko=True)[1:-1]

        self.zadanie = super().prepis(r"h(t) = \cfrac{\sqrt{AA-t^2}}{\log_E(D+"+str(C)+r"t)}", [A,B,C,D,E])

        if A > 0:
            bod = super().texRiesZlomCisla((1-D)*(A-1),-D, nicefrac=False, popZnamienko=True)[1:-1]
            self.riesenie = super().texInterval([[-A,bod], [bod,A-1]], [[True,False],[False,False]], premenna=False)
            self.neriesenie = super().texInterval([[-A,bod], [bod,A-1]], [[True,False],[False,True]], premenna=False)
        else:
            bod = super().texRiesZlomCisla((1-D)*(A+1),-D, nicefrac=False, popZnamienko=True)[1:-1]
            self.riesenie = super().texInterval([[A+1,bod], [bod,-A]], [[False,False],[False,True]], premenna=False)
            self.neriesenie = super().texInterval([[A+1,bod], [bod,-A]], [[False,False],[False,False]], premenna=False)





class P4(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D = super().zvolKoef(4, [[]])
            if -B/A != -D/C:
                break

        self.zadanie = super().prepis(r"u(x) = \cfrac{Ax+B}{Cx+D}", [A,B,C,D])

        NB1 = super().texRiesZlomCisla(-B,A, nicefrac=False)[1:-1]
        NB2 = super().texRiesZlomCisla(-D,C, nicefrac=False)[1:-1]

        if -B/A < 0:
            if -D/C > 0:
                if B*D > 0:
                    self.riesenie = super().texInterval([[NB1,NB2]], [[True,False]], premenna=False)
                    self.neriesenie = super().texInterval([[NB1,NB2]], [[True,True]], premenna=False)
                else:
                    self.riesenie = super().texInterval([["-inf",NB1],[NB2,"inf"]], [[False,True],[False,False]], premenna=False)
                    self.neriesenie = super().texInterval([["-inf",NB1],[NB2,"inf"]], [[False,False],[False,False]], premenna=False)
            else:
                if -B/A > -D/C:
                    if B*D > 0:
                        self.riesenie = super().texInterval([["-inf",NB2],[NB1,"inf"]], [[False,False],[True,False]], premenna=False)
                        self.neriesenie = super().texInterval([["-inf",NB2],[NB1,"inf"]], [[False,True],[False,False]], premenna=False)
                    else:
                        self.riesenie = super().texInterval([[NB2,NB1]], [[False, True]], premenna=False)
                        self.neriesenie = super().texInterval([[NB2,NB1]], [[False, False]], premenna=False)
                else:
                    if B*D > 0:
                        self.riesenie = super().texInterval([["-inf",NB1],[NB2,"inf"]], [[False,True],[False,False]], premenna=False)
                        self.neriesenie = super().texInterval([["-inf",NB1],[NB2,"inf"]], [[False,False],[False,False]], premenna=False)
                    else:
                        self.riesenie = super().texInterval([[NB1,NB2]], [[True,False]], premenna=False)
                        self.neriesenie = super().texInterval([[NB1,NB2]], [[False,True]], premenna=False)
        else:
            if -D/C < 0:
                if B*D > 0:
                    self.riesenie = super().texInterval([[NB2,NB1]], [[False, True]], premenna=False)
                    self.neriesenie = super().texInterval([[NB2,NB1]], [[False, False]], premenna=False)
                else:
                    self.riesenie = super().texInterval([["-inf",NB2],[NB1,"inf"]], [[False,False],[True,False]], premenna=False)
                    self.neriesenie = super().texInterval([["-inf",NB2],[NB1,"inf"]], [[False,True],[True,False]], premenna=False)
            else:
                if -B/A > -D/C:
                    if B*D > 0:
                        self.riesenie = super().texInterval([["-inf",NB2],[NB1,"inf"]], [[False,False],[True,False]], premenna=False)
                        self.neriesenie = super().texInterval([["-inf",NB2],[NB1,"inf"]], [[False,False],[False,False]], premenna=False)
                    else:
                        self.riesenie = super().texInterval([[NB2,NB1]], [[False, True]], premenna=False)
                        self.neriesenie = super().texInterval([[NB2,NB1]], [[True, False]], premenna=False)
                else:
                    if  B*D > 0:
                        self.riesenie = super().texInterval([["-inf",NB1],[NB2,"inf"]], [[False,True],[False,False]], premenna=False)
                        self.neriesenie = super().texInterval([["-inf",NB1],[NB2,"inf"]], [[False,True],[True,False]], premenna=False)
                    else:
                        self.riesenie = super().texInterval([[NB1,NB2]], [[True,False]], premenna=False)
                        self.neriesenie = super().texInterval([[NB1,NB2]], [[False,False]], premenna=False)





class P5(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[5,5,5]])
            E = -abs(E)
            if E != -1:
                break

        znamienko = ""
        if C < 0:
            znamienko = "-"
        self.zadanie = super().prepis(r"\varphi(t) = At^3+Bt^2+"+znamienko+r"\frac{"+str(abs(C))+r"}{t}+D \enspace , \enspace t_0="+super().texRiesZlomCisla(1,E, nicefrac=False, popZnamienko=True)[1:-1], [A,B,C,D,E])
        self.riesenie = super().prepis(super().texRiesZlomCisla(A+B*E+C*E*E*E*E+D*E*E*E, E*E*E, nicefrac=False, popZnamienko=True)[1:-1], [A,B,C,D,E])
        self.neriesenie = super().prepis(super().texRiesZlomCisla(A+B*E+C*E*E+D*E*E*E, E*E*E, nicefrac=False, popZnamienko=True)[1:-1], [A,B,C,D,E])




class P6(Zadanie):
    def __init__(self):
        super().__init__()
        vetva = random()

        if vetva < 0.333:
            while True:
                A,B = super().zvolKoef(2, [[]])
                if abs(A) != 1:
                    break
            if A > 0:
                self.zadanie = super().prepis(r"w(x) = \frac{x}{A}+\frac{A}{x}", [A])
            else:
                A = -A
                self.zadanie = super().prepis(r"w(x) = -\frac{x}{A}-\frac{A}{x}", [A])
            self.riesenie = "0"
            self.neriesenie = choice(["1","2"])

        elif vetva < 0.666:
            while True:
                A,B,C,D = super().zvolKoef(4, [[]])
                D = abs(D)
                if D in [3,5,7,9] and B*B-4*A*C < 0:
                    break
            self.zadanie = super().prepis(r"w(x) = \sqrt[D]{Ax^2+Bx+C}", [A,B,C,D])
            self.riesenie = "0"
            self.neriesenie = choice(["1","2"])

        else:
            while True:
                A,B,C,D,E = super().zvolKoef(5, [[]])
                B = A*E+D
                C = D*E
                if B != 0:
                    break
            self.zadanie = super().prepis(r"w(x) = Ax^3+Bx^2+Cx", [A,B,C,D,E])
            self.riesenie = "3"
            self.neriesenie = choice(["1","2"])



# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), P5(), P6()]

