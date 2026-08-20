from zadanie import *
from random import random, choice
from math import e

jazyk = None

def init(jazyk_):
    global jazyk
    jazyk = jazyk_



# TECNY

class P1(Zadanie):     # par der a gradient
    def __init__(self):
        super().__init__()
        while True:
            A,B,C = super().zvolKoef(3, [[]])
            A = abs(A) ; B = abs(B) ; C = abs(C)
            if C == 2 or C == 3 or C == 4:
                break
        
        D = 2*A
        E = C-1
        F = 2*B

        global koef12
        koef12 = [A,B,C,D,E,F]
        
        nahoda = random()

        vybersi = choice([0,1])
        
        if C == 2:
            self.zadanie = super().prepis(r'f(x,y) = \sqrt{Ax^2y + Bxy^2}', [A,B,C])[:-1] + r'\enspace , \enspace ' + [r'\pdv{f}{x}', r'\pdv{f}{y}'][vybersi] + r'$'
            self.riesenie = super().prepis([r'\frac{Dxy+By^2}{C\,\sqrt{Ax^2y+Bxy^2}}', r'\frac{Ax^2+Fxy}{C\,\sqrt{Ax^2y+Bxy^2}}'][vybersi], [A,B,C,D,E,F])
            if nahoda < 0.25:
                self.neriesenie = super().prepis([r'\frac{Axy+By^2}{C\,\sqrt{Ax^2y+Bxy^2}}', r'\frac{Ax^2+Bxy}{C\,\sqrt{Ax^2y+Bxy^2}}'][vybersi], [A,B,C,D,E,F])
            elif nahoda < 0.5:
                self.neriesenie = super().prepis([r'\frac{Dxy-By^2}{C\,\sqrt{Ax^2y+Bxy^2}}', r'\frac{Ax^2-Fxy}{C\,\sqrt{Ax^2y+Bxy^2}}'][vybersi], [A,B,C,D,E,F])
            elif nahoda < 0.75:
                self.neriesenie = super().prepis([r'\frac{Dxy+By^2}{\sqrt{Ax^2y+Fxy^2}}', r'\frac{Ax^2+Fxy}{\sqrt{Ax^2y+Fxy^2}}'][vybersi], [A,B,C,D,E,F])
            else:
                self.neriesenie = super().prepis([r'\frac{Axy-Fy^2}{C\,\sqrt{Ax^2y+Bxy^2}}', r'\frac{Ax^2-Fxy}{\sqrt{Ax^2y+Bxy^2}}'][vybersi], [A,B,C,D,E,F])
        else:
            self.zadanie = super().prepis(r'f(x,y) = \sqrt[C]{Ax^2y + Bxy^2}',[A,B,C])[:-1]  + r'\enspace , \enspace ' + [r'\pdv{f}{x}', r'\pdv{f}{y}'][vybersi] + r'$'
            self.riesenie = super().prepis([r'\frac{Dxy+By^2}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}', r'\frac{Ax^2+Fxy}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}'][vybersi], [A,B,C,D,E,F])
            if nahoda < 0.25:
                self.neriesenie = super().prepis([r'\frac{Axy+By^2}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}', r'\frac{Ax^2+Bxy}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}'][vybersi], [A,B,C,D,E,F])
            elif nahoda < 0.5:
                self.neriesenie = super().prepis([r'\frac{Dxy-By^2}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}', r'\frac{Ax^2-Fxy}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}'][vybersi], [A,B,C,D,E,F])
            elif nahoda < 0.75:
                self.neriesenie = super().prepis([r'\frac{Dxy+Fy^2}{\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}', r'\frac{Dx^2+Fxy}{\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}'][vybersi], [A,B,C,D,E,F])
            else:
                self.neriesenie = super().prepis([r'\frac{Dxy-By^2}{C\,\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}', r'\frac{Ax^2-Bxy}{C\sqrt[C]{(Ax^2y+Bxy^2)^{E}}}'][vybersi], [A,B,C,D,E,F])


