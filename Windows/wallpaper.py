# To know more about the code and how to run this script at startup,
# kindly refer to the README file in the GitHub Repository

# Importing the required libraries
import ctypes                               
import os                                   
import random
import shutil
from tkinter import *


# A user defined function to change the desktop background
def changeBG(images,path):
    '''
    This function chooses an image at random,
    sets it as the desktop background,
    and moves it to the "Applied" folder.

    Parameters:
        images (list) : The list containing the name of all the images present in the "Wallpapers" folder.
        path (string) : The path of "Wallpapers" folder 
    '''

    index = random.randrange(0, len(images))    # Gives a random number from the range of number of images present in "Wallpapers" folder
    path = (path + '\\' + str(images[index]))   # Gives the complete path of the image chosen by using the random index number which was generated

    # Sets the desktop background
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

    shutil.move(path, 'D:\\Wallpapers\\Applied') # Moves the applied image to the "Applied" folder


# A user defined function acting as the command of the "Yes" button 
def wallchange():
    '''
    This function initializes the path of the "Wallpapers" folder and the list of images in it.
    If the list of images is not empty, it calls the changeBG function with the required arguments.
    If there are no images in "Wallpapers" folder, it checks whether there are images in the "Applied" folder.
    If yes, it moves all the images back to the "Wallpapers" and calls the changeBG function with the required arguments.
    If not, it shows an ERROR window.
    '''
    
    path = 'D:\\Wallpapers' # Initializing the path of the "Wallpapers" folder

    # Initializing the list of images and removing the "Applied" folder entry
    images = os.listdir(path)
    images.remove('Applied')

    # To check whether the list is empty or not
    if not images:
        # Executes if the list is empty

        path = (path + '\\Applied') # Change the path to the path of the "Applied" folder
        images = os.listdir(path) # Gives the list of images in "Applied" folder

        # To check whether the list is empty or not
        if(images):
            # Executes if the list is not empty

            # To move all images back to the "Wallpapers" folder
            for f in images:
                f = (path + '\\' + f) # Gives the complete path of the image
                shutil.move(f, 'D:\\Wallpapers')

            path = 'D:\\Wallpapers' # Changing back to the path of "Wallpapers" folder

    
        else:
            # Executes if there are no images in both the folders

            error = Tk() # Instantiating an object of Tk class to create GUI window
            error.title("ERROR!!!") # Title of the GUI window
            error.geometry("400x200+500+250") # Size and placement of the window on the screen
            error.configure(bg='black') # Setting background color of window

            label=Label(error,text="There are no wallpapers in both your folders !!!",
                        font="bold",bg='black',fg="white") # Text label with attributes
            label.pack() # Places the label widget within the window

            close_button=Button(error,text="Close",bg='red',fg='white',width=8,height=2,command=error.destroy) # Button with attributes which destroys the error window when clicked
            close_button.place(relx=0.4,rely=0.5) # Place the button within the window according to values

            root.destroy() # Destroys our main GUI window
            error.mainloop() # Runs the application
            sys.exit() # Exits the program

    # Call to our function with the required arguments.
    changeBG(images,path)

    # Destroys our GUI window
    root.destroy()


# To create the main GUI window
root=Tk()

root.title("Wallpaper Change") 
root.geometry("400x200+500+250") 
root.configure(bg='black') 

label1=Label(root,text="Do you want to change the wallpaper?",font="bold",bg='black',fg="white")
label1.pack()

button1=Button(root,text="Yes",bg='green',fg='white',width=8,height=2,command=wallchange) # Calls the 'wallchange' function when clicked
button2=Button(root,text="No",bg='red',fg='white',width=8,height=2,command=root.destroy) # Destroys the main GUI window when clicked

button1.place(relx=0.3,rely=0.5)
button2.place(relx=0.6,rely=0.5)

root.mainloop()