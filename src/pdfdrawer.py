#
# pdfdrawer.py by Grant Weaver
#
# These are the functions that draw to the pdf
# 

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


#creates the entire sightreading
#takes integer values of clef key and time
#to determine which value gets passed
def createReading(clef, key, time):
	clefkeytimeList = determineValues()
	c = createPdf()




#creates a canvas 8x11.5 and returns it as c
def createPdf():
	c = canvas.Canvas("randomSightReading.pdf")
	c.setTitle("Random Sight Reading")
	c.setAuthor("Random Sight Reader")
	c.drawString(3*inch, 11*inch, "Created by Random Sight Reader")
	return c

#draws clef to the bars (clef = -1 for bass and 1 for treble)
def drawClef(c, clef):
		if(clef == -1):
			clef = "../img/Clefs/BassClef.png"
		else:
			clef = "../img/Clefs/TrebleClef.jpg"

		y = 9.95
		for i in range(0,10):
			c.drawImage(clef, .5*inch,y*inch,width = None, height = None, mask = None)
			y = y - 1

#just an if statement that determines which clef is selected
#then uses the draw bass or treble keys
def drawKeySignature(c, clef, key):
	if(clef == -1):
		drawBassKeySignature(c, key)
	else:
		drawTrebleKeySignature(c, key)

#draws the bass key signatures
def drawBassKeySignature(c, key):
	xpositions = [1.1, 1.2, 1.3,1.4, 1.5, 1.6, 1.7]
	flatY = [9.94, 10.20, 9.9, 10.13, 9.83, 10.03, 9.76]
	sharpY = [10.22, 10.01, 10.3, 10.07, 9.86, 10.15, 9.93]
	if(key < 0):
		for x in range(0, abs(key)):
			c.drawImage("../img/Flat_Sharp/flat.png", xpositions[x]*inch, flatY[x]*inch,width = None, height = None, mask = None)
	if(key > 0):
		for x in range (0, key):
			c.drawImage("../img/Flat_Sharp/sharp.png", xpositions[x]*inch, sharpY[x]*inch,width = None, height = None, mask = None)

#draws the treble key signatures
def drawTrebleKeySignature(c,key):
	#stuff
	i = 0

#safely closes the pdfwriter
def close(c):
	c.showPage()
	c.save()

#this will change the integer values of key time and clef into
#string values this makes it slightly more readable but a little
#more annoying to work with
def determineValues(clef, key, time):
	clefs = ["bass", "treble"]
	keys = ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb", "G","D","A", "E", "B", "F#", "C#"]
	time = ["2/4", "3/4", "4/4"]