from PyQt5.QtCore import QPoint


def read_conf() -> list:
    with open("conf/my_game.conf", "r", encoding="utf-8") as f:
        info = f.read()
        return eval(info)

def write_conf(file_data: str):
    with open('conf/my_game.conf', "w", encoding="utf-8") as f:
        f.write(str(file_data))

def read_ini() -> QPoint:
    with open('conf/QPoint.ini', "r", encoding="utf-8") as f:
        return QPoint(int(f.readline().split('=')[1]), int(f.readline().split('=')[1]))

def write_ini(file_data: str):
    with open('conf/QPoint.ini', "w", encoding="utf-8") as f:
        f.write(str(file_data))
