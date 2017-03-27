#randomizer by Grant Weaver
#
#
# The goal of this file is to randomly generate notes and
# measures that will be incorporated into the music


import note
import random

pitchs = ["A","B","C","D","E","F","G"]
durations = [64,32,16]

#takes measureNumber which determines notes y values
#returns a list of notes that would be in the measure
def generateMeasure(measureNumber, clef, timeSig):

	measure = []
	tot_duration = 64 - (16*timeSig)

	noteBar = -100
	if(measureNumber < 4):
		noteBar = 0
	elif(measureNumber < 8):
		noteBar = 1
	elif(measureNumber < 12):
		noteBar = 2
	elif(measureNumber < 16):
		noteBar = 3
	elif(measureNumber < 20):
		noteBar = 4
	elif(measureNumber < 24):
		noteBar = 5
	else:
		noteBar = 6

	while(tot_duration > 0):
		octave = random.randint(0,2)
		duration = durations[random.randint(0,2)]
		randDuration = durations[random.randint(0,2)]
		pitch = pitchs[random.randint(0,6)]
		if(random.randint(0,1) == 1):
			isRest = True
		else:
			isRest = False
		if(tot_duration - duration >= 0):
			measure.append(note.Note(pitch,duration,isRest,clef,octave,noteBar))
			tot_duration = tot_duration - duration

	return measure

def generateMusic(clef,time):
	sheetMusic = []
	for x in range(0,26):
		sheetMusic.append(generateMeasure(x + 1,clef,time))

	return sheetMusic
