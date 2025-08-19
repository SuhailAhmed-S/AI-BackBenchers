# pushup_counter.py
import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
counter = 0
stage = None

def calculate_angle(a, b, c):
    ang = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) -
        math.atan2(a[1]-b[1], a[0]-b[0])
    )
    return abs(ang)

while cap.isOpened():
    ret, frame = cap.read()
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)
    
    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark
        # Get coordinates
        shoulder = [landmarks[11].x, landmarks[11].y]
        elbow = [landmarks[13].x, landmarks[13].y]
        wrist = [landmarks[15].x, landmarks[15].y]

        angle = calculate_angle(shoulder, elbow, wrist)

        # Push-up logic
        if angle > 160:
            stage = "up"
        if angle < 90 and stage == "up":
            stage = "down"
            counter += 1
            print("Push-up Count:", counter)
        
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Push-Up Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
