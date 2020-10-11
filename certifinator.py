from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image
import os
import tkinter.font as font

# Create GUI window
root = Tk()
root.title("Certifinator")
myFont = font.Font(family='Helvetica', size=10, weight='bold')
root.geometry('1920x1080')
root.configure(bg = '#2c2a2b')

# Useful Global Variables
fln = ""
data = 0
folder = ""

# All Functions
# Opens browsing window to load certificate template
def showimage():
    global fln
    img_dir=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select the Image", filetypes=[('all files','*.*')])
    fln = img_dir

# Opens browsing window to load CSV data
def open_file():
    global data
    file = filedialog.askopenfile(mode='r', filetypes=[('Comma Separated Value', '*.csv')])
    data_load = pd.read_csv(file)
    data = data_load

# Select destination folder
def set_destination():
    global folder
    folder_selected = filedialog.askdirectory()
    folder = folder_selected + "/"


# Executes mapping and generation of certificates
def gen_cert():
    coordinates = map_coord(fln)
    # Save individual column data
    data1_list = np.array(data.iloc[:,0]).T
    data2_list = np.array(data.iloc[:,1]).T
    data3_list = np.array(data.iloc[:,2]).T
    # Generate certificates
    create_certificate(data1_list, data2_list, data3_list, coordinates)


# Show Template and set coordinates
def map_coord(fln):
    coordinate_list = []

    def draw_circle(event, x, y, flag, param):
        if event == cv2.EVENT_LBUTTONDBLCLK:              # Double click a point on certificate
            tup = (x, y)                                  # Record the coordinates of that point
            coordinate_list.append(tup)

    img = cv2.imread(fln)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return coordinate_list


# Generate certificate by mapping csv content to coordinates
def create_certificate(data1_list, data2_list, data3_list, coordinates):
    for i in range(len(data1_list)):
        data1_to_print = data1_list[i]
        data2_to_print = data2_list[i]
        data3_to_print = data3_list[i]

        # Load image in OpenCV
        image = cv2.imread(fln)

        # Convert the image to RGB (OpenCV uses BGR)
        cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Pass the image to PIL
        pil_im = Image.fromarray(cv2_im_rgb)

        draw = ImageDraw.Draw(pil_im)
        # use a truetype font
        font = ImageFont.truetype("./fonts/MLSJN.TTF", 29)  # You can change fonts from list given bottom

        # Draw the text
        draw.text((int(coordinates[0][0]), int(coordinates[0][1])), data1_to_print, font=font, fill='black')
        draw.text((int(coordinates[1][0]), int(coordinates[1][1])), data2_to_print, font=font, fill='black')
        draw.text((int(coordinates[2][0]), int(coordinates[2][1])), data3_to_print, font=font, fill='black')

        # Get back the image to OpenCV
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

        path = ''
        cv2.imwrite(folder + data1_to_print + '.png', cv2_im_processed)


# All Buttons
# "Load Certificate" Button
btn1 = Button(root, text ='Load Certificate', width=20, height=2,bg = '#6d4884', fg= 'white',command = lambda: showimage())
btn1.pack(side = TOP, pady = 10)
btn1['font']=myFont

# "Load Data" Button
btn2 = Button(root, text='Load Data',width=20, height=2, bg='#6d4884', fg='white', command=lambda: open_file())
btn2.pack(side=TOP, pady=10)
btn2['font']=myFont

# Set destination folder for the certificates
btn3=Button(root,text="Set Destination", width=20, height=2, bg = '#6d4884', fg= 'white', command=lambda: set_destination())
btn3.pack(side=TOP,pady=10)
btn3['font']=myFont

# "Generate Certificate" Button
btn4=Button(root,text="Generate Certificate", width=20, height=3, bg = '#6d4884', fg= 'white', command=lambda: gen_cert())
btn4.pack(side=TOP,pady=10)
btn4['font']=myFont

mainloop()

