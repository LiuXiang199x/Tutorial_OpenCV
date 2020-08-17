import cv2 as cv
import numpy as np

def video_demo():
	capture = cv.VideoCapture(0)
	while(True):
		ret, frame = capture.read()
		frame = cv.flip(frame,1)  # 这是镜像正过来，一般视频中都是反向的。
		cv.imshow("video", frame)
		c = cv.waitKey(50)
		if c == 27:
			break

def get_image_info(image):
	print(type(image))
	print(image.shape)
	print(image.size)
	print(image.dtype)
	pixel_data = np.array(image)
	print(pixel_data)
 

print("------------Hello Python----------")

src = cv.imread("1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("First_pic",src)
cv.waitKey(0)
get_image_info(src)

cv.destroyAllWindows()   # 这里是destroy all，若我们只想销毁某一个窗口，就要给他传参
