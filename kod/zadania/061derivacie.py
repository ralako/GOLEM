from zadanie import *
from random import random, randint
from numpy import sign


jazyk = None
jazyky = ["slovak", "czech", "english"]

def init(jazyk_):
    global jazyk
    jazyk = jazyk_



class P1(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            A = abs(A)
            if A > 1:
                break
        if B < 0:
            C = -A + B
        else:
            C = B
            if B >= A:
                A = B + randint(1,3)

        self.zadanie = super().prepis(r"f(x)=\frac{x}{A}+\frac{A}{x} \enspace , \enspace x_0=C", [A,B,C])
        if B < 0:
            self.riesenie = [r"\text{rastúca}", r"\text{rostoucí}", r"\text{increasing}"][jazyky.index(jazyk)]
            self.neriesenie = [r"\text{klesajúca}", r"\text{klesajíci}", r"\text{decreasing}"][jazyky.index(jazyk)]
        else:
            self.riesenie = [r"\text{klesajúca}", r"\text{klesajíci}", r"\text{decreasing}"][jazyky.index(jazyk)]
            self.neriesenie = [r"\text{rastúca}", r"\text{rostoucí}", r"\text{increasing}"][jazyky.index(jazyk)]



class P2(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            if 1 == 1:
                break

        self.zadanie = super().prepis(r"g(x)=x^2\, e^{Ax+B}", [A,B])
        bod = super().texRiesZlomCisla(-2,A, nicefrac=False, popZnamienko=True)[1:-1]
        if A > 0:
            self.riesenie = super().texInterval([[bod,0]], [[True,True]], premenna=False)
            self.neriesenie = super().texInterval([["-inf",0]], [[False,True]], premenna=False)[:-1] + r"\enspace , \enspace " + super().texInterval([[bod,"inf"]], [[True,False]], premenna=False)[1:]
        else:
            self.riesenie = super().texInterval([["-inf",0]], [[False,True]], premenna=False)[:-1] + r"\enspace , \enspace " + super().texInterval([[bod,"inf"]], [[True,False]], premenna=False)[1:]
            self.neriesenie = super().texInterval([[bod,0]], [[True,True]], premenna=False)



class P3(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            A = abs(A) ; B = abs(B)
            if A > 2 and A < 6:
                break

        self.zadanie = super().prepis(r"h(t)=\cfrac{\ln t}{Bt^A}", [A,B])
        self.riesenie = "1"
        self.neriesenie = choice(["0","2"])



class P4(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D = super().zvolKoef(4, [[]])
            if D in [3,5,7]:
                break

        self.zadanie = super().prepis(r"v(x)=C-\sqrt[D]{(Ax+B)^2}", [A,B,C,D])
        self.riesenie = r"$\text{áno}$"
        self.neriesenie = r"$\text{nie}$"



class P5(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[]])
            if D+E != 0 and B*(D+E)-2*D*E != 0 and D-E != 0:
                if (D+E) % 2 == 0 and (B*(D+E)-2*D*E) % 2 == 0:
                    break

        A = super().texRiesZlomCisla(D+E,2, nicefrac=False, popZnamienko=True)[1:-1]    # k
        C = super().texRiesZlomCisla(B*(D+E)-2*D*E,2, nicefrac=False, popZnamienko=True)[1:-1]

        self.zadanie = super().prepis(r"\varphi(x)=\cfrac{x^2+Bx+C}{x+A}", [A,B,C,D,E])
        if -D < -E:
            self.riesenie = r"$"+str(2*(E-D))+r"$"
            self.neriesenie = choice([r"$"+str(2*(D-E))+r"$", r"$"+str(2*(E-D-1))+r"$"])
        else:
            self.riesenie = r"$"+str(2*(D-E))+r"$"
            self.neriesenie = self.neriesenie = choice([r"$"+str(2*(E-D))+r"$", r"$"+str(2*(D-E+1))+r"$"])






class P6(Zadanie):
    def __init__(self):
        super().__init__()
        if random() < 0.5:  # vetva 1 (k > 0)
            while True:
                A,B,C,D,E,F = super().zvolKoef(6, [[]])
                A = abs(A)
                B = (A*F+E)/2
                C = E*F
                if -F > -E/A and (-E-sign(A)-2*A) % A == 0 and A*F+E != 0:
                    if self.omega(-E/A-1/A, A,B,C,D) > self.omega(-F, A,B,C,D) and self.omega(-F+2, A,B,C,D) > self.omega(-E/A, A,B,C,D):
                        break

            B_string = super().texRiesZlomCisla(A*F+E,2, nicefrac=False, popZnamienko=True)[1:-1]
            zlomok = super().texRiesZlomCisla(A,3, nicefrac=False, popZnamienko=True)[1:-1]
            zlomok2 = super().texRiesZlomCisla(-E-1,A, nicefrac=False, popZnamienko=True)[1:-1]
            interval = super().texInterval([[zlomok2, -F+2]], [[True, True]])[1:]
            self.zadanie = super().prepis(r"\omega(x)="+zlomok+r"x^3+"+B_string+r"x^2+Cx+D \enspace , \enspace ", [A,B,C,D,E,F])[:-1] + interval
            self.riesenie = r"$"+str((-F+2)*(-F))+r"$"
            self.neriesenie = choice([r"$"+str((-F+1)*(-F))+r"$", r"$"+str((-F)*(-F))+r"$"])

        else:   # vetva 2 (k < 0)
            while True:
                A,B,C,D,E,F = super().zvolKoef(6, [[]])
                A = -abs(A)
                B = (A*F+E)/2
                C = E*F
                if -F > -E/A and (-E-sign(A)-2*A) % A == 0 and A*F+E != 0:
                    if self.omega(-E/A-1/abs(A)-2, A,B,C,D) > self.omega(-F, A,B,C,D) and self.omega(-F+1, A,B,C,D) > self.omega(-E/A, A,B,C,D):
                        break

            B_string = super().texRiesZlomCisla(A*F+E,2, nicefrac=False, popZnamienko=True)[1:-1]
            C = E*F
            zlomok = super().texRiesZlomCisla(A,3, nicefrac=False, popZnamienko=True)[1:-1]
            zlomok2 = super().texRiesZlomCisla(-E-sign(A)-2*A,A, nicefrac=False, popZnamienko=True)[1:-1]
            interval = super().texInterval([[zlomok2, -F+1]], [[True, True]])[1:]
            self.zadanie = super().prepis(r"\omega(x)="+zlomok+r"x^3+"+B_string+r"x^2+Cx+D \enspace , \enspace ", [A,B,C,D,E,F])[:-1] + interval
            self.riesenie = super().texRiesZlomCisla(E*E+E*sign(A)+2*E*A, A*A, nicefrac=False, popZnamienko=True)
            self.neriesenie = choice([super().texRiesZlomCisla(E*E-E*sign(A)+2*E, A*A, nicefrac=False, popZnamienko=True),
                                      super().texRiesZlomCisla(E*E+E*sign(A)+4*E, A*A, nicefrac=False, popZnamienko=True),
                                      super().texRiesZlomCisla(E*E+E*sign(A)+2*E, -A*A, nicefrac=False, popZnamienko=True)])

    def omega(self, x, A,B,C,D):
        return (A/3)*x**3 + B*x**2 + C*x + D




# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), P5(), P6()]