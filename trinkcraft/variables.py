#!/bin/python3

#Game variables that can be changed!
import random

#game background colour.
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
BACKGROUNDCOLOUR = (r,g,b)

#map variables.
MAXTILES  = 64
MAPWIDTH  = 32
MAPHEIGHT = 32

#variables representing the different resources.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANKS  = 6
GLASS   = 7
COBBLESTONE = 8
STONE   = 9
LAVA    = 10
IRON    = 11
DIAMOND = 12
GOLD    = 13
EMERALD = 14
LEAVES = 15

#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK, WOOD, SAND, PLANKS, GLASS, COBBLESTONE, STONE,LAVA, IRON, DIAMOND, GOLD, EMERALD, LEAVES]

#the names of the resources.
names = {
  DIRT    : 'Dirt',
  GRASS   : 'Grass',
  WATER   : 'Water',
  BRICK   : 'Brick',
  WOOD    : 'Wood',
  SAND    : 'Sand',
  PLANKS  : 'Planks',
  GLASS   : 'Glass',
  COBBLESTONE : 'Cobblestone',
  STONE   : 'Stone',
  LAVA    : 'Lava',
  IRON    : 'Iron',
  DIAMOND : 'Diamond',
  GOLD    : 'Gold',
  EMERALD : 'Emerald',
  LEAVES  : 'Leaves',
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  WOOD    : 'wood.gif',
  SAND    : 'sand.gif',
  PLANKS  : 'plank.gif',
  GLASS   : 'glass.gif',
  COBBLESTONE: 'cobblestone.gif',
  STONE   : 'stone.gif',
  LAVA    : 'lava.gif',
  IRON    : 'iron.gif',
  DIAMOND : 'diamond.gif',
  GOLD    : 'gold.gif',
  EMERALD : 'emerald.gif',
  LEAVES  : 'leaves.gif',
}

#the number of each resource the player has.
inventory = {
  DIRT    : random.randint(0, 15),
  GRASS   : random.randint(0, 15),
  WATER   : random.randint(0, 15),
  BRICK   : random.randint(0, 15),
  WOOD    : random.randint(0, 15),
  SAND    : random.randint(0, 15),
  PLANKS  : random.randint(0, 15),
  GLASS   : random.randint(0, 15),
  COBBLESTONE: random.randint(0,15),
  STONE   : random.randint(0,15),
  LAVA    : random.randint(0,15),
  IRON    : random.randint(0, 15),
  DIAMOND : random.randint(0, 15),
  GOLD    : random.randint(0, 15),
  EMERALD : random.randint(0, 15),
  LEAVES  : random.randint(0, 15)
}

#the player image.
playerImg = 'player.gif'

#the player position.
playerX = random.randint(0, MAPWIDTH-1)
playerY = random.randint(0, MAPHEIGHT-1)

#rules to make new resources.
crafting = {
  BRICK    : { WATER : 0.5, DIRT : 0.5, SAND: 0.5 },
  GRASS    : { WATER : 0.5, DIRT : 1},
  SAND     : {DIRT : 1, LAVA : 0.5},
  PLANKS   : { WOOD : 0.5},
  GLASS    : { SAND : 1, LAVA : 0.5},
  COBBLESTONE: {WATER: 1, LAVA : 1},
}

#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4',
  WOOD  : '5',
  SAND  : '6',
  PLANKS: '7',
  GLASS : '8',
  COBBLESTONE: '9',
  STONE : '0',
  LAVA  : 'o',
  IRON  : 'p',
  DIAMOND: 'f',
  GOLD  : 'g',
  EMERALD: 'h',
  LEAVES: 'j'
  
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'e',
  GRASS : 'r',
  SAND  : 't',
  PLANKS: 'y',
  GLASS : 'u',
  COBBLESTONE:'i',
  
}
#game instructions that are displayed.
instructions =  [
  'Instructions:',
  'Use WASD to move',
  'Space to mine',
  "Use the corresponding keys to place/craft"
]
