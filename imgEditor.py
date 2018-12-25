#!/usr/bin/python3

from tkinter import *
from PIL import Image
import numpy as np	
import os

class App:  
	def __init__(self, master):
		self.image_data = np.array([])

		master_frame = Frame(master, borderwidth=2)
		master_frame.pack(fill=BOTH, expand=1)

		menubar = Menu(master, font="Arial 10")

		''' FILE MENU BAR '''
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save ...", command=self.saveFile)
		filemenu.add_command(label="Open ...", command=self.openFile)
		filemenu.add_command(label="Exit", command=master.destroy) 
		menubar.add_cascade(label="File", menu=filemenu)
		
		''' TRANSFORM MENU BAR '''
		transformmenu = Menu(menubar, tearoff=0)
		
		''' ROTATE TRANSFORM '''
		rotatemenu = Menu(transformmenu, tearoff=0)
		rotatemenu.add_command(label="Rotate 90 clockwise", command=self.rotateRight)
		rotatemenu.add_command(label="Rotate 90 counter-clockwise", command=self.rotateLeft)
		transformmenu.add_cascade(label="Rotate", menu=rotatemenu)

		''' FLIP TRANSFORM '''
		flipmenu = Menu(transformmenu, tearoff=0)
		flipmenu.add_command(label="Flip Horizontally", command=self.flitHoriz)
		flipmenu.add_command(label="Flip Vertically", command=self.flitVert)
		transformmenu.add_cascade(label="Flip", menu=flipmenu)

		menubar.add_cascade(label="Transform", menu=transformmenu)
		master.config(menu=menubar)

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
		label_brightness.pack(side=LEFT)

		button_brightness_inc = Button(
			frame_brightness, font="Arial 10", text="+", command=btn_frame.quit
		)
		button_brightness_inc.pack(side=RIGHT)

		button_brightness_dec = Button(
			frame_brightness, font="Arial 10", text="-", command=btn_frame.quit
		)
		button_brightness_dec.pack(side=RIGHT)

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
			frame_show, font="Arial 10", fg='red', text="Show image", command=self.showImage
		)		
		button_show.pack(padx=5, pady=5)

		''' LABEL STATUS '''
		frame_status = Frame(master)
		frame_status.pack(side=LEFT)
		self.label_status = Label(
			frame_status, font="Arial 10", text=" ", fg='green',
		)
		self.label_status.pack(padx=5, pady=5)

	def openFile(self):
		self.top = Toplevel()
		self.top.title('Open File')
		self.top.resizable(False, False)

		label_show = Label(
			self.top, text="Enter the name of image:", font="Arial 10"
		)
		label_show.pack(padx=5, pady=5)

		self.e_open = Entry(self.top, font="Arial 12")
		self.e_open.pack(padx=5, pady=5)
		
		button_open = Button(
			self.top, text="Open Image", command=self.openImage, font="Arial 10"
		)
		button_open.pack(padx=5, pady=5)

		self.top.mainloop()

	def openImage(self):
		name = self.e_open.get()
		exists = os.path.isfile(name)
		if not name:
			self.label_status.config(text='WRITE THE NAME OF FILE.', fg='red')
			return
		elif not exists:
			self.label_status.config(text='FILE DOESN\'T EXISTS.', fg='red')
			return
		else:
			img = Image.open(name)
			self.image_data = np.asarray(img)
			img.show()
			self.label_status.config(text='FILE IS OPEN.', fg='green')

		self.top.destroy()

	def saveFile(self):
		self.top = Toplevel()
		self.top.title('Save File')
		self.top.resizable(False, False)

		label_show = Label(
			self.top, text="Enter the name of image:", font="Arial 10"
		)
		label_show.pack(padx=5, pady=5)

		self.e_save = Entry(self.top, font="Arial 12")
		self.e_save.pack(padx=5, pady=5)
		
		button_save = Button(
			self.top, text="Save Image", command=self.saveImage, font="Arial 10"
		)
		button_save.pack(padx=5, pady=5)

		self.top.mainloop()

	def saveImage(self):
		name = self.e_save.get()
		out = Image.fromarray(self.image_data, 'RGB')
		out.save(name)
		self.label_status.config(text='IMAGE IS SAVE.', fg='green')
		self.top.destroy()

	def showImage(self):
		out = Image.fromarray(self.image_data, 'RGB')
		out.show()

	def rotateRight(self):
		self.image_data = np.rot90(self.image_data, -1)
		self.label_status.config(text='IMAGE WAS ROTATED.', fg='green')

	def rotateLeft(self):
		self.image_data = np.rot90(self.image_data, 1)
		self.label_status.config(text='IMAGE WAS ROTATED.', fg='green')

	def flitHoriz(self):
		self.image_data = np.flipud(self.image_data)
		self.label_status.config(text='IMAGE WAS FLIPED.', fg='green')

	def flitVert(self):
		self.image_data = np.fliplr(self.image_data)
		self.label_status.config(text='IMAGE WAS FLIPED.', fg='green')

def main():
	root = Tk()
	root.title('Image Editor')

	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2 - 150
	h = h//2 - 150
	root.geometry('300x300+{}+{}'.format(w, h))
	root.resizable(False, False)

	app = App(root)

	root.mainloop()
 
if __name__ == '__main__':
	main()