from zadanie import *
from random import randint, random

# TOTO JE KOMPILAT 110 a 111


class P1(Zadanie):     # imaginarna cast
    def __init__(self):
        super().__init__()
        D,E,F = super().zvolKoef(3, [[]])
        A = randint(20,1000)
        B = randint(20,1000)
        C = randint(20,1000)
        self.zadanie = super().prepis(r'i^{A}+Di^{B}+Ei^{-C}+F', [A,B,C,D,E,F])

        vysledok = 0
        
        if A % 4 == 1:
            vysledok += 1
        elif A % 4 == 3:
            vysledok -= 1

        if B % 4 == 1:
            vysledok += D
        elif B % 4 == 3:
            vysledok -= D

        if C % 4 == 1:
            vysledok -= E
        elif C % 4 == 3:
            vysledok += E

        self.riesenie = r'$' + str(vysledok) + r'$'
        if vysledok == 1+D+E:
            self.neriesenie = r'$' + str(1+D+E+F) + r'$'
        else:
            self.neriesenie = r'$' + str(1+D+E) + r'$'



        

class P2(Zadanie):     # zjednodusenie vyrazu
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G = super().zvolKoef(7, [[]])
            if abs(G) != 1:
                break
        self.zadanie = super().prepis(r'G(A+Bi)-(C+Di)\overline{(E+Fi)}', [A,B,C,D,E,F,G])
        self.riesenie = self.texKomplexneCislo(G*A-C*E-D*F , G*B+C*F-D*E)
        nahoda = random()
        if nahoda < 0.33:
            self.neriesenie = self.texKomplexneCislo(G*A+C*E-D*F , G*B+C*F-D*E)
        elif nahoda < 0.66:
            self.neriesenie = self.texKomplexneCislo(G*A-C*E-D*F , G*B-C*F-D*E)
        else:
            self.neriesenie = self.texKomplexneCislo(G*A-C*E-2*D*F , G*B+C*F-D*E)
        




class P3(Zadanie):     # exponencionalny tvar
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G,H = super().zvolKoef(8, [[]])
            B = abs(B) ; C = abs(C)
            E = abs(E) ; F = abs(F)
            #G = abs(G) ; H = abs(H)
            if B/C <= 2 and E/F <= 2 and H != 1 and D != 1 and G != 1:
                if abs(D**H) <= 1000:
                    break
        if H < 0:
            D = 1
        aa = super().texRiesZlomPi(B,C, nicefrac=False, popZnamienko = True)[1:-1]
        bb = super().texRiesZlomPi(E,F, nicefrac=False, popZnamienko = True)[1:-1]
        
        vyber = random()
        if vyber < 2:
            self.zadanie = super().prepis(r'\left(De^{i' + bb + r'}\right)^{H}\left(\cos{' + aa + r'}+i\sin{' + aa + r'}\right)^{G}', [A,B,C,D,E,F,G,H])
            cit = H*E*C + F*B*G
            citfake = H*E*C - F*B*G
            men = F*C
            while True:
                if cit >= 2*men:
                    cit -= 2*men
                elif cit < 0:
                    cit += 2*men
                else:
                    break
            while True:
                if citfake >= 2*men:
                    citfake -= 2*men
                elif citfake < 0:
                    citfake += 2*men
                else:
                    break
            if cit == 0:
                self.riesenie = r'$' + str(int(D**H)) + r'$'
                self.neriesenie = r'$' + str(int(D**H)) + r'e^{i\pi}$'
            else:
                A = super().texRiesZlomPi(cit,men, nicefrac=False, popZnamienko = True)[1:-1]
                Afake = super().texRiesZlomPi(citfake,men, nicefrac=False, popZnamienko = True)[1:-1]
                while Afake == A:
                    citfake += 1
                    Afake = super().texRiesZlomPi(citfake,men, nicefrac=False, popZnamienko = True)[1:-1]                        
                self.riesenie = r'$' + super().check(str(int(D**H)) + r'e^{i' + A + r'}') + r'$'
                self.neriesenie = r'$' + super().check(str(int(D**H)) + r'e^{i' + Afake + r'}') + r'$'



class P4(Zadanie):     # argument
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




class P5(Zadanie):     # zjednodusenie vyrazu
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
        



class P6(Zadanie):     # exponencionalny tvar
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
    return [P1(),P2(),P3(),P4(),P5(),P6()]


