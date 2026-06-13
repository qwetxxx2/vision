from ultralytics import YOLO


class Detector:

    def __init__(self):
        self.model = YOLO("yolov8m.pt")

    def detect_image(self, image_path):
        return self.model(image_path)

    def detect_video(self, video_path):
        return self.model(video_path, save=True)