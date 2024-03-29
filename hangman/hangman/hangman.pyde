#hangman by alexandra sergueeva and joshua yu
import random
import time
import pickle
from datetime import datetime
add_library("minim")
def setup():
    global minim, click, bloop, scoreadded, gamemode, font, playerName, wrongGuesses, hangmanImage, guessLimit, keyboard, listGuessed, listWrongGuesses, points, hintChosen, highscoreDict
    gamemode = "startMenu"
    font = loadFont("BradleyHandITC-48.vlw")
    words = getFileInfo("hangmanwords.txt")
    hangmanImage = {0:loadImage("hangman.png"), 1:loadImage("hangman1.png"), 2:loadImage("hangman2.png"), 3:loadImage("hangman3.png"), 4:loadImage("hangman4.png"), 5:loadImage("hangman5.png"), 6:loadImage("hangman6.png")}
    keyboard = [[['q', True],['w', True],['e', True],['r', True],['t', True],['y', True],['u', True],['i', True],['o', True],['p', True]],
                [['a', True],['s', True],['d', True],['f', True],['g', True],['h', True],['j', True],['k', True],['l', True]],
                [['z', True],['x', True],['c', True],['v', True],['b', True],['n', True],['m', True]]]
    wordGenerator()
    listGuessed = []
    listWrongGuesses = []
    ###print(words)
    size(800,600)
    playerName = []
    wrongGuesses = 0
    guessLimit = 6
    points = 0
    highscoreDict = {}
    hintChosen = False
    scoreadded = False
    add_library('minim')
    minim = Minim(this)
    click = minim.loadFile("click.wav")
    bloop = minim.loadFile("correct.wav")
   
           
def draw():
    imageMode(CENTER)
    if gamemode == "startMenu":
        startMenu()
    if gamemode == "playerMenu":
        playerMenu()
    if gamemode == "scoresMenu":
        scoresMenu()
    if gamemode == "helpMenu":
        helpMenu()
    if gamemode == "inGame":
        game()
        keyboardDisplay()
        hintDisplay()
    if gamemode == "end":
        endScreen()
    if gamemode == "won":
        wonScreen()

def getFileInfo(fileName):
    global fileInfo
    file = open(fileName)
    fileInfo = []
    fileText = file.readlines()
    for x in fileText:
        x = x.strip()
        x = x.split(",")
        fileInfo.append(x)
    return fileInfo

def startMenu(): #start menu
    background(255)
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    text("hangman", width/2, height/5)
    if width/2-50 <= mouseX <= width/2+50 and 200 <= mouseY <= 270:
        fill(225)
        text("play", width/2, (height/5)*2)
        fill(0)
    else:
        fill(0)
        text("play", width/2, (height/5)*2)
    if width/2-50 <= mouseX <= width/2+50 and 325 <= mouseY <= 380:
        fill(225)
        text("help", width/2, (height/5)*3)
        fill(0)
    else:
        fill(0)
        text("help", width/2, (height/5)*3)
    if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
        fill(225)
        text("scores", width/2, (height/5)*4)
        fill(0)
    else:
        fill(0)
        text("scores", width/2, (height/5)*4)
   
def playerMenu(): #where you select number of players and input names
    global minLimit
    background(255)
    minLimit = 3
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    text("type your name", width/2, height/3)
    text(getPlayerName(), width/2, height/2)
    if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485 or len(playerName) < minLimit:
        fill(225)
        text("begin", width/2, (height/5)*4)
        fill(0)
    else:
        fill(0)
        text("begin", width/2, (height/5)*4)
    if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
        fill(225)
        text("<", 50, 50)
        fill(0)
    else:
        fill(0)
        text("<", 50, 50)
   
def getPlayerName():
    global curKey, playerName
    curKey = ""
    return str("".join(playerName))
   
def helpMenu(): #help menu
    global helpmode, prevGamemode
    imageMode(CORNER)
    background(255)
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    if helpmode == "help1":
        help = loadImage("help1.jpg")
        image(help,0,60,830,450)
        stroke(255,0,0)
        line(539,209,575,209)
        stroke(0)
        if 700 <= mouseX <= 735 and 510 <= mouseY <= 540:
            fill(225)
            text(">", 720, 540)
            fill(0)
        else:
            fill(0)
            text(">", 720, 540)
    if helpmode == "help2":
        help = loadImage("help2.jpg")
        image(help,0,80,830,400)
    if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
        fill(225)
        text("<", 50, 50)
        fill(0)
    else:
        fill(0)
        text("<", 50, 50)
       




