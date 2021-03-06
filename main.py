#!/bin/python3

#############
# CodeCraft #
#############

#---
#Game functions
#--- 
import time 
#moves the player left 1 tile.
pickupdelay = False

  
def moveLeft():
  global playerX
  if(drawing == False and playerX > 0):
    oldX = playerX
    playerX -= 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#moves the player right 1 tile.
def moveRight():
  global playerX, MAPWIDTH
  if(drawing == False and playerX < MAPWIDTH - 1):
    oldX = playerX
    playerX += 1
    drawResource(oldX, playerY)
    drawResource(playerX, playerY)
    
#moves the player up 1 tile.
def moveUp():
  global playerY
  if(drawing == False and playerY > 0):
    oldY = playerY
    playerY -= 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)
    
#moves the player down 1 tile.
def moveDown():
  global playerY, MAPHEIGHT
  if(drawing == False and playerY < MAPHEIGHT - 1):
    oldY = playerY
    playerY += 1
    drawResource(playerX, oldY)
    drawResource(playerX, playerY)

  
def findloot():
  if random.randint(1, 3) == 1:
    print('You found some stone in the dirt!')
    inventory[STONE] += 0.5
  elif random.randint(1, 3) == 1:
    print('You found some iron in the dirt!')
    inventory[IRON] += 0.25
  elif random.randint(1, 10) == 1:
    if random.randint(1, 3) == 1:
      print('You found some diamond in the dirt!')
      inventory[DIAMOND] += 0.5
    elif random.randint(1, 2) == 1: 
      print('You found some gold in the dirt!')
      inventory[GOLD] += 0.5
    else: 
      print('You found some emerald in the dirt!')
      inventory[EMERALD] +=0.5
  
#picks up the resource at the player's position.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #if the user doesn't already have too many...
  if inventory[currentTile] < MAXTILES:
    #player now has 1 more of this resource
    if currentTile == WATER or currentTile == WOOD or currentTile == LAVA :
      inventory[currentTile] += 2
      if currentTile == WOOD:
        if random.randint(1, 2) == 1:
          print('You found some leaves in the wood!')
    else:
      inventory[currentTile] += 1
    #the player is now standing on dirt
    if not currentTile == DIRT:
      world[playerX][playerY] = DIRT
    else:
      findloot()
    #draw the new DIRT tile
    drawResource(playerX, playerY)
    #redraw the inventory with the extra resource.
    drawInventory()
    #drawPlayer()
  else: 
    print("I can\'t hold this much of this!")


#place a resource at the player's current position
def place(resource):
  #only place if the player has some left...
  if inventory[resource] > 0.5:
    #find out the resourcee at the player's current position
    currentTile = world[playerX][playerY]
    #pick up the resource the player's standing on
    #(if it's not DIRT)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #place the resource at the player's current position
    
    world[playerX][playerY] = resource
    #add the new resource to the inventory
    inventory[resource] -= 1
    #update the display (world and inventory)
    drawResource(playerX, playerY)
    drawInventory()
    #drawPlayer()
    print('You just placed', names[resource].lower())
  #...and if they have none left...
  else:
    print('Oops! You have no more', names[resource].lower(),'left')

#craft a new resource
def craft(resource): 
  #if the resource can be crafted...
  if resource in crafting:
    #keeps track of whether we have the resources
    #to craft this item
    canBeMade = True
    #for each item needed to craft the resource
    for i in crafting[resource]:
      #...if we don't have enough...
      if crafting[resource][i] > inventory[i]:
      #...we can't craft it!
        canBeMade = False
        break
    #if we can craft it (we have all needed resources)
    if canBeMade == True:
      #take each item from the inventory
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #add the crafted item to the inventory
      inventory[resource] += 1
      print('You just crafted', names[resource].lower())
    #...otherwise the resource can't be crafted...
    else:
      print('Oops! You can\'t craft', names[resource].lower())
    #update the displayed inventory
    drawInventory()

#creates a function for placing each resource
def makeplace(resource):
  return lambda: place(resource)

#attaches a 'placing' function to each key press
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#creates a function for crafting each resource
def makecraft(resource):
  return lambda: craft(resource)

#attaches a 'crafting' function to each key press
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#draws a resource at the position (y,x)
def drawResource(y, x):
  turtle.tracer(0, 1)
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #draw the resource at that position in the tilemap, using the correct image
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #draw tile with correct texture
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #nothing is now being drawn
    drawing = False
  turtle.tracer(1,1 )
    
