#!/usr/bin/env python3
"""
demonstration of Qt5 QtWebEngineWidget for use as a 'standalone'
window for local web apps
"""

import sys
import argparse
import subprocess

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


parser = argparse.ArgumentParser()
parser.add_argument(
    'url',
    type=str,
    help='url to host')


def main():
    args = parser.parse_args()

    app = QApplication(sys.argv)

    browser = QWebEngineView()
    browser.load(QUrl(args.url))
    browser.show()

    app.exec_()  # this will block until the window is closed
    
    # shutdown the server
    subprocess.run(["jupyter", "notebook", "stop"])

    sys.exit()


if __name__ == "__main__":
    main()

