import cv2
import numpy as np

VIZ_DIMS = (800, 800) # H, W
VIZ_COLOR = [20, 20, 20]
VIZ_NAME = 'KNN'


def draw_dist_lines(frame, points, target, line_color=(255, 255, 255)):
    for point in points:
        cv2.line(frame, point, target, line_color, 1)




frame = np.uint8(np.full((*VIZ_DIMS, 3), VIZ_COLOR))
print(frame)
print(frame.shape)


num_points = 200

points_xs = np.random.randint(low=0, high=VIZ_DIMS[1], size=(num_points, 1))
points_ys = np.random.randint(low=0, high=VIZ_DIMS[0], size=(num_points, 1))

points = np.hstack((points_xs, points_ys))


test_point = (400, 300)
cv2.circle(frame, test_point, 15, (255, 255, 255), -1)


for pt in points:
    color = (3, 161, 252)
    if pt[0] > pt[1]:
        color = (232, 252, 3)
    cv2.circle(frame, pt, 5, color, -1)


draw_dist_lines(frame, points, test_point)




cv2.namedWindow(VIZ_NAME, cv2.WINDOW_NORMAL)

# show the image, provide window name first
cv2.imshow('image window', frame)


cv2.waitKey(0)
# and finally destroy/close all open windows
cv2.destroyAllWindows()