# Aakash Sai Unnam

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
def mouse_coord(event, x_pos, y_pos, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global r,g,b, mouse_x, mouse_y, clicked
        mouse_x = x_pos
        mouse_y = y_pos
        clicked = True
        b, g, r = image[y_pos, x_pos]
        r = int(r)
        g = int(g)
        b = int(b)
        
# Creating a window for user interaction and calling the mouse coordinates function
cv2.namedWindow('DS_Assignment')
cv2.setMouseCallback('DS_Assignment', mouse_coord)

# Loop to keep the window open
while True:
    cv2.imshow("DS_Assignment", image)
    if clicked:
        cv2.rectangle(image, (350, 25), (900, 65), (b, g, r), -1)
        image_text = calc_color(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(image, image_text, (380, 55), 2, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
        clicked = False

# Hit 'esc' key to close window
    if cv2.waitKey(20) & 0xFF == 27:
        break          
cv2.destroyAllWindows()
