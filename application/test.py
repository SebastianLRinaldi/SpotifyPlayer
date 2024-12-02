import sys
import webview  # PyWebView
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QEventLoop

class WebViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 + PyWebView Integration")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Initialize PyWebView
        self.webview = webview.create_window("Webview", "https://example.com", frameless=False, easy_drag=True)

        # Access native QWebEngineView after pywebview loads
        webview.start(self._add_webview_to_layout, debug=False)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

    def _add_webview_to_layout(self):
        """Callback to add the QWebEngineView to the PyQt5 layout."""
        print(dir( webview.windows[0]))
        native_view = webview.native  # Attempt to access the native view
        print(f"Native View: {native_view}")
        if native_view:
            self.layout.addWidget(native_view)  # Embed the native view into the PyQt layout
        else:
            print("Native view is not available.")
        # """Add the native QWebEngineView to PyQt5 layout."""
        # print("Addded")
        # qwebview = self.webview  # Get native QWebEngineView
        # print(dir(qwebview))
        # self.layout.addWidget(qwebview)  # Add QWebEngineView to layout

# Main application loop
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = WebViewWindow()
    main_window.show()
    sys.exit(app.exec_())
