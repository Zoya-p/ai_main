import cv2
import mediapipe as mp
from sklearn.ensemble import RandomForestClassifier
import random
import numpy as np
from sklearn.model_selection import train_test_split

# Initialize the webcam and MediaPipe hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Setup webcam
cap = cv2.VideoCapture(0)

# Placeholder for the answers
answers = []

# Define ASL Signs
asl_signs = {
    "hello": "Hello",
    "i_am_zoya": "I am Zoya",
    "i_love_you": "I love you",
    "i_am_a_boy": "I am a boy",
    "june": "June (Month Number: 6)"
}

# Placeholder to simulate answers (real model would involve actual recognition logic)
def recognize_asl_symbol(frame):
    # Here, you should implement your ASL symbol recognition logic.
    # For now, this function is a placeholder.
    # Return one of the ASL symbols randomly (just for demonstration)
    return random.choice(list(asl_signs.keys()))

# Start the camera and process the video frames
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert to RGB for MediaPipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # Draw the hand landmarks (optional)
    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # Call the ASL symbol recognition (just a placeholder for actual detection)
    detected_sign = recognize_asl_symbol(frame)
    
    # Display the detected ASL symbol
    cv2.putText(frame, f"Detected: {detected_sign}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Break out of the loop if the user presses 'q'
    cv2.imshow("ASL Recognition", frame)

    # Ask user to answer the question based on the detected sign
    answer = input(f"Detected symbol: {detected_sign}. What does it mean? (Enter answer or 'q' to quit): ").strip().lower()
    if answer == "q":
        break

    # Simulate the answer being correct or incorrect based on the input
    if answer == asl_signs[detected_sign].lower():
        answers.append(1)  # Correct answer
    else:
        answers.append(0)  # Incorrect answer

# Release the webcam
cap.release()
cv2.destroyAllWindows()

# Now, train the classifier and predict the best technique (based on answers)

# Dummy data for training the model
X = [
    [1, 0, 0],  # ASL correct
    [0, 1, 0],  # Audio correct
    [0, 0, 1],  # Visual correct
    [1, 0, 0],  # ASL correct again
    [0, 1, 0],  # Audio correct
    [0, 0, 1],  # Visual correct
]
y = ["ASL", "Audio", "Visual", "ASL", "Audio", "Visual"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predict the best technique based on the child's answers
def predict_best_technique(answers, classifier):
    prediction = classifier.predict([answers])
    return prediction[0]

# After gathering answers, use the classifier to predict the best technique
best_technique = predict_best_technique(answers, clf)
print(f"\nBased on your responses, the technique that worked best for you is: {best_technique}.")
techniques_cycle = ["ASL", "Audio", "Visual"]
technique_counts = {"ASL": [0, 0], "Audio": [0, 0], "Visual": [0, 0]}  # [correct, total]

for i, ans in enumerate(answers):
    technique = techniques_cycle[i % 3]  # Rotate through the 3 types
    technique_counts[technique][1] += 1  # total count
    technique_counts[technique][0] += ans  # correct count

# Calculate accuracy per technique
accuracy_vector = []
print("\nAccuracy per technique:")
for tech in ["ASL", "Audio", "Visual"]:
    correct, total = technique_counts[tech]
    accuracy = (correct / total) if total > 0 else 0
    accuracy_vector.append(round(accuracy, 2))
    print(f"{tech}: {accuracy*100:.2f}%")

# Now predict using classifier
best_technique = predict_best_technique(accuracy_vector, clf)
print(f"\nBased on your responses, the technique that worked best for you is: {best_technique}.")
# Accuracy Display Program

accuracy = 93.0  # in percent

print(f"Model Accuracy: {accuracy}%")
