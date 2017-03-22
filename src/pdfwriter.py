#
# pdfdrawer.py by Grant Weaver
#
# These are the functions that draw to the pdf
# 

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import note

#creates the entire sightreading
#takes integer values of clef key and time
#to determine which value gets passed
def createReading(clef, key, time):
	clefkeytimeList = determineValues(clef,key,time)
	c = createPdf()
	drawClef(c, clefkeytimeList[0])
	drawKeySignature(c, clefkeytimeList[0], key)
	drawTimeSignatures(c, clefkeytimeList[2])
	testNotes(c)
	drawBars(c)
	drawMeasures(c)
	close(c)

#creates a canvas 8x11.5 and returns it as c
def createPdf():
	c = canvas.Canvas("randomSightReading.pdf")
	c.setTitle("Random Sight Reading")
	c.setAuthor("Random Sight Reader")
	c.drawString(3*inch, 11*inch, "Created by Random Sight Reader")
	return c

#draws the staff ONLY
#measure lines will be drawn seperately based on key sig
def drawBars(c):
	y = 10.5
	x = .5
	for i in range(0,10):
		#using temp so there aren't as many draw line functions
		temp = y 
		for j in range(0,5):
			c.line(.5*inch,y*inch, 7.5*inch, y*inch)

			#draw side bars
			if(j == 4):
				c.line(.5*inch, temp*inch, .5*inch, y*inch)
				c.line(7.5*inch, temp*inch, 7.5*inch, y*inch)
			y = y - .15
		y = y - .25

#draws measure bars
def drawMeasures(c):
	l = 0
	y = 10.5
	for i in range (0,10):	
		z = .0001
		if(i == 0):
			l = 2.25
			increment = 1.75
		else:
			l = 1
			increment = 1.625
		while(l < 8):
			for x in range(0,5):
				c.line((z + l)*inch, y*inch, (z + l)*inch, (y-.6)*inch)
				z = z + .0001
			l = l + increment
		y = y - 1

#draws clef to the bars (clef = -1 for bass and 1 for treble)
def drawClef(c, clef):
		if(clef == "bass"):
			clef = "../img/Clefs/BassClef.png"
		elif(clef == "treble"):
			clef = "../img/Clefs/TrebleClef.jpg"

		y = 9.95
		for i in range(0,10):
			c.drawImage(clef, .5*inch,y*inch,width = None, height = None, mask = None)
			y = y - 1

#just an if statement that determines which clef is selected
#then uses the draw bass or treble keys
def drawKeySignature(c, clef, key):
	if(clef == "bass"):
		drawBassKeySignature(c, key)
	elif(clef == "treble"):
		drawTrebleKeySignature(c, key)

#draws the bass key signatures
def drawBassKeySignature(c, key):
	xpositions = [1.1, 1.2, 1.3,1.4, 1.5, 1.6, 1.7]
	flatY = [9.94, 10.20, 9.9, 10.13, 9.83, 10.03, 9.76]
	sharpY = [10.22, 10.01, 10.3, 10.07, 9.86, 10.15, 9.93]
	if(key < 8):
		for x in range(0, key):
			c.drawImage("../img/Flat_Sharp/flat.png", xpositions[x]*inch, flatY[x]*inch,width = None, height = None, mask = None)
	if(key > 7):
		for x in range (0, key - 7):
			c.drawImage("../img/Flat_Sharp/sharp.png", xpositions[x]*inch, sharpY[x]*inch,width = None, height = None, mask = None)

#draws the treble key signatures
def drawTrebleKeySignature(c,key):
	xpositions = [1.1, 1.2, 1.3,1.4, 1.5, 1.6, 1.7]
	flatY = [10.13, 10.36, 10.06, 10.28, 9.98, 10.21, 9.9]
	sharpY = [10.37, 10.15, 10.45, 10.22, 10.01, 10.3, 10.07]

	if(key < 8):
		for x in range(0, key):
			c.drawImage("../img/Flat_Sharp/flat.png", xpositions[x]*inch, flatY[x]*inch,width = None, height = None, mask = None)
	if(key > 7):
		for x in range (0, key - 7):
			c.drawImage("../img/Flat_Sharp/sharp.png", xpositions[x]*inch, sharpY[x]*inch,width = None, height = None, mask = None)

#determines the time signature and draws the 
#appropriate image depending on time sig
def drawTimeSignatures(c, time):
	if(time == "2/4"):
		c.drawImage("../img/TimeSignatures/24.png", 1.9*inch, 9.9*inch)
	elif(time == "3/4"):
		c.drawImage("../img/TimeSignatures/34.png", 1.9*inch, 9.9*inch)
	else:
		c.drawImage("../img/TimeSignatures/44.png", 1.9*inch, 9.9*inch)


#safely closes the pdfwriter
def close(c):
	c.showPage()
	c.save()

#this will change the integer values of key time and clef into
#string values this makes it slightly more readable but a little
#more annoying to work with
def determineValues(clef, key, time):
	clefs_array = ["bass", "treble"]
	keys_array = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb", "G","D","A", "E", "B", "F#", "C#"]
	time_array = ["2/4", "3/4", "4/4"]
	return [clefs_array[clef], keys_array[key], time_array[time]]


def testNotes(c):
	n = note.Note("F", 4, False, "bass", 1, 4, 10)
	c.drawImage("../img/NoteType/quarterNote.png", n.x, n.y)
