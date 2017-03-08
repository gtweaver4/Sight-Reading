#
# main.py by Grant Weaver
#
# This is the main application to the random sheet music generator
# The page is 8x11.5, the staff has a .5 inch padding
#

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image
from Tkinter import *
import sys

#returns the newly created canvas (8x11.5)
def create_canvas():
	c = canvas.Canvas("test.pdf")
	c.setTitle("Sheet Music")
	c.setAuthor("Random Sheet Music Generator")
	c.drawString(3*inch, 11*inch, "Created by Random Sight Reader")
	return c

#draws the staff ONLY
#measure lines will be drawn seperately based on key sig
def draw_bars(c):
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

#draws clef to the bars (clef = -1 for bass and 1 for treble)
def draw_clef(c, clef):
		if(clef == "bass"):
			clef = "../img/Clefs/BassClef.png"
		else:
			clef = "../img/Clefs/TrebleClef.jpg"

		y = 9.95
		for i in range(0,10):
			c.drawImage(clef, .5*inch,y*inch,width = None, height = None, mask = None)
			y = y - 1




#BEADGCF
def draw_bass_key_signature(c, key):
	#stuff
	i = 0

def draw_treble_key_signature(c,key):
	#stuff
	i = 0

#does the ending operations of "show page"
#which ends editing of file and saves file
def close(c):
	c.showPage()
	c.save()



#tk functions
def exit():
	sys.exit()

def update():
	v.get()


#
# MAIN STATEMENT
#


#Tk window
root = Tk()
root.title("Random Sheet Music")
root.geometry('750x750')

#Tk widgets
explanation_label = Label(root, text = "You are currently in treble clef in the key of C in the time of 4/4", padx = 175, pady = 50)
explanation_label.pack(anchor = W)

#clef stuff
clef_label = Label(root, text = "Clef Options",pady = 10).pack(anchor = W)
clef_radiobtn_group = IntVar()
treble_clef_radiobtn = Radiobutton(root, text = "Treble", variable = clef_radiobtn_group, value = 1).pack(anchor = W)
bass_clef_radiobtn = Radiobutton(root, text = "Bass", variable = clef_radiobtn_group, value = 2).pack(anchor = W)


#key signature stuff
key_signature_label = Label(root, text = "Key Signatures Options",pady = 10).pack(anchor = W)
key_sigs_radiobtn_group = IntVar()
twofour_radiobtn = Radiobutton(root, text = "2/4", variable = key_sigs_radiobtn_group, value = 1)
twofour_radiobtn.pack(anchor = W)
threefour_radiobtn = Radiobutton(root, text = "3/4", variable = key_sigs_radiobtn_group, value = 2)
threefour_radiobtn.pack(anchor = W)
fourfour_radiobtn = Radiobutton(root, text = "4/4", variable = key_sigs_radiobtn_group, value = 3)
fourfour_radiobtn.pack(anchor = W)




update_button = Button(root, text = "Update", command = lambda root = root:update()).pack(anchor = W)
generate_music_button = Button(root,text = "Generate Music", command = lambda root = root:generate()).pack(anchor = W)
cancel_button = Button(root, text = "Cancel", command = lambda root = root:exit()).pack(anchor = W)




root.mainloop()



'''
clef = "treble"
#creating the canvas to draw on
c = create_canvas()
#draw the clef first because the bars go over the clef 
draw_clef(c, clef)

key = "F"

if(clef == "bass"):
	draw_bass_key_signature(c, key)
else:
	draw_treble_key_signature(c,key)

draw_bars(c)

#closing file gracefully
close(c)
'''