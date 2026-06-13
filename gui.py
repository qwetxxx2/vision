from translator import translations

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QFileDialog,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

import cv2

from detector import Detector
from statistics import Statistics


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.detector = Detector()

        self.setWindowTitle(
            "Система распознавания объектов"
        )

        self.resize(1080, 900)

        self.image_label = QLabel()

        self.image_label.setMinimumHeight(
            650
        )

        self.statistics_box = QTextEdit()

        self.statistics_box.setReadOnly(
            True
        )

        self.image_button = QPushButton(
            "Выбрать изображение"
        )

        self.video_button = QPushButton(
            "Выбрать видео"
        )

        top_layout = QHBoxLayout()

        top_layout.addWidget(
            self.image_button
        )

        top_layout.addWidget(
            self.video_button
        )

        main_layout = QVBoxLayout()

        main_layout.addLayout(
            top_layout
        )

        main_layout.addWidget(
            self.image_label,
            5
        )

        main_layout.addWidget(
            self.statistics_box,
            1
        )

        self.setLayout(
            main_layout
        )

        self.image_button.clicked.connect(
            self.process_image
        )

        self.video_button.clicked.connect(
            self.process_video
        )

    def process_image(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение"
        )

        if not file_name:
            return

        results = self.detector.detect_image(
            file_name
        )

        counts = Statistics.get_counts(
            results
        )

        Statistics.save_statistics(
            counts,
            "results/statistics.txt"
        )

        image = results[0].plot(
            conf=False,
            line_width=1,
            font_size=6
        )

        output = "images/result.jpg"

        cv2.imwrite(
            output,
            image
        )

        text = "Обнаруженные объекты:\n\n"

        for name, count in counts.items():

            russian_name = translations.get(
                name,
                name
            )

            text += (
                f"{russian_name}: "
                f"{count}\n"
            )

        self.statistics_box.setText(
            text
        )

        image_pixmap = QPixmap(
            output
        )

        self.image_label.setPixmap(
            image_pixmap.scaled(
                self.image_label.width(),
                self.image_label.height(),
                Qt.AspectRatioMode.KeepAspectRatio
            )
        )

    def process_video(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите видео"
        )

        if not file_name:
            return

        self.detector.detect_video(
            file_name
        )

        self.statistics_box.setText(
            "Видео обработано\n\n"
            "Результат сохранён в папке runs/detect/"
        )


def run_app():

    app = QApplication([])

    window = MainWindow()

    window.show()

    app.exec()