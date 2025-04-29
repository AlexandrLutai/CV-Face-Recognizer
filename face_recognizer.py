import face_recognition
import cv2

class FaceRecognizer:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

    def add_known_face(self, frame, name):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_frame)
        if len(face_encodings) == 0:
            print("Ошибка: Лицо не обнаружено на кадре.")
            return
        face_encoding = face_encodings[0]
        self.known_face_encodings.append(face_encoding)
        self.known_face_names.append(name)
        print(f"Лицо {name} добавлено в базу.")

    def recognize_faces(self, frame, face_locations):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        recognized_faces = []
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                match_index = matches.index(True)
                name = self.known_face_names[match_index]
            recognized_faces.append((name, face_location))
        return recognized_faces