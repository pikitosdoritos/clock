from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QTime, QTimer, QPoint
from PySide6.QtGui import QFont, QRegion, QColor




def main():

    def update():
        now = QTime.currentTime()
        time = now.toString("HH:mm:ss.zzz")
        label.setText(time)

    drag_pos = {'offset': None}

    def handle_mouse_down(event):
        if event.button() == Qt.LeftButton:
            drag_pos["offset"] = event.globalPosition().toPoint() - window.pos()

    def handle_mouse_move(event):
        if event.buttons() == Qt.LeftButton and drag_pos['offset'] is not None:
            window.move(event.globalPosition().toPoint() - drag_pos["offset"])


    app = QApplication()
    window = QMainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    window.setAttribute(Qt.WA_TranslucentBackground)
    window.resize(800, 350)
    window.mousePressEvent = handle_mouse_down
    window.mouseMoveEvent = handle_mouse_move
    window.setMask(QRegion(window.rect(), QRegion.Ellipse))

    window.setWindowTitle("CLOCK")    

    wrapper = QWidget()
    window.setCentralWidget(wrapper)

    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)
    wrapper.setLayout(layout)


    label = QLabel()
    label.setAlignment(Qt.AlignCenter)
    label.setFont(QFont("Trebuchet MS", 80))
    

    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setColor(QColor(255, 255, 255, 255))
    shadow.setOffset(0, 0)

    label.setGraphicsEffect(shadow)

    layout.addWidget(label)

    window.show()
    

    timer = QTimer()
    timer.timeout.connect(update)
    timer.start(1)

    update()

    app.exec()

main()