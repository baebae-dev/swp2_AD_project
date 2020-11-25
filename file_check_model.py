## usage : folder file classify Model
## made by Yuna Bae.

import sys, os, shutil, random, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 변경사항 : 1. 구분 기준 (날짜 -> 파일 확장자별?)
#          2. 폴더 path 입력 받기

class main(QWidget):
    def __init__(self):
        super().__init__()
        # self.srcDir = "/Users/baeyuna/Documents/univ/swp2/12-1"
        self.extensions = [".py", ".ipynb", ".pdf", 'zip', 'dat', 'csv']
        self.pathedit = QLineEdit()
        self.pathlbl = QLabel(self)
        self.pathedit.setText("                                                                 분류할 폴더 경로를 입력하세요. ")
        self.searchbutton = QPushButton("경로지정")
        self.btnClss = QPushButton("확장자 파일분류")
        self.btnClss2 = QPushButton("생성날짜 파일분류")
        self.resultlbl = QLabel(self)
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300, 300, 700, 400)
        self.setWindowTitle("파일 식별기")

        # self.tv.setModel(self.model)
        # self.table.setColumnCount(len(self.extensions))
        # self.table.setRowCount(1)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.pathedit)
        vbox1.addWidget(self.searchbutton)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btnClss)
        hbox.addWidget(self.btnClss2)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.pathlbl)
        vbox2.addWidget(self.resultlbl)

        vbox = QVBoxLayout()
        vbox.addLayout(vbox1)
        vbox.addLayout(hbox)
        vbox.addLayout(vbox2)
        self.setLayout(vbox)

    def pathClicked(self):
        self.file_path = self.pathedit.text()
        self.file_list = os.listdir(self.file_path)
        self.pathlbl.setText(f"{self.file_path} 폴더 파일을 분류하겠습니다.")
        return

    def setSlot(self):
        self.searchbutton.clicked.connect(self.pathClicked)
        self.btnClss.clicked.connect(self.classify)
        self.btnClss2.clicked.connect(self.check_publishtime)
        return

    def classify(self):
        self.file_count_dict = dict(zip(self.extensions, [0]*len(self.extensions)))
        for extension in self.extensions:
            file_num = len([file for file in self.file_list if file.endswith(extension)])
            self.file_count_dict[extension] = file_num

        answer = ""
        for i in range(len(self.file_count_dict)):
            answer += f"{list(self.file_count_dict.values())[i]}개의 {list(self.file_count_dict.keys())[i]}가 존재합니다. \n"

        self.resultlbl.setText(answer)
        return

    def check_publishtime(self):
        self.file_time_dict = {}
        for file in self.file_list:
            file_time = time.ctime(os.path.getctim(f"{self.file_path}/{file}"))
            if file_time not in self.file_time_dict:
                self.file_time_dict[file_time] = 1
            else:
                self.file_time_dict[file_time] += 1
        self.file_time_dict = sorted(self.file_time_dict.items(), reverse=True)
        self.filetimelbl.setText(self.file_time_dict)

        answer = ""
        for i in range(len(self.file_time_dict)):
            answer += f"{list(self.file_time_dict.values())[i]}개의 {list(self.file_time_dict.keys())[i]}가 존재합니다. \n"

        self.resultlbl.setText(answer)
        return


if __name__ == '__main__':
    app = QApplication([])
    ex = main()
    ex.show()
    sys.exit(app.exec_())