class P2(Zadanie):
    def __init__(self):
        super().__init__()
        global koef12
        A,B,C,D,E,F = koef12
        while True:
            G,H = super().zvolKoef(2,[[]])
            G = abs(G) ; H = abs(H)
            if G < 5 and H < 5:
                if A*G*G*H + B*G*H*H > 0:
                    break
        
        self.zadanie = r'$A = ['+str(G)+r', '+str(H)+r']$'
        I = D*G*H + B*H*H
        J = A*G*G*H + B*G*H*H
        K = A*G*G + F*G*H
        L = 2*I
        M = 2*K
        nahoda = random()
        if C == 2:
            self.riesenie = super().prepis(r'\left( \frac{I}{C\,\sqrt{J}} \;,\; \frac{K}{C\,\sqrt{J}} \right)', [A,B,C,D,E,F,G,H,I,J,K])
            if nahoda < 0.5:
                self.neriesenie = super().prepis(r'\left( \frac{L}{C\,\sqrt{J}} \;,\; \frac{K}{C\,\sqrt{J}} \right)', [A,B,C,D,E,F,G,H,I,J,K,L,M])
            else:
                self.neriesenie = super().prepis(r'\left( \frac{I}{C\,\sqrt{J}} \;,\; \frac{M}{C\,\sqrt{J}} \right)', [A,B,C,D,E,F,G,H,I,J,K,L,M])
        else:
            self.riesenie = super().prepis(r'\left( \frac{I}{C\,\sqrt[C]{J^E}} \;,\; \frac{K}{C\,\sqrt[C]{J^E}} \right)', [A,B,C,D,E,F,G,H,I,J,K])
            if nahoda < 0.5:
                self.neriesenie = super().prepis(r'\left( \frac{L}{C\,\sqrt[C]{J^E}} \;,\; \frac{K}{C\,\sqrt[C]{J^E}} \right)', [A,B,C,D,E,F,G,H,I,J,K,L,M])
            else:
                self.neriesenie = super().prepis(r'\left( \frac{I}{C\,\sqrt[C]{J^E}} \;,\; \frac{M}{C\,\sqrt[C]{J^E}} \right)', [A,B,C,D,E,F,G,H,I,J,K,L,M])




class P3(Zadanie):
    def __init__(self):
        super().__init__()
        vetva = choice(["log","sin"])
        if vetva == "log":
            while True:
                A,B = super().zvolKoef(2, [[]])
                if abs(A) <= 6:
                    break
            A = abs(A)-1
            
            nahoda = random()
            global d0string

            if A == 0:
                self.zadanie = super().prepis(r'g(x,y) = \ln\frac{x}{y} \enspace , \enspace D=[1,1,?]', [A])
                d0string = "D_0 = [1,1]"
                self.riesenie = super().prepis(r'x - y - z + A = 0', [A])
                if nahoda < 0.5:
                    self.neriesenie = super().prepis(r'x + y + z + A = 0', [A])
                else:
                    B = A+1
                    self.neriesenie = super().prepis(r'x - y - z + B = 0', [A,B])
                    
            elif A == 1:
                self.zadanie = super().prepis(r'g(x,y) = \ln\frac{x}{y} \enspace , \enspace D=[e,1,?]', [A])
                d0string = "D_0 = [e,1]"
                self.riesenie = super().prepis(r'\frac{x}{e} - y - z + A = 0', [A])
                if nahoda < 0.5:
                    self.neriesenie = super().prepis(r'\frac{x}{e} + y + z + A = 0', [A])
                else:
                    B = A+1
                    self.neriesenie = super().prepis(r'\frac{x}{e} - y - z + B = 0', [A,B])

            else:
                self.zadanie = super().prepis(r'g(x,y) = \ln\frac{x}{y} \enspace , \enspace D=[e^{A},1,?]', [A])
                d0string = super().prepis("D_0 = [e^{A},1]", [A])[1:-1]
                self.riesenie = super().prepis(r'\frac{x}{e^A} - y - z + A = 0', [A])
                if nahoda < 0.5:
                    self.neriesenie = super().prepis(r'\frac{x}{e^A} + y + z + A = 0', [A])
                else:
                    B = A+1
                    self.neriesenie = super().prepis(r'\frac{x}{e^B} - y - z + B = 0', [A,B])


        if vetva == "sin":
            while True:
                A,B = super().zvolKoef(2, [[]])
                if abs(A) <= 7 and abs(A) != 4:
                    break
            A = abs(A)-4
            
            nahoda = random()

            self.zadanie = super().prepis(r'g(x,y) = \sin\frac{x}{y} \enspace , \enspace D = [0, A, ?]', [A])
            d0string = super().prepis("D_0 = [0,A]", [A])[1:-1]

            self.riesenie = super().prepis(r'x-Az=0', [A])

            if nahoda < 0.5:
                self.neriesenie = super().prepis(r'x-Az=1', [A])
            else:
                self.neriesenie = super().prepis(r'x+Az=0', [A])
        

        global koef34
        koef34 = [vetva,A]





