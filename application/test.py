import os
import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from queue import Queue
import webview
import webview.menu as wm
import webview.window
from threading import Thread
import threading
import time
import re
from enum import Enum
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QVBoxLayout, QLabel, QListWidget,QProgressBar
from PyQt5.QtWidgets import QListView, QListWidgetItem, QMessageBox, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QProgressBar
from PyQt5.QtCore import Qt, pyqtSlot

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QListWidget, QTabWidget, QPushButton, QProgressBar

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("PyQt5 Window")
#         self.setGeometry(100, 100, 800, 600)

#         # Apply the stylesheet
#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: #1a0d1c;
#             }
#             QLabel {
#                 color: #f6e2f8;
#                 font-weight: bold;
#                 font-size: 18px;
#             }
#             QLineEdit {
#                 background-color: #1a0d1c;
#                 color: #f6e2f8;
#                 border: 1px solid #79253e;
#                 border-radius: 10px;
#                 padding: 5px;
#                 font-size: 18px;
#             }
#             QListWidget {
#                 background-color: #1a0d1c;
#                 color: #f6e2f8;
#                 border: 1px solid #79253e;
#                 border-radius: 10px;
#                 padding: 5px;
#                 font-size: 16px;
#             }
#             QListWidget::item {
#                 background-color: #1a0d1c;
#                 color: #f6e2f8;
#                 border: none;
#                 padding: 5px;
#             }
#             QListWidget::item:selected {
#                 background-color: #79253e;
#                 color: #1a0d1c;
#                 border-radius: 5px;
#             }
#             QTabWidget::pane {
#                 background-color: #1a0d1c;
#                 border: 1px solid #79253e;
#                 border-radius: 10px;
#             }
#             QTabWidget::tab-bar {
#                 alignment: center;
#             }
#             QTabBar::tab {
#                 background: #79253e;
#                 color: #f6e2f8;
#                 border: 1px solid #79253e;
#                 border-radius: 10px;
#                 padding: 5px;
#                 margin: 2px;
#                 min-height: 30px;
#                 min-width: 100px;
#                 font-size: 18px;
#             }
#             QTabBar::tab:selected {
#                 background: #79253e;
#                 color: #f6e2f8;
#             }
#             QTabBar::tab:hover {
#                 background: #d26076;
#             }
#             QPushButton {
#                 background-color: #79253e;
#                 color: white;
#                 border: none;
#                 border-radius: 10px;
#                 padding: 16px;
#                 font-size: 24px;
#             }
#             QPushButton:hover {
#                 background-color: #d26076;
#             }
#             QProgressBar {
#                 text-align: center;
#                 background-color: #79253e;
#                 border: 1px solid #79253e;
#                 border-radius: 10px;
#                 height: 8px;
#                 font-size: 24px;
#                 padding: 12px;
#             }
#             QProgressBar::chunk {
#                 background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
#                                     stop:0.1 #290D12,
#                                     stop:0.2 #341118,
#                                     stop:0.3 #42161E,
#                                     stop:0.4 #541C27,
#                                     stop:0.5 #6B2533,
#                                     stop:0.6 #893042,
#                                     stop:0.7 #AE3F55,
#                                     stop:0.8 #C55C71,
#                                     stop:0.9 #D78A99,
#                                     stop:1 #EBC3CB
#                                     );
#                         }
#                 border-radius: 5px;
#                 width: 20px;
#                 margin: 1px;
#             }
#         """)

#         self.create_widgets()
#         self.layout_setup()

#     def create_widgets(self):
#         self.label = QLabel("Welcome to PyQt5", self)
#         self.label.setGeometry(100, 50, 600, 40)

#         self.line_edit = QLineEdit("Enter text here", self)
#         self.line_edit.setGeometry(100, 150, 300, 30)

#         self.list_widget = QListWidget(self)
#         self.list_widget.setGeometry(100, 250, 300, 200)

#         self.add_item("Item 1")
#         self.add_item("Item 2")
#         self.add_item("Item 3")

#         self.tab_widget = QTabWidget(self)
#         self.tab_widget.setGeometry(500, 50, 300, 400)

#         self.tab1 = QWidget()
#         self.tab2 = QWidget()

#         self.tab1_layout = QVBoxLayout()
#         self.tab2_layout = QVBoxLayout()

