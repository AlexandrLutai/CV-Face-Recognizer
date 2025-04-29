import face_recognition
import cv2

class FaceDetector:

    def detect_faces(self, frame):
        """
        Обнаруживает лица на переданном кадре.
        :param frame: Кадр из камеры
        :return: Список координат обнаруженных лиц
        """
       
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      
        face_locations = face_recognition.face_locations(rgb_frame)

        return face_locations