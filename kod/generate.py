import zadanie
import configparser
import importlib


def generuj(meno,jazyk,tabulkyBraille=False,minimalistic=False, rieseniaNaStranu=12, nameless=False):

    filepath = "config/" + jazyk + "/" + meno + ".ini"

    codepath = "zadania." + meno
    codeSada = importlib.import_module(codepath)
    codeSada.init(jazyk)

    zadanie.init(jazyk)

    config = configparser.ConfigParser()
    config.read(filepath, encoding="utf-8")

    latex_output = "latex/" + jazyk + "/" + meno + ".tex"

    textpath = "texty/" + jazyk + "/" + meno + ".txt"
    with open(textpath, "r", encoding="utf-8") as f:
        text = f.read()
        #print(text)
    
    pdfdir = "pdfka/" + jazyk
    
    zadanie.filewrite(latex_output, 
              config["database"]["nazov"],
              codeSada.prikladyLoad,
              text,
              pdfdir = pdfdir,
              prikladyFontsize = config["database"]["prikladyFontsize"],
              rieseniaFontsize = config["database"]["rieseniaFontsize"],
              tightLayout = "True" == config["database"]["tightLayout"],
              tightLayoutRies = eval(config["database"]["tightLayoutRies"]),
              nicefracSolution = "True" == config["database"]["nicefracSolution"],
              tabulkyBraille = tabulkyBraille,
              minimalistic = minimalistic,
              rieseniaNaStranu=rieseniaNaStranu,
              nameless=nameless)


sady = [["."],
        ["010zatvorky"],
        ["020kvadros"],
        ["030kubric"],
        ["040definic", "041definic"],
        ["050limity" , "051limity", "052limity"],
        ["060derivacie", "061derivacie"],
        ["070dotycnica"],
        ["080stacinflex"],
        ["090","091parcialMulti"],
        ["100"],
        ["110komplex","111komplex","112komplex"]
]




generuj(sady[2][0], "czech", minimalistic=False, rieseniaNaStranu=12, nameless=False)