from PyQt5.QtCore import QRect

from write_conf import read_ini


class MyQr(QRect):

    x: int = 300
    y: int = 300
    w: int = 245
    h: int = 100

    def __init__(self):

        q_point = read_ini()
        self.x = q_point.x()
        self.y = q_point.y()

        super().__init__(self.x, self.y, self.w, self.h)

    def set_w(self, w):
        self.w = w
        super().setWidth(w)

    def set_h(self, h):
        self.h = h
        super().setHeight(h)
