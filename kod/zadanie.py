from random import choices, choice, shuffle
from itertools import chain
import os, sys
from brailleSlovnik import *
from math import sqrt
import numpy as np


jazyk = None

def init(jazyk_):
    global jazyk
    jazyk = jazyk_



class Zadanie:
    
    def __init__(self, maxnum=10,fontsize=False,dajnulu=False):
        self.maxnum = maxnum
        self.fontsize = fontsize
        self.vyber = []
        self.spravne = None
        for i in range(1,self.maxnum):
            self.vyber += [i]*(self.maxnum+1-i)
            self.vyber += [-i]*(self.maxnum+1-i)
        if dajnulu == True:
            self.vyber += [0]

    def zvolKoef(self,pocet,problemy,limit=100,menovatel=1):
        hladaj = True
        while hladaj == True:
            koeficienty = choices(self.vyber, k=pocet)
            #print(koeficienty)
            hladaj = False
            for problem in problemy:
                sucin = 1
                for p in problem:
                    #print(sucin,p)
                    sucin *= abs(koeficienty[p-1])
                if sucin > limit:
                    #print("ech")
                    hladaj = True
        return koeficienty


    def check(self,string):
        if string[0] == '+':
            string = string[1:]
        cisloStr = ''
        odstran = []
        odstranenePocet = 0
        
        for i in range(len(string)):
            try:
                cifra = int(string[i])
                cisloStr += string[i]
            except:
                if string[i] in ['x','y','z','t','\\','n','i','e']:
                    if cisloStr != '':
                        if int(cisloStr) == 1:
                            odstran.append(i-1-odstranenePocet)
                            odstranenePocet += 1
                cisloStr = ''
                
        for i in range(len(string)):
            if i in odstran:
                string = string[:i] + string[i+1:]
                
        return string.replace(r'+-',r'-').replace(r'{+',r'{').replace(r'--',r'+').replace(r'-+',r'-').replace(r'++',r'+').replace(r'-\pm',r' \pm')


    def prepis(self,string,koef,koefStr=False):
        if koefStr == False:
            koefStr = []
            for i in range(len(koef)):
                koefStr.append(abeceda[i])
            
        
        sucinKoefStr = ''
        sucinKoef = 1
        nahradzujStr = []
        nahradeneKoef = []

        for prvok in string+' ':
            jetupismenko = False
            for i in range(len(koefStr)):
                if prvok == koefStr[i]:
                    sucinKoefStr += prvok
                    sucinKoef *= koef[i]
                    jetupismenko = True

            if jetupismenko == False:
                if sucinKoefStr != '':
                    nahradzujStr.append(sucinKoefStr)
                    nahradeneKoef.append(sucinKoef)
                    sucinKoefStr = ''
                    sucinKoef = 1
                    
        for i in range(len(nahradzujStr)):
            string = string.replace(nahradzujStr[i],str(nahradeneKoef[i]),1)

        return r'$' + self.check(string) + r'$'
    
    
    
    def texRiesPoly(self,cleny,premenna='x'):    # cleny v poradi od absolutneho po najväcšiu mocninu
        riesenie = ''
        for i in reversed(range(1,len(cleny))):
            koef = cleny[i]
            if koef != 0:
                if koef > 0:
                    riesenie += '+'+str(cleny[i])+premenna
                else:
                    riesenie += str(cleny[i])+premenna
                if i >= 2:
                    riesenie += '^'+str(i)
        if cleny[0] != 0:
            riesenie += r'+'+str(cleny[0])
        if riesenie == '':
            riesenie = '0'
        return r'$' + self.check(riesenie) + r'$'


    def texRiesZlom(self,citatel,menovatel):
        riesenieCit = self.texRiesPoly(citatel)[1:-1]
        riesenieMen = self.texRiesPoly(menovatel)[1:-1]
        return r'$\cfrac{' + self.check(riesenieCit) + r'}{' + self.check(riesenieMen) + r'}$'


    def texRiesZlomCisla(self,citatel,menovatel,pripoj='',nicefrac=True,popZnamienko=False,textoutput=True):
        if menovatel == 0:
            if textoutput:
                return 'nedefinovane'
            else:
                return (0,0)
        elif citatel == 0:
            if textoutput:
                return r'$0$'
            return (0,1)
        else:
            if menovatel < 0:
                citatel = -citatel
                menovatel = -menovatel
            # krátenie
            kratenie = True
            while kratenie == True:
                kratenie = False
                for prvocislo in prvocisla:
                    if citatel % prvocislo == 0 and menovatel % prvocislo == 0:
                        citatel //= prvocislo ; menovatel //= prvocislo
                        kratenie = True

            if citatel == 1:
                if pripoj == '1':
                    citatel = 1 ; pripoj = ''
                elif pripoj == '-1':
                    citatel = -1 ; pripoj = ''
                elif pripoj != '':
                    if pripoj[0] == '-':
                        citatel = '-'
                    else:
                        citatel = ' '
                    
            elif citatel == -1:
                if pripoj == '1':
                    citatel = -1 ; pripoj = ''
                elif pripoj == '-1':
                    citatel = 1 ; pripoj = ''
                elif pripoj != '':
                    if pripoj[0] == '-':
                        citatel = ' '
                    else:
                        citatel = '-'

            else:
                if pripoj != '':
                    if pripoj[0] == '-':
                        if citatel < 0:
                            citatel = abs(citatel) ; pripoj = pripoj[1:]
                        else:
                            citatel = -citatel ; pripoj = pripoj[1:]
                    
                    if pripoj == '1':
                        pripoj = ''

            if menovatel == 1:
                if textoutput:
                    return r'$'+ str(citatel) + pripoj + r'$'
                else:
                    return (citatel,1)
            else:
                if textoutput:
                    if popZnamienko and str(citatel)[0] == '-':
                        if nicefrac:
                            return r'$-\nicefrac{' + str(citatel)[1:] + pripoj + r'}{' + str(menovatel) + r'}$'
                        else:
                            return r'$-\frac{' + str(citatel)[1:] + pripoj + r'}{' + str(menovatel) + r'}$'
                    else:
                        if nicefrac:
                            return r'$\nicefrac{' + str(citatel) + pripoj + r'}{' + str(menovatel) + r'}$'
                        else:
                            return r'$\frac{' + str(citatel) + pripoj + r'}{' + str(menovatel) + r'}$'
                else:
                    return (citatel,menovatel)


    
    def texRiesZlomPi(self,citatel,menovatel,nicefrac=False,popZnamienko=True):
        if menovatel == 0:
            return 'nedefinovane'
        elif citatel == 0:
            return r'$0$'
        else:
            if menovatel < 0:
                citatel = -citatel
                menovatel = -menovatel
            # krátenie
            kratenie = True
            while kratenie == True:
                kratenie = False
                for prvocislo in prvocisla:
                    if citatel % prvocislo == 0 and menovatel % prvocislo == 0:
                        citatel //= prvocislo ; menovatel //= prvocislo
                        kratenie = True

            if menovatel == 1:
                if citatel == 1:
                    citatel = ''
                return r'$'+ str(citatel) + r'\pi$'
            else:
                if popZnamienko and citatel < 0:
                    if citatel == 1:
                        citatel = ''
                    if nicefrac:
                        return r'$-\nicefrac{' + str(abs(citatel)) + r'\pi}{' + str(menovatel) + r'}$'
                    else:
                        return r'$-\frac{' + str(abs(citatel)) + r'\pi}{' + str(menovatel) + r'}$'
                else:
                    if citatel == 1:
                        citatel = ''
                    if nicefrac:
                        return r'$\nicefrac{' + str(citatel) + r'\pi}{' + str(menovatel) + r'}$'
                    else:
                        return r'$\frac{' + str(citatel) + r'\pi}{' + str(menovatel) + r'}$'



    def texRiesSqrt(self,cislo):
        odmocnina = sqrt(cislo)
        if round(odmocnina, 7) == odmocnina:
            return r'$' + str(int(odmocnina)) + r'$'
        else:
            return r'$\sqrt{'+str(cislo)+'}$'


        
    
    def texRiesVypis(self,cleny):
        vypis = ''
        oddelovac = r' , '
        for clen in cleny:
            if type(clen) == str:
                if clen[0] == r'$':
                    clen = clen[1:-1]
            vypis += str(clen) + oddelovac
        return r'$' + vypis[:-len(oddelovac)] + r'$'


    def texInterval(self,intervaly,uzavretia, premenna="x", husty=False):
        uzavSymZac = [r"\left(",r"\left\langle"]
        uzavSymKon = [r"\right)",r"\right\rangle"]
        if premenna == False:
            string = r"$"
        else:
            if husty:
                string = r"$"+premenna+r"\!\in\!"
            else:
                string = r"$"+premenna+r"\in"

        for i in range(len(intervaly)):
            zaciatok = intervaly[i][0]
            koniec = intervaly[i][1]
            uzavZac = uzavretia[i][0]
            uzavKon = uzavretia[i][1]
            if zaciatok in ['inf','infty','INF','INFTY','infinity','INFINITY']:
                zaciatok = r'\infty'
            if zaciatok in ['-inf','-infty','-INF','-INFTY','-infinity','-INFINITY']:
                zaciatok = r'-\infty'
            if koniec in ['inf','infty','INF','INFTY','infinity','INFINITY']:
                koniec = r'\infty'
            if koniec in ['-inf','-infty','-INF','-INFTY','-infinity','-INFINITY']:
                koniec = r'-\infty'
            if husty:
                string += uzavSymZac[uzavZac] + str(zaciatok) + r",\!" + str(koniec) + uzavSymKon[uzavKon]
            else:
                string += uzavSymZac[uzavZac] + str(zaciatok) + r" , " + str(koniec) + uzavSymKon[uzavKon]
            if i != len(intervaly)-1:
                if husty:
                    string += r'\!\cup\!'
                else:
                    string += r'\cup'
        return string + r"$"


    def texIntervalR(self,body):
        string = r'$ \mathbb{R}'
        if len(body) > 0:
            string += r' \smallsetminus\{'
            for bod in body:
                bodTu = str(bod)
                if bodTu[0] == r'$':
                    bodTu = bodTu[1:-1]
                string += bodTu+r','
            string = string[:-1]
        string += r' \}$'
        return string


    def texKomplexneCislo(self,re,im,pm=False):
        if pm == True:
            string = str(re) + r' \pm{}' + str(im) + r'i'
        else:
            string = str(re) + r'+' + str(im) + r'i'
        return r'$' + self.check(string) + r'$'


    def texKomplexneCisloGoniometric(self,A,arg):
        if A == 0:
            return r'$0$'
        elif arg == 0:
            return r'$' + str(A) + r'$'
        elif arg == r'\pi':
            return r'$' + str(-A) + r'$'
        elif A == 1:
            string = r'\cos{' + str(arg) + r'}+i\sin{' + str(arg) + '}'
            return r'$' + self.check(string) + r'$'
        else:
            string = str(A) + r'\left(\cos{' + str(arg) + r'}+i\sin{' + str(arg) + r'}\right)'
            return r'$' + self.check(string) + r'$'


    def texKomplexneCisloExp(self,A,arg):
        if A == 0:
            return r'$0$'
        elif arg == 0:
            return r'$' + str(A) + r'$'
        elif arg == r'\pi':
            return r'$' + str(-A) + r'$'
        else:
            string = str(A) + r'e^{i' + str(arg) + '}'
            return r'$' + self.check(string) + r'$'


    def texMatica2x2(self,A,B,C,D):
        maticaLatex = str(A) + r"&" + str(B) + r"\\" + str(C) + r"&" + str(D)
        return r"$\begin{pmatrix} " + maticaLatex + r"\end{pmatrix}$"
    

    def texMatica3x3(self,A,B,C,D,E,F,G,H,I):
        maticaLatex = str(A) + r"&" + str(B) + r"&" + str(C) + r"\\" + str(D) + r"&" + str(E) + r"&" + str(F) + r"\\" + str(G) + r"&" + str(H) + r"&" + str(I)
        return r"$\begin{pmatrix} " + maticaLatex + r"\end{pmatrix}$"
    
    def texMatica4x4(self,M):   # numpy array
        string = ""
        for i in range(4):
            for j in range(4):
                string += str(int(round(M[i][j])))
                if j != 3:
                    string += r"&"
            if i != 3:
                string += r"\\"
        return r"$\begin{pmatrix} " + string + r"\end{pmatrix}$"

    def texVektor(self,vec):
        string = r""
        for prvok in vec:
            string += str(prvok) + r"\\"
        return r"$\begin{pmatrix} " + string[:-2] + r"\end{pmatrix}$"
    

    def texKoVektor(self,vec):
        string = r""
        for prvok in vec:
            string += str(prvok) + r", "
        return r"$\left(" + string[:-2] + r"\right)$"
    

    def texVektorKomplex(self,vec):
        string = r""
        dim = vec.size
        for i in range(dim):
            real = int(vec.real[i])
            imag = int(vec.imag[i])
            if imag == 0:
                if real == 0:
                    string += r"0\\"
                else:
                    string += str(real) + r"\\"
            else:
                if real == 0:
                    real = ""
                string += self.check(str(real) + r"+" + str(imag) + r"i\\")
        return r"$\begin{pmatrix} " + string[:-2] + r"\end{pmatrix}$"
    


    def VektorZcelociselnenie(self,vec):
        #print(vec)
        a = 0
        dim = vec.size
        opakuj = True
        #print(vec)
        while opakuj == True:
            a += 1
            counter = 0
            for i in range(dim):
                real = vec.real[i]
                imag = vec.imag[i]
                skuskaReal = real*sqrt(a)
                skuskaImag = imag*sqrt(a)
                if round(skuskaReal, 7) == round(skuskaReal, 0) and round(skuskaImag, 7) == round(skuskaImag, 0):
                    #print("Heureka",a)
                    counter += 1
                    #print(a,i)
                    #print(real, imag)
            
            if counter == dim:
                opakuj = False
            if a > 1000:
                opakuj = False

        vecOprav = vec*sqrt(a)

        if np.array_equal(np.around(vecOprav, 7) , vecOprav):
            vecOprav_ = np.around(vecOprav, 0)
        else:
            vecOprav_ = np.nan

        return a, np.around(vecOprav, 0)


    def text(self,texty):
        jazyky = ["slovak", "czech", "english"]
        return r'\text{' + texty[jazyky.index(jazyk)] +'}'
    
    def mathrm(self,texty):
        jazyky = ["slovak", "czech", "english"]
        return r'\mathrm{' + texty[jazyky.index(jazyk)] +'}'




