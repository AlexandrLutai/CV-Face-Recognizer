# Face Recognition App

Приложение для распознавания лиц с использованием Python, OpenCV и библиотеки Face Recognition.

## Описание

Приложение позволяет:
- Записывать лица с указанием имени.
- Распознавать лица в реальном времени через веб-камеру.
- Управлять процессом через графический интерфейс, созданный с использованием `tkinter`.

## Установка

### 1. Клонирование репозитория
Склонируйте проект на ваш компьютер:
```bash
git clone https://github.com/your-username/face-recognition-app.git
cd face-recognition-app
```

### 2. Установка зависимостей
Убедитесь, что у вас установлен Python 3.11 или выше. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 3. Запуск приложения
Запустите приложение:
```bash
python main.py
```

## Использование

1. **Запись лица**:
   - Нажмите кнопку `Record Face`.
   - Введите имя в появившемся диалоговом окне.
   - Нажмите клавишу `S` для сохранения лица.
   - Нажмите `Q` для выхода из режима записи.

2. **Распознавание лиц**:
   - Нажмите кнопку `Recognize Faces`.
   - Лица будут распознаваться в реальном времени.
   - Нажмите `Q` для выхода из режима распознавания.

3. **Выход**:
   - Нажмите кнопку `Exit`, чтобы закрыть приложение.

## Зависимости

- `face_recognition` — библиотека для распознавания лиц.
- `opencv-python` — для работы с изображениями и видеопотоком.
- `tkinter` — для создания графического интерфейса.

## Структура проекта

```plaintext
face-recognition-app/
├── Dockerfile
├── requirements.txt
├── main.py
├── face_detector.py
├── face_recognizer.py
├── face_recognizer_app.py
├── tests/
│   ├── test_face_detector.py
│   ├── test_face_recognizer.py
│   ├── test_face_recognizer_app.py
│   └── test_images/
│       ├── test_face.jpg
│       └── no_face.jpg
```

## Тестирование

Для запуска тестов выполните:
```bash
pytest tests
```

## Docker

Для запуска приложения в контейнере Docker:

1. Соберите образ:
   ```bash
   docker build -t face_recognition_app .
   ```

2. Запустите контейнер:
   ```bash
   docker run -it --rm -p 5000:5000 face_recognition_app
   ```

