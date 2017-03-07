#
# main.py by Grant Weaver
#
# This is the main application to the random sheet music generator
#

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image

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


		
#does the ending operations of "show page"
#which ends editing of file and saves file
def close(c):
	c.showPage()
	c.save()

#
# MAIN STATEMENT
#

#creating the canvas to draw on
c = create_canvas()
draw_clef(c, "treble")
draw_bars(c)

#closing file gracefully
close(c)