## usage : folder file classify Model
## made by Yuna Bae & Sunghyuk Oh

import sys, os, shutil, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.extensions = ["py", "ipynb", "pdf", 'zip', 'dat', 'csv','ui']
        self.extens = ['분류개수']

        #  분류 폴더 경로 지정
        self.pathlabel = QLabel(" 분류할 폴더 경로 지정 => ")
        self.pathlabel.setStyleSheet("background-color: rgb(226, 255, 208);")
        self.pathedit = QLineEdit(" ")

        #  정리될 폴더 경로 지정
        self.folderlabel = QLabel(" 정리될 폴더 경로 지정 => ")
        self.folderlabel.setStyleSheet("background-color: rgb(226, 255, 208);")
        self.folderedit = QLineEdit(" ")
        #  키워드 분류시 키워드 지정
        self.keylabel = QLabel(" 키워드 분류시 =>            ")
        self.keylabel.setStyleSheet("background-color: rgb(226, 255, 208);")
        self.keyedit = QLineEdit()
        self.keyedit.setText("띄어쓰기 기준")

        self.spaceitem1 = QLabel("  ")
        self.spaceitem2 = QLabel("  ")

        # 분류 방법
        self.cblabel = QLabel("분류 방법 : ")
        self.cb = QComboBox()
        self.cb.setStyleSheet("background-color: rgb(0, 170, 0);")

        self.cb.addItem('확장자별 분류')
        self.cb.addItem('날짜별 분류')
        self.cb.addItem('키워드별 분류')

        # OK 버튼
        self.okbutton = QPushButton("OK")
        self.okbutton.setStyleSheet("font: 75 20pt \"Berlin Sans FB Demi\";\n"
                                    "background-color: rgb(250, 250, 250);")
        # 결과창
        self.resultlbl1 = QLabel(self)
        self.resultlbl2 = QLabel(self)
        self.resultlbl3 = QLabel(self)

        # 테이블
        self.model = QStandardItemModel(12, 3)
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(100, 100, 750, 520)
        self.setWindowTitle("파일 식별기")
        self.okbutton.setMinimumSize(90, 50)

        hbox = QHBoxLayout()

        # 폴더 위젯
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.pathlabel)
        hbox1.addWidget(self.pathedit)

        # 정리 폴더 위젯
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.folderlabel)
        hbox2.addWidget(self.folderedit)

        # 키워드 박스 위젯
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.keylabel)
        hbox3.addWidget(self.keyedit)

        # OK 버튼 위젯
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.spaceitem1)
        hbox4.addWidget(self.spaceitem2)
        hbox4.addWidget(self.cblabel)
        hbox4.addWidget(self.cb)
        hbox4.stretch(1)

        # 분류 박스 위젯
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.okbutton)
        hbox5.stretch(1)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.resultlbl1)
        vbox1.addWidget(self.resultlbl2)
        vbox1.addWidget(self.resultlbl3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addLayout(vbox1)

        # 테이블 뷰 지정
        self.tableView = QTableView()

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.tableView)

        hbox.addLayout(vbox)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

    # 위젯 동작 연결
    def setSlot(self):
        self.okbutton.clicked.connect(self.okClicked)
        return

    # 확장자별 분류 함수
    def ex_classify(self):
        self.model = QStandardItemModel(7, 1)
        self.extensions = ["py", "ipynb", "pdf", 'zip', 'dat', 'csv', 'ui']
        self.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.extens)
        self.model.setVerticalHeaderLabels(self.extensions)

        # 파일 분류 딕셔너리 생성
        self.file_count_dict = {}
        for extension in self.extensions:
            for file in self.file_list:
                if file.endswith(extension):    # 파일의 확장자가 리스트목록에 포함되는지 확인
                    if extension not in self.file_count_dict:
                        self.file_count_dict[extension] = [file]    # 없다면 새로운 딕셔너리 추가
                    else:
                        self.file_count_dict[extension].append(file) # 있다면 기존 딕셔너리에 추가

        # 확장자별 파일 개수 세기 (다른 분류기준도 동일하게 정렬함)
        for yidx, y in enumerate(self.extens):          # 표의 열 값은 분류 개수로(1열)
            for xidx, x in enumerate(self.extensions):  # 표의 행 값은 확장자 리스트로 함(7행)
                try:
                    kk = len(list(self.file_count_dict.values())[xidx])
                    self.model.setData(self.model.index(xidx, yidx),kk)
                    # 파일을 분류했던 딕셔너리 value 값들의 개수를 표에 각각 대입한다

                except:
                    self.model.setData(self.model.index(xidx, yidx),0)
                    # 값이 없다면 해당 표의 값을 0으로 표시

        # 이쪽도 위와 동일하게 딕셔너리의 value 값들의 개수를 표시
        answer = ""
        for i in range(len(self.file_count_dict)):
            answer += f"{list(self.file_count_dict.keys())[i]} extension file : {len(list(self.file_count_dict.values())[i])}개 \n"
        self.tableView.setModel(self.model)

        # 분류할 파일이 없을 때를 따로 가정함
        if answer == "":
            answer = "분류할 파일이 없습니다."
        self.resultlbl2.setText(answer)
        return

    # 생성날짜별 분류 함수
    def time_classify(self):
        self.file_time_dict = {}
        self.flist = []

        # 파일의 생성날짜 분류 딕셔너리 생성
        for file in self.file_list:
            file_time = time.ctime(os.path.getctime(f"{self.file_path}\\{file}"))
            times = file_time.split(" ")    # 파일 내의 시간을 불러와 각각의 데이터를 분리
            times = [x for x in times if x != ""]
            year = times[4]; month = times[1]; day = times[2];  # 각각을 년, 월, 일로 데이터를 분리하고
            str_time = f"{year}_{month}_{day}"                  # 다시 이것을 합쳐서 하나의 변수로 만듦
            if str_time not in self.flist:
                self.flist.append(str_time)
            if str_time not in self.file_time_dict:
                self.file_time_dict[str_time] = [file]
            else:
                self.file_time_dict[str_time].append(file)
        # 딕셔너리안의 시간변수를 정렬함
        self.file_time_dict = sorted(self.file_time_dict.items(), reverse=True)

        self.model = QStandardItemModel(len(self.flist), 1)     # 각각의 날짜별 폴더수로 표의 행렬을 맞춤
        self.model.setHorizontalHeaderLabels(self.extens)
        self.model.setVerticalHeaderLabels(self.flist)

        for yidx, y in enumerate(self.extens):
            for xidx, x in enumerate(self.flist):
                try:
                    kk = len(self.file_time_dict[xidx][1])
                    self.model.setData(self.model.index(xidx, yidx),kk)
                except:
                    self.model.setData(self.model.index(xidx, yidx),0)
        answer = ""
        for i in range(len(self.file_time_dict)):
            answer += f"{self.file_time_dict[i][0]} date created file : {len(self.file_time_dict[i][1])}개 \n"
        if answer == "":
            answer = "분류할 파일이 없습니다."

        self.tableView.setModel(self.model)
        self.resultlbl2.setText(answer)
        return

    # 키워드별 분류 함수
    def keyword_classify(self):
        keyword_text = self.keyedit.text()
        self.keywords = keyword_text.split(" ")     # 키워드를 띄어쓰기를 기준으로 데이터를 분리
        a = len(self.keywords)
        self.model = QStandardItemModel(a, 1)       # 키워드 개수만큼 표의 행렬을 맞춤

        self.keywordlist = []
        self.keyword_dict = {}
        for keyword in self.keywords:
            for file in self.file_list:
                if keyword in file:                 # 키워드가 파일명 안에 있는지 확인
                    if keyword not in self.keyword_dict:    # 나머지는 위의 과정과 동일
                        self.keyword_dict[keyword] = [file]
                    else:
                        self.keyword_dict[keyword].append(file)
            if keyword not in self.keyword_dict.keys():     # 키워드에 해당하는 파일이 없으면
                self.keyword_dict[keyword] = ''      # 딕셔너리 value 값에 공백을 두어
                                                     # 해당 키워드 파일 개수의 값을 0으로 맞추기

        for yidx, y in enumerate(self.extens):
            for xidx, x in enumerate(self.keywords):
                try:
                    kk = len(list(self.keyword_dict.values())[xidx])
                    self.model.setData(self.model.index(xidx, yidx),kk)
                except:
                    self.model.setData(self.model.index(xidx, yidx),0)
        self.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.extens)
        self.model.setVerticalHeaderLabels(self.keywords)
        answer = ""
        for i in range(len(self.keyword_dict)):
            answer += f"{list(self.keyword_dict.keys())[i]} keyword file : {len(list(self.keyword_dict.values())[i])}개 \n"

        if answer == "":
            answer = "분류할 파일이 없습니다."
        self.tableView.setModel(self.model)
        self.resultlbl2.setText(answer)
        return

    # 폴더 분류 함수
    def folder_move(self):
        self.criterion = self.cb.currentText()
        self.folderpath = self.folderedit.text()
        self.folderedit.clear()  # 다음 연속해서 값을 받기위해 위젯 초기화

        # 확장자별 분류 (다른 분류 기준도 비슷한 방식으로 파일분류)
        if self.criterion == "확장자별 분류":
            for extenstion in self.extensions:

                # 분류 폴더 생성
                dir = self.folderpath + "\\" + extenstion
                if not os.path.exists(dir):
                    os.makedirs(dir)    # 자신의 지정한 폴더 안에 폴더를 만들기

                for file in self.file_list:
                    if file.endswith(extenstion):
                        try:
                            shutil.copy(file, self.folderpath + "\\" + file)
                        except:
                            print(f"can't move {file} files")

        # 생성 날짜별 분류
        elif self.criterion== "날짜별 분류":
            for key in self.file_time_dict:
                date = key[0]
                try:
                    dir = self.folderpath + "\\" + date + "\\"
                    if not os.path.exists(dir):
                        os.makedirs(dir)

                    for file in self.file_list:     # 파일의 시간 데이터를 분리하여 새로운 폴더로 만드는 과정은 위와 동일
                        file_time = time.ctime(os.path.getctime(f"{self.file_path}\\{file}"))
                        times = file_time.split(" ")
                        times = [x for x in times if x != ""]
                        year = times[4];
                        month = times[1];
                        day = times[2];
                        str_time = f"{year} {month} {day}"
                        if str_time == date:
                            try:
                                shutil.copy(file, self.folderpath + "\\" + file)
                            except:
                                print(f"can't move {file} files")
                except:
                    print(f"Error: Creating directory. {dir}")

        # 키워드별 분류
        elif self.criterion == "키워드별 분류":
            for i in range(len(self.keyword_dict)):
                dir = self.folderpath + "\\" + list(self.keyword_dict.keys())[i] + "\\"
                if not os.path.exists(dir):
                    os.makedirs(dir)
                files = list(self.keyword_dict.values())[i]
                for file in files:
                    try:
                        shutil.copy(self.file_path + "\\" + file, dir + file)
                    except:
                        print(f"Error: Creating directory. {dir}")
        return

    def okClicked(self):
        # 1. 경로 폴더 가져오기.
        self.file_path = self.pathedit.text()
        # 다음 연속해서 값을 받기위해 위젯 초기화
        self.pathedit.clear()
        self.file_list = os.listdir(self.file_path)
        #  분류할 폴더 위치 사용자 보여주기
        self.resultlbl1.setText(f"{self.file_path} 폴더 파일을 분류하겠습니다.")

        # 2. 폴더 지정 분류 기준으로 분류하기
        self.criterion = self.cb.currentText()      # 콤보박스에서 분류기준 가져오기.
        if self.criterion == "확장자별 분류":
            self.ex_classify()

        elif self.criterion== "날짜별 분류":
            self.time_classify()

        elif self.criterion == "키워드별 분류":
            self.keyword_classify()

        # 3. 분류된 폴더 지정된 폴더로 분류하기
        self.folder_move()
        self.resultlbl3.setText(
            f"{self.file_path} 폴더의 파일 {len(self.file_list)}"
            f"개를 {self.criterion}에 따라 \n \t 지정된 폴더 {self.folderpath}에 분류 완료하였습니다.")
        return

if __name__ == '__main__':
    app = QApplication([])
    ex = main()
    ex.show()
    sys.exit(app.exec_())
