#
# note.py by Grant Weaver
#
# This creates the class note which stores
# information about the note
#

from reportlab.lib.units import inch

class Note:
	#pitch is the note itself (can also be rest) without flats or sharps these are
	#determines by the key signature
	#duration is what determines the image drawn
	#is rest will take the mix duration and is rest to determine image
	#clef is defined by treble or bass which will determine the y draw value
	#octaves will range from 0-2 (bass low F 3 lines below to high F 2 lines above staff)
	#bar will be which bar line the note is on 10 is top 1 is lowest
	def __init__(self, pitch, duration, isRest, clef, octave, x, bar):
		self.pitch = pitch
		self.duration = duration
		self.isRest = isRest
		self.clef = clef
		self.octave = octave
		self.bar = bar
		self.barInches = self.getBarInches(bar)
		self.y = self.getArrayPosition(pitch, self.barInches, clef, octave)

	#retturns the position on the letter array (used to determine y values)
	@staticmethod
	def getArrayPosition(pitch, barInches, clef, octave):
		#these two arrays will be the position of the notes
		letterBassArray = ["F","G","A","B","C","D","E"]
		letterTrebleArray = ["D","E","F","G","A","B","C"]
		positionArray = [-.76,-.69,-.6,-.51,-.46,-.37,-.3,-.23,-.16,-.09,-.01,.06,.14,.21,.28,.36,.43,.5,.60,.67,.75]
		xVal = 0
		if(clef == "bass"):
			for x in range(0, len(letterBassArray)):
				if(letterBassArray[x] == pitch):
					xVal = x + (octave * 7)
					return ((positionArray[xVal] * inch)+ barInches)
		elif(clef == "treble"):
			for x in range(0, len(letterTrebleArray)):
				if(letterTrebleArray[x] == pitch):
					xVal = x + (octave * 7)
					return ((positionArray[xVal] * inch)+ barInches)
		else: #returns 0 for notes
			return 0

		return 0

	#turns the bar number into the number of inches from the bottom
	@staticmethod
	def getBarInches(bar):
		barInches = [10, 8.5, 7, 5.5, 4, 2.5, 1]
		return barInches[bar] * inch