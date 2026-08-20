from zadanie import *
from random import randint, random


class P21(Zadanie):     # imaginarna cast
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



class P22(Zadanie):     # kvadraticka rovnica
    def __init__(self):
        super().__init__()
        while True:
            A,B,C = super().zvolKoef(3, [[]])
            if B*B - 4*A*C < 0 and A > 0:
                break
            
        self.zadanie = super().prepis(r'Ax^2+Bx+C=0', [A,B,C])

        re = super().texRiesZlomCisla(-B, 2*A, nicefrac=False)[1:-1]
        D = 4*A*C-B*B
        odmocnina = super().texRiesSqrt(D)[1:-1]

        if len(odmocnina) < 4:
            im = super().texRiesZlomCisla(int(odmocnina),2*A,nicefrac=False,popZnamienko=True)[1:-1]
        else:
            im = super().texRiesZlomCisla(1,2*A,pripoj=odmocnina,nicefrac=False,popZnamienko=True)[1:-1]

        self.riesenie = super().texKomplexneCislo(re,im,pm=True)
        
        nahoda = random()
        
        if nahoda < 0.5:
            D = 8*A*C-B*B
            odmocninafake = super().texRiesSqrt(D)[1:-1]
            if len(odmocninafake) < 4:
                im = super().texRiesZlomCisla(int(odmocninafake),2*A,nicefrac=False,popZnamienko=True)[1:-1]
            else:
                im = super().texRiesZlomCisla(1,2*A,pripoj=odmocninafake,nicefrac=False,popZnamienko=True)[1:-1]
            self.neriesenie = super().texKomplexneCislo(re,im,pm=True)
            
        else:
            D = 4*A*C-B*B
            odmocninafake = super().texRiesSqrt(D)[1:-1]
            if len(odmocninafake) < 4:
                im = super().texRiesZlomCisla(int(odmocninafake),A,nicefrac=False,popZnamienko=True)[1:-1]
            else:
                im = super().texRiesZlomCisla(1,A,pripoj=odmocninafake,nicefrac=False,popZnamienko=True)[1:-1]
            self.neriesenie = super().texKomplexneCislo(re,im,pm=True)
            



class P23(Zadanie):     # rovnica
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F = super().zvolKoef(6, [[1,1,3,4],[2,2,3,4],[1,4,5],[2,4,6],[1,3,6],[3,5,6]])
        self.zadanie = super().prepis(r'(A+Bi)(Cx+Dyi)=E+Fi', [A,B,C,D,E,F])
        self.riesenie = super().texRiesZlomCisla(E*A*D + B*F*D + A*C*F - B*C*E , C*D*(A*A+B*B))
        nahoda = random()
        if nahoda < 0.33:
            self.neriesenie = super().texRiesZlomCisla(E*A*D - B*F*D + A*C*F - B*C*E , C*D*(A*A+B*B))
        elif nahoda < 0.66:
            self.neriesenie = super().texRiesZlomCisla(E*A*D + B*F*D - A*C*F - B*C*E , C*D*(A*A+B*B))
        else:
            self.neriesenie = super().texRiesZlomCisla(E*A*D + B*F*D + A*C*F + B*C*E , C*D*(A*A+B*B))
        
        

class P24(Zadanie):     # zjednodusenie vyrazu
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F,G = super().zvolKoef(7, [[]])
        self.zadanie = super().prepis(r'G(A+Bi)-(C+Di)\overline{(E+Fi)}', [A,B,C,D,E,F,G])
        self.riesenie = self.texKomplexneCislo(G*A-C*E-D*F , G*B+C*F-D*E)
        nahoda = random()
        if nahoda < 0.33:
            self.neriesenie = self.texKomplexneCislo(G*A+C*E-D*F , G*B+C*F-D*E)
        elif nahoda < 0.66:
            self.neriesenie = self.texKomplexneCislo(G*A-C*E-D*F , G*B-C*F-D*E)
        else:
            self.neriesenie = self.texKomplexneCislo(G*A-C*E-2*D*F , G*B+C*F-D*E)
        


class P25(Zadanie):     # realna cast
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D = super().zvolKoef(4, [[1,1,3,3],[1,2,3,4],[2,2,4,4],[2,2,3,3],[1,1,4,4],[3,3,3,3],[3,3,4,4],[4,4,4,4]])
            if A != C and B != D:
                if A != -C and B != -D:
                    break
        self.zadanie = r'$\left(\frac{' + str(self.texKomplexneCislo(A,B)[1:-1]) + r'}{' + str(self.texKomplexneCislo(C,D)[1:-1]) + r'}\right)^2$'
        self.riesenie = super().texRiesZlomCisla((A*C+B*D)**2 - (B*C-A*D)**2 , (C*C+D*D)**2)
        nahoda = random()
        if nahoda < 0.33:
            self.neriesenie = super().texRiesZlomCisla((A*C+B*D)**2 + (B*C-A*D)**2 , (C*C+D*D)**2)
        elif nahoda < 0.66:
            if C*C+D*D != 2 and C+D != 0:
                self.neriesenie = super().texRiesZlomCisla((A*C+B*D)**2 - (B*C-A*D)**2 , (C+D)**2)
            else:
                self.neriesenie = super().texRiesZlomCisla((A*C+B*D)**2 - (B*C-A*D)**2 , (C*C+D*D+1)**2)
        else:
            self.neriesenie = super().texRiesZlomCisla(-(A*C+B*D)**2 - (B*C-A*D)**2 , (C*C+D*D)**2)
        


class P26(Zadanie):     # exponencionalny tvar
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
                


###---------


def prikladyLoad():
    return [P21(),P22(),P23(),P24(),P25(),P26()]


