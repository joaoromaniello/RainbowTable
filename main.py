import hashlib
import os

probablePasswordsSW = [
    'starwars',
    'deathstar',
    '21b',
    '4lom',
    '8d8',
    '8t88',
    'admiralackbar',
    'stassallie',
    'allanasolo',
    'padmeamidala',
    'masamedda',
    'bailantilles',
    'raymusantilles',
    'wedgeantilles',
    'queenbrehaantillesorgana',
    'tavionaxmis',
    'pondababa',
    'cadbane',
    'baodur',
    'garmbeliblis',
    'siobibble',
    'jarjarbinks',
    'joleebindo',
    'bluemax',
    'bossk',
    'bollux',
    'borvothehutt',
    'brianna',
    'noabriqualon',
    'c3p0',
    'cb99',
    'joruuscbaoth',
    'darthcaedus',
    'landocalrissian',
    'charal',
    'chewbacca',
    'naschoka',
    'generalairencracken',
    'arvelcrynyd',
    'salaciousb.crumb',
    'admiralnatasidaala',
    'biggsdarklighter',
    'dengar',
    'brenderlin',
    'desann',
    'grandmoffvilimdisra',
    'jandodonna',
    'countdooku',
    'grandmoffdunhausen',
    'captaindunwell',
    'durge',
    'kypdurron',
    'darthdesolous',
    'captainjunoeclipse',
    'ev9d9',
    'doctorcorneliusevazan',
    'keyanfarlander',
    'jaggedfel',
    'roanfel',
    'baronsoontirfel',
    'davinfelth',
    'jangofett',
    'bobafett',
    'borskfeylya',
    'kitfisto',
    'fode',
    'bibfortuna',
    'adigallia',
    'garindan',
    'gonkdroid',
    'mirtagev',
    'greedo',
    'generalgrievous',
    'nutegunray',
    'hk47',
    'runehaako',
    'sanhill',
    'grandmoffbertroffhissa',
    'corranhorn',
    'ig88',
    'ysanneisard',
    'irekismaren',
    'isolder',
    'jabbathehutt',
    'marajadeskywalker',
    'queenjamillia',
    'jarael',
    'carnorjax',
    'jediexile',
    'jerec',
    'moffjerjerrod',
    'dexterjettster',
    'quigonjinn',
    'bardanjusik',
    'tenelka',
    'captainkael',
    'kirkanos',
    'talonkarrde',
    'kylekatarn',
    'obiwankenobi',
    'kiadimundi',
    'klaatu',
    'ken',
    'derekhobbieklivian',
    'agenkolar',
    'plokoon',
    'generalrahmkota',
    'kreia',
    'exarkun',
    'warmastertsavonglah',
    'berulars',
    'cliegglars',
    'owenlars',
    'lobot',
    'logray',
    'lumiya',
    'generalcrixmadine',
    'darthmalak',
    'galenmarek',
    'darthmaul',
    'md5',
    'tionmedon',
    'generalrommohc',
    'kasanmoor',
    'slymoore',
    'monmothma',
    'admiralconanantoniomotti',
    'grandmoffmuzzer',
    'momawnadon',
    'bossrugornass',
    'captainlorthneeda',
    'darthnihilus',
    'niennunb',
    'barrissoffee',
    'ricolie',
    'calomas',
    'omegasquad',
    'carthonasi',
    'onimi',
    'oola',
    'canderousordo',
    'bailorgana',
    'princessleiaorgana',
    'janors',
    'generalotto',
    'admiralkendalozzel',
    'emperorpalpatine',
    'captainpanaka',
    'giladpellaeon',
    'evenpiell',
    'firmuspiett',
    'darthplagueis',
    'pogglethelesser',
    'jektonoporkins',
    'ulicqeldroma',
    'danniquee',
    'oorylqrygg',
    'r2d2',
    'r2q5',
    'r4p17',
    'r5d4',
    'dackralter',
    'opporancisis',
    'maxrebo',
    'dashrendar',
    'reeyees',
    'darthrevan',
    'generalcarlistrieekan',
    'roguesquadron',
    'rookieone',
    'rukh',
    'sabe',
    'thrackansalsolo',
    'admiralsarn',
    'sebulba',
    'aaylasecura',
    'moffkohlseerdon',
    'zevsenesca',
    'shedaoshai',
    'bastilashan',
    'shimrra',
    'darthsidious',
    'sifodyas',
    'aurrasing',
    'darthsion',
    'anakinskywalker',
    'benskywalker',
    'cadeskywalker',
    'lukeskywalker',
    'luukeskywalker',
    'marajadeskywalker',
    'shmiskywalker',
    'sysnootles',
    'anakinsolo',
    'hansolo',
    'hanssolo',
    'jacensolo',
    'jainasolo',
    'leiaorganasolo',
    'lamasu',
    'nomisunrider',
    'gavynsykes',
    'generalcassiotagge',
    'grandmoffwilhufftarkin',
    'captainroostarpals',
    'tc14',
    'boosterterrik',
    'miraxterrik',
    'modterrik',
    'tessek',
    'briatharen',
    'grandmoffthistleborn',
    'raynarthul',
    'grandadmiralthrawn',
    'shaakti',
    'tibor',
    'saeseetiin',
    'majorgrodintierce',
    'triclops',
    'trioculus',
    'darthtyranus',
    'captaingregartypho',
    'ahsokatano',
    'darthvader',
    'supremechancellorfinisvalorum',
    'nahdarvebb',
    'generalmaximilianveers',
    'tahiriveila',
    'asajjventress',
    'vergere',
    'kingveruna',
    'vimadaboda',
    'qunlanvos',
    'vuffiraa',
    'wicketw.warrick',
    'watto',
    'taunwe',
    'zamwesell',
    'beruwhitesun',
    'macewindu',
    'winter',
    'wuher',
    'xanatos',
    'princexizor',
    'yaddle',
    'yoda',
    'zaxthehutt',
    'zekk',
    'zirothehutt',
    'zorbathehutt',
    'zuckuss',
    'commodorezuggs'
]
# Jogar isso em um arquivo, para poder ler sem precisar rodar varias vezes
table = []


