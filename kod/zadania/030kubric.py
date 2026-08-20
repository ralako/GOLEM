from zadanie import *
jazyk = None
def init(jazyk_):
    global jazyk
    jazyk = jazyk_

class P1(Zadanie):  # kubická rovnica (sucet rieseni)
    def __init__(self, narocnost):
        super().__init__()
        while True:
            if narocnost == 3:
                A,B,C,D,E,F,G = super().zvolKoef(7, [[2,4,7],[2,5,7],[3,4,7],[3,5,7]], limit=60)
            else:
                A,B,C,D,E,F,G = super().zvolKoef(7, [[1,2,4,7],[1,2,5,7],[1,3,4,7],[1,3,5,7]], limit=60)
            F = 1
            if narocnost == 3:
                A = choice([-1,1])
            elif narocnost == 1:
                B = 1 ; D = 1
            elif narocnost == 0:
                B = 1 ; D = 1 ; G = 0
                
            if (B*D*G + B*E*F + C*D*F != 0) or (B*E*G + C*D*G + C*E*F != 0):
                break
        #print(super().prepis(r'ABDFx^3+'+str(A*B*D*G + A*B*E*F + A*C*D*F)+r'x^2+'+str(A*B*E*G + A*C*D*G + A*C*E*F)+r'x+ACEG=0', [A,B,C,D,E,F,G]))
        self.zadanie = super().texRiesPoly([A*C*E*G, A*B*E*G + A*C*D*G + A*C*E*F, A*B*D*G + A*B*E*F + A*C*D*F, A*B*D*F])[:-1] + r'=0$'
        self.riesenie = super().texRiesZlomCisla(-C*D*F - B*E*F - B*D*G, B*D*F)
        self.neriesenie = super().texRiesZlomCisla(-C*D*F + B*E*F - B*D*G, B*D*F)





def prikladyLoad():
    return [P1(0), P1(1), P1(2), P1(3), blank(), blank()]


