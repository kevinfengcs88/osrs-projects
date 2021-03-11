import tkinter as tk    # import tkinter, the GUI module
from PIL import Image   # import Python Image Library's Image functions, so image files can be accessed
import PIL.ImageTk as ptk   # import Python Image Library's Image Tk functions, so that image files can be altered and gridded in
import tkinter.font as font # import tkinter font for custom fonts

def main(): # the main loop of the entire program that is called each time it's run, or the RESTART button is clicked

    def openAndConvertImages(rotation, startend):   # automates the process of opening and gridding the images into the window
        start = 2
        if (rotation == 1 or rotation == 2) and startend == 1:
            count = 3
        elif (rotation == 1 or rotation == 2) and startend == 2:
            start = 4
            count = 10
        elif rotation == 1 or rotation == 2:    # for rotations 1 and 2, 10 images need to be displayed
            count = 10
        elif rotation == 3: # for rotation 3, 11 images need to be displayed
            count = 11
        elif rotation == 4: # for rotation 4, 12 images need to be displayed
            count = 12

        dict1 = {}  # this dictionary will open and contain the image files as Image objects
        phaseDictionary = {}    # this dictionary will convert and contain the Image objects into ptk objects
        labelDictionary = {}    # this dictionary will contain labels that display the ptk objects

        for i in range(start, count + 1):   # loops through the range of start (specified earlier in the function, and by default, is 2) to count + 1
            # f-strings are used throughout so that the for loop can quickly open all of the image files and also for the dictionaries to reference each other easily
            dict1[f"zulrah{rotation}-{i}"] = Image.open(f"zulrah{rotation}-{i}.PNG")
            size = (200, 200)
            dict1[f"zulrah{rotation}-{i}"].thumbnail(size)
            phaseDictionary[f"zulrah{rotation}-{i}"] = ptk.PhotoImage(dict1[f"zulrah{rotation}-{i}"])
            labelDictionary[f"labelZulrah{rotation}-{i}"] = tk.Label(topFrame, image=phaseDictionary[f"zulrah{rotation}-{i}"])
            labelDictionary[f"labelZulrah{rotation}-{i}"].image_names = phaseDictionary[f"zulrah{rotation}-{i}"]
            # one of the most cryptic lines of code in the program^^^
            # tkinter isn't always able to display an image in a widget, such as a label or a button
            # the conditions aren't very specific, but by keeping another reference to the image via a built-in function of
            # the widget that will display the image, it guarantees tkinter access to that image
            # in some cases, tkinter will only have the image's reference in memory, and as a result
            # it will display a label (in this case) that has the proper resolution, but is strangely blank
            # without this line of code, all of the rotations are just blank rectangles of their proper resolutions
            if i <= 4:  # this if block (which is under the for loop) properly grids in the images into columns of 4, to be read from left to right
                labelDictionary[f"labelZulrah{rotation}-{i}"].grid(row=1, column=i - 1)
            elif i <= 8:
                labelDictionary[f"labelZulrah{rotation}-{i}"].grid(row=2, column=i - 5)
            elif i <= 12:
                labelDictionary[f"labelZulrah{rotation}-{i}"].grid(row=3, column=i - 9)

    def rotationOneTwo():   # the function that is called when buttonMELEE is clicked
        buttonMELEE.grid_remove()
        buttonRANGED.grid_remove()
        buttonMAGE.grid_remove()
        openAndConvertImages(1, 1)
        pray = Image.open("zulrah1-4.PNG")
        noPray = Image.open("zulrah2-4.PNG")
        size2 = (200, 200)
        pray.thumbnail(size2)
        noPray.thumbnail(size2)
        zulrahPray = ptk.PhotoImage(pray)
        zulrahNoPray = ptk.PhotoImage(noPray)
        buttonPRAY = tk.Button(topFrame, image=zulrahPray, cursor="dotbox") # cursor is an attribute that will change the user's cursor when hovering over a widget
        buttonNOPRAY = tk.Button(topFrame, image=zulrahNoPray, cursor="dotbox")
        buttonPRAY.image_names = zulrahPray # once again, .image_names is used so that the widgets aren't blank when gridded in
        buttonNOPRAY.image_names = zulrahNoPray
        buttonPRAY.grid(row=2)
        buttonNOPRAY.grid(row=2, column=1)

# click events are defined instead of assigning a functions to buttons because of the inaccessible, higher scopes if a function was assigned to the widget command
        def leftClick1(event):
            buttonPRAY.grid_remove()
            buttonNOPRAY.grid_remove()
            openAndConvertImages(1, 2)
            labelTitle["text"] = "Zulrah Guide: Rotation 1"

        def leftClick2(event):
            buttonPRAY.grid_remove()
            buttonNOPRAY.grid_remove()
            openAndConvertImages(2, 2)
            labelTitle["text"] = "Zulrah Guide: Rotation 2"

