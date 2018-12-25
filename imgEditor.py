#!/usr/bin/python3

from tkinter import *
from PIL import Image
import numpy as np

def createMenuBar(master):
		menubar = Menu(master, font="Arial 10")

		''' FILE MENU BAR '''
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save ...", command=master.quit)
		filemenu.add_command(label="Load ...", command=master.quit)
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

def createButtons(master):
		master_frame = Frame(master)
		master_frame.pack()

		btn_frame = Frame(master_frame, relief=SUNKEN, borderwidth=2)
		btn_frame.pack(fill=BOTH, expand=1)
		
		button_invert = Button(
			btn_frame, font="Arial 10", text="Invert color", command=btn_frame.quit
		)
		button_invert.pack(padx=5, pady=5)
		
		button_grayscale = Button(
			btn_frame, font="Arial 10", text="Grayscale", command=btn_frame.quit
		)
		
		button_grayscale.pack(padx=5, pady=5)

		button_brightness = Button(
			btn_frame, font="Arial 10", text="Brightness", command=btn_frame.quit
		)
		
		button_brightness.pack(padx=5, pady=5)

		button_edges = Button(
			btn_frame, font="Arial 10", text="Edges", command=btn_frame.quit
		)
		
		button_edges.pack(padx=5, pady=5)

		button_show = Button(
			btn_frame, font="Arial 10", fg='red', text="Show image", command=btn_frame.quit
		)
		
		button_show.pack(padx=5, pady=5)

class App:  
	def __init__(self, master):
		createMenuBar(master)
		createButtons(master)

	def showIMG(self):
		root = Tk()
		root.title('Show Image')

		e = Entry(root, font="Arial 16")
		e.pack(padx=5, pady=5)

		img = Image.open('kvetina.jpg')
		
		self.button_show = Button(
			root, text="Show Image", command=img.show
		)
		self.button_show.pack(padx=5, pady=5)

def main():
	root = Tk()
	root.title('Image Editor')
	app = App(root)

	root.mainloop()
 
if __name__ == '__main__':
	main()