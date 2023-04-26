from PyQt5 import QtWidgets,uic
import sys

def printt():
    v1=win.lineEdit.text()
    # v2=win.lineEdit2.text()
    # v3=win.lineEdit3.text()
    # v4=win.lineEdit4.text()
    # v5=win.lineEdit5.text()
    # v6=win.lineEdit6.text()
    # v7=win.lineEdit7.text()
    # v8=win.lineEdit8.text()

    print("You are submit ! ! :",v1)
    # print("Enter your Name ! ! :",v2)
    # print("You your Dob! ! :",v3)
    # print("You your Age ! ! :",v4)
    # print("You your Height ! ! :",v5)
    # print("You your weight ! ! :",v6)
    # print("YouBloodPressure ! ! :",v7)
    # print("You Medication  ! ! :",v8)
    # print("You Date  ! ! :",v8)
    # print("You Gender  ! ! :",v8)

app = QtWidgets.QApplication([])
win = uic.loadUi("apt.ui")

win.pushButton_2.clicked.connect(printt)

win.show()
sys.exit(app.exec())