def addAllPhoneNumbers():
    phoneFile = open("Data/phoneTable.txt", 'w')
    for i in range(980000000, 1000000000):
        number = "34" + str(i)
        hash = hashWord(number)
        phoneFile.write("Number:" + number + "\t|\tHash:" + hash + '\n')

    phoneFile.close()


def getAllCombinations(word):
    allWords = []

    allWords.append(word)
    allWords.append(word.upper())
    allWords.append(word.lower())

    if (word.__contains__('a') or word.__contains__('A')):
        allWords.append(subAto4(word))
    if (word.__contains__('i') or word.__contains__('I')):
        allWords.append(subIto1(word))
    if (word.__contains__('o') or word.__contains__('O')):
        allWords.append(subOtoZero(word))
    if (word.__contains__('e') or word.__contains__('E')):
        allWords.append(subEto3(word))
    if (word.__contains__('s') or word.__contains__('S')):
        allWords.append(subSto2(word))

    allWords.append(subSto2(subAto4(subOtoZero(subIto1(subEto3(word))))))

    for words in getAlternateCase(word):
        allWords.append(words)
        allWords.append(addExclamation(words))

        for words in addNumbers(word):
            allWords.append(words)

    return allWords


def addNumbers(word):
    wordsArray = []

    for i in range(1000):
        wordsArray.append(word + str(i))

    return wordsArray


def getAlternateCase(word):
    new_str = word
    words = []

    for i in range(0, len(word)):
        if (i % 2 == 0):
            my_list = list(new_str)
            my_list[i] = my_list[i].lower()
            new_str = ''.join(my_list)
        else:
            my_list = list(new_str)
            my_list[i] = my_list[i].upper()
            new_str = ''.join(my_list)

    words.append(new_str)

    new_str = word

    for i in range(0, len(word)):

        if i % 2 == 0:
            my_list = list(new_str)
            my_list[i] = my_list[i].upper()
            new_str = ''.join(my_list)
        else:
            my_list = list(new_str)
            my_list[i] = my_list[i].lower()
            new_str = ''.join(my_list)

    words.append(new_str)

    return words


def addExclamation(word):
    return word + "!"


def subAtoAT(word):
    new_str = word

    if 'a' not in word and 'A' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'a' or new_str[i] == 'A':
                my_list = list(new_str)
                my_list[i] = '@'
                new_str = ''.join(my_list)

    return new_str


