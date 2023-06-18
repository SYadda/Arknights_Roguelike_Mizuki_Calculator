import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_MainWindow


class login_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(login_window, self).__init__(parent)
        self.setupUi(self)

    def calculate(self):
        选手名字 = self.lineEdit.text()

        游戏内结算得分 = self.sb_1.value()

        开局分队 = self.rb_1.isChecked() * (-50) * self.sb_2.value() + self.rb_2.isChecked() * 40 + self.rb_4.isChecked() * 40 + self.rb_5.isChecked() * 250 + self.rb_6.isChecked() * 150

        结局 = self.rb_9.isChecked() * 450 + self.rb_10.isChecked() * 50 + self.rb_11.isChecked() * 700

        临时招募 = self.sb_3.value() * 50 + self.sb_4.value() * 30 + self.sb_5.value() * 20

        紧急关卡 = self.cb_1.isChecked() * 30 + self.cb_2.isChecked() * 30 + \
                   self.cb_3.isChecked() * 40 + self.cb_4.isChecked() * 40 + \
                   self.cb_5.isChecked() * 40 + self.cb_6.isChecked() * 40 + \
                   self.cb_7.isChecked() * 60 + self.cb_8.isChecked() * 60 + \
                   self.cb_9.isChecked() * 50 + self.cb_10.isChecked() * 50 + \
                   self.cb_11.isChecked() * 100 + self.cb_12.isChecked() * 100 + \
                   self.cb_13.isChecked() * 60 + self.cb_14.isChecked() * 60 + \
                   self.cb_15.isChecked() * 60 + self.cb_16.isChecked() * 60 + \
                   self.cb_17.isChecked() * 90 + self.cb_18.isChecked() * 90 + \
                   self.cb_19.isChecked() * 150 + self.cb_20.isChecked() * 150 + \
                   self.cb_21.isChecked() * 90 + self.cb_22.isChecked() * 90 + \
                   self.cb_23.isChecked() * 50 + self.cb_24.isChecked() * 50 + \
                   self.cb_25.isChecked() * 70 + self.cb_26.isChecked() * 70 + \
                   self.cb_27.isChecked() * 150 + self.cb_28.isChecked() * 150 + \
                   self.cb_29.isChecked() * 80 + self.cb_30.isChecked() * 80

        隐藏关卡 = self.cb_31.isChecked() * 50 + self.cb_32.isChecked() * 100 + \
                   self.cb_33.isChecked() * 80 + self.cb_34.isChecked() * 120 + \
                   self.cb_35.isChecked() * 30 + self.cb_36.isChecked() * 40 + \
                   self.cb_37.isChecked() * 50 + \
                   self.cb_38.isChecked() * (20 + self.rb_13.isChecked() * 50 + self.rb_15.isChecked() * 50)

        奇境BOSS = self.rb_17.isChecked() * 120 + self.rb_18.isChecked() * 150 + self.rb_19.isChecked() * 230

        击杀鸭狗熊 = (self.sb_6.value() + self.sb_7.value() + self.sb_8.value()) * 20

        收藏品 = self.sb_9.value() * 10

        启示 = self.sb_10.value() * 50

        if self.rb_3.isChecked() and self.rb_10.isChecked():
            self.label_show.setText('禁止使用心胜于物分队\n完成大蒂结局！')
        else:
            self.label_show.setText('选手: ' + 选手名字 + '\n最终得分: ' + str(游戏内结算得分 + 开局分队 + 结局 + 临时招募 + 紧急关卡 + 隐藏关卡 + 奇境BOSS + 击杀鸭狗熊 + 收藏品 + 启示))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    first_window = login_window()
    first_window.show()
    sys.exit(app.exec_())
