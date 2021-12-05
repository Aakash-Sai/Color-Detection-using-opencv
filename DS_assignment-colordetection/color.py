# Aakash Sai Unnam - 2019A7PS0196U
# Siddharth Bhandary - 2019A7PS0218U
# Data Science Assignment - Color Detection

import pandas as pd
import cv2

# Reading image with opencv
imgDestination = r'pic.jpg'
image = cv2.imread(imgDestination)

# Initializing variables
clicked = False
r = 0
g = 0
b = 0 
mouse_x = 0
mouse_y = 0

# Giving coloumn names and reading the 'colors' csv file
index = ["color", "colors", "hexa", "R", "G", "B"]      
file = pd.read_csv('colors.csv', names=index, header=None)

# Function to find the appropriate color from the csv file 
def calc_color(R, G, B):
    min = 10000
    for i in range(len(file)):
        value = abs(R - int(file.loc[i, "R"])) + abs(G - int(file.loc[i, "G"])) + abs(B - int(file.loc[i, "B"]))
        if value <= min:
            min = value
            getcolor = file.loc[i, "colors"]
    return getcolor

# Function to find the mouse coordinates when clicked
def mouse_coord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, mouse_x, mouse_y, clicked
        mouse_x = x
        mouse_y = y
        clicked = True
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# Creating a window for user interaction and calling the mouse coordinates function
cv2.namedWindow('DS_Assignment')
cv2.setMouseCallback('DS_Assignment', mouse_coord)

# Loop to keep the window open
while True:
    cv2.imshow("DS_Assignment", image)
    if clicked:
        cv2.rectangle(image, (350, 20), (900, 60), (b, g, r), -1)
        text = calc_color(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(image, text, (380, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False

# Hit 'esc' key to close window
    if cv2.waitKey(20) & 0xFF == 27:
        break          
cv2.destroyAllWindows()