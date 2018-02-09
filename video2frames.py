import cv2

filedir = ""
savedir = ""
video = ""

vidcap = cv2.VideoCapture(filedir + video)
success, image = vidcap.read()
count = 0
success = True
while success:
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    cv2.imwrite(savedir + "frame%d.jpg" % count, image)     # save frame as JPEG file  count += 1
    count += 1
