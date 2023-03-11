import os
def ocr():
    # ocr the images

    image_frames = 'image_frames'


    files = os.listdir(image_frames)

    print(files)
    # dirlist = [file for file in sorted(
    #     files, key=lambda x: int(x.replace("frame", "")[:-4]))]

    # for filename in dirlist:

    #     print(filename)


if __name__ == '__main__':
    ocr()
