import os
import cv2

# 매개변수 설정
video_path = 'C:/Users/clova/Desktop/recording.mp4'
save_folder = '../../extract'
os.makedirs(save_folder, exist_ok=True)

# Video 열기
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print('Video opening process is failed.')
    exit(1)

# 각 프레임을 이미지로 저장
i = 0
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    cv2.imwrite(os.path.join(save_folder, f'{i}.jpg'), frame)
    i += 1
cap.release()