class blank(Zadanie):   # nepriklad
    def __init__(self):
        super().__init__()
        self.zadanie = 'vyfarbi?'
        self.riesenie = r'$\text{\ding{51}}$'
        self.neriesenie = r'$\text{\ding{55}}$'


class kubic(Zadanie):  # kubická rovnica
    def __init__(self):
        super().__init__()
        while True:
            A,B,C,D,E,F,G = super().zvolKoef(7, [[1,2,4,7],[1,2,5,7],[1,3,4,7],[1,3,5,7]], limit=60)
            F = 1
            B = 1 ; D = 1       
            if (B*D*G + B*E*F + C*D*F != 0) or (B*E*G + C*D*G + C*E*F != 0):
                break
        self.koeficienty = [A*C*E*G, A*B*E*G + A*C*D*G + A*C*E*F, A*B*D*G + A*B*E*F + A*C*D*F, A*B*D*F]
        self.riesenie = set([-C,-E,-G])
        self.neriesenie = set([-C,-E+choice([-2,-1,1,2]),G])




# TEXOVANIE

def t(prikaz):
    global file
    file.write(prikaz)
    file.write('\n')


def stranawrite(skupina,slovo,nazov,prikladyLoad,text,N,prikladyFontsize=r'\small',tightLayout=False,nameless=False):
    #global braille
    tabularsep = [r'&', r'\\ \hdashline', r'&', r'%']
    t(r'\thispagestyle{empty}')
    t(r'\begin{tabular}{c:c}')
    prikladyRiesALL = []
    # stvrtina
    for j in range(N):
        t(r'\begin{minipage}[c][104.5mm][t]{0.5\linewidth}')
        t(r'\begin{center}')
        if tightLayout:
            t(r'\vspace{5mm}')
        else:
            t(r'\vspace{7mm}')
        
        if jazyk == "slovak" or jazyk == "czech":
            t(r'{\huge '+nazov+r', skupina \textit{'+skupina+r' $'+'\\'+skupina.lower()+r'$} -\romannumeral'+str(j+1)+r'}\\[5mm]')
        else:
            t(r'{\huge '+nazov+r', group \textit{'+skupina+r' $'+'\\'+skupina.lower()+r'$} -\romannumeral'+str(j+1)+r'}\\[5mm]')
        if nameless == False:
            if jazyk == "slovak":
                t(r'\textit{Meno:}\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\\[5mm]')
            elif jazyk == "czech":
                t(r'\textit{Jméno:}\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\\[5mm]')
            else:
                t(r'\textit{Name:}\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\\[5mm]')
        t(r'\begin{minipage}{0.95\linewidth}')
        t(r'\begin{center}')
        t(text)
        t(r'\end{center}')
        t(r'\end{minipage}')
        if tightLayout:
            t(r'\\[1mm]')
        else:
            t(r'\\[4mm]')
        t(r'\begin{minipage}{0.79\linewidth}')
        # priklady
        t(r'\begin{center}')
        t(r'\begin{varwidth}{\linewidth}')
        if tightLayout:
            t(r'\setlength{\itemsep}{0pt}')
        t(r'\begin{enumerate}')
        t(prikladyFontsize)
        priklady = prikladyLoad()    # load prikladov
        prikladyRies = []
        for i in range(6):
            priklad = priklady[i]
            if braille[slovo[j]][i] == 1:
                zaotaznikom = priklad.riesenie
                priklad.spravne = 1
            else:
                zaotaznikom = priklad.neriesenie
                priklad.spravne = 0
            if priklad.fontsize == False:
                t(r'\item ' + priklad.zadanie + r'\quad \dotfill\; ???\;\dotfill \quad ' + zaotaznikom)
            else:
                t(r'\item {' + priklad.fontsize + priklad.zadanie + r'\quad \dotfill\; ???\;\dotfill \quad ' + zaotaznikom + r'}')
            prikladyRies.append([priklad.riesenie,priklad.spravne])
        prikladyRiesALL.append(prikladyRies)
        t(r'\end{enumerate}')
        t(r'\end{varwidth}')
        t(r'\end{center}')
        t(r'\end{minipage}')
        # braille
        t(r'\begin{minipage}{0.20\linewidth}')
        t(r'\begin{center}')
        #t(r'\vspace{4mm}')
        t(r'{\Huge\bfseries '+str(j+1)+r'.} \\[2mm]')
        t(r'\includegraphics[height=37mm]{images/braille.png}')
        if jazyk == "slovak":
            t(r'{\small Braillovo písmeno}')
        elif jazyk == "czech":
            t(r'{\small Braillovo písmeno}')
        else:
            t(r'{\small Braille letter}')
        t(r'\end{center}')
        t(r'\end{minipage}')
        t(r'\end{center}')
        t(r'\end{minipage}')
        t(tabularsep[j])
    t(r'\end{tabular}')
    #t(r'\begin{tikzpicture}[remember picture,overlay]\node[xshift=151.1mm,yshift=-7mm,anchor=north west,rotate=270] at (current page.north west){\ding{33}};\end{tikzpicture}')
    #t(r'\begin{tikzpicture}[remember picture,overlay]\node[xshift=7mm,yshift=-100.8mm,anchor=north west] at (current page.north west){\ding{33}};\end{tikzpicture}')
    return prikladyRiesALL


