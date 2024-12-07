import random
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient

import random
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient

import random
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, pyqtProperty, QPoint
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient

# class AnimatedColorSeparationLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("color: white; font-size: 36px; background-color: black;")
#         self.setup_flicker()
        
#         self.red_offset = 0
#         self.blue_offset = 0
#         self.yellow_offset = 0
        

#         # Timer for color separation animation
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_offsets)
#         self.timer.start(60)  # Update at ~12.5fps
        
        
#     def setup_flicker(self):
#         # Flicker Timer
#         self.flicker_timer = QTimer(self)
#         self.flicker_timer.timeout.connect(self.random_flicker)
#         self.flicker_timer.start(60)  # Faster flickering

#     def random_flicker(self):
#         # Random opacity flicker (0-255)
        
#         opacity = random.randint(150, 255)  # Random opacity between 150-255
#         print(f"INT: {opacity}")
#         self.setStyleSheet(f"color: rgb({opacity}, {opacity}, {opacity}); background-color: black;")
        
#         # # Random opacity flicker (0-255)
#         # self.opacity = random.randint(0, 255)  # Random opacity between 0-255
#         # self.update()  # Make sure to trigger a repaint after opacity change

        
#     def update_offsets(self):
#         # Randomize offsets for red, blue, and yellow shadows
#         self.red_offset = random.uniform(-4, 8)
#         self.blue_offset = random.uniform(-8, 4)
#         self.yellow_offset = random.uniform(-4, 4)
#         self.update()  # Trigger repaint

#     def paintEvent(self, event):
#         super().paintEvent(event)
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
        
#         # # Draw main white text
#         # painter.setPen(Qt.white)
#         # painter.drawText(rect, Qt.AlignCenter, text)

#         # Apply a CRT-like gradient overlay
#         gradient = QLinearGradient(0, 0, 0, self.height())
#         gradient.setColorAt(0.5, QColor(50, 50, 200, 80))  # Soft blue color
#         gradient.setColorAt(1.0, QColor(150, 50, 200, 30))  # Soft purple color
#         painter.fillRect(self.rect(), gradient)

#         # Add scanline effect
#         for y in range(0, self.height(), 2):
#             painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 16))  # Less intense scanlines

#         painter.end()
        
#     def resizeEvent(self, event):
#         # Adjust font size based on width
#         self.adjustFontSize()
#         super().resizeEvent(event)

#     def adjustFontSize(self):
#         font = QFont("Arial", 36)
#         # Dynamically adjust font size based on label width (the text size)
#         # new_font_size = 50  # Set the font size to be the same as the label's width
#         # font.setPointSize(new_font_size)  # Adjust the font size
#         self.setFont(font)

# if __name__ == "__main__":
#     app = QApplication([])
#     label = AnimatedColorSeparationLabel("Animated Color Separation and Flicker Effect")
#     label.resize(800, 400)
#     label.show()
#     app.exec_()


# import random
# from PyQt5.QtWidgets import QApplication, QLabel
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient

# class AnimatedColorSeparationLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("color: white; font-size: 36px; background-color: black;")
        
#         # Initialize color offsets for shadows
#         self.red_offset = 0
#         self.blue_offset = 0
#         self.yellow_offset = 0
        
#         # Initialize flicker opacity
#         self.opacity = 0  # Initial random opacity
        
#         # Set up flicker timer
#         self.flicker_timer = QTimer(self)
#         self.flicker_timer.timeout.connect(self.random_flicker)
#         self.flicker_timer.start(150)  # Flickering faster
        
#         # # Timer for color separation animation
#         # self.timer = QTimer(self)
#         # self.timer.timeout.connect(self.update_offsets)
#         # self.timer.start(60)  # Update at ~12.5fps

#     def random_flicker(self):
#         # Random opacity flicker (0-255)
#         self.opacity = random.randint(200, 255)  # Random opacity between 0-255
#         self.update_offsets()
#         self.update()  # Trigger a repaint to reflect the new opacity

#     def update_offsets(self):
#         # Randomize offsets for red, blue, and yellow shadows
#         self.red_offset = random.uniform(-3, 3)
#         self.blue_offset = random.uniform(-3, 3)
#         self.yellow_offset = random.uniform(-3, 3)
#         self.update()  # Trigger repaint

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Get text details
#         text = self.text()
#         rect = self.rect()

#         # Set font for custom drawing
#         font = QFont("Arial", 36)
#         painter.setFont(font)