#         self.tab1_layout.addWidget(QPushButton("Button 1"))
#         self.tab1_layout.addWidget(QProgressBar())
#         self.tab2_layout.addWidget(QPushButton("Button 2"))

#         self.tab1.setLayout(self.tab1_layout)
#         self.tab2.setLayout(self.tab2_layout)

#         self.tab_widget.addTab(self.tab1, "Tab 1")
#         self.tab_widget.addTab(self.tab2, "Tab 2")

#     def add_item(self, text):
#         item = QListWidgetItem()
#         item.setText(text)
#         self.list_widget.addItem(item)

#     def layout_setup(self):
#         pass

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
# from PyQt5.QtCore import Qt, QPropertyAnimation, QSequentialAnimationGroup, QRect, QEasingCurve, QTimer
# from PyQt5.QtGui import QColor, QPainter, QLinearGradient

# class AnimatedLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("color: white; font-size: 500px; background-color: black;")
#         self.setup_shadow_animation()
#         self.setup_opacity_flicker()

#     def setup_shadow_animation(self):
#         # Text Shadow Animation
#         self.shadow_effect = QGraphicsDropShadowEffect(self)
#         self.shadow_effect.setBlurRadius(3)
#         self.shadow_effect.setColor(QColor(255, 0, 80, 77))  # rgba(255,0,80,0.3)
#         self.setGraphicsEffect(self.shadow_effect)

#         self.shadow_animation = QPropertyAnimation(self.shadow_effect, b"offset")
#         self.shadow_animation.setDuration(1600)
#         self.shadow_animation.setKeyValueAt(0.0, (0.44, 0))  # Start small offset
#         self.shadow_animation.setKeyValueAt(0.5, (3.9, 0))  # Larger offset
#         self.shadow_animation.setKeyValueAt(1.0, (0.44, 0))  # Back to start
#         self.shadow_animation.setLoopCount(-1)  # Infinite loop
#         self.shadow_animation.start()

#     def setup_opacity_flicker(self):
#         # Flicker Animation
#         self.opacity_effect = QGraphicsOpacityEffect(self)
#         self.setGraphicsEffect(self.opacity_effect)

#         self.flicker_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
#         self.flicker_animation.setDuration(150)
#         self.flicker_animation.setKeyValues([
#             (0.0, 0.28),
#             (0.05, 0.34),
#             (0.1, 0.23),
#             (0.15, 0.91),
#             (0.2, 0.18),
#             (0.25, 0.84),
#             (0.3, 0.66),
#             (0.35, 0.68),
#             (0.4, 0.27),
#             (0.45, 0.85),
#             (0.5, 0.96),
#             (0.55, 0.09),
#             (0.6, 0.2),
#             (0.65, 0.72),
#             (0.7, 0.53),
#             (0.75, 0.37),
#             (0.8, 0.71),
#             (0.85, 0.7),
#             (0.9, 0.7),
#             (0.95, 0.36),
#             (1.0, 0.24),
#         ])
#         self.flicker_animation.setLoopCount(-1)
#         self.flicker_animation.start()

#     def paintEvent(self, event):
#         # Custom CRT Overlay
#         super().paintEvent(event)
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Add gradient lines
#         gradient = QLinearGradient(0, 0, 0, self.height())
#         gradient.setColorAt(0.5, QColor(0, 0, 0, 0))
#         gradient.setColorAt(1.0, QColor(0, 0, 0, 63))  # rgba(0,0,0,0.25)
#         painter.fillRect(self.rect(), gradient)

#         # Add scanline effect
#         for y in range(0, self.height(), 2):
#             painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 26))  # rgba(18,16,16,0.1)

#         painter.end()

# if __name__ == "__main__":
#     app = QApplication([])
#     label = AnimatedLabel("Flickering CRT Effect")
#     label.resize(400, 200)
#     label.show()
#     app.exec_()

"""
Got a cool line gradient going
"""

import random
from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QLinearGradient


class AnimatedLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: white; font-size: 1px; background-color: black;")
        self.setup_flicker()

    def setup_flicker(self):
        # Flicker Timer
        self.flicker_timer = QTimer(self)
        self.flicker_timer.timeout.connect(self.random_flicker)
        self.flicker_timer.start(30)  # Faster flickering

    def random_flicker(self):
        # Random brightness flicker
        brightness = random.randint(150, 255)  # Random brightness between 150-255
        self.setStyleSheet(f"color: rgb({brightness}, {brightness}, {brightness}); background-color: black;")

    def paintEvent(self, event):
        # Custom CRT Overlay
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # gradient = QRadialGradient(self.width() / 2, self.height() / 2, min(self.width(), self.height()) / 2)
        # gradient.setColorAt(0.5, Qt.red)
        # gradient.setColorAt(1, Qt.blue)
        # gradient.setColorAt(0.5, QColor(0, 120, 90, 80))  # Midpoint color with some transparency
        # gradient.setColorAt(1.0, QColor(100, 0, 0, 30))  # Less intense color with transparency
        
        # gradient = QConicalGradient(self.width() / 2, self.height() / 2, 0)  # 0 degrees for starting angle
        # # gradient.setColorAt(0, Qt.green)
        # # gradient.setColorAt(1, Qt.yellow)
        # gradient.setColorAt(0.5, QColor(0, 120, 90, 80))  # Semi-transparent color at 50% angle
        # gradient.setColorAt(1.0, QColor(100, 0, 0, 30))  # Less intense color at 100% angle (full rotation)

        # Add gradient lines
        gradient = QLinearGradient(0, 0, 0, self.height())
        
        """
        This is a cool green to black top-bottm graddient
        """
        # gradient.setColorAt(0.5, QColor(0, 120, 90, 30))
        # gradient.setColorAt(1.0, QColor(100, 0, 0, 30))  # Less intense gradient
        
        gradient.setColorAt(0.5, QColor(50, 50, 200, 30))  # A soft blue color
        gradient.setColorAt(1.0, QColor(150, 50, 200, 30))  # A soft purple color
        
        # gradient.setColorAt(0.5, QColor(0, 255, 100, 80))  # A bright green color
        # gradient.setColorAt(1.0, QColor(255, 100, 0, 80))  # A warm orange color
        
        # gradient.setColorAt(0.5, QColor(40, 120, 40, 80))  # Faded green color
        # gradient.setColorAt(1.0, QColor(0, 0, 0, 100))    # Almost black, representing the dark, shadowy areas
        
        # gradient.setColorAt(0.5, QColor(0, 255, 255, 80))  # A bright cyan color
        # gradient.setColorAt(1.0, QColor(0, 0, 128, 80))    # A deep blue, representing the darker edges
        
        
        # gradient.setColorAt(0.5, QColor(85, 100, 50, 90))  # A muted olive green, typical of older CRT screens
        # gradient.setColorAt(1.0, QColor(20, 20, 20, 150))   # A very dark gray/black, giving the screen depth
        
        # gradient.setColorAt(0.5, QColor(40, 40, 100, 80))  # Dark purple/blue
        # gradient.setColorAt(1.0, QColor(0, 0, 40, 100))    # Deep midnight blue
        
        # gradient.setColorAt(0.5, QColor(255, 0, 255, 80))   # Neon pink
        # gradient.setColorAt(1.0, QColor(0, 0, 255, 80))     # Electric blue

        # gradient.setColorAt(0.5, QColor(0, 100, 255, 80))   # Deep blue
        # gradient.setColorAt(1.0, QColor(0, 200, 255, 80))   # Lighter blue, almost turquoise

        # gradient.setColorAt(0.5, QColor(255, 255, 255, 80))   # Deep blue
        # gradient.setColorAt(1, QColor(0, 0, 0, 80))   # Lighter blue, almost turquoise
        
        
        painter.fillRect(self.rect(), gradient)

        # Add scanline effect
        for y in range(0, self.height(), 2):
            painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 16))  # Less intense scanlines

        painter.end()
        
    def resizeEvent(self, event):
        # Adjust font size based on width
        self.adjustFontSize()
        super().resizeEvent(event)

    def adjustFontSize(self):
        font = self.font()
        # Dynamically adjust font size based on label width (the text size)
        new_font_size = 50  # Set the font size to be the same as the label's width
        font.setPointSize(new_font_size)  # Adjust the font size
        self.setFont(font)


if __name__ == "__main__":
    app = QApplication([])
    label = AnimatedLabel("Flickering CRT Effect")
    label.resize(800, 400)
    label.show()
    app.exec_()
    
    