def filewrite(filename,nazov,prikladyLoad,text,
              pdfdir=".",
              prikladyFontsize=r'\small',
              rieseniaFontsize=r'\scriptsize',
              tabulkyBraille=False,
              minimalistic=False,
              nicefracSolution=True,
              tightLayout=False,
              tightLayoutRies=0,
              rieseniaNaStranu=12,
              nameless=False):

    global file
    file = open(filename, 'w', encoding="utf-8")
    # hlavicka
    t(r'\documentclass[10pt]{report}')
    t(r'\usepackage[slovak]{babel}')
    t(r'\usepackage{lmodern}')
    t(r'\usepackage{graphicx}')
    t(r'\usepackage{varwidth}')
    t(r'\usepackage{enumitem}')
    t(r'\usepackage{amsmath}')
    t(r'\usepackage{amssymb}')
    t(r'\usepackage{mathtools}')
    t(r'\usepackage{pifont}')
    t(r'\usepackage{arydshln}')
    t(r'\usepackage{tikz}')
    t(r'\usepackage{lscape}')
    t(r'\usepackage{bm}')
    t(r'\usepackage{nicefrac}')
    t(r'\usepackage{multicol}')
    t(r'\usepackage{vwcol}')
    t(r'\usepackage{physics}')
    t(r'\usepackage{fontsize}')
    t(r'\usepackage[landscape]{geometry}')
    t(r'\geometry{a4paper, total={296mm,210mm}, left=-5mm, top=0mm}')    # total={300mm,200mm}, left=0mm, top=5mm
    t(r'\renewcommand{\labelenumi}{\bfseries(\alph{enumi})\phantom{x}}')
    #t(r'\renewcommand{\tabcolsep}{1pt}')
    t(r'\newcommand\omicron{o}')
    t(r'\hfuzz=50pt')
    t(r'\setlist[enumerate]{leftmargin=0pt,itemindent=34pt}')
    t(r'\pagenumbering{gobble}')
    t(r'\setlength{\tabcolsep}{0pt}')
    # dokument
    t(r'\begin{document}')
    global zadaniaRiesALL
    zadaniaRiesALL = []
    for strana in range(24):
        zadaniaRiesALL.append(stranawrite(skupiny[strana],slova[jazyk][strana],nazov,prikladyLoad,text,4,prikladyFontsize=prikladyFontsize,tightLayout=tightLayout,nameless=nameless))
        t(r'\newpage')
        if minimalistic:
            break     
        
    # RIESENIA #
    t(r'\begin{landscape}')
    if tightLayoutRies > 0:
        t(r'\newgeometry{total={202mm,290mm}, left=4mm, top=5mm}')
    else:
        t(r'\newgeometry{total={194mm,285mm}, left=8mm, top=9mm}')
    t(r'\begin{center}')
    if jazyk == "slovak":
        t(r'{\huge '+str(nazov)+r' (riešenia)}\\[4mm]')
    elif jazyk == "czech":
        t(r'{\huge '+str(nazov)+r' (řešení)}\\[4mm]')
    else:
        t(r'{\huge '+str(nazov)+r' (solutions)}\\[4mm]')
    t(r'\begin{varwidth}{\linewidth}')
    t(r'\begin{center}')
    t(rieseniaFontsize)
    t(r'\rule[1mm]{\linewidth}{0.5pt}')
    for i in range(24):
        if i % rieseniaNaStranu == 0 and i != 0:
            if jazyk == "slovak":
                t(r'\end{center}\end{varwidth}\end{center}\clearpage\begin{center}{\huge '+str(nazov)+r' (riešenia)}\\[4mm]\begin{varwidth}{\linewidth}\begin{center}')
            elif jazyk == "czech":
                t(r'\end{center}\end{varwidth}\end{center}\clearpage\begin{center}{\huge '+str(nazov)+r' (řešení)}\\[4mm]\begin{varwidth}{\linewidth}\begin{center}')
            else:
                t(r'\end{center}\end{varwidth}\end{center}\clearpage\begin{center}{\huge '+str(nazov)+r' (solutions)}\\[4mm]\begin{varwidth}{\linewidth}\begin{center}')
            if tightLayoutRies:
                t(r'\vspace{-'+str(1.6*tightLayoutRies)+r'mm}')
            t(rieseniaFontsize)
            t(r'\rule[1mm]{\linewidth}{0.5pt}')
        t(r'$\boxed{\bm{'+'\\'+skupiny[i].lower()+r'}} \quad \begin{aligned}')
        for j in range(4):
            t(r'\romannumeral'+str(j+1)+r' : \; &\textbf{'+slova[jazyk][i][j].upper()+r'} ')
            for k in range(6):
                podzadanie = ['a','b','c','d','e','f'][k]
                if nicefracSolution:
                    t(r' &&\mathrm{\textbf{('+podzadanie+r') }} '+zadaniaRiesALL[i][j][k][0].replace(r'\cfrac',r'\nicefrac').replace(r'\frac',r'\nicefrac').replace(r'$','').replace(r'\enspace',' ')+[r'\,\text{\ding{55}}',r'\,\text{\ding{51}}'][zadaniaRiesALL[i][j][k][1]])
                else:
                    if tightLayoutRies:
                        t(r' &&\mathrm{\textbf{('+podzadanie+r') }} '+zadaniaRiesALL[i][j][k][0].replace(r'$','').replace('cfrac','tfrac').replace(r'\enspace',' ')+[r'\,\text{\ding{55}}',r'\,\text{\ding{51}}'][zadaniaRiesALL[i][j][k][1]])
                    else:
                        t(r' &&\mathrm{\textbf{('+podzadanie+r') }} '+zadaniaRiesALL[i][j][k][0].replace(r'$','').replace(r'\enspace',' ')+[r'\,\text{\ding{55}}',r'\,\text{\ding{51}}'][zadaniaRiesALL[i][j][k][1]])
            if j != 3:
                if tightLayoutRies:
                    t(r'\\[-'+str(0.4+0.2*tightLayoutRies)+r'mm]')
                else:
                    t(r'\\[-0.4mm]')
        t(r'\end{aligned} $')
        if i != 23:
            if tightLayoutRies:
                t(r'\\['+str(2-0.6*tightLayoutRies)+r'mm]')
                t(r'\rule['+str(1-0.3*tightLayoutRies)+r'mm]{\linewidth}{0.5pt}')
            else:
                t(r'\\[2mm]')
                t(r'\rule[1mm]{\linewidth}{0.5pt}')
        if minimalistic:
            break
        
    t(r'\\[1mm]')
    t(r'\rule[-1mm]{\linewidth}{0.5pt}')
    t(r'\end{center}')
    t(r'\end{varwidth}')
    t(r'\end{center}')
    t(r'\end{landscape}')
    
    if tabulkyBraille == True:
        for i in range(8):
            t(r'\clearpage')
            t(r'\setlength{\tabcolsep}{4mm}')
            t(r'\begin{tabular}{c c}')
            for koncovka in [r'&',r'\\',r'&','']:
                t(r'\begin{minipage}{0.47\textwidth}')
                t(r'\begin{center}')
                t(r'\phantom{x}\\[10mm]')
                if jazyk == "slovak":
                     t(r'{\Large Braillova abeceda na dekódovanie slov}\\[1mm]')
                elif jazyk == "czech":
                    t(r'{\Large Braillova abeceda pro dekódování slov}\\[1mm]')
                else:
                    t(r'{\Large Braille alphabet for decoding words}\\[1mm]')
                t(r'\includegraphics[width=\textwidth]{images/brailleSkratene.png}')
                t(r'\end{center}')
                t(r'\end{minipage}')
                t(koncovka)
            t(r'\end{tabular}')

    t(r'\end{document}')

    file.close()

    os.system("pdflatex -output-directory="+str(pdfdir)+" "+str(filename))






