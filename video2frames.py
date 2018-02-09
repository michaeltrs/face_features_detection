import cv2

filedir = "/vol/atlas/homes/thanos/bbc/lipread_mp4/LONDON/test/"
savedir = "/homes/mat10/Programming/OpenCV/frames/"

vidcap = cv2.VideoCapture(filedir + 'LONDON_00025.mp4')
success, image = vidcap.read()
count = 0
success = True
while success:
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    cv2.imwrite(savedir + "frame%d.jpg" % count, image)     # save frame as JPEG file  count += 1
    count += 1
