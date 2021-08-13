#!/usr/bin/python3
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView
import sys

app = QApplication(sys.argv)
view = QWebView()
view.show()
view.setUrl(QUrl('http://linuxvoice.com'))
app.exec()

