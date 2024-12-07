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
        self.BackgroundColor = "white"
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
            # Values can be either 255-0 or 1.0-0.0 but they must match for same animation
            self.flicker_animation.setKeyValueAt(0.0, 1.0)  # Start at full opacity
            self.flicker_animation.setKeyValueAt(0.05, random.uniform(0.7, 0.9))  # Slight dimming
            self.flicker_animation.setKeyValueAt(0.1, random.uniform(0.8, 1.0))  # Slight bounce
            self.flicker_animation.setKeyValueAt(0.2, random.uniform(0.4, 0.8))  # Deeper drop
            self.flicker_animation.setKeyValueAt(0.3, random.uniform(0.9, 1.0))  # Subtle recovery
            self.flicker_animation.setKeyValueAt(0.4, random.uniform(0.0, 0.6))  # Strong flicker
            self.flicker_animation.setKeyValueAt(0.5, random.uniform(0.7, 0.9))  # Stabilizing
            self.flicker_animation.setKeyValueAt(0.6, random.uniform(0.6, 1.0))  # Variation
            self.flicker_animation.setKeyValueAt(0.7, random.uniform(0.2, 0.8))  # Sharp drop
            self.flicker_animation.setKeyValueAt(0.8, random.uniform(0.8, 1.0))  # Back to near full
            self.flicker_animation.setKeyValueAt(0.9, random.uniform(0.7, 1.0))  # Final rise
            self.flicker_animation.setKeyValueAt(1.0, 1.0)  # End at full opacity
        else:
            self.flicker_animation.setKeyValueAt(0.0, 0.15)  # Start at highest opacity
            self.flicker_animation.setKeyValueAt(0.05, random.uniform(0.10, 0.14))  # Slight dimming
            self.flicker_animation.setKeyValueAt(0.1, random.uniform(0.11, 0.15))  # Subtle bounce
            self.flicker_animation.setKeyValueAt(0.2, random.uniform(0.07, 0.12))  # Deeper drop
            self.flicker_animation.setKeyValueAt(0.3, random.uniform(0.12, 0.15))  # Subtle recovery
            self.flicker_animation.setKeyValueAt(0.4, random.uniform(0.06, 0.10))  # Sharp flicker
            self.flicker_animation.setKeyValueAt(0.5, random.uniform(0.10, 0.13))  # Stabilizing
            self.flicker_animation.setKeyValueAt(0.6, random.uniform(0.07, 0.15))  # Variation
            self.flicker_animation.setKeyValueAt(0.7, random.uniform(0.05, 0.09))  # Sharp drop
            self.flicker_animation.setKeyValueAt(0.8, random.uniform(0.08, 0.13))  # Gentle recovery
            self.flicker_animation.setKeyValueAt(0.9, random.uniform(0.12, 0.15))  # Final rise
            self.flicker_animation.setKeyValueAt(1.0, 0.15)  # End at full opacity

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
        
        
        if self.BackgroundColor == "black":
            self.red_offset = random.uniform(-3, 1)#value.x()  # Use x() for red offset
            self.blue_offset = random.uniform(-1, 3) #value.y()  # Use y() for blue offset
            self.yellow_offset = random.uniform(-2, 2)  # Randomize yellow offset
            
        else:
            self.red_offset = random.uniform(-2, 1)#value.x()  # Use x() for red offset
            self.blue_offset = random.uniform(-1, 2) #value.y()  # Use y() for blue offset
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

        """
        Color Seperation
        """
        painter.setOpacity(255)
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

        # Draw the main text
        if self.BackgroundColor == "white":
            painter.setPen(QColor(0, 0, 0, 255)) # Black
        else:
            painter.setPen(QColor(255, 255, 255, 255)) # White
        
        painter.drawText(rect, Qt.AlignCenter, text)


        
        
        """
        CRT TV OVERLAY
        """
        # Control opacity using QPainter
        painter.setOpacity(self._opacity)  # Use the set opacity
        
        # Apply a CRT-like gradient overlay
        # center_x = self.width() / 2
        # center_y = self.height() / 2
        # radius = min(self.width(), self.height()) / 2
        # gradient = QRadialGradient(center_x, center_y, radius)
        
        gradient_CRT_backlight = QLinearGradient(0, 0, 0, self.height())
        
        

        
        if self.BackgroundColor == "black":
            gradient_CRT_backlight.setColorAt(0.5, QColor(255, 255, 255, 10))   # Neutral white in the center
            # gradient_CRT_backlight.setColorAt(0.5, QColor(150, 50, 200, 80))  # Soft blue color
         
        
        if self.colorOverlay == True and self.BackgroundColor == "black":
            gradient_CRT_backlight.setColorAt(0.0, QColor(0, 0, 0, 255))
            gradient_CRT_backlight.setColorAt(1.0, QColor(0, 0, 0, 255))
            # gradient_CRT_backlight.setColorAt(0.0, QColor(20, 20, 20, 30))   # A very dark gray/black, giving the screen depth
            # gradient_CRT_backlight.setColorAt(1.0, QColor(20, 20, 20, 30))   # A very dark gray/black, giving the screen depth
        
        if self.colorOverlay == True and self.BackgroundColor != "black":
            gradient_CRT_backlight.setColorAt(0.0, QColor(200, 255, 150, 255))  # Soft green-yellow at the top
            gradient_CRT_backlight.setColorAt(1.0, QColor(150, 150, 255, 255))  # Soft blue-purple at the bottom  

        
        painter.fillRect(self.rect(), gradient_CRT_backlight)

        # Add scanline effect
        line_desnity_v = 2
        line_desnity_h = 2
        
        
        # Add Horizontal scan lines # linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%),
        for y in range(0, self.height(), line_desnity_v):
            painter.fillRect(0, y, self.width(), 1, QColor(18, 16, 16, 50))  # Less intense scanlines
            
            
        # Add vertical scan lines #  linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        for x in range(0, self.width(), line_desnity_h):

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
