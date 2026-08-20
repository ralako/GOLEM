from zadanie import *

jazyk = None

def init(jazyk_):
    global jazyk
    jazyk = jazyk_



# TECNY

class P1(Zadanie):     # Je v bode rastuca
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F = super().zvolKoef(6, [[1,4,6,6],[1,5,6]])
            if D*F != -E:
                break
        self.zadanie = r'$f(x)=' + super().texRiesZlom([C,B,A], [E,D])[1:-1] + r'\enspace , \enspace x_0='+str(F)+r'$'
        citatelDer = A*D*F*F + 2*A*E*F + B*E - C*D
        #print(self.zadanie, citatelDer)
        if citatelDer > 0:
            self.riesenie = super().text(['áno','ano','yes'])
            self.neriesenie = super().text(['nie','ne','no'])
        else:
            self.riesenie = super().text(['nie','ne','no'])
            self.neriesenie = super().text(['áno','ano','yes'])



class P2(Zadanie):     # Je v bode konvexná
    def __init__(self):
        super().__init__()
        A,B,C,D,E,F = super().zvolKoef(6, [[1,6,6,6],[2,6,6]])
        self.zadanie = r'$f(x)=' + super().texRiesPoly([E,D,C,B,A])[1:-1] + r'\enspace , \enspace x_0='+str(F)+r'$'
        Der = 12*A*F*F + 6*B*F + 2*C
        if Der > 0:
            self.riesenie = super().text(['áno','ano','yes'])
            self.neriesenie = super().text(['nie','ne','no'])
        else:
            self.riesenie = super().text(['nie','ne','no'])
            self.neriesenie = super().text(['áno','ano','yes'])


class P3(Zadanie):     # Sucet stac a inflex
    def __init__(self):
        super().__init__()
        A,B = super().zvolKoef(2, [[]])
        self.zadanie = r'$f(x)=' + super().prepis(r'Axe^{Bx}',[A,B])[1:]
        self.riesenie = super().texRiesZlomCisla(-3,B)
        self.neriesenie = super().texRiesZlomCisla(1,B)
        


class P4(Zadanie):     # stac max min
    def __init__(self):
        super().__init__(maxnum=6)
        while True:
            A,B,C = super().zvolKoef(3, [[]])
            if A > 0 and (B*B - 4*A*C) < 0:
                break
        self.zadanie = r'$f(x)=' + super().prepis(r'\sqrt{Ax^2+Bx+C}',[A,B,C])[1:]
        DDerCit = 4*A*C - B*B
        if DDerCit < 0:
            self.riesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace' + super().text(['lomax', 'lomax', 'lomax']) + r'$'
            self.neriesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace' + choice(5*[super().text(['lomin', 'lomin', 'lomin'])] + [super().text(['sedlo', 'sedlo', 'saddle'])]) + r'$'
        elif DDerCit > 0:
            self.riesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace' + super().text(['lomin', 'lomin', 'lomin']) + r'$'
            self.neriesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace' + choice(5*[super().text(['lomax', 'lomax', 'lomax'])] + [super().text(['sedlo', 'sedlo', 'saddle'])]) + r'$'
        else:
            self.riesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace' + super().text(['sedlo', 'sedlo', 'saddle']) + r'$'
            self.neriesenie = super().texRiesZlomCisla(-B,2*A)[:-1] + r'\enspace , \enspace' + choice([super().text(['lomax', 'lomax', 'lomax']),super().text(['lomin', 'lomin', 'lomin'])]) + r'$'





            
# GENERACIA

def prikladyLoad():
    return [P1(), P2(), P3(), P4(), blank(), blank()]
