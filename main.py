import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QFormLayout, QSpacerItem, QSizePolicy, QScrollArea, QFrame
from PyQt6.QtWidgets import QPushButton, QRadioButton, QButtonGroup



class FloatingGifApp(QLabel):
    def __init__(self):
        super().__init__()

        self.spooky_gifs = ["skeleton-dance.gif", "skelly_dance2.gif", "skelly_dance3.gif"]
        self.index = 0

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        

        # Set window properties
        self.setWindowTitle("Spoooooooooky")
        self.resize(250, 250)
        # self.setGeometry(100, 100, 500, 500) # (x, y, width, height)

        screen = QApplication.primaryScreen().geometry()

        window_width = 300
        window_height = 300
        self.resize(window_width, window_height) 
        
        # Calculate coordinates (Screen border minus window size)
        # We subtract an optional padding (e.g., 20 pixels) so it doesn't clip right against the edge
        padding = 20 
        x = screen.width() - window_width - padding
        y = screen.height() - window_height - padding

        self.move(x, y)

        self.movie = QMovie(self.spooky_gifs[self.index]) 
        self.setMovie(self.movie)
        self.movie.start()


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.nextGif()

    def keyPressEvent(self, event):
        # Pressing the Escape key closes the app immediately
        if event.key() == Qt.Key.Key_Escape:
            print("Escape key pressed. Quitting application...")
            QApplication.quit()
        if event.key() == Qt.Key.Key_Space:
            self.nextGif()

    def nextGif(self):
        # 1. Stop the current animation loop
        self.movie.stop()
        
        # 2. Advance the index (wrapping back to 0 at the end of the list)
        self.index = (self.index + 1) % len(self.spooky_gifs)
        
        # 3. Update the movie's file source and restart it
        new_file_path = self.spooky_gifs[self.index]
        self.movie.setFileName(new_file_path)
        self.movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FloatingGifApp()
    window.show()
    sys.exit(app.exec())