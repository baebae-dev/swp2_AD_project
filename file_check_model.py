## usage : folder file classify Model
## made by Yuna Bae.

import sys, os, shutil, random, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 변경사항 : 1. 구분 기준 (날짜 -> 파일 확장자별?) & 생성 날자별 (기존 파일명에 날짜를 넣어 랜덤하게 생성 -> 파일 정보상의 생성 날짜를 가져와 자동 분류해줌)
#          2. 폴더 path 입력 받기
#          3. 분류된 파일, 군집 별로 폴더 생성 후 폴더 안에 저장

# What To Do : 1. 결과 표로 보이게 생성


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
        self.btnmove = QPushButton("분류 폴더생성")
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
        vbox2.addWidget(self.btnmove)
        vbox2.addWidget(self.pathlbl)
        vbox2.addWidget(self.resultlbl)

        vbox = QVBoxLayout()
        vbox.addLayout(vbox1)
        vbox.addLayout(hbox)
        vbox.addLayout(vbox2)
        self.setLayout(vbox)

    def pathClicked(self):
        self.file_path = self.pathedit.text()
        self.pathedit.clear()
        self.file_list = os.listdir(self.file_path)
        self.pathlbl.setText(f"{self.file_path} 폴더 파일을 분류하겠습니다.")
        return

    def setSlot(self):
        self.searchbutton.clicked.connect(self.pathClicked)
        self.btnClss.clicked.connect(self.classify)
        self.btnClss2.clicked.connect(self.check_publishtime)
        self.btnmove.clicked.connect(self.folder_move)
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
            file_time = time.ctime(os.path.getctime(f"{self.file_path}/{file}"))
            times = file_time.split(" ")
            year = times[4]; month = times[1]; day = times[2];
            str_time = f"{year} {month} {day}"
            if str_time not in self.file_time_dict:
                self.file_time_dict[str_time] = 1
            else:
                self.file_time_dict[str_time] += 1
        self.file_time_dict = sorted(self.file_time_dict.items(), reverse=True)

        answer = ""
        for i in range(len(self.file_time_dict)):
            answer += f"{self.file_time_dict[i][0]}에 생성한 파일이 {self.file_time_dict[i][1]}개 존재합니다. \n"

        self.resultlbl.setText(answer)
        return

    # 폴더 생성 및 분류
    def folder_move(self):
        # 확장자별 분류
        if len(self.resultlbl.text().split(" ")) == 3:
            for extenstion in self.extensions:
                try:
                    dir = self.file_path + "/" + extenstion
                    os.makedirs(dir)
                    for file in self.file_list:
                        if file.endswith(extenstion):
                            shutil.move(self.file_path+"/"+file, dir+"/"+file)
                except:
                    print(f"Error: Creating directory. {dir}")

        # 생성 날짜별 분류
        else:
            for key in self.file_time_dict:
                date = key[0]
                try:
                    dir = self.file_path + "/" + date
                    os.makedirs(dir)
                    for file in self.file_list:
                        file_time = time.ctime(os.path.getctime(f"{self.file_path}/{file}"))
                        times = file_time.split(" ")
                        year = times[4];
                        month = times[1];
                        day = times[2];
                        str_time = f"{year} {month} {day}"
                        if str_time == date:
                            shutil.move(self.file_path+"/"+file. dir+"/"+file)
                except:
                    print(f"Error: Creating directory. {dir}")



if __name__ == '__main__':
    app = QApplication([])
    ex = main()
    ex.show()
    sys.exit(app.exec_())