# import random
# from PyQt5.QtWidgets import QApplication, QLabel, QGraphicsOpacityEffect
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QColor, QPainter, QLinearGradient


# class AnimatedLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("color: white; font-size: 250px; background-color: black;")
#         self.setup_opacity_flicker()

#     def setup_opacity_flicker(self):
#         # Flicker Effect with Randomness
#         self.opacity_effect = QGraphicsOpacityEffect(self)
#         self.setGraphicsEffect(self.opacity_effect)

#         self.flicker_timer = QTimer(self)
#         self.flicker_timer.timeout.connect(self.random_flicker)
#         self.flicker_timer.start(100)  # Adjust the interval for faster flicker

#     def random_flicker(self):
#         # Generate a random opacity value between 0.2 and 1.0
#         random_opacity = random.uniform(0.1, 1.0)
#         self.opacity_effect.setOpacity(random_opacity)

#     def paintEvent(self, event):
#         # Custom CRT Overlay
#         super().paintEvent(event)
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Add gradient lines
#         gradient = QLinearGradient(0, 0, 0, self.height())
#         gradient.setColorAt(0.5, QColor(0, 120, 90, 100))
#         gradient.setColorAt(1.0, QColor(100, 0, 0, 63))  # rgba(0,0,0,0.25)
#         painter.fillRect(self.rect(), gradient)

#         # Add scanline effect
#         for y in range(0, self.height(), 2):
#             painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 26))  # rgba(18,16,16,0.1)

#         painter.end()


# if __name__ == "__main__":
#     app = QApplication([])
#     label = AnimatedLabel("Flickering CRT Effect")
#     label.resize(400, 200)
#     label.show()
#     app.exec_()



"""
Working text aberations
Color Separation
The color separation effect isnt really a CRT TV-specific effect, 
but one which people like to associate with CRT TVs. 
Im not sure if this really ever happened with CRT TVs, but it does give a cool effect, 
so well use it anyway.

The magic here is done with text-shadow, specifically two text shadows, 
that will be added to the text and then varied in their offset using another animation.
"""
# import random
# from PyQt5.QtWidgets import QApplication, QLabel
# from PyQt5.QtCore import QTimer, Qt
# from PyQt5.QtGui import QPainter, QColor, QFont

# class ColorSeparationLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("color: white; font-size: 36px; background-color: black;")
        
#         self.red_offset = 0
#         self.blue_offset = 0
#         self.yellow_offset = 0
        
#         # Timer for color separation animation
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_offsets)
#         self.timer.start(60)  # 80 = Update at ~12.5fps try 30, 60, 90

#     def update_offsets(self):
#         # Randomize offsets for red and blue shadows
#         self.red_offset = random.uniform(-2, 2)
#         self.blue_offset = random.uniform(-2, 2)
#         self.yellow_offset = random.uniform(-2, 2)
#         self.update()  # Trigger repaint

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
        
#         # Get text details
#         text = self.text()
#         rect = self.rect()
        
#         # Set font
#         font = QFont("Arial", 36)
#         painter.setFont(font)
        
#         # Draw blue shadow
#         blue_offset_int = int(self.blue_offset)  # Cast to int
#         painter.setPen(QColor(0, 30, 255, 128))  # Blue with transparency
#         painter.drawText(rect.adjusted(blue_offset_int, 0, blue_offset_int, 0), Qt.AlignCenter, text)
        
#         # Draw red shadow
#         red_offset_int = int(self.red_offset)  # Cast to int
#         painter.setPen(QColor(255, 0, 80, 128))  # Red with transparency
#         painter.drawText(rect.adjusted(-red_offset_int, 0, -red_offset_int, 0), Qt.AlignCenter, text)
        
        
#         # Draw yellow shadow
#         yellow_offset_int = int(self.yellow_offset)  # Cast to int
#         painter.setPen(QColor(255, 255, 0, 128))  # Yellow with transparency
#         painter.drawText(rect.adjusted(0, yellow_offset_int, 0, yellow_offset_int), Qt.AlignCenter, text)
        
#         # Draw main white text
#         painter.setPen(Qt.white)
#         painter.drawText(rect, Qt.AlignCenter, text)
        
#         painter.end()

# if __name__ == "__main__":
#     app = QApplication([])
#     label = ColorSeparationLabel("Color Separation Effect")
#     label.resize(600, 200)
#     label.show()
#     app.exec_()


