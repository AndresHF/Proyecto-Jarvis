import sys
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineCore, QtWebEngineWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

from adblockparser import AdblockRules
import threading
import time

# with open(os.getcwd() + "/core/orders/web-operations/easylist.txt") as f:
#     raw_rules = f.readlines()
#     rules = AdblockRules(raw_rules)


class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        # if rules.should_block(url):
        #     # print("block::::::::::::::::::::::", url)
        #     info.block(True)


class ProcessRunnable(QtCore.QRunnable):
    def __init__(self, target, args):
        QtCore.QRunnable.__init__(self)
        self.t = target
        self.args = args

    def run(self):
        self.t(*self.args)

    def start(self):
        QtCore.QThreadPool.globalInstance().start(self)


class HiddenBrowser:
    def __init__(self, url):
        self.url = url
        self.app = QtWidgets.QApplication(sys.argv)
        interceptor = WebEngineUrlRequestInterceptor()
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setRequestInterceptor(
            interceptor
        )
        self.view = QtWebEngineWidgets.QWebEngineView()

    def exec(self):
        self.view.load(QtCore.QUrl(self.url))
        self.view.show()
        # time.sleep(0.1)
        self.app.exec_()
        # QtWidgets.QApplication.processEvents()

    def run(self):

        process = ProcessRunnable(target=self.exec(), args=(self.exec()))
        process.start()


def hiddenBrowser(url):

    app = QtWidgets.QApplication(sys.argv)
    interceptor = WebEngineUrlRequestInterceptor()
    QtWebEngineWidgets.QWebEngineProfile.defaultProfile().setRequestInterceptor(
        interceptor
    )
    view = QtWebEngineWidgets.QWebEngineView()
    view.load(QtCore.QUrl(url))
    view.show()
    app.exec_()


def worker(url):
    thread2 = threading.Thread(target=hiddenBrowser(url), name="youtube")
    thread2.run()
