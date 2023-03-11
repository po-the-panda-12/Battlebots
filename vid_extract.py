from PIL import Image
import pytesseract
from wand.image import Image as Img
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag

import os
import cv2

#name path to image files
image_frames = 'image_frames'

def files():
    try:
        os.remove(image_frames)
    except OSError:
        pass
    
    if not os.path.exists(image_frames):
        os.mkdir(image_frames)

    #specify the source video path 
    src_vid = cv2.VideoCapture('test2.mp4')
    return(src_vid)

def process(src_vid):
    #use count to integer name the files
    count = 0
    while(src_vid.isOpened()):
        ret, frame = src_vid.read()
        if ret == False:
            break
        #name each frame and save as png
        name = './image_frames/frame' + str(count) + '.png'

        #save every 100th frame
        if count % 100 == 0:
            print ('Extracting frames...' + str(count))
            cv2.imwrite(name, frame)
        count += 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    src_vid.release()
    cv2.destroyAllWindows()

def ocr():
    #ocr the images

    files = os.listdir(image_frames)
    dirlist = [file for file in sorted(
        files, key=lambda x: int(x.replace("frame", "")[:-4]))]
    
    for filename in dirlist:

        print(filename)

        #specify the path to tesseract
        #pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
        
        #open the image
        my_example = Image.open(image_frames + '/' + filename)
        #convert to text
        text = pytesseract.image_to_string(my_example)
        #save the text to a file
        with open('ocr.txt', 'a') as f:
            f.write(text)


def clean():
    #input text file
    inputFile = "ocr.txt"
    # Opening the given file in read-only mode.
    with open(inputFile, 'r') as filedata:
        # Read the file lines using readlines()
        inputFilelines = filedata.readlines()

        # Enter the line number to be deleted
        deleteLine = "@ Chrome"
        # Opening the given file in write mode.
        with open(inputFile, 'w') as filedata:
            # Traverse in each line of the file
            for textline in inputFilelines:

                if deleteLine not in textline:
                    # If it is true, then write that corresponding line into file
                    outputString = textline.strip() + " "
                    if '.' in outputString:
                        outputString = outputString.replace('. ', '.\n')
                    filedata.write(outputString)

        # Closing the input file
        filedata.close()
    

           
#main driver
if __name__ == '__main__':
    vid = files()
    process(vid)
    ocr()
    clean()