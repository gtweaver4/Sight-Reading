#
# note.py by Grant Weaver
#
# This creates the class note which stores
# information about the note
#

from reportlab.lib.units import inch

class Note:

	#these two arrays will be the position of the notes
	letterBassArray = ["F","G","A","B","C","D","E"]
	letterTrebleArray = ["D","E","F","A","B","C"]
	bassclefArray = [0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,00]
	trebleclefArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

	#pitch is the note itself (can also be rest)
	#duration is what determines the image drawn
	#is rest will take the mix duration and is rest to determine image
	#clef is defined by treble or bass which will determine the y draw value
	#octaves will range from 0-2 (bass low F 3 lines below to high F 2 lines above staff)
	#x is the position the note will be placed and y which line the note is on
	#bar will be which bar line the note is on 10 is top 1 is lowest
	def __init__(self, pitch, duration, isRest, clef, octave, x, bar):
		self.pitch = pitch
		self.duration = duration
		self.isRest = isRest
		self.clef = clef
		self.octave = octave
		self.x = x * inch
		self.bar = bar + .5 #this is to get the top of the bar
		self.y = self.getArrayPosition(pitch, bar, clef, octave)

	#retturns the position on the letter array (used to determine y values)
	@staticmethod
	def getArrayPosition(pitch, bar, clef, octave):
		#these two arrays will be the position of the notes
		letterBassArray = ["F","G","A","B","C","D","E"]
		letterTrebleArray = ["D","E","F","A","B","C"]
		bassclefArray = [0,0,0,0,0,0,0,-.7,0,0,00,0,0,0,0,0,0,0,0,0,00]
		trebleclefArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


		xVal = 0
		if(clef == "bass"):
			for x in range(0, len(letterBassArray)):
				if(letterBassArray[x] == pitch):
					xVal = x + (octave * 6)
					return (bassclefArray[xVal] + bar) * inch
		if(clef == "treble"):
			for x in range(0, len(letterTrebleArray)):
				if(letterTrebleArray[x] == pitch):
					xVal = x + (octave * 6)
					return (trebleclefArray[xVal] + bar) * inch
		return 0;

	#not sure if this will be used but figured i would include it
	def dropOctave():
		self.octave = self.ocatave - 1

	def raiseOctave():
		self.octave = self.octave + 1

