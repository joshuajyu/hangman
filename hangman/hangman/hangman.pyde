#hangman
import random
def setup():
    global gamemode, font, hangman
    gamemode = "startMenu"
    font = loadFont("BradleyHandITC-48.vlw")
    words = getFileInfo("hangmanwords.txt")
    hangman = {1:loadImage("hangman1.png"), 2:loadImage("hangman2.png"), 3:loadImage("hangman3.png"), 4:loadImage("hangman4.png"), 5:loadImage("hangman5.png"), 6:loadImage("hangman6.png")} 
    print(words)
    size(800,600)
    
def draw():
    if gamemode == "startMenu":
        startMenu()
    if gamemode == "playerMenu":
        playerMenu()

def getFileInfo(fileName):
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
    background(255)
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    text("Type your name", width/2, height/3)
        
    
def helpMenu(): #help menu
    pass

def scoresMenu(): #scores menu
    pass
    
def game():
    pass

def restart(): #restarts the game
    pass
    
def mousePressed():
    global gamemode
    print(mouseX, mouseY)
    if gamemode == "startMenu":
        if width/2-50 <= mouseX <= width/2+50 and 200 <= mouseY <= 270:
            gamemode = "playerMenu"
        if width/2-50 <= mouseX <= width/2+50 <= mouseY <= 380:
            gamemode = "helpMenu"
        if width/2-60 <= mouseX <= width/2+60 <= mouseY <= 485:
            gamemode = "scoresMenu"

    
def keyReleased():
    global whichKey, asciList, controlKeys
    
    #for entering name
    if key == CODED:
        if keyCode in controlKeys:
            whichKey = keyCode
    elif key in asciList:
        whichKey = key
    else:
        whichKey = ''
'''
def getPlayerName():
    global whichKey, nameIn, nameLimit, nameCount, mode
    
    if mode == "Start":  
        if ( whichKey == "0" ) or ( nameCount >= nameLimit ):
            mode = "Play"
        else:
            if whichKey != "":
                print("here")
                nameIn += whichKey.upper()
                nameCount += 1
                text( nameIn, 300, 300 )

    if mode == "Play":   # Finished entering name now ready to control games    
        text(nameIn,200,200)
    
    whichKey = ""
    

    
def setup():
    global whichKey, asciList, controlKeys, nameIn, nameLimit, nameCount, mode, numBoundaries, activeBoundaries, allBoundaries
    global removeBoundary, whichBoundary, startChosen, helpChosen, scoresChosen, resetGame
      
#variables for entering name
    asciList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0"
    controlKeys = [ ]
    whichKey = ''
    nameIn = ""
    nameLimit = 15
    nameCount = 0
    fill( 255 )
    rect ( 0 ,0, 600, 600 )
    fill( 150, 200, 200 )
    textSize ( 20 )
    text( "Enter your name > ", 100, 300 ) 
    mode = "Start"
    
    cornerPointX = 0
    cornerPointY = 0
    canvasWidth = 600
    canvasHeight = 600
    size(600,600)
    
    allBoundaries = []
    
#menu bar dimensions
    menuBarWidth = canvasWidth
    menuBarHeight = 100
    menuBarX = cornerPointX
    menuBarY = cornerPointY
    menuItemWidth = menuBarWidth // 4
    menuItemHeight = menuBarHeight
    numMenuItems = 4
    
# Adding menu items to click areas
    startLocX = menuBarX
    startLocY = menuBarY                                                                                                                   
    for i in range ( numMenuItems ):
        upperLeft = [ startLocX, startLocY ]                                        
        lowerRight = [ startLocX + menuItemWidth, startLocY + menuItemHeight ]
        clickBoundary = [ upperLeft, lowerRight ]
        allBoundaries.append( clickBoundary )
        startLocX += menuItemWidth
        
        
    startChosen = 0
    helpChosen = 1
    scoresChosen = 2
    resetGame = 3

    numBoundaries = len( allBoundaries )
    activeBoundaries = [ True for i in range( numBoundaries ) ]
    removeBoundary = False
    whichBoundary = -1
    
    image (loadImage("menu.png"), menuBarX, menuBarY, menuBarWidth, menuBarHeight)    
def mouseReleased():
    global allBoundaries, whichBoundary, removeBoundary, activeBoundaries, numBoundaries, validLocation,removeBoundary

    
    validLocation = False

    for i in range( numBoundaries ):        
        if activeBoundaries[ i ]:
            validXRange = allBoundaries[i][0][0] <= mouseX <= allBoundaries[i][1][0] 
            validYRange = allBoundaries[i][0][1]  <= mouseY <= allBoundaries[i][1][1]
            validLocation = validXRange and validYRange
            if validLocation:
                
                whichBoundary = i
                break
    if validLocation and removeBoundary:
        activeBoundaries[ whichBoundary ] = False
    
def draw():
    global whichKey, asciList, controlKeys, nameIn, nameLimit, nameCount, mode, whichBoundary, startChosen, helpChosen, scoresChosen, resetGame
    
    getPlayerName()
    
    
# menu      
    if whichBoundary == startChosen:
             
                            #Turns the click areas back on
        activeBoundaries = [ True for i in range( numBoundaries ) ]
        print("start")      
    elif whichBoundary == helpChosen:
                    # Temporarily turns off all buttons except reset game
        activeBoundaries = [ False for i in range( numBoundaries ) ]
        activeBoundaries [ resetGame ] = True
        print("help")    
    elif whichBoundary == scoresChosen:
        activeBoundaries = [ False for i in range( numBoundaries ) ]
        activeBoundaries [ resetGame ] = True
        print("scores") 
    elif whichBoundary == resetGame:
        activeBoundaries =  [ True for i in range( numBoundaries )]
        print("reset")  
    whichBoundary = -1
    
    

def keyReleased():
    global whichKey, asciList, controlKeys
    
#for entering name
    if key == CODED:
       if keyCode in controlKeys:
        whichKey = keyCode
    elif key in asciList:
        whichKey = key
    else:
        whichKey = ''
'''
