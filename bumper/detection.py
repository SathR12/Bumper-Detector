#Uses PyVision Library to detect bumper
import cv2 as cv
import numpy as np
import pytesseract
import sys
import json

sys.path.append(r"C:\Users\laks\Desktop\src\util")
sys.path.append(r"C:\Users\laks\Desktop\src\OCR")
sys.path.append(r"C:\Users\laks\Desktop\src\tessexc")
sys.path.append(r"E:\sathya\csv-parser\csv-parse")

import parse_data
import text_extraction
import contour_features
import detect_colors
import edit
import object_info


#tesseract path differs for each operating system
text_extraction.setPath(r"C:\Users\laks\Desktop\src\tessexc\tesseract.exe")

camera = cv.VideoCapture(0, cv.CAP_DSHOW)

#HSV Values for Blue Bumper
f = open("constants.json")
data = json.load(f)

LOWER_1 = data["colors"]["blue"]["lower1"]
LOWER_2 = data["colors"]["blue"]["lower2"]
UPPER_1 = data["colors"]["blue"]["upper1"]
UPPER_2 = data["colors"]["blue"]["upper2"]

#HSV Values for Red Bumper
LOW_1 = data["colors"]["red"]["lower1"]
LOW_2 = data["colors"]["red"]["lower2"]
UP_1 = data["colors"]["red"]["upper1"]
UP_2 = data["colors"]["red"]["upper2"]

print("Data table for FRC")

def detectBlueBumper(frame):
    global mask_blue
    mask_blue = detect_colors.createDoubleMask(frame, LOWER_1, UPPER_1, LOWER_2, UPPER_2)
    mask_blue = cv.morphologyEx(mask_blue, cv.MORPH_CLOSE, (7,7))
    mask_blue = cv.morphologyEx(mask_blue, cv.MORPH_OPEN, (7,7))
    contours = contour_features.getContours(mask_blue)
    digits = text_extraction.extractText(mask_blue)    
    parse_data.parser(digits)  
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        if cv.contourArea(contour) > 1000 and 4 >= w/h >= 1.9 and len(digits) >= 2:
            contour_features.drawBoundingRect(frame, contour)
            cv.putText(frame, "Blue Bumper", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return digits

def detectRedBumper(frame):
    global mask_red
    mask_red = detect_colors.createDoubleMask(frame, LOW_1, UP_1, LOW_2, UP_2)
    mask_red = cv.morphologyEx(mask_red, cv.MORPH_CLOSE, (7,7))
    mask_red = cv.morphologyEx(mask_red, cv.MORPH_OPEN, (7,7))
    contours = contour_features.getContours(mask_red)
    digits = text_extraction.extractText(mask_red)
    parse_data.parser(digits)
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        if cv.contourArea(contour) > 1000 and 2.4 >= w/h >= 1.9 and len(digits) >= 2:
            contour_features.drawBoundingRect(frame, contour)
            cv.putText(frame, "Red Bumper", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    
    return digits


    
    
while True:
    ret, frame = camera.read()
    detectBlueBumper(frame)
    detectRedBumper(frame)
   
    
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == 27:
        break
    

cv.destroyAllWindows()
camera.release()