def scoresMenu(): #scores menu
    global highscoreDict, points, playerName, fromhighscore, tohighscore
    filename = 'highscores'
    infile = open(filename, 'rb')
    try:
        highscoreDict = pickle.load(infile)
    except EOFError:
        highscoreDict = {}
    infile.close()
    background(255)
    fill(0)
    textSize(30)
    textAlign(CENTER)
    text("Scores", width/5, 50)
    text("Name", (width/5)*2, 50)
    text("Date", (width/5)*3, 50)
    text("Time", (width/5)*4, 50)
    itemlist = highscoreDict.items()
    sortlist(itemlist)
    if len(itemlist) > 10:
        numloop = 10
    else:
        numloop = len(itemlist)
    for x in range(numloop):
        text(str(itemlist[x][1]), width/5, 100+50*x)
        namedatetimelist = itemlist[x][0].split(", ")
        text(str(namedatetimelist[0]), (width/5)*2, 100+50*x)
        text(str(namedatetimelist[1]), (width/5)*3, 100+50*x)
        text(str(namedatetimelist[2]), (width/5)*4, 100+50*x)
    textSize(48)
    if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
        fill(225)
        text("<", 50, 50)
        fill(0)
    else:
        fill(0)
        text("<", 50, 50)


def sortlist(itemlist):
    for z in range(len(itemlist)-1, 0, -1): #sorting by score
        for y in range(z):
            if itemlist[y][1] < itemlist[y+1][1]:
                itemlist[y], itemlist[y+1] = itemlist[y+1], itemlist[y]
    for z in range(len(itemlist)-1, 0, -1): #sorting by datetime
        for y in range(z):
            if itemlist[y][1] == itemlist[y+1][1]:
                datetimeobj1 = datetime.strptime(itemlist[y][0].split(", ", 1)[1], "%m/%d/%Y, %H:%M:%S")
                datetimeobj2 = datetime.strptime(itemlist[y+1][0].split(", ", 1)[1], "%m/%d/%Y, %H:%M:%S")
                if datetimeobj1 > datetimeobj2:
                    itemlist[y], itemlist[y+1] = itemlist[y+1], itemlist[y]            
    return itemlist

def game():
    global wrongGuesses, fileInfo, guessWord, displayWord, gamemode
    background(255)
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    image(hangmanImage[wrongGuesses], width/5, height/4, 300, 300)
    strokeWeight(15)
    line(0, 300, width, 300)
    strokeWeight(1)
    for letter in range(len(displayWord)): #put correctly guessed letters on screen
        if displayWord[letter] != "_":
            text(displayWord[letter], (550-(len(displayWord)*40/2)+(40*letter)), 250)            
        line((535-(len(displayWord)*40/2)+(40*letter)),250,(565-(len(displayWord)*40/2)+(40*letter)),250)
    textAlign(LEFT, BOTTOM)
    textSize(25)
    text("Points: "+str(points), 20, height-20)
    if wrongGuesses == guessLimit:
        gamemode = "end"
    textAlign(RIGHT, BOTTOM)
    if 735 <= mouseX <= 780 and 555 <= mouseY <= 575:
        fill(225)
    text("help",width-20, height-20)
    if 660 <= mouseX <= 720 and 555 <= mouseY <= 575:
        fill(225)
    else:
        fill(0)    
    text("Menu",width-80, height-20)

def wordGenerator(): #get random guess word from list
    global displayWord, guessWord, worth, wordHint, gamemode
    if len(fileInfo) != 0:
        randWord = random.randint(0,len(fileInfo) - 1)
        guessWord = fileInfo[randWord][0]
        wordHint = fileInfo[randWord][1]
        displayWord = ["_"]*len(guessWord)
        fileInfo.pop(randWord) #pop word from list when it is guessed correctly
    elif len(fileInfo) == 0: #if there are no words left in the list, player won
        gamemode = "won"
       
def hintDisplay():  #if player clicks for hint, display hint
    textFont(font)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(0)
    if hintChosen:
        text("Click for Hint", 550, 30)
        text(wordHint, 550, 60)
    elif 450 <= mouseX <= 650 and 15 <= mouseY <= 50:
        fill(225)
        text("Click for Hint", 550, 30)
    else:
        fill(0)
        text("Click for Hint", 550, 30)