#draws the world map
def drawWorld():
  turtle.tracer(0,1)
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
      #draw the tile at the current position
      drawResource(column, row)
  turtle.tracer(1, 1)

#draws the inventory to the screen
def drawInventory():
  turtle.tracer(0, 1)
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #use a rectangle to cover the current inventory
    rendererT.color(BACKGROUNDCOLOUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    #rendererT.setheading(0)
    for i in range(2):
      rendererT.forward(inventory_height - 60)
      rendererT.right(90)
      rendererT.forward(width)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('black')
    #display the 'place' and 'craft' text
    for i in range(1,num_rows+1):
      rendererT.goto(50, (height - (MAPHEIGHT * TILESIZE)) - (i * 100))
      rendererT.write("Amount:", False, align="center", font=("Verdana", 10, "normal"))
      rendererT.goto(50, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("Key to place:", False, align="center", font=("Verdana", 10, "normal"))
      rendererT.goto(50, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("Key to craft:", False, align="center", font=("Verdana", 10, "normal"))
    #set the inventory position
    xPosition = 120
    YPosition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #add the image
      rendererT.goto(xPosition, YPosition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #add the number in the inventory
      rendererT.goto(xPosition, YPosition - TILESIZE)
      rendererT.write(inventory[item], False, align="center", font=("Verdana", 10, "normal")) 
      #add key to place
      rendererT.goto(xPosition, YPosition - TILESIZE - 20)
      rendererT.write(placekeys[item], False, align="center", font=("Verdana", 10, "normal"))
      #add key to craft
      if crafting.get(item) != None:
        rendererT.goto(xPosition, YPosition - TILESIZE - 40)
        rendererT.write(craftkeys[item], False, align="center", font=("Verdana", 10, "normal"))     
      #move along to place the next inventory item
      xPosition += 50
      itemNum += 1
      #drop down to the next row every 10 items
      if itemNum % INVWIDTH == 0:
        xPosition = 120
        itemNum = 0
        YPosition -= TILESIZE + 80
    drawing = False
  turtle.tracer(1, 1)
#generate the instructions, including crafting rules
def generateInstructions():
  turtle.tracer(0,1)
  instructions.append('Crafting rules:')
  #for each resource that can be crafted...
  for rule in crafting:
    #create the crafting rule text
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #add the crafting rule to the instructions
    instructions.append(craftrule)
  #display the instructions
  yPos = height - 20
  for item in instructions:
    rendererT.goto(MAPWIDTH*TILESIZE + 160, yPos)
    rendererT.write(item, False, align="center", font=("Verdana", 10, "normal"))
    yPos-=20
  turtle.tracer(1,1 )
#generate a random world
def generateRandomWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in that row
    for column in range(MAPWIDTH):
      #pick a random number between 0 and 10
      randomNumber = random.randint(0,18)
      #WATER if the random number is a 1 or a 2
      if randomNumber in [1,2,3,4]:
        tile = WATER
      #GRASS if the random number is a 3 or a 4
      elif randomNumber in [5, 6, 7,8]:
        tile = GRASS
      elif randomNumber in [9, 10, 11]:
        tile = WOOD
      #otherwise it's DIRT
      elif randomNumber in [12, 13, 14]:
        tile = SAND
      elif randomNumber in [15]:
        tile = LAVA
      else:
        tile = DIRT
      #set the position in the tilemap to the randomly chosen tile
      world[column][row] = tile
  turtle.tracer(1,1)

#---
#Code starts running here
#---

#import the modules and variables needed
import turtle
import random
from variables import *
from math import ceil
print("Go to https://github.com/Coder2195Text/TrinkCraft for source code!")

TILESIZE = 20
#the number of inventory resources per row
INVWIDTH = 10
drawing = False

#create a new 'screen' object
screen = turtle.Screen()
#calculate the width and height
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height


screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#register the player image  
screen.register_shape(playerImg)
#register each of the resource images
for texture in textures.values():
  screen.register_shape(texture)

#create another turtle to do the graphics drawing
turtle.tracer(0, 1)
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#create a world of random resources.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#map the keys for moving and picking up to the correct functions.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd' )
screen.onkey(pickUp, 'space')



#set up the keys for placing and crafting each resource
bindPlacingKeys()
bindCraftingKeys()

#these functions are defined above
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()


