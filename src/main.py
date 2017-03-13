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
import pdfdrawer


#tk functions
def exit():
	sys.exit()

#generates the music and writes to the file all of the music
def generate():
	clef = clef_group.get()
	key = key_sig_group.get()
	time = time_sigs_group.get()

	pdfdrawer.createReading(clef, key, time)

	exit()

#
# MAIN STATEMENT
#


#Tk window
root = Tk()
root.title("Random Sheet Music")
root.geometry('400x450')

#Tk widgets
#clef stuff
clef_frame = Frame(root)
clef_label = Label(clef_frame, text = "Clef Options",padx = 170,pady = 10).pack(anchor = W)
clef_group = IntVar()
treble_clef_radiobtn = Radiobutton(clef_frame, text = "Treble",padx = 60 ,variable = clef_group, value = 1).pack(side = LEFT)
bass_clef_radiobtn = Radiobutton(clef_frame, text = "Bass", padx = 60, variable = clef_group, value = -1).pack(side = LEFT)

clef_frame.pack(anchor = W)

#time signature stuff
time_sig_frame = Frame(root)
Label(root, text = "Time Signatures Options",padx = 125,pady = 10).pack(anchor = W)
time_sigs_group = IntVar()
twofour_radiobtn = Radiobutton(time_sig_frame, text = "2/4",padx = 40 ,variable = time_sigs_group, value = 1)
twofour_radiobtn.pack(side = LEFT)
threefour_radiobtn = Radiobutton(time_sig_frame, text = "3/4",padx = 40 ,variable = time_sigs_group, value = 2)
threefour_radiobtn.pack(side = LEFT)
fourfour_radiobtn = Radiobutton(time_sig_frame, text = "4/4",padx = 40 ,variable = time_sigs_group, value = 3)
fourfour_radiobtn.pack(side = LEFT)

time_sig_frame.pack(anchor = W)

#key sig stuff I could probably loop this but
#am having issues with the frames
# every sharp is +1 every flat is -1 with key of C beting 0
Label(root, text = "Key Signature Options", padx = 125 ,pady = 10).pack(anchor = W)
key_sig_group = IntVar()
key_c_radiobtn = Radiobutton(root, text = "Key of C", padx = 170 ,variable = key_sig_group, value = 0).pack(anchor = W)

key_sig_frame1 = Frame(root)
key_f_radiobtn = Radiobutton(key_sig_frame1, text = "Key of F  ", padx = 60 ,variable = key_sig_group, value = -1).pack(side = LEFT)
key_G_radiobtn = Radiobutton(key_sig_frame1, text = "Key of G",  padx = 60 ,variable = key_sig_group, value =  1).pack(side = LEFT)
key_sig_frame1.pack(anchor = W)

key_sig_frame2 = Frame(root)
key_Bb_radiobtn = Radiobutton(key_sig_frame2, text = "Key of Bb", padx = 60 , variable = key_sig_group, value = -2).pack(side = LEFT)
key_D_radiobtn = Radiobutton(key_sig_frame2, text = "Key of D", padx = 60 , variable = key_sig_group, value = 2).pack(side = LEFT)
key_sig_frame2.pack(anchor = W)

key_sig_frame3 = Frame(root)
key_Eb_radiobtn = Radiobutton(key_sig_frame3, text = "Key of Eb", padx = 60 , variable = key_sig_group, value = -3).pack(side = LEFT)
key_A_radiobtn = Radiobutton(key_sig_frame3, text = "Key of A", padx = 60 , variable = key_sig_group, value = 3).pack(side = LEFT)
key_sig_frame3.pack(anchor = W)

key_sig_frame4 = Frame(root)
key_Ab_radiobtn = Radiobutton(key_sig_frame4, text = "Key of Ab", padx = 60 , variable = key_sig_group, value = -4).pack(side = LEFT)
key_E_radiobtn = Radiobutton(key_sig_frame4, text = "Key of E", padx = 60 , variable = key_sig_group, value = 4).pack(side = LEFT)
key_sig_frame4.pack(anchor = W)

key_sig_frame5 = Frame(root)
key_Db_radiobtn = Radiobutton(key_sig_frame5, text = "Key of Db", padx = 60 , variable = key_sig_group, value = -5).pack(side = LEFT)
key_B_radiobtn = Radiobutton(key_sig_frame5, text = "Key of B", padx = 60 , variable = key_sig_group, value = 5).pack(side = LEFT)
key_sig_frame5.pack(anchor = W)

key_sig_frame6 = Frame(root)
key_Gb_radiobtn = Radiobutton(key_sig_frame6, text = "Key of Gb", padx = 60 , variable = key_sig_group, value = -6).pack(side = LEFT)
key_FS_radiobtn = Radiobutton(key_sig_frame6, text = "Key of F#", padx = 60 , variable = key_sig_group, value = 6).pack(side = LEFT)
key_sig_frame6.pack(anchor = W)

key_sig_frame7 = Frame(root)
key_Cb_radiobtn = Radiobutton(key_sig_frame7, text = "Key of Cb", padx = 60 , variable = key_sig_group, value = -7).pack(side = LEFT)
key_CS_radiobtn = Radiobutton(key_sig_frame7, text = "Key of C#", padx = 60 , variable = key_sig_group, value = 7).pack(side = LEFT)
key_sig_frame7.pack(anchor = W)

Label(root,text = "\n\n").pack()

#button stuff
generate_music_button = Button(root,text = "Generate Music", padx = 170, pady = 10 ,command = lambda root = root:generate()).pack(anchor = W)

cancel_button = Button(root, text = "Cancel", padx = 190 , pady = 10 ,command = lambda root = root:exit()).pack(anchor = W)

root.mainloop()

#safe fail of tk window & program
sys.exit()