import tkinter as tk
from tkinter import simpledialog
import cv2
from face_detector import FaceDetector
from face_recognizer import FaceRecognizer

class FaceRecognitionApp:
    def __init__(self):
        self.face_detector = FaceDetector()
        self.face_recognizer = FaceRecognizer()
        self.camera = cv2.VideoCapture(0)
        self.root = tk.Tk()
        self.root.title("Face Recognition App")
        tk.Button(self.root, text="Record Face", command=self.record_face).pack(pady=10)
        tk.Button(self.root, text="Recognize Faces", command=self.recognize_faces).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.exit_app).pack(pady=10)

    def process_video(self, callback, window_title):
        print(f"{window_title}...")
        while True:
            ret, frame = self.camera.read()
            if not ret:
                print("Не удалось получить кадр")
                break
            callback(frame)
            cv2.imshow(window_title, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print(f"Выход из режима {window_title.lower()}.")
                break
        cv2.destroyWindow(window_title)

    def record_face(self):
        name = simpledialog.askstring("Record Face", "Enter name:")
        if not name:
            print("Имя не введено. Отмена записи.")
            return

        def callback(frame):
            if cv2.waitKey(1) & 0xFF == ord('s'):
                self.face_recognizer.add_known_face(frame, name)
                print(f"Лицо {name} записано.")
                return

        self.process_video(callback, "Record Face")

    def recognize_faces(self):
        def callback(frame):
            face_locations = self.face_detector.detect_faces(frame)
            recognized_faces = self.face_recognizer.recognize_faces(frame, face_locations)
            for name, (top, right, bottom, left) in recognized_faces:
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        self.process_video(callback, "Recognize Faces")

    def exit_app(self):
        print("Выход из приложения.")
        self.camera.release()
        cv2.destroyAllWindows()
        self.root.destroy()

    def run(self):
        self.root.mainloop()