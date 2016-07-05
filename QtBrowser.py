#!/usr/bin/env python

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import * 

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://bakkal.linuxdiyari.com"))
web.show()
web.setWindowTitle('Pisi Linux: BAKKAL')
web.setWindowIcon(QIcon('icon.png')) 
 

sys.exit(app.exec_())
