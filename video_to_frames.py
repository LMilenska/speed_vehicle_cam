import cv2

def video_to_frames(input_vid='speed_challenge_2017/data/train.mp4',output_loc='images/'):
	capture = cv2.VideoCapture(input_vid)
	success, frame = capture.read()
	count = 0
	while success:
		cv2.imwrite(output_loc+'frame%d.jpg' % count, frame)
		success, frame = capture.read()
		count += 1