# the click events are binded to the buttons
        buttonPRAY.bind("<Button-1>", leftClick1)
        buttonNOPRAY.bind("<Button-1>", leftClick2)

    def rotationThree():    # the function that is called when buttonRANGED is clicked
        buttonMELEE.grid_remove()
        buttonRANGED.grid_remove()
        buttonMAGE.grid_remove()
        openAndConvertImages(3, 0)
        labelTitle["text"] = "Zulrah Guide: Rotation 3"

    def rotationFour(): # the function that is called when buttonMAGE is clicked
        buttonMELEE.grid_remove()
        buttonRANGED.grid_remove()
        buttonMAGE.grid_remove()
        openAndConvertImages(4, 0)
        labelTitle["text"] = "Zulrah Guide: Rotation 4"

    window = tk.Tk()    # create the window
    window.configure(bg="black")    # set background to black
    window.title("Zulrah Guide")    # set title of the window to "Zulrah Guide"
    window.geometry("850x750+0+0")    # set the dimensions of the window

# although gridding and packing cannot be mixed into the same parent frame (often named "window" or "root"),
# packing in frames creates new parent windows that can then have slaves be gridded in
    topFrame = tk.Frame(window, bg="black")
    topFrame.pack()
    leftFrame = tk.Frame(window, bg="black")
    leftFrame.pack(side=tk.LEFT)
    rightFrame = tk.Frame(window, bg="black")
    rightFrame.pack(side=tk.RIGHT)
    bottomFrame = tk.Frame(window, bg="black")
    bottomFrame.pack(side=tk.BOTTOM)

    myFont = font.Font(family="Runescape UF", size=30)  # create a custom font
    labelTitle = tk.Label(topFrame, text="Zulrah Guide: Rotation ?", fg="yellow", bg="black")
    labelTitle["font"] = myFont
    labelTitle.grid(row=0, columnspan=4)    # columnspan is used to make the title be centered in relation to the resolution of the parent window


# this is the general process for opening an image file, setting the resolution, converting it to a ptk object, assigning it to a widget, and then gridding it in
# this process is automated in the openAndConvertImages() function
    start = Image.open("zulrahSTART.PNG") # open image of Zulrah starting phase
    size1 = (200, 200)  # declare the size of the image to 200 x 200 pixels
    start.thumbnail(size1)    # actually set the size of the image
    zulrahSTART = ptk.PhotoImage(start) # convert the Image object to a ptk PhotoImage object
    labelSTART = tk.Label(topFrame, image=zulrahSTART)    # create a label to display the image with the ptk object
    labelSTART.grid(row=1, column=0)   # grid in the label

    melee = Image.open("zulrah1-2.PNG")
    melee.thumbnail(size1)
    zulrahMELEE = ptk.PhotoImage(melee)
    buttonMELEE = tk.Button(topFrame, image=zulrahMELEE, command=rotationOneTwo, cursor="dotbox")
    buttonMELEE.grid(row=2)

    ranged = Image.open("zulrah3-2.PNG")
    ranged.thumbnail(size1)
    zulrahRANGED = ptk.PhotoImage(ranged)
    buttonRANGED = tk.Button(topFrame, image=zulrahRANGED, command=rotationThree, cursor="dotbox")
    buttonRANGED.grid(row=2, column=1)

    mage = Image.open("zulrah4-2.PNG")
    mage.thumbnail(size1)
    zulrahMAGE = ptk.PhotoImage(mage)
    buttonMAGE = tk.Button(topFrame, image=zulrahMAGE, command=rotationFour, cursor="dotbox")
    buttonMAGE.grid(row=2, column=2)

    def leftClick3(event):  # a third left click event is created that will later be binded to the RESTART button
        window.destroy()
        main()
# the parent window actually isn't cleared, as the main() function also encompasses the creation of the GUI
# clearing the window would effectively create memory leaks every instance the user clicks the RESTART button
# instead, the parent window is destroyed, and by executing the main() function again, there is only one parent window running at any given time

    buttonRestart = tk.Button(bottomFrame, text="RESTART", fg="yellow", bg="black", relief=tk.RIDGE, cursor="dotbox")
    buttonRestart["font"] = myFont
    buttonRestart.bind("<Button-1>", leftClick3)    # bind the RESTART button to the leftClick3 event
    buttonRestart.grid()

    window.mainloop()   # the main loop of the GUI

main()  # execute the main() function for the first time; clicking the RESTART button will destroy this window and create a new one as main() is executed again
