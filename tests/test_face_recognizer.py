import cv2
import pytest
from face_recognizer import FaceRecognizer

@pytest.fixture
def recognizer():
    return FaceRecognizer()

def test_add_known_face(recognizer):
    frame = cv2.imread("tests/test_images/test_face.jpg")
    recognizer.add_known_face(frame, "Test Name")
    assert len(recognizer.known_face_encodings) == 1
    assert recognizer.known_face_names[0] == "Test Name"

def test_add_known_face_no_face(recognizer):
    frame = cv2.imread("tests/test_images/no_face.jpg")
    recognizer.add_known_face(frame, "No Face")
    assert len(recognizer.known_face_encodings) == 0

def test_recognize_faces(recognizer):
    frame = cv2.imread("tests/test_images/test_face.jpg")
    recognizer.add_known_face(frame, "Test Name")
    face_locations = [(0, frame.shape[1], frame.shape[0], 0)]
    recognized_faces = recognizer.recognize_faces(frame, face_locations)
    assert len(recognized_faces) > 0
    assert recognized_faces[0][0] == "Test Name"

def test_recognize_faces_unknown(recognizer):
    frame = cv2.imread("tests/test_images/test_face.jpg")
    face_locations = [(0, frame.shape[1], frame.shape[0], 0)]
    recognized_faces = recognizer.recognize_faces(frame, face_locations)
    assert len(recognized_faces) > 0
    assert recognized_faces[0][0] == "Unknown"