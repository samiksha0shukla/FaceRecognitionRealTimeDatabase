
# FaceRecognitionRealTimeDatabase

## Tech Stack Used & Description:
### 1.OpenCV & cvzone:
- Capture webcam video and perform image operations.
- Draw on images for interface enhancements.
### 2.numpy:
- Manage numerical data for efficient image processing.
### 3.face_recognition:
- Detect and recognize faces in video frames.
### 4.firebase_admin & pickle:
- Connect to Firebase services for real-time database interactions.
- Save and load face encodings and student information.
### 5.datetime:
- Handle time-related operations for attendance tracking.
### 6.Description:
- Initializes libraries and connects to Firebase.
- Grabs webcam frames and detects faces.
- Retrieves student info from Firebase based on face matches.
- Updates attendance data dynamically based on time constraints.
- Displays real-time student information and images on the interface.

This model integrates face recognition with Firebase for real-time attendance tracking, using libraries for image processing, database interactions, and time handling. It provides a dynamic interface for monitoring attendance data and student information.
