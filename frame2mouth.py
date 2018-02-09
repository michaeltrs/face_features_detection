import numpy as np
import cv2
import os

# USER INPUT
filedir = "/homes/mat10/Programming/OpenCV/frames/"
savedir = "/homes/mat10/Programming/OpenCV/frames/mouths/"
files   = 'all'#'['frame0.jpg']  # put all files in list, if all files are needed write: files = 'all'


# PROGRAM
if not os.path.isdir(savedir):
    print("save_directory does not exist")
    print("making save_directory: %s" % savedir)
    os.mkdir(savedir)

if files == 'all':
    files = [file for file in os.listdir(filedir) if file[-3:] == 'jpg']

face_cascade = cv2.CascadeClassifier(
    '/homes/mat10/Programming/OpenCV/haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier(
    '/homes/mat10/Programming/OpenCV/haarcascade_mcs_mouth.xml')

#file = files[0]
for i, file in enumerate(files):

    img = cv2.imread(filedir + file, 0)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # First detect face - assuming a single face
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    x, y, w, h = faces[0]
    # cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 3)
    roi_face = img[y:y+h, x:x+w]

    # Then detect mouth
    mouth = mouth_cascade.detectMultiScale(roi_face, minNeighbors=100, maxSize=(100, 100))
    ex, ey, ew, eh = mouth[0]
    # cv2.rectangle(roi_face, (ex, ey), (ex+ew, ey+eh) , (0, 255, 0), 1)
    roi_mouth = roi_face[ey:ey+eh, ex:ex+ew]

    cv2.imwrite(savedir + "mouth%d.jpg" % i, roi_mouth)

    # Not fully automated yet!!!

    # cv2.imshow('img', roi_mouth)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
