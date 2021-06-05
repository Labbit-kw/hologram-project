import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    frame_gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier("../res/haarcascade_frontalface_alt.xml")

    # 얼굴 인식 실행하기
    face_list = cascade.detectMultiScale(frame_gs, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

    # 인식한 부분 표시하기
    if len(face_list) > 0:
        for face in face_list:
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), thickness=5)

    # 프레임 표시
    cv2.imshow("Face detection", frame)

capture.release()
cv2.destroyAllWindows()
