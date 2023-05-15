import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from pytube import YouTube

class YoutubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Downloader")
        self.setWindowIcon(QIcon("youtube.png"))  # Replace "icon.png" with your icon file path
        self.setGeometry(400, 400, 400, 400) # You can Custom Big GUI In this command 

        # URL Label
        url_label = QLabel("Enter YouTube Video URL:", self)
        url_label.move(20, 20)

        # URL Text Field
        self.url_text = QLineEdit(self)
        self.url_text.setGeometry(20, 40, 250, 25)

        # Download Button
        download_button = QPushButton("Download", self)
        download_button.setGeometry(20, 80, 100, 30)
        download_button.clicked.connect(self.on_download)

        # Status Label
        self.status_label = QLabel("", self)
        self.status_label.move(20, 120)

    def on_download(self):
        url = self.url_text.text()
        try:
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            self.status_label.setText("Downloading: " + yt.title)
            video.download()
            self.status_label.setText("Download Complete!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YoutubeDownloader()
    window.show()
    sys.exit(app.exec_())
