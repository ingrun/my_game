#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt, QPoint, QRect

import win32api

from MyQr import MyQr
from write_conf import write_ini, read_conf


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__(flags=Qt.WindowFlags())
        self.GAME_LIST = read_conf()

        z_quit = QAction("退出", self, triggered=self.exit)
        z_save_xy = QAction("保存位置", self, triggered=self.save_xy)
        z_show_window = QAction("显示主界面", self, triggered=self.show_window)

        self.trayIconMenu = QMenu(self)

        self.trayIconMenu.addAction(z_show_window)
        self.trayIconMenu.addAction(z_save_xy)
        self.trayIconMenu.addAction(z_quit)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("img/ingrun.png"))
        self.tray_icon.setContextMenu(self.trayIconMenu)
        self.tray_icon.show()
        self.tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.icon_activated)

        self.init_ui()

    def init_ui(self):
        data = QPoint(10, 5)
        k = 10
        for i in self.GAME_LIST:
            btn1 = QPushButton(i['game_name'], self)
            btn1.move(data)
            btn1.setFixedWidth(220)
            data.setY(data.y() + k + btn1.height())
            btn1.clicked.connect(self.button_clicked)

        qr = MyQr()
        qr.set_h(data.y() + 10)
        self.setGeometry(qr)
        self.setWindowTitle('My_Game')

        self.setFixedSize(self.width(), self.height())
        self.show()

    def button_clicked(self):
        sender = self.sender()
        for i in self.GAME_LIST:
            if sender.text() == i['game_name']:
                # os.system(i['path'])
                win32api.ShellExecute(0, 'open', i['path'], '', '', 1)

    def save_xy(self):
        xy = self.pos()
        file_data = 'QPoint_x=' + str(xy.x() + 1) +'\nQPoint_y=' + str(xy.y() + 31)
        write_ini(file_data)

    def closeEvent(self, event):
        event.ignore()  # 忽isVisible略关闭事件
        self.hide()  # 隐藏窗口

    def show_window(self):
        self.show()

    def exit(self):
        sys.exit(self)

    def icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
