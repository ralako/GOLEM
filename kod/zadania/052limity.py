from zadanie import *
from random import random


jazyk = None
jazyky = ["slovak", "czech", "english"]

def init(jazyk_):
    global jazyk
    jazyk = jazyk_




class P1(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E = super().zvolKoef(5, [[]])
            if 1 == 1:
                break
        D = abs(D)
        if E > 0:   # vetva 1
            self.zadanie = super().prepis(r'\displaystyle\lim_{x\to'+super().texRiesZlomCisla(-B,A)[1:-1]+r'}{\frac{C}{(Ax+B)^{'+str(2*D+1)+r'}}}',[A,B,C,D])
            self.riesenie = [r"\text{neexistuje}", r"\text{neexistuje}", r"\text{does not exist}"][jazyky.index(jazyk)]
            self.neriesenie = [r"\text{existuje}", r"\text{existuje}", r"\text{does exist}"][jazyky.index(jazyk)]
        else:       # vetva 2
            self.zadanie = super().prepis(r'\displaystyle\lim_{x\to'+super().texRiesZlomCisla(-B,A)[1:-1]+r'}{\frac{C}{(Ax+B)^{'+str(2*D)+r'}}}',[A,B,C,D])
            self.riesenie = [r"\text{existuje}", r"\text{existuje}", r"\text{does exist}"][jazyky.index(jazyk)]
            self.neriesenie = [r"\text{neexistuje}", r"\text{neexistuje}", r"\text{does not exist}"][jazyky.index(jazyk)]



class P2(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C = super().zvolKoef(3, [[]])
            C = abs(C)
            if C > 1:
                break

        if C >= 8:
            C = "e"
        self.zadanie = super().prepis(r"\displaystyle\lim_{x\to\infty}{"+str(C)+r"^{A+Bx^2}}",[A,B])
        if B > 0:
            self.riesenie = [r"\text{diverguje}", r"\text{diverguje}", r"\text{diverge}"][jazyky.index(jazyk)]
            self.neriesenie = [r"\text{konverguje}", r"\text{konverguje}", r"\text{converge}"][jazyky.index(jazyk)]
        else:
            self.riesenie = [r"\text{konverguje}", r"\text{konverguje}", r"\text{converge}"][jazyky.index(jazyk)]
            self.neriesenie = [r"\text{diverguje}", r"\text{diverguje}", r"\text{diverge}"][jazyky.index(jazyk)]



class P3(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F = super().zvolKoef(6, [[]])
            if 1 == 1:
                break
        A = abs(A)
        if F > 0:   # vetva 1
            self.zadanie = super().prepis(r'\displaystyle\lim_{x\to\infty}{\left(Ax - \sqrt{AAx^2+Bx+C}\right)}',[A,B,C])
            self.riesenie = super().texRiesZlomCisla(-B, 2*A, nicefrac=False, popZnamienko=True)
            nahoda = random()
            if nahoda < 0.33:
                self.neriesenie = super().texRiesZlomCisla(B, 2*A, nicefrac=False, popZnamienko=True)
            elif nahoda < 0.66:
                self.neriesenie = super().texRiesZlomCisla(-B, A, nicefrac=False, popZnamienko=True)
            else:
                self.neriesenie = super().texRiesZlomCisla(B, A, nicefrac=False, popZnamienko=True)
        else:       # vetva 2
            self.zadanie = super().prepis(r'\displaystyle\lim_{x\to\infty}{\left(\sqrt{AAx^2+Bx+C} - \sqrt{AAx^2+Dx+E}\right)}',[A,B,C,D,E])
            self.riesenie = super().texRiesZlomCisla(B-D, 2*A, nicefrac=False, popZnamienko=True)
            nahoda = random()
            if nahoda < 0.33:
                self.neriesenie = super().texRiesZlomCisla(B+D, 2*A, nicefrac=False, popZnamienko=True)
            elif nahoda < 0.66:
                self.neriesenie = super().texRiesZlomCisla(B+D, A, nicefrac=False, popZnamienko=True)
            else:
                self.neriesenie = super().texRiesZlomCisla(B-D, A, nicefrac=False, popZnamienko=True)



class P4(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D = super().zvolKoef(4, [[]])
            if B != C and abs(D) > 1:
                break
        D = abs(D)
        self.zadanie = super().prepis(r'\displaystyle\lim_{x\to\infty}{\left( \frac{Ax+B}{Ax+C} \right)^{\nicefrac{x}{D}}}',[A,B,C,D])
        zlomok = super().texRiesZlomCisla(B-C, A*D)[1:-1]
        if zlomok == "0":
            self.riesenie = r"$1$"
        elif zlomok == "1":
            self.riesenie = r"$e$"
        else:
            self.riesenie = r"$e^{"+zlomok+r"}$"
        if random() > 0.5:
            zlomok2 = super().texRiesZlomCisla(B+C, A*D)[1:-1]
            if zlomok2 == "0":
                self.neriesenie = r"$1$"
            elif zlomok2 == "1":
                self.neriesenie = r"$e$"
            else:
                self.neriesenie = r"$e^{"+zlomok2+r"}$"
        else:
            self.neriesenie = r"$\infty$"
        



class P5(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F = super().zvolKoef(6, [[3,5,5]])
            E = abs(E)
            if abs(A) != 1 and (B-E*A) != 0 and (B+E*A) != 0 and (C*E*E+D) != 0:
                break
        
        if F > 0:   # vetva 1
            self.zadanie = super().prepis(r"\displaystyle\lim_{x\to -E}{\;\frac{Ax^2+"+str(B+E*A)+r"x+BE}{x^2-EE}}", [A,B,C,D,E])
            self.riesenie = super().texRiesZlomCisla(-A*E+B, -2*E, nicefrac=False, popZnamienko=True)
            if random() > 0.5:
                self.neriesenie = super().texRiesZlomCisla(-A*E+B, -2*E*A, nicefrac=False, popZnamienko=True)
            else:
                self.neriesenie = r"$0$"
        else:       # vetva 2
            self.zadanie = super().prepis(r"\displaystyle\lim_{x\to -E}{\;\frac{Ax^2+"+str(B+E*A)+r"x+BE}{Cx^3+CEx^2+Dx+ED}}", [A,B,C,D,E])
            self.riesenie = super().texRiesZlomCisla(-A*E+B, C*E*E+D, nicefrac=False, popZnamienko=True)
            if random() > 0.5:
                self.neriesenie = super().texRiesZlomCisla(-A*E+B, A*(C*E*E+D), nicefrac=False, popZnamienko=True)
            else:
                self.neriesenie = r"$0$"




class P6(Zadanie):
    def __init__(self):
        super().__init__()
        vetva = random()
        if vetva <= 0.5:    # vetva 1
            while True:
                A,B,C,D,E,F = super().zvolKoef(6, [[]])
                if A > 0 and A*F+B > 0:
                    break
            E = abs(E)
            self.zadanie = super().prepis(r"\displaystyle\lim_{x\to F}{\;\frac{"+super().texRiesSqrt(A*F+B)[1:-1]+r"-\sqrt{Ax+B}}{Ex-FE}}", [A,B,C,D,E,F])
            (citatel,menovatel) = super().texRiesZlomCisla(-A, 2*E, nicefrac=False, textoutput=False)
            odmocnina = super().texRiesSqrt(A*F+B)[1:-1]
            if r"\sqrt" in odmocnina:
                self.riesenie = super().check(r"$\frac{"+str(citatel)+r"}{"+str(menovatel)+odmocnina+r"}$")
            elif int(menovatel)*int(odmocnina) == 1:
                self.riesenie = super().check(r"$"+str(citatel)+r"$")
            else:
                self.riesenie = super().texRiesZlomCisla(int(citatel), int(menovatel)*int(odmocnina), nicefrac=False, popZnamienko=True)
                #self.riesenie = super().check(r"$\frac{"+str(citatel)+r"}{"+str(int(menovatel)*int(odmocnina))+r"}$")

            if random() > 0.5:
                self.neriesenie = r"$\infty$"
            else:
                self.neriesenie = r"$0$"

        else:       # vetva 2
            while True:
                A,B,C,D,E = super().zvolKoef(5, [[1,1,1],[3,3,3],[1,4,5,5],[2,3,5,5]])
                A = abs(A) ; E = abs(E)
                if A+C>0 and A*D+B*C>0 and D != B:
                    break
            self.zadanie = super().prepis(r"\displaystyle\lim_{x\to "+super().texRiesZlomCisla(D-B,A+C)[1:-1]+r"}{\;\frac{Ex-"+super().texRiesZlomCisla(E*(D-B),A+C, nicefrac=False, popZnamienko=True)[1:-1]+r"}{\sqrt{Ax+B} - \sqrt{D-Cx}}}", [A,B,C,D,E])

            (citatelpodsqrt, menovatelpodsqrt) = super().texRiesZlomCisla(2*2*E*E*(A*D+B*C), (A+C)**3, nicefrac=False, textoutput=False)
            citatel = super().texRiesSqrt(citatelpodsqrt)[1:-1]
            menovatel = super().texRiesSqrt(menovatelpodsqrt)[1:-1]
            if r"\sqrt" in citatel or r"\sqrt" in menovatel:
                if r"\sqrt" not in menovatel:
                    if int(menovatel) == 1:
                        self.riesenie = r"$"+super().check(citatel)+r"$"
                    else: self.riesenie = super().prepis(r"\frac{"+citatel+r"}{"+menovatel+r"}", [A,B,C,D,E])
                else:
                    self.riesenie = super().prepis(r"\frac{"+citatel+r"}{"+menovatel+r"}", [A,B,C,D,E])
            else:
                if int(menovatel) == 1:
                    self.riesenie = super().check(citatel)
                else:
                    self.riesenie = super().texRiesZlomCisla(int(citatel),int(menovatel), nicefrac=False, popZnamienko=True)

            if random() > 0.5:
                self.neriesenie = r"$\infty$"
            else:
                self.neriesenie = r"$0$"

            



# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), P5(), P6()]

