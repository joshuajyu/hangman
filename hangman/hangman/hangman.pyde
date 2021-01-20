#hangman

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
                text( nameIn, 300, 100 )

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
    text( "Enter your name > ", 100, 100 ) 
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
