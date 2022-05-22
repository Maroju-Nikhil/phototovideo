import os
import cv2
from PIL import Image
import tkinter 
from tkinter import filedialog
import random 
import pyttsx3
from tkinter import messagebox
import getpass

file_formats = ['.jpg' , '.png' , '.jpeg' , '.tiff' , 'jfif']
mean_height = 0								
mean_width = 0


try:
	os.chdir(path1)

	for file in os.listdir('.'):
		for form in file_formats:
			if file.find('.')!=-1 and (file.endswith(form) or file.endswith(form.upper())) and os.stat(file).st_size!=0:
				im = Image.open(os.path.join(path1,file))
				width,height = im.size
				mean_width += width
				mean_height +=height
				#im.show()
	images = []
	for img in os.listdir(path1):
				for form in file_formats:
					if (img.endswith(form) or img.endswith(form.upper())) and os.stat(img).st_size!=0:
						images.append(img)

	num = len(images)
	mean_width = int(mean_width / num)
	mean_height = int(mean_height / num)

	#print(mean_width , mean_height)

	for file in os.listdir('.'):
		for form in file_formats:
			if (file.endswith(form) or file.endswith(form.upper())) and os.stat(file).st_size!=0:
				#print(file , os.stat(file).st_size)
				im = Image.open(os.path.join(path1,file))

				width,height = im.size
				#print(width , height)

				imResize = im.resize((mean_width,mean_height), Image.ANTIALIAS)
				imResize.save(file ,'JPEG',quality = 95)
				#print(im.filename.split('\\')[-1],'is resized')
except:
	#print('image format is not supported..')
	pass

def knowmore():
	knowmore.counter += 1
	top = tkinter.Toplevel()
	top.resizable(0,0)
	top.geometry("500x200")
	tkinter.Label(top, width = 50 , text = """\t\tIts simple one,
1.)  You have to select the folder in which you have pictures 
(its ok even if it contains other file formats other than pictures)
2.)  You have to enter video file name
3.)  You have to click Generate button to generate video,
4.)  Finally ,You have your video file in same folder mentioned.""", font = ('Calibri', 14) , justify = "left").pack()
	#print(knowmore.counter)
	if knowmore.counter == 3:
		converter = pyttsx3.init()
		converter.setProperty('rate' , 130)
		converter.setProperty('volume' , 1)
		converter.say('Please don\'t continuously press the button')
		converter.runAndWait()
		return 
	top.mainloop()

#path1 = ""
knowmore.counter = 0

def askfolder():
	global path1
	path1 =  tkinter.filedialog.askdirectory()
	if path1!="":
		b2.configure(text = 'Folder selected'  , bg = 'lightgreen')

def gen_video():
	try:

		try:
			image_fol = path1
		except:
			image_fol = ""
		#video_name = 'video4.mp4'
		os.chdir(path1)

		images = []

		for img in os.listdir(image_fol):
			for form in file_formats:
				if (img.endswith(form) or img.endswith(form.upper())) and os.stat(img).st_size!=0:
					images.append(img)
					#print(images,  end='\n')

		#images = [img for img in os.listdir(image_fol) if (img.endswith('.JPG') or file.endswith('.PNG') or file.endswith('.')) and os.stat(file).st_size!=0]
		#images = set(images)
		#print(set(images))
		if len(images)>=1:			
	            frame = cv2.imread(os.path.join(image_fol,images[0]))
	            extensions = [('All Files','*.*'),('mp4 files','*.mp4')]
	            messagebox.showinfo('info','please enter the file name with extension to save it..')
	            video_name = tkinter.filedialog.asksaveasfile(filetypes = extensions , defaultextension = extensions).name.split('\\')[-1]

	            height ,width , layers = frame.shape
	            print(frame.shape , height , width , video_name)
	            video = cv2.VideoWriter(video_name, 0, 1, (width,height))

	            for image in set(images):
	                    #print(image , end='\n')
	                    video.write(cv2.imread(os.path.join(image_fol,image)))

	            cv2.destroyAllWindows()
	            video.release()

	            b3.configure(text = 'video generated' , bg = 'lightgreen')
	            messagebox.showinfo('Success!','finished succesfully..')
	            converter = pyttsx3.init()
	            converter.setProperty('rate', 130)
	            converter.setProperty('volume', 1)
	            converter.say('The video is made succesfully in same folder!')
	            converter.say('Thank you '+ getpass.getuser().lower() + 'for using this application')
	            converter.runAndWait()
		else:	
			    messagebox.showinfo('info','The folder doesnot contain enough images to make it video.')
			    converter = pyttsx3.init()
			    converter.setProperty('rate' , 130)
			    converter.setProperty('volume' , 1)
			    converter.say('sorry , The folder doesn\'t contain images to make it a video')
			    converter.runAndWait()                 
	except:
		messagebox.showinfo('Failed!','some error occured!..Please check if folders contains correct format images.\n or \nplease check if you entered correct video format')
		converter = pyttsx3.init()
		converter.setProperty('rate', 130)
		converter.setProperty('volume', 1)
		if image_fol == "":
			converter.say('Please select folder')
		else:
			converter.say('Sorry , some error occured!')
		converter.runAndWait()
		

root = tkinter.Tk()
root.title("Picture to video converter") 
root.geometry("500x350") 
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')
tkinter.Label(root, text = "Hi "+ getpass.getuser().lower().capitalize() + "\nWelcome to simple python application!\n Picture to video Converter\n", font = ('Calibri', 18)).pack()
tkinter.Button(root , text='Know how to do that' , bg = 'lightblue', command = knowmore , height = 1 , width = 20 , font = ('Calibri',15)).pack()
tkinter.Label().pack()
b2 = tkinter.Button(root, text = 'select folder' , bg = 'orange' , command = askfolder , height =1 , width = 17 , font = ('Calibri',15))
b2.pack()
tkinter.Label().pack()
b3 = tkinter.Button(root , text = 'Generate video' , bg = 'orange' , command = gen_video , height = 1 , width = 17 , font = ('Calibri',15))
b3.pack()
root.mainloop()