def keyboardDisplay(): #display letters
    global keyboard
    textFont(font)
    textAlign(CENTER, CENTER)
    textSize(48)
    for x in range(len(keyboard)): #displays the keyboard
        for y in range(len(keyboard[x])):
            if keyboard[x][y][1] == False:
                fill(225)
            else:
                fill(0)
            text(keyboard[x][y][0],40+width/2-((80*len(keyboard[x]))/2)+(80*y), 350+(80*x))
           
def endScreen():
    global guessWord, scoreadded
    textFont(font)
    textAlign(CENTER, CENTER)
    textSize(48)
    background(255)
    fill(0)
    text("The word was " + guessWord, width/2, height/5)
    text(getPlayerName()+", you lost!", width/2, (height/5)*2)
    text("Final Score: "+str(points), width/2, (height/5)*3)
    if 250 <= mouseX <= 550 and 470 <= mouseY <= 510:
        fill(225)
    text("Click to restart", width/2, (height/5)*4)
    if scoreadded == False:
        addscore()
        scoreadded = True

def wonScreen():
    global playerName, highscoreDict, points, scoreadded
    textFont(font)
    textAlign(CENTER, CENTER)
    textSize(48)
    background(255)
    fill(0)
    text(getPlayerName()+ ", you won!", width/2, height/3)
    text("Final Score: "+str(points), width/2, height/2)
    if 250 <= mouseX <= 550 and 390 <= mouseY <= 420:
        fill(225)
    text("Click to restart", width/2, height/3*2)
    if scoreadded == False:
        addscore()
        scoreadded = True
       
def addscore():
    global highscoreDict, points, playerName, fromhighscore, tohighscore
    filename = 'highscores'
    ##print("before open")
    infile = open(filename, 'rb')
    ##print("before load")
    try:
        highscoreDict = pickle.load(infile)
    except EOFError:
        highscoreDict = {}
    infile.close()
    itemlist = highscoreDict.items()
    if len(highscoreDict) < 10 or points > sortlist(itemlist)[9][1]:
        outfile = open(filename, 'wb')
        highscoreDict[str("".join(playerName))+", "+str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))] = points
        if len(highscoreDict) > 10:
            itemlist = highscoreDict.items()
            del highscoreDict[sortlist(itemlist)[9][0]]
        pickle.dump(highscoreDict, outfile)
        outfile.close()    


def restart(): #restarts the game
    global points, gamemode, playerName, wrongGuesses, keyboard, listWrongGuesses, listGuessed, hintChosen, scoreadded
    gamemode = "startMenu"
    playerName = []
    getFileInfo("hangmanwords.txt")
    wordGenerator()
    keyboard = [[['q', True],['w', True],['e', True],['r', True],['t', True],['y', True],['u', True],['i', True],['o', True],['p', True]],
    [['a', True],['s', True],['d', True],['f', True],['g', True],['h', True],['j', True],['k', True],['l', True]],
    [['z', True],['x', True],['c', True],['v', True],['b', True],['n', True],['m', True]]]
    wrongGuesses = 0
    listWrongGuesses = []
    listGuessed = []
    hintChosen = False
    scoreadded = False
    points = 0
   
   