class P4(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B = super().zvolKoef(2, [[]])
            if abs(A) <= 3 and abs(B) <= 3:
                break
        kA = choice([10,100])
        kB = choice([10,100])
        A = round(A/kA, 3)
        B = round(B/kB, 3)

        # print(A,B)
        global d0string

        global koef34
        vetva, C = koef34

        nahoda = random()

        if vetva == "log":

            self.zadanie = super().prepis(r'\Delta x = {A} \enspace,\enspace \Delta y = {B} \enspace,\enspace '+d0string, [A,B])
            
            self.riesenie = r'$' + str(round(A/e**C - B + C, 3)) + r'$'

            if nahoda < 0.5 and A != B:
                self.neriesenie = r'$' + str(round(A/e**C - A + C, 3)) + r'$'
            else:
                self.neriesenie = r'$' + str(round(A/e**C + B + C, 3)) + r'$'
        

        if vetva == "sin":
            self.zadanie = super().prepis(r'\Delta x = {A} \enspace,\enspace \Delta y = {B} \enspace,\enspace '+d0string, [A,B])
            
            self.riesenie = r'$' + str(round(A/C, 3)) + r'$'

            if nahoda < 0.5 and abs(C) != 1:
                self.neriesenie = r'$' + str(round(A*C, 3)) + r'$'
            elif A != B:
                self.neriesenie = r'$' + str(round(B/C, 3)) + r'$'
            else:
                self.neriesenie = r'$' + str(round(2*A/C, 3)) + r'$'





class P5(Zadanie):
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D = super().zvolKoef(4, [[2,4,4]])
            if abs(A) < 8 and abs(B) < 8 and abs(C) < 8:
                if 4*A*B - C*C > 0:
                    break
        
        global koef56
        koef56 = [A,B,C,D]
        
        self.zadanie = super().prepis(r'h(x,y) = Ax^2+By^2+Cxy+Dx', [A,B,C,D])

        nahoda = random()

        self.riesenie = super().texRiesZlomCisla(-B*D*D, 4*A*B-C*C)

        if nahoda < 0.5:
            self.neriesenie = super().texRiesZlomCisla(-B*D*D+1, 4*A*B-C*C)
        else:
            self.neriesenie = super().texRiesZlomCisla(-B*D*D, 4*A*B+C*C)




class P6(Zadanie):
    def __init__(self):
        super().__init__()
        global koef56
        A,B,C,D = koef56
        while True:
            E,F = super().zvolKoef(2, [[]],)
            if abs(B*F*E*E) < 100 and abs(C*F*E) < 100:
                break


        self.zadanie = super().prepis(r'y = Ex+F', [A,B,C,D,E,F])

        self.riesenie = r'$\left[' + super().texRiesZlomCisla(-C*F-D-2*B*F*E, 2*A+2*B*E*E+2*C*E, nicefrac=False)[1:-1] + r'\;,\;' + super().texRiesZlomCisla(C*E*F-E*D+2*A*F, 2*A+2*B*E*E+2*C*E, nicefrac=False)[1:-1] + r'\right]$'

        nahoda = random()
        if nahoda < 0.5:
            self.neriesenie = r'$\left[' + super().texRiesZlomCisla(-C*F-D+2*B*F*E, 2*A+2*B*E*E+2*C*E, nicefrac=False)[1:-1] + r'\;,\;' + super().texRiesZlomCisla(C*E*F-E*D+2*A*F, 2*A+2*B*E*E+2*C*E, nicefrac=False)[1:-1] + r'\right]$'
        else:
            self.neriesenie = r'$\left[' + super().texRiesZlomCisla(-C*F-D-2*B*F*E, 2*A+2*B*E*E+2*C*E, nicefrac=False)[1:-1] + r'\;,\;' + super().texRiesZlomCisla(C*E*F-E*D+2*A*F, 2*A+2*B*E*E-2*C*E, nicefrac=False)[1:-1] + r'\right]$'



            
# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), P5(), P6()]
