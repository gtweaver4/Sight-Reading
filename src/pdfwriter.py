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
			if(i == 0):
				c.line(1.10*inch,y*inch, 7.5*inch, y*inch)
			else:	
				c.line(.5*inch,y*inch, 7.5*inch, y*inch)

			#draw side bars
			if(j == 4):
				if(i == 0):
					c.line(1.10*inch, temp*inch, 1.10*inch, y*inch)
					c.line(7.5*inch, temp*inch, 7.5*inch, y*inch)
				else:
					c.line(.5*inch, temp*inch, .5*inch, y*inch)
					c.line(7.5*inch, temp*inch, 7.5*inch, y*inch)
			y = y - .15
		y = y - .75

#draws measure bars
def drawMeasures(c):
	l = 0
	y = 10.5
	for i in range (0,10):	
		z = .0001
		if(i == 0):
			l = 2.625
			increment = 1.625
		else:
			l = 1
			increment = 1.625
		while(l < 8):
			for x in range(0,5): #bolden lines
				c.line((z + l)*inch, y*inch, (z + l)*inch, (y-.6)*inch)
				z = z + .0001
			l = l + increment
		y = y - 1.5

#draws clef to the bars (clef = -1 for bass and 1 for treble)
def drawClef(c, clef):
		if(clef == "bass"):
			clef = "../img/Clefs/BassClef.png"
		elif(clef == "treble"):
			clef = "../img/Clefs/TrebleClef.jpg"

		y = 9.95
		for i in range(0,10):
			if(i == 0):
				c.drawImage(clef,1.10*inch,y*inch,width = None, height = None, mask = None)
			else:
				c.drawImage(clef, .5*inch,y*inch,width = None, height = None, mask = None)
			y = y - 1.5

#just an if statement that determines which clef is selected
#then uses the draw bass or treble keys
def drawKeySignature(c, clef, key):
	if(clef == "bass"):
		drawBassKeySignature(c, key)
	elif(clef == "treble"):
		drawTrebleKeySignature(c, key)

#draws the bass key signatures
def drawBassKeySignature(c, key):
	xpositions = [1.6,1.7,1.8,1.9,2.0,2.1,2.2]
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
	xpositions = [1.6,1.7,1.8,1.9,2.0,2.1,2.2]
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
		c.drawImage("../img/TimeSignatures/24.png", 2.35*inch, 9.9*inch)
	elif(time == "3/4"):
		c.drawImage("../img/TimeSignatures/34.png", 2.35*inch, 9.9*inch)
	else:
		c.drawImage("../img/TimeSignatures/44.png", 2.35*inch, 9.9*inch)


#safely closes the pdfwriter and saves the pdf
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

#draws the bars if the note is above or below the staff
def drawNoteBarsBelow(c, note):
	if(note.clef == "bass"):
		pitch_list = ["E","D","C","B","A","G","F"]
	else:
		pitch_list = ["C","B","A","G","F","E","D"]

	xVal = -1
	#getting the array value of the pitch
	for i in range(0, len(pitch_list)):
		if(pitch_list[i] == note.pitch):
			xVal = i
	
	if(xVal >= 0): #E or lower (bass)
		c.line(note.x - (.05 * inch), note.barInches - (.25 * inch),note.x + (.25*inch), note.barInches - (.25 * inch))
	if(xVal >= 2): #C or lower (bass)
		c.line(note.x - (.05 * inch), note.barInches - (.40 * inch),note.x + (.25*inch), note.barInches - (.40 * inch))
	if(xVal >= 4): #A or lower (bass)
		c.line(note.x - (.05 * inch), note.barInches - (.55 * inch),note.x + (.25*inch), note.barInches - (.55 * inch))
	if(xVal >= 6): #F or lower (bass)
		c.line(note.x - (.05 * inch), note.barInches - (.7 * inch),note.x + (.25*inch), note.barInches - (.7 * inch))

def drawNoteBarsAbove(c, note):
	#TODO fix array search to only include notes above clef?
	#TODO make the notes inverted above the staff?
	if(note.clef == "bass"):
		pitch_list = ["G","A","B","C","D","E","F"]
	else:
		pitch_list = ["E","F","G","A","B","C","D"]

	xVal = -1
	#getting value of the pitch
	for i in range(0, len(pitch_list)):
		if(pitch_list[i] == note.pitch):
			xVal = i

	if(xVal == 6):
		return
	if(xVal >= 3): #C or Higher
		c.line(note.x - (.05 * inch), note.barInches + (.65 * inch),note.x + (.25*inch), note.barInches + (.65 * inch))
	if(xVal >= 5): #E or Higher
		c.line(note.x - (.05 * inch), note.barInches + (.8 * inch),note.x + (.25*inch), note.barInches + (.8 * inch))


############
#DRAW NOTES
#draws notes at (x,y) which is built into the note class
def drawQuarterNote(c,note):
	c.drawImage("../img/NoteType/quarterNote.png", note.x, note.y)
	if(note.octave == 0):
		drawNoteBarsBelow(c,note)
	elif(note.octave == 2):
		drawNoteBarsAbove(c,note)

def drawHalfNote(c,note):
	drawNoteBars(c,note)
	c.drawImage("../img/NoteType/halfNote.png", note.x,note.y)

def drawWholeNote(c,note):
	drawNoteBars(c,note)
	c.drawImage("../img/NoteType/wholeNote.png",note.x,note.y)

def drawSingleEigthNote(c,note):
	drawNoteBars(c,note)
	c.drawImage("../img/NoteType/singleEigth.png", note.x,note.y)

def drawSingleSixteenthNote(c,note):
	drawNoteBars(c,note)
	c.drawImage("../img/NoteType/singleSixteenth.png",note.x,note.y)

##########
#DRAW RESTS
#draws the rests at (x,y) which is built into the Note class
def drawQuarterRest(c,note):
	c.drawImage("../img/NoteType/quarterRest.png",note.x,note.y)

def drawWholeRest(c,note):
	c.drawImage("../img/NoteType/whole_halfRest.png",note.x,note.y + 20)

def drawHalfRest(c,note):
	c.drawImage("../img/NoteType/whole_halfRest.png",note.x,note.y - 20)

def drawEigthRest(c,note):
	c.drawImage("../img/NoteType/singleEigth.png",note.x,note.y)

def drawSingleSixteenthRest(c,note):
	c.drawImage("../img/NoteType/singleSixteenth.png",note.x,note.y)

def testNotes(c):
	noteTestList = []
	for x in range(0,7):
		noteTestList.append(note.Note("F",4,False,"bass",0,3,x))
	for notetest in noteTestList:
		drawQuarterNote(c,notetest)