def mousePressed():
    global helpmode, prevGamemode, gamemode, minLimit, wrongGuesses, keyboard, guessWord, listWrongGuesses, points, listGuessed, hintChosen, playerName, bloop, click
    #center coords of each letter on screen
    keyCoords = [[40, 350], [120, 350], [200, 350], [280, 350], [360, 350], [440, 350], [520, 350], [600, 350], [680, 350], [760, 350], [80, 430], [160, 430], [240, 430], [320, 430], [400, 430], [480, 430], [560, 430], [640, 430], [720, 430], [160, 510], [240, 510], [320, 510], [400, 510], [480, 510], [560, 510], [640, 510]]
    print(mouseX, mouseY)
    if gamemode == "startMenu" and mouseButton == LEFT:
       
        #if "start" clicked
        if width/2-50 <= mouseX <= width/2+50 and 200 <= mouseY <= 270:
            gamemode = "playerMenu"
            click = minim.loadFile("click.wav")
            click.play()
           
        #if "help" clicked
        if width/2-50 <= mouseX <= width/2+50 and 325 <= mouseY <= 380:
            gamemode = "helpMenu"
            helpmode = "help1"
            prevGamemode = "startMenu"
            print(gamemode)
           
        #if "scores clicked"
        if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
            gamemode = "scoresMenu"
            print("scores")

    if gamemode == "helpMenu":
        if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
            if helpmode == "help1":
                gamemode = prevGamemode
            if helpmode == "help2":
                gamemode = "helpMenu"
                helpmode = "help1"
        #if next arrow clicked in help menu
        if 700 <= mouseX <= 735 and 510 <= mouseY <= 540:
            helpmode = "help2"

    #if "begin" clicked
    if gamemode == "playerMenu" and mouseButton == LEFT:
        if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
            if len(playerName) >= minLimit:
                gamemode = "inGame"
                time.sleep(0.5)
        #if back arrow clicked
        if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
            gamemode = "startMenu"
            playerName = []
 
    if gamemode == "scoresMenu":
        if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
            gamemode = "startMenu"
    if gamemode == "inGame" and mouseButton == LEFT:
        for x in range(len(keyCoords)):
            if keyCoords[x][0]-20 <= mouseX <= keyCoords[x][0]+20 and keyCoords[x][1]-20 <= mouseY <= keyCoords[x][1]+20:
                if 0 <= x <= 9:
                    row = 0
                    column = x
                if 10 <= x <= 18:
                    row = 1
                    column = x - 10
                if 19 <= x <= 25:
                    row = 2
                    column = x - 19
                ###print("key "+str(x)+" clicked")
                if keyboard[row][column][1] == True:  #if letter clicked, turn it off and add letter to listGuessed[]
                    keyboard[row][column][1] = False
                    listGuessed.append(keyboard[row][column][0])
                for y in range(len(listGuessed)):
                    if listGuessed[y] in guessWord: #if clicked letter is in the guess word, add letter to displayWord[]
                        for z in range(guessWord.count(listGuessed[y])):
                            ###print("correct letter guessed")
                            displayWord[[i for i, n in enumerate(list(guessWord)) if n == listGuessed[y]][z]] = listGuessed[y]
                        if ''.join(displayWord) == guessWord: #if letters in displayWord[] match the guessWord, add points and generate new word, and reset keyboard, num wrong guesses, and list of guessed letters
                            bloop = minim.loadFile("correct.wav")
                            bloop.play()
                            if hintChosen == True:
                                points += int(round(len(guessWord)/2))
                            else:
                                points += len(guessWord)
                            wordGenerator()
                            keyboard = [[['q', True],['w', True],['e', True],['r', True],['t', True],['y', True],['u', True],['i', True],['o', True],['p', True]],
                            [['a', True],['s', True],['d', True],['f', True],['g', True],['h', True],['j', True],['k', True],['l', True]],
                            [['z', True],['x', True],['c', True],['v', True],['b', True],['n', True],['m', True]]]
                            wrongGuesses = 0
                            listWrongGuesses = []
                            listGuessed = []
                            hintChosen = False
                    elif listGuessed[y] not in listWrongGuesses:
                        listWrongGuesses.append(listGuessed[y])
                        wrongGuesses = len(listWrongGuesses)
                        ###print("wrong guesses: "+str(wrongGuesses))
                ###print(listGuessed)
                ###print(keyboard)
                ###print(displayWord)
            #if "click for hint" clicked
            if 450 <= mouseX <= 650 and 15 <= mouseY <= 50:
                hintChosen = True
        #if "help" in game mode clicked
        if 735 <= mouseX <= 780 and 555 <= mouseY <= 575:
            gamemode = "helpMenu"
            helpmode = "help1"
            prevGamemode = "inGame"
        #if "menu" in game mode clicked
        if 660 <= mouseX <= 720 and 555 <= mouseY <= 575:
            gamemode = "startMenu"
    if gamemode == "end":
        if 250 <= mouseX <= 550 and 470 <= mouseY <= 510: #if "click to restart" clicked
            restart()
    if gamemode == "won":
        if 250 <= mouseX <= 550 and 390 <= mouseY <= 420:
            restart()
           
def keyPressed():  #player name
    global gamemode, playerName, guessLimit
    nameLimit = 20
    validKeys = "abcdefghijklmnopqrstuvwxyz1234567890 "
    if gamemode == "playerMenu":
        if keyCode != SHIFT and key in validKeys and len(playerName) < nameLimit:
            curKey = key
            playerName.append(curKey)
            ###print(curKey)
        if key == BACKSPACE and len(playerName) > 0:
            playerName.pop()
