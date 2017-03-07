#
# main.py by Grant Weaver
#
# This is the main application to the random sheet music generator
#

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image

#11.5 top of paper very top of paper for draw string


'''
Tried to get the jpg image of the sheet music to be drawn and it doesnt work
def draw_bass_cleff(c):
	bass_cleff = Image.open("../img/BassCleff/CommonTimeCMajorBassCleff")
	bass_cleff.load()
	c.drawImage(bass_cleff, 0, 12*inch, width = None, height = None, mask = None)
'''



def create_canvas():
	'''
	c.translate(inch,inch)
	c.setFont("Helvetica", 14)
	c.setStrokeColorRGB(0.2,0.5,0.3)
	c.setFillColorRGB(1,0,1)
	c.line(0,10.5*inch,0,1.7*inch)
	c.line(0,10*inch,1*inch,0)
	'''
	c = canvas.Canvas("test.pdf")
	c.setTitle("Sheet Music")
	c.setAuthor("Random Sheet Music Generator")
	c.drawString(3*inch, 11*inch, "Created by Random Sight Reader")

	return c


#creating the canvas to draw on
c = create_canvas()





#draw_bass_cleff(c)



#ending the page
c.showPage()

#saving the page
c.save()