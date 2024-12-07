import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt

class ClickableLabel(QLabel):
    """Custom QLabel that emits a signal when clicked."""
    def __init__(self, text, clipboard):
        super().__init__(text)
        self.clipboard = clipboard

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Copy the text to the clipboard
            font_name = self.text().replace("Font: ", "")
            self.clipboard.setText(font_name)
            print(f"Copied to clipboard: {font_name}")

def show_fonts():
    app = QApplication(sys.argv)

    # Get the system clipboard
    clipboard = app.clipboard()
    
    # Get the available fonts
    font_db = QFontDatabase()
    available_fonts = font_db.families()

    # Create a window
    window = QWidget()
    window.setWindowTitle("Available Fonts")

    # Create a vertical layout to hold the labels
    layout = QVBoxLayout()

    # Loop through each available font and create a clickable label for it
    for font_name in available_fonts:
        label = ClickableLabel(f"Font: {font_name}", clipboard)
        label.setFont(QFont(font_name, 12))  # Set font style and size
        layout.addWidget(label)

    # Create a scroll area and set the layout
    scroll_area = QScrollArea()
    scroll_widget = QWidget()  # Create a widget to contain the layout
    scroll_widget.setLayout(layout)
    
    # Set the scroll area to contain the widget with the layout
    scroll_area.setWidget(scroll_widget)
    scroll_area.setWidgetResizable(True)  # Make the scroll area resize with the window

    # Set the scroll area as the main layout of the window
    main_layout = QVBoxLayout()
    main_layout.addWidget(scroll_area)
    window.setLayout(main_layout)

    # Resize window to fit the content (the scrollable content will expand)
    window.resize(600, 800)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    show_fonts()

