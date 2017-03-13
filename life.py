# life.py
# A simulation of life.
# 
# Jody Shanabrook
# 3/1/17

import picture
import time
import copy
import random




def setup():  #Gets inputs from user and sets up the starting board accordingly
	print("Welcome to Conway's: Game of Life")
	print("There are 3 preset starting positions")
	presetinput=input("Enter \"1\" for preset 1, \"2\" for preset 2, \"3\" for preset 3, or \"rand\" for a surprise!")
	advanced=input("Would you like to access the advanced settings? Input y/n.")
	
	global w
	global h
	global rounds
	global board
	global boardNew
	global cellsize
	global timedelay
	
	w=50										#default settings
	h=80
	rounds=200
	cellsize=6
	timedelay=0
	
	if advanced == "y":							#advanced imput just for fun
		w=eval(input("Please input a width:"))
		h=eval(input("Please input a height:"))
		rounds=eval(input("Please input a number of rounds:"))
		cellsize=eval(input("Please input the size of each cell (in pixels):"))
		timedelay=eval(input("Please input a time delay:"))
	
	preset1 = []
	for i in range(h) :
		preset1.append([0]*w)
	preset1[10][10]=1
	preset1[10][11]=1
	preset1[9][11]=1
	preset1[11][11]=1
	preset1[9][12]=1
	
	preset2 = []
	for i in range(h) :
		preset2.append([0]*w)
	preset2[3][3]=1
	preset2[5][3]=1
	preset2[4][4]=1
	preset2[5][4]=1
	preset2[4][5]=1
	preset2[5][3]=1
	preset2[6][3]=1
	preset2[7][4]=1
	preset2[8][4]=1
	preset2[9][5]=1
	preset2[6][13]=1
	preset2[7][14]=1
	preset2[8][14]=1
	preset2[9][15]=1
	preset2[8][13]=1
	preset2[10][14]=1
	preset2[8][14]=1
	preset2[9][15]=1
	
	preset3 = []				#glider
	for i in range(h) :
		preset3.append([0]*w)
	preset3[3][3]=1
	preset3[5][3]=1
	preset3[4][4]=1
	preset3[5][4]=1
	preset3[4][5]=1
	
	presetrand = []				#this one is a raondom 50/50 distribution of starting tiles
	for i in range(h) :
		presetrand.append([0]*w)
	for i in range (0,h):
		for j in range (0,w):
			presetrand[i][j]=rInt = random.randrange(2)
	
	if presetinput=="1":
		board=preset1
	elif presetinput=="2":
		board=preset2
	elif presetinput=="3":
		board=preset3
	elif presetinput=="rand":
		board=presetrand

	boardNew = copy.deepcopy(board)




def numneighbors(i,j): 			#this function gets the number of neighbors, it just sums the values of the 8 surrounding "tiles"
	num = board[(i-1)%h][(j-1)%w] + board[(i-1)%h][(j)%w] + board[(i-1)%h][(j+1)%w] + board[(i)%h][(j-1)%w] + board[(i)%h][(j+1)%w] + board[(i+1)%h][(j-1)%w] + board[(i+1)%h][(j)%w] + board[(i+1)%h][(j+1)%w]
	return num


def iterate():
	global board #for some reason it needed this here as well
	for i in range (0,h):			#cycles through the rows
		for j in range (0,w):		#and columns
			if board[i][j] == 1:
				if numneighbors(i,j) == 0 or numneighbors(i,j) == 1 or numneighbors(i,j) >= 4:		#conditions resulting in dead cell
					boardNew[i][j] = 0
			else:
				if numneighbors(i,j) == 3:															#condution resulting in new live cell
					boardNew[i][j] = 1
	board = copy.deepcopy(boardNew)				#reseting the board

def vissetup():
	global boardvis
	global tiles
	boardvis = picture.Picture((cellsize*h+1,cellsize*w+1))		#creating canvas (the +1 is just for the outline on the edge, which would get cut off)
	tiles=[]													#creates empty list of lists
	for i in range(h) :
		tiles.append([0]*w)
	for i in range(h):											#fills lists with "tile" objects in canvas
		for j in range (w):
			tile=boardvis.drawRectFill(cellsize*i,cellsize*j,cellsize,cellsize)
			tiles[i][j] = tile

def visiterate(): 
	for i in range (0,h):			#cycles through all tiles
		for j in range (0,w):	
			if board[i][j] == 1:	#green if alive
				tiles[i][j].changeFillColor((10, 250,105))
			if board[i][j] == 0:	#black if dead
				tiles[i][j].changeFillColor((255,255,255))
	boardvis.display()

def main():
	setup()
	vissetup()
	for i in range (0,rounds+1):
		visiterate()
		iterate()
		time.sleep(timedelay)  #useful if you want the game to run slower, but not necessary with larger board sizes (because it's already pretty slow)

main()
