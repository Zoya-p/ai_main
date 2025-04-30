This project is a machine learning-based assessment tool designed to identify the preferred learning modality—ASL (kinesthetic), visual (image-based), or auditory—for neurodivergent individuals. The system consists of three distinct modules, each evaluating a different sensory pathway to determine how effectively users engage and respond.
 Project Overview

Neurodivergent learners often benefit from tailored educational methods. This project aims to detect the most suitable learning style using three separate tests:

1. **ASL-Based Gesture Recognition Test**  
2. **Pictorial (Visual) Comprehension Test**  
3. **Auditory Processing Test**

At the end of the assessment, the system predicts the optimal learning mode based on individual test performance.



 Methodology

 1. ASL Gesture Recognition

- **Input:** Real-time hand gestures via webcam.
- **Technology:** MediaPipe Hands is used to extract 21 3D landmarks per hand.
- **Classifier:** Random Forest Classifier.
- **Output:** ASL class label predicted from live hand movement.
- **Example Accuracy:** 91.4%

2. Pictorial Test (Visual)

- **Input:** Multiple-choice questions with image-based prompts.
- **Technology:** User selections are recorded and classified.
- **Classifier:** Support Vector Machine (SVM).
- **Output:** Accuracy based on visual question response.
- **Example Accuracy:** 88.6%

 3. Auditory Test

- **Input:** Audio-based questions played through the system.
- **Technology:** Text-to-speech and speech understanding.
- **Classifier:** Logistic Regression.
- **Output:** Accuracy of user responses to verbal questions.
- **Example Accuracy:** 76.3%

### Final Evaluation

A combined classifier analyzes the results from the three individual modules to determine the user's most effective learning style.

## Technologies Used

- Python 3.x  
- OpenCV (for webcam access and frame processing)  
- MediaPipe (for hand tracking in ASL module)  
- Scikit-learn (for all ML classification tasks)  
- Numpy, Pandas (for data handling) 
