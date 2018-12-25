#!/usr/bin/python3

from tkinter import *
from PIL import Image
import numpy as np	

class App:  
	def __init__(self, master):
		menubar = Menu(master, font="Arial 10")

		''' FILE MENU BAR '''
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save ...", command=master.quit)
		filemenu.add_command(label="Open ...", command=master.quit)
		filemenu.add_command(label="Exit", command=master.quit) 
		menubar.add_cascade(label="File", menu=filemenu)
		
		''' TRANSFORM MENU BAR '''
		transformmenu = Menu(menubar, tearoff=0)
		rotatemenu = Menu(transformmenu, tearoff=0)

		rotatemenu.add_command(label="Rotate 90 clockwise", command=master.quit)
		rotatemenu.add_command(label="Rotate 90 counter-clockwise", command=master.quit)
		transformmenu.add_cascade(label="Rotate", menu=rotatemenu)

		transformmenu.add_command(label="Flip", command=master.quit)
		menubar.add_cascade(label="Transform", menu=transformmenu)

		master.config(menu=menubar)

		master_frame = Frame(master, borderwidth=2)
		master_frame.pack(fill=BOTH, expand=1)

		btn_frame = Frame(master_frame, relief=SUNKEN, borderwidth=2)
		btn_frame.pack(fill=BOTH, expand=1)

		''' BUTTON INVERT '''
		frame_invert = Frame(btn_frame)
		frame_invert.pack(fill=Y, expand=1)
		button_invert = Button(
			frame_invert, font="Arial 10", text="Invert color", command=btn_frame.quit
		)
		button_invert.pack(padx=5, pady=5)

		''' BUTTON GRAYSCALE '''
		frame_grayscale = Frame(btn_frame)
		frame_grayscale.pack(fill=Y, expand=1)
		button_grayscale = Button(
			frame_grayscale, font="Arial 10", text="Grayscale", command=btn_frame.quit
		)
		button_grayscale.pack(padx=5, pady=5)

		''' BUTTON BRIGHTNESS '''
		frame_brightness = Frame(btn_frame)
		frame_brightness.pack(fill=Y, expand=1)
		label_brightness = Label(
			frame_brightness, relief=RAISED, padx=5, pady=5, font="Arial 10", text="Brightness"
		)
		label_brightness.pack(side=LEFT, padx=5, pady=5)

		button_brightness_inc = Button(
			frame_brightness, font="Arial 10", text="+", command=btn_frame.quit
		)
		button_brightness_inc.pack(side=RIGHT, padx=1, pady=1)

		button_brightness_dec = Button(
			frame_brightness, font="Arial 10", text="-", command=btn_frame.quit
		)
		button_brightness_dec.pack(side=RIGHT, padx=1, pady=1)

		''' BUTTON EDGE '''
		frame_edge = Frame(btn_frame)
		frame_edge.pack(fill=Y, expand=1)
		button_edge = Button(
			frame_edge, font="Arial 10", text="Edge highlighting", command=btn_frame.quit
		)
		button_edge.pack(padx=5, pady=5)

		''' BUTTON SHOW IMAGE '''
		frame_show = Frame(btn_frame)
		frame_show.pack(fill=Y, expand=1)
		button_show = Button(
			frame_show, font="Arial 10", fg='red', text="Show image", command=btn_frame.quit
		)		
		button_show.pack(padx=5, pady=5)

		''' LABEL STATUS '''
		frame_status = Frame(master)
		frame_status.pack(side=LEFT)
		self.label_status = Label(
			frame_status, font="Arial 10", text="STATUS: OK.", fg='green',
		)
		self.label_status.pack(padx=5, pady=5)

	def showIMG(self):
		root = Tk()
		root.title('Show Image')

		e = Entry(root, font="Arial 10")
		e.pack(padx=5, pady=5)

		img = Image.open('kvetina.jpg')
		
		self.button_show = Button(
			root, text="Show Image", command=img.show
		)
		self.button_show.pack(padx=5, pady=5)

def main():
	root = Tk()
	root.title('Image Editor')

	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2 
	h = h//2 
	w = w - 200
	h = h - 200
	root.geometry('300x300+{}+{}'.format(w, h))
	root.resizable(False, False)

	app = App(root)

	root.mainloop()
 
if __name__ == '__main__':
	main()