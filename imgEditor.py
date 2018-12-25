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

class App:  
	def __init__(self, master):
		master_frame = Frame(master)
		master_frame.pack()
		
		createMenuBar(master)

def main():
	root = Tk()
	root.title('Image Editor')
	app = App(root)

	root.mainloop()
 
if __name__ == '__main__':
	main()