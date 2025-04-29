import cv2
import pytest
from face_detector import FaceDetector

@pytest.fixture
def detector():
    """
    Фикстура для создания экземпляра FaceDetector.
    """
    return FaceDetector()

def test_detect_faces_with_faces(detector):
    """
    Тестирует обнаружение лиц на изображении, содержащем лица.
    """
    
    frame = cv2.imread("tests/test_images/test_face.jpg")  
 
    face_locations = detector.detect_faces(frame)
    assert len(face_locations) > 0, "Лица не обнаружены на изображении"

def test_detect_faces_without_faces(detector):
    """
    Тестирует обнаружение лиц на изображении без лиц.
    """
   
    frame = cv2.imread("tests/test_images/no_face.jpg")  


    face_locations = detector.detect_faces(frame)
    assert len(face_locations) == 0, "Обнаружены лица на изображении без лиц"

def test_detect_faces_invalid_input(detector):
    """
    Тестирует обработку некорректного ввода.
    """
    with pytest.raises(Exception):
        detector.detect_faces(None) 