from random import shuffle

# 0 5   a f
# 1 4   b e
# 2 3   c d

braille = {
    "a":[1,0,0, 0,0,0],
    "b":[1,1,0, 0,0,0],
    "c":[1,0,0, 0,0,1],
    "d":[1,0,0, 0,1,1],
    "e":[1,0,0, 0,1,0],
    "f":[1,1,0, 0,0,1],
    "g":[1,1,0, 0,1,1],
    "h":[1,1,0, 0,1,0],
    "i":[0,1,0, 0,0,1],
    "j":[0,1,0, 0,1,1],
    "k":[1,0,1, 0,0,0],
    "l":[1,1,1, 0,0,0],
    "m":[1,0,1, 0,0,1],
    "n":[1,0,1, 0,1,1],
    "o":[1,0,1, 0,1,0],
    "p":[1,1,1, 0,0,1],
    "q":[1,1,1, 0,1,1],
    "r":[1,1,1, 0,1,0],
    "s":[0,1,1, 0,0,1],
    "t":[0,1,1, 0,1,1],
    "u":[1,0,1, 1,0,0],
    "v":[1,1,1, 1,0,0],
    "w":[0,1,0, 1,1,1],
    "x":[1,0,1, 1,0,1],
    "y":[1,0,1, 1,1,1],
    "z":[1,0,1, 1,1,0],
    "á":[1,0,0, 1,0,0],
    "é":[0,0,1, 0,1,1],
    "í":[0,0,1, 0,0,1],
    "ó":[0,1,0, 1,0,1],
    "ú":[0,0,1, 1,0,1],
    "ý":[1,1,1, 1,0,1],
    "ô":[0,1,1, 1,1,1],
    "č":[1,0,0, 1,0,1],
    "ď":[1,0,0, 1,1,1],
    "ě":[1,1,0, 1,0,0],
    "ň":[1,1,0, 1,0,1],
    "ř":[0,1,0, 1,1,1], # problem
    "š":[1,0,0, 1,1,0],
    "ť":[1,1,0, 1,1,0],
    "ž":[0,1,1, 1,0,1],
    "ľ":[0,0,0, 1,1,1],
    "ĺ":[0,0,0, 1,0,1],
    "?":[0,1,0, 1,0,0],
    "!":[0,1,1, 0,1,0]
    }



slovaStringSlovak = "žaba auto repa ruka ivan mama jana okno čína sova jaro emil noha zima urán slon úpal zuby ucho pero iglu prah krab mapa prst golf úlet most žito žila cena jama baba vaňa čelo anna krst hora ryba drak mrak lama blaf býky časť dáma domy elán hady husi jóga kráľ lyža mlok mzda nula obor olej okno ovad pena rado sane vrah kóma sklo sója špeh taxi tóga úraz váha vlci vlek vzor zrub žaba žula ibis kosť hrad uhol euro tlak vlak úlet jojo nora film lano erik česť figy voda pivo osol igor epos lupa fľak olej ústa doma deka seno hana ropa hlad cela rada"
slovaSlovak = slovaStringSlovak.split(' ')
shuffle(slovaSlovak)

slovaStringCzech = "žába auto řepa ruka ivan šála kolo cukr máma jana okno čína sova jaro emil noha táta zima uran bota slon úpal zuby ucho pero iglu golf úlet most žito žíla cena jáma bába vana čelo anna hora šnek ryba drak ibis kost hrad úhel euro jako tlak vlak úkol ústí jojo žrát bobr nora film lano erik urna zubr únor čest fíky voda pivo osel igor epos lupa foto flek fena zelí olej ústa doma deka seno hana řasa ropa hlad cela copy dort čokl rada mrak"
slovaCzech = slovaStringCzech.split(' ')
shuffle(slovaCzech)

slovaStringEnglish = "acid area army atom baby ball bank base bear bell bird body book boss bowl case cash cell chat city clip club cold date deal desk dirt door dust east edge face fall farm feet fire fish five food foot game gate gift girl goal gold gray half hand head help home hope idea iron land lead leaf life line love mail mark meet mind name news nine note page path peak plan rain road room root rule sale sand save seat shop show side site size slow snow soul star step suit task team test time town tree trip turn unit user view walk wall week west wild wind wine wing wish wood work year"
slovaEnglish = slovaStringEnglish.split(' ')
shuffle(slovaEnglish)

slova = {
    "slovak": slovaSlovak,
    "czech": slovaCzech,
    "english": slovaEnglish
}


skupiny = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega']


abeceda = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

prvocisla = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
