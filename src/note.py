#
# note.py by Grant Weaver
#
# This creates the class note which stores
# information about the note
#

class Note:

	note_array = ["F","G","A","B","C","D","E",]


	#pitch is the note itself (can also be rest)
	#duration is what determines the image drawn
	#clef is defined by treble or bass which will determine the y draw value
	#octaves will range from 0-2 (bass low F 3 lines below to high F 2 lines above staff)
	#x is the position the note will be placed and y which line the note is on
	def __init__(pitch, duration, clef, octave, x, y):
		self.pitch = pitch
		self.duration = duration
		self.clef = clef
		self.octave = octave
		self.x = x
		self.y = y