#         # Control opacity using QPainter
#         painter.setOpacity(self.opacity / 255)  # Normalize opacity to a value between 0 and 1

#         # First, draw the text with shadows (color separation)
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

#         # Draw the main white text
#         painter.setPen(Qt.white)
#         painter.drawText(rect, Qt.AlignCenter, text)

#         # Apply a CRT-like gradient overlay
#         gradient = QLinearGradient(0, 0, 0, self.height())
#         gradient.setColorAt(0.5, QColor(50, 50, 200, 80))  # Soft blue color
#         gradient.setColorAt(1.0, QColor(150, 50, 200, 30))  # Soft purple color
#         painter.fillRect(self.rect(), gradient)

#         # Add scanline effect
#         for y in range(0, self.height(), 2):
#             painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 16))  # Less intense scanlines

#         painter.end()

# if __name__ == "__main__":
#     app = QApplication([])
#     label = AnimatedColorSeparationLabel("Animated Color Separation and Flicker Effect")
#     label.resize(800, 400)
#     label.show()
#     app.exec_()




import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QVariantAnimation, QPropertyAnimation, pyqtProperty, QPoint
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QLinearGradient, QRadialGradient
from PyQt5.QtGui import QLinearGradient


class AnimatedColorSeparationLabel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setAlignment(Qt.AlignCenter)
        self.BackgroundColor = "black"
        self.colorOverlay = True
        self.setStyleSheet(f"color: white; background-color: {self.BackgroundColor};")
        
        # Initialize color offsets for shadows
        self.red_offset = 0
        self.blue_offset = 0
        self.yellow_offset = 0
        
        # Initialize flicker opacity
        self._opacity = 255  # Set initial opacity to 1 (fully visible)
        self.flicker_speed_ms = 150
        # Set up flicker animation with keyframes
        self.flicker_animation = QVariantAnimation(self)
        self.flicker_animation.setStartValue(self._opacity)
        self.flicker_animation.setEndValue(self._opacity)  # Start and end with initial value, we'll update manually
        self.flicker_animation.setDuration(self.flicker_speed_ms)  # Duration for the whole cycle (in milliseconds)
        self.flicker_animation.setLoopCount(-1)  # Loop indefinitely
        
        if self.BackgroundColor == "black":
            # Define keyframe-like opacity values (from your CSS flicker)
            self.flicker_animation.setKeyValueAt(0.0, 0.95)  # Start at the highest opacity
            self.flicker_animation.setKeyValueAt(0.1, 0.91)  # Slight drop
            self.flicker_animation.setKeyValueAt(0.2, 0.93)  # Bounce back up
            self.flicker_animation.setKeyValueAt(0.3, 0.87)  # Subtle drop
            self.flicker_animation.setKeyValueAt(0.4, 0.91)  # Slight rise
            self.flicker_animation.setKeyValueAt(0.5, 0.93)  # Bounce back up
            self.flicker_animation.setKeyValueAt(0.6, 0.87)  # Slight drop
            self.flicker_animation.setKeyValueAt(0.7, 0.89)  # Subtle rise
            self.flicker_animation.setKeyValueAt(0.8, 0.87)  # Gentle drop
            self.flicker_animation.setKeyValueAt(0.9, 0.92)  # Slight rise
            self.flicker_animation.setKeyValueAt(1.0, 0.95)  # End at the highest opacity
        else:
            self.flicker_animation.setKeyValueAt(0.0, 0.15)  # Start at the highest opacity
            self.flicker_animation.setKeyValueAt(0.1, 0.11)  # Slight drop
            self.flicker_animation.setKeyValueAt(0.2, 0.13)  # Bounce back up
            self.flicker_animation.setKeyValueAt(0.3, 0.07)  # Subtle drop
            self.flicker_animation.setKeyValueAt(0.4, 0.11)  # Slight rise
            self.flicker_animation.setKeyValueAt(0.5, 0.13)  # Bounce back up
            self.flicker_animation.setKeyValueAt(0.6, 0.07)  # Slight drop
            self.flicker_animation.setKeyValueAt(0.7, 0.09)  # Subtle rise
            self.flicker_animation.setKeyValueAt(0.8, 0.07)  # Gentle drop
            self.flicker_animation.setKeyValueAt(0.9, 0.12)  # Slight rise
            self.flicker_animation.setKeyValueAt(1.0, 0.15)  # End at the highest opacity

        # Connect the animation's value change signal to a function that updates the opacity
        self.flicker_animation.valueChanged.connect(self.update_opacity)
        
        # Start the animation
        self.flicker_animation.start()
        


        # Set up color separation animation with start and end values
        self.color_animation = QPropertyAnimation(self, b"colorOffsets")
        self.color_animation.setDuration(1600)  # Animation duration for color offset
        self.color_animation.setStartValue(QPoint(int(self.red_offset), int(self.blue_offset)))
        self.color_animation.setEndValue(QPoint(int(random.uniform(-3, 3)), int(random.uniform(-3, 3))))  # Randomize end values for offsets
        self.color_animation.setLoopCount(-1)  # Loop indefinitely
        self.color_animation.start()

    @pyqtProperty(int)
    def opacity(self):
        return self._opacity
    
    @opacity.setter
    def opacity(self, value):
        self._opacity = value
        self.update()  # Trigger a repaint

    @pyqtProperty(QPoint)
    def colorOffsets(self):
        return QPoint(int(self.red_offset), int(self.blue_offset))

    @colorOffsets.setter
    def colorOffsets(self, value):
        self.red_offset = random.uniform(-3, 1)#value.x()  # Use x() for red offset
        self.blue_offset = random.uniform(-1, 3) #value.y()  # Use y() for blue offset
        self.yellow_offset = random.uniform(-2, 2)  # Randomize yellow offset
        self.update()  # Trigger repaint

    def update_opacity(self, value):
        # Update the opacity value with the one from the animation
        self._opacity = value
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        super().paintEvent(event)

        # Get text details
        text = "NEON GENESIS EVANGELION"
        rect = self.rect()
        
        """
        Helvetica Neue 
        Helvetica
        Xanh Mono | Don't have
        all-caps Helvetica 
        Matisse EB (Jap Font) | Dont ahve
        Microsoft Sans Serif = sans-serif
        Times New Roman
        TT-JTCE'EE'CE'i`M9 
        TT-JTCE'EE'CE'i`M9P | True Eva
        TT-NISi:e^ :n~i'(c)e:A~W3 | True Eva
        TT-NISi:e^ :n~i'(c)e:A~W3P
        TT-NIS平成明朝体W9 | Best Eva
        TT-n~xn~i'(c) | Close Eva
        TT-n~xn~i'(c)P
        """
        
        # Set font for custom drawing
        font = QFont("TT-NIS平成明朝体W9", 48)
        font.setWeight(QFont.DemiBold)
        painter.setFont(font)


        painter.setOpacity(1)
        # First, draw the text with shadows (color separation)
        # Draw blue shadow
        blue_offset_int = int(self.blue_offset)  # Cast to int
        painter.setPen(QColor(0, 0, 255, 255))  # Blue with transparency
        painter.drawText(rect.adjusted(blue_offset_int, 0, blue_offset_int, 0), Qt.AlignCenter, text)

        # # Draw red shadow
        red_offset_int = int(self.red_offset)  # Cast to int
        painter.setPen(QColor(255, 0, 0, 128))  # Red with transparency
        painter.drawText(rect.adjusted(red_offset_int, 0, red_offset_int, 0), Qt.AlignCenter, text)

        # Draw yellow shadow
        yellow_offset_int = int(self.yellow_offset)  # Cast to int
        # painter.setPen(QColor(255, 255, 0, 128))  # Yellow with transparency
        painter.setPen(QColor(0, 255, 0, 128))  # Green with transparency
        painter.drawText(rect.adjusted(0, yellow_offset_int, 0, yellow_offset_int), Qt.AlignCenter, text)

        # Draw the main white text
        
        if self.BackgroundColor == "white":
            painter.setPen(QColor(0, 0, 0, 255)) # Black
        else:
            painter.setPen(QColor(255, 255, 255, 255)) # White
        
        painter.drawText(rect, Qt.AlignCenter, text)

        # Control opacity using QPainter
        painter.setOpacity(self._opacity)  # Use the set opacity
        # Apply a CRT-like gradient overlay
        gradient_CRT_backlight = QLinearGradient(0, 0, 0, self.height())
        
        
        # center_x = self.width() / 2
        # center_y = self.height() / 2
        # radius = min(self.width(), self.height()) / 2
        # gradient = QRadialGradient(center_x, center_y, radius)
        
        # gradient.setColorAt(0.0, QColor(248, 248, 248, 30))  # Soft purple color
        # gradient.setColorAt(0.5, QColor(150, 50, 200, 80))  # Soft blue color
        # gradient.setColorAt(1, QColor(248, 248, 248, 30))  # Soft purple color
        
        if self.BackgroundColor == "black":
            # gradient.setColorAt(0.0, QColor(200, 255, 150, 30))  # Soft green-yellow at the top
            gradient_CRT_backlight.setColorAt(0.5, QColor(255, 255, 255, 10))   # Neutral white in the center
            # gradient.setColorAt(1.0, QColor(150, 150, 255, 30))  # Soft blue-purple at the bottom
            # gradient.setColorAt(0.5, QColor(85, 100, 50, 90))  # A muted olive green, typical of older CRT screens
            # gradient.setColorAt(1.0, QColor(20, 20, 20, 150))   # A very dark gray/black, giving the screen depth
        
        if self.colorOverlay == True and self.BackgroundColor == "black":
            gradient_CRT_backlight.setColorAt(0.0, QColor(0, 0, 0, 255))
            
            gradient_CRT_backlight.setColorAt(1.0, QColor(0, 0, 0, 255))
        
        if self.colorOverlay == True and self.BackgroundColor != "black":
            gradient_CRT_backlight.setColorAt(0.0, QColor(200, 255, 150, 255))  # Soft green-yellow at the top
            # gradient.setColorAt(0.5, QColor(255, 255, 255, 255))   # Neutral white in the center
            # gradient.setColorAt(0.5, QColor(0, 0, 0, 128))   # Neutral white in the center

            gradient_CRT_backlight.setColorAt(1.0, QColor(150, 150, 255, 255))  # Soft blue-purple at the bottom  
        
        # painter.setBrush(QBrush(gradient))
        # painter.drawRect(0, 0, self.width(), self.height())
        
        painter.fillRect(self.rect(), gradient_CRT_backlight)

        # Add scanline effect
        line_desnity_v = 2
        line_desnity_h = 2
        
        
        
        # Add Horizontal scan lines # linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%),
        for y in range(0, self.height(), line_desnity_v):
            painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 50))  # Less intense scanlines
            
            
        # Add vertical scan lines #  linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        for x in range(0, self.width(), line_desnity_h):
            # painter.fillRect(x, 0, 1, self.height(), QColor(18, 16, 16, 60)) # Slightly lighter dark line
            
            # gradient = QLinearGradient(x, 0, x + 1, self.height())  # Vertical gradient
            # gradient = QLinearGradient(x, 0, x + 1, 0)  # Horizontal gradient (90 degrees)

            gradient_CRT_ScanLines = QLinearGradient(0, 0, 20, 0)  # Horizontal gradient (90 degrees, spans 1 pixel horizontally)
            
            if self.BackgroundColor == "black":
                gradient_CRT_ScanLines.setColorAt(0.0, QColor(255, 0, 0, 15))  # Subtle red
                gradient_CRT_ScanLines.setColorAt(0.5, QColor(0, 255, 0, 11))   # Subtle green
                gradient_CRT_ScanLines.setColorAt(1, QColor(0, 0, 255, 15))  # Subtle blue
                
            else:
                gradient_CRT_ScanLines.setColorAt(0.0, QColor(255, 0, 0, 150))  # Subtle red
                gradient_CRT_ScanLines.setColorAt(0.5, QColor(0, 255, 0, 110))   # Subtle green
                gradient_CRT_ScanLines.setColorAt(1, QColor(0, 0, 255, 150))  # Subtle blue
                
            gradient_CRT_ScanLines.setSpread(QLinearGradient.RepeatSpread)
            painter.fillRect(x, 0, 1, self.height(), gradient_CRT_ScanLines)

        
        # else:
        #     # Add Horizontal scan lines 
        #     for y in range(0, self.height(), 2):
        #         painter.fillRect(0, y, self.width(), 1, QColor(100, 100, 100, 255))  # Light gray line with transparency

        #     # Add vertical scan lines
        #     for x in range(0, self.width(), 2):
        #         painter.fillRect(x, 0, 1, self.height(), QColor(110, 110, 110, 255))  # Less intense scanlines

        painter.end()

"""
Animated Color Separation and Flicker Effect
"""
if __name__ == "__main__":
    app = QApplication([])
    label = AnimatedColorSeparationLabel()
    label.resize(800, 400)
    label.show()
    app.exec_()
