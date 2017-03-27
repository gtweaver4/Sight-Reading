#randomizer by Grant Weaver
#
#
# The goal of this file is to randomly generate notes and
# measures that will be incorporated into the music


import note
import random

pitchs = ["A","B","C","D","E","F","G"]
durations = [4,2,1]

#takes measureNumber which determines notes y values
#returns a list of notes that would be in the measure
def generateMeasure(measureNumber, clef):

	measure = []
	tot_duration = 64

	noteBar = -100
	if(measureNumber < 4):
		noteBar = 1
	elif(measureNumber < 8):
		noteBar = 2
	elif(measureNumber < 12):
		noteBar = 3
	elif(measureNumber < 16):
		noteBar = 4
	elif(measureNumber < 20):
		noteBar = 5
	elif(measureNumber < 24):
		noteBar = 6
	else:
		noteBar = 7


	while(tot_duration > 0):
		randDuration = durations[random.randint(0,2)]
		pitch = pitchs[random.randint(0,6)]
		if(random.randint(0,1) == 1):
			isRest = True
		else:
			isRest == False

		measure.append(note.Note(pitch,duration,isRest,clef,noteBar))

	return measure