#hangman
import random
import time
def setup():
    global gamemode, font, hangman, playerName, wrongGuesses, hangmanImage, guessLimit, keyboard, listGuessed, listWrongGuesses, points
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
    print(words)
    size(800,600)
    playerName = []
    wrongGuesses = 0
    guessLimit = 6
    points = 0
        
def draw():
    imageMode(CENTER)
    if gamemode == "startMenu":
        startMenu()
    if gamemode == "playerMenu":
        playerMenu()
    if gamemode == "inGame":
        game()
        keyboardDisplay()
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
        x = x.split(", ")
        fileInfo.append(x)
    print(fileInfo)
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
    pass

def scoresMenu(): #scores menu
    pass
    
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
    for letter in range(len(displayWord)):
        if displayWord[letter] != "_":
            text(displayWord[letter], (550-(len(displayWord)*40/2)+(40*letter)), 250)            
        line((535-(len(displayWord)*40/2)+(40*letter)),250,(565-(len(displayWord)*40/2)+(40*letter)),250)
    textAlign(LEFT, BOTTOM)
    textSize(25)
    text("Points: "+str(points), 20, height-20) 
    if wrongGuesses == guessLimit:
        gamemode = "end"

def wordGenerator():
    global displayWord, guessWord, worth, wordHint, gamemode
    if len(fileInfo) != 0:
        randWord = random.randint(0,len(fileInfo) - 1) #*****need to make this run once*******
        guessWord = fileInfo[randWord][0]
        wordHint = fileInfo[randWord][1]
        displayWord = ["_"]*len(guessWord)
        fileInfo.pop(randWord)
    elif len(fileInfo) == 0:
        gamemode = "won"
        
    


def keyboardDisplay():
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
    textFont(font)
    textAlign(CENTER, CENTER)
    textSize(48)
    background(255)
    fill(0)
    text("You Lost!", width/2, height/2)

def wonScreen():
    textFont(font)
    textAlign(CENTER, CENTER)
    textSize(48)
    background(255)
    fill(0)
    text("You Won!", width/2, height/2)

def restart(): #restarts the game
    pass
    
    
def mousePressed():
    global gamemode, minLimit, wrongGuesses, keyboard, guessWord, listWrongGuesses, points, listGuessed
    keyCoords = [[40, 350], [120, 350], [200, 350], [280, 350], [360, 350], [440, 350], [520, 350], [600, 350], [680, 350], [760, 350], [80, 430], [160, 430], [240, 430], [320, 430], [400, 430], [480, 430], [560, 430], [640, 430], [720, 430], [160, 510], [240, 510], [320, 510], [400, 510], [480, 510], [560, 510], [640, 510]]
    print(mouseX, mouseY)
    if gamemode == "startMenu" and mouseButton == LEFT:
        if width/2-50 <= mouseX <= width/2+50 and 200 <= mouseY <= 270:
            gamemode = "playerMenu"
        if width/2-50 <= mouseX <= width/2+50 and 325 <= mouseY <= 380:
            gamemode = "helpMenu"
        if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
            gamemode = "scoresMenu"
    if gamemode == "playerMenu" and mouseButton == LEFT:
        if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
            if len(playerName) >= minLimit:
                gamemode = "inGame"
                time.sleep(0.5)
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
                print("key "+str(x)+" clicked")
                if keyboard[row][column][1] == True:
                    keyboard[row][column][1] = False
                    listGuessed.append(keyboard[row][column][0])
                for y in range(len(listGuessed)):
                    if listGuessed[y] in guessWord:
                        for z in range(guessWord.count(listGuessed[y])):
                            print("correct letter guessed")
                            displayWord[[i for i, n in enumerate(list(guessWord)) if n == listGuessed[y]][z]] = listGuessed[y]
                        if ''.join(displayWord) == guessWord:
                            points += len(guessWord)
                            print(points)
                            wordGenerator()
                            keyboard = [[['q', True],['w', True],['e', True],['r', True],['t', True],['y', True],['u', True],['i', True],['o', True],['p', True]],
                            [['a', True],['s', True],['d', True],['f', True],['g', True],['h', True],['j', True],['k', True],['l', True]],
                            [['z', True],['x', True],['c', True],['v', True],['b', True],['n', True],['m', True]]]
                            wrongGuesses = 0
                            listWrongGuesses = []
                            listGuessed = []
                    elif listGuessed[y] not in listWrongGuesses:
                        listWrongGuesses.append(listGuessed[y])
                        wrongGuesses = len(listWrongGuesses)
                        print("wrong guesses: "+str(wrongGuesses))
                print(listGuessed)
                print(keyboard)
                print(displayWord)
    
def keyPressed():
    global gamemode, playerName, guessLimit
    nameLimit = 20
    validKeys = "abcdefghijklmnopqrstuvwxyz1234567890 "
    if gamemode == "playerMenu":
        if keyCode != SHIFT and key in validKeys and len(playerName) < nameLimit:
            curKey = key
            playerName.append(curKey)
            print(curKey)
        if key == BACKSPACE and len(playerName) > 0:
            playerName.pop()
