# CSV project (inconsistent)

Detects robot's bumper and outputs description of robot if it exists in CSV file 


## Dependencies

OpenCV 

PyVision - https://github.com/SathR12/PyVision

Numpy

Pytesseract

Json

CSV


## Output

Running the code will open a window that displays the live feed. Bumper detection is in progress and will detect other objects accidentally. In the terminal, it should display csv data of the team number it detected. 

## Inconsistency

OCR - Optical Character Recognition is very inconsistent when it comes to extracting text from models that it is not well trained with. This project will only work if camera is right in front of the the bumper with a straight angle. 

## Huge framerate tanks - Pytesseract + live video feed


<img width="764" alt="158041176-59e0f6e4-ae35-4fa9-99b3-a8246f5127af" src="https://user-images.githubusercontent.com/74515743/160261605-67f428fa-015c-4272-9e24-02947c792274.png">
