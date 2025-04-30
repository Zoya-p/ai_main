import os

import cv2
import mediapipe as mp


DATA_DIR = './Data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 10
dataset_size = 100

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting Data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(50) == ord('q'):
            break

    counter = 0
    mp_hands = mp.solutions.hand
with mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.5) as hands:
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        cv2.imshow('frame', frame)
        if results.multi_hand_landmarks:
            cv2.imwrite(os.path.join(DATA_DIR, str(j), f'{counter}.jpg'), frame)
            print(f"Saved image {counter} for class {j}")
            counter += 1

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