def subAto4(word):
    new_str = word

    if 'a' not in word and 'A' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'a' or new_str[i] == 'A':
                my_list = list(new_str)
                my_list[i] = '4'
                new_str = ''.join(my_list)

    return new_str


def subIto1(word):
    new_str = word

    if 'i' not in word and 'I' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'I' or new_str[i] == 'i':
                my_list = list(new_str)
                my_list[i] = '1'
                new_str = ''.join(my_list)

    return new_str


def subItoExcl(word):
    new_str = word

    if 'i' not in word and 'I' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'I' or new_str[i] == 'i':
                my_list = list(new_str)
                my_list[i] = '!'
                new_str = ''.join(my_list)

    return new_str


def subEto3(word):
    new_str = word

    if 'e' not in word and 'E' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'e' or new_str[i] == 'E':
                my_list = list(new_str)
                my_list[i] = '3'
                new_str = ''.join(my_list)

    return new_str


def subSto2(word):
    new_str = word

    if 'Z' not in word and 'z' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'z' or new_str[i] == 'Z':
                my_list = list(new_str)
                my_list[i] = '2'
                new_str = ''.join(my_list)

    return new_str


def subOtoZero(word):
    new_str = word

    if 'o' not in word and 'O' not in word:
        return word
    else:
        for i in range(0, len(new_str)):
            if new_str[i] == 'o' or new_str[i] == 'O':
                my_list = list(new_str)
                my_list[i] = '0'
                new_str = ''.join(my_list)

    return new_str


def printTable():
    for obj in table:
        pw = obj['pw']
        hash = obj['hash']
        print("Pass:" + obj['pw'] + "\t|\tHash:" + obj['hash'])


def generateTable():
    file = open("Data/rainbowTable.txt", 'w')
    for pw in probablePasswordsSW:
        for word in getAllCombinations(pw):
            auxDict = dict()
            hashed = hashWord(word)
            auxDict["pw"] = word
            auxDict["hash"] = hashed
            file.write("Pass:" + auxDict['pw'] + "\t|\tHash:" + auxDict['hash'] + '\n')

    file.close()


def generateNumberTable():
    file = open("Data/numberTable.txt", 'w')
    for i in range(980000000, 1000000000):
        number = "34" + str(i)
        hashed = hashWord(number)
        file.write("Pass:" + number + "\t|\tHash:" + hashed + '\n')

    file.close()


def hashWord(word):
    hash_object = hashlib.sha256(bytes(word, 'utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def findHashInFile(hash, fileName):
    f = open("Data/" + fileName, "r")
    Lines = f.readlines()

    for line in Lines:
        passw = line.split("\t")[0].split("Pass:")[1]
        hashed = line.split("Hash:")[1].split("\n")[0]
        if hashed == hash:
            return (passw)

    return None


def findNumberInFile(hash, fileName):
    indicator = 0

    f = open("Data/" + fileName, "r")
    Lines = f.readlines()

    for line in Lines:
        number = line.split("\t")[0].split("Number:")[1]
        hashed = line.split("Hash:")[1].split("\n")[0]
        if hashed == hash:
            print("O hash corresponde a " + number)
            indicator = 1
            break

    if indicator == 0:
        print("Não foi possivel encontrar nenhum hash correspondente...")


def configDataFiles():
    generateTable()
    generateNumberTable()


def generateDynamicTables():

    for pw in probablePasswordsSW:
        for word in getAllCombinations(pw):
            auxDict = dict()
            hashed = hashWord(word)
            MS3 = hashed[0:3]
            file = open("Data/"+MS3+"Table.txt", 'a')
            auxDict["pw"] = word
            auxDict["hash"] = hashed
            file.write("Pass:" + auxDict['pw'] + "\t|\tHash:" + auxDict['hash'] + '\n')

    file.close()

    for i in range(980000000, 1000000000):
        number = "34" + str(i)
        hashed = hashWord(number)
        MS3 = hashed[0:3]
        file = open("Data/"+MS3+"Table.txt", 'a')
        file.write("Pass:" + number + "\t|\tHash:" + hashed + '\n')

    file.close()











