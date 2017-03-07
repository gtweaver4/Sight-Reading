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
		




#creating the canvas to draw on
c = create_canvas()

draw_bars(c)



#draw_bass_cleff(c)



#ending the page
c.showPage()

#saving the page
c.save()