
import sys, os, shutil, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# What To Do : 1. 결과 표로 보이게 생성 2. 테이블 생성(버튼 눌렀을때)
# 수정해야 할 것 : 


class main(QWidget):
    def __init__(self):
        super().__init__()
        # self.srcDir = "/Users/baeyuna/Documents/univ/swp2/12-1"
        self.extensions = ["py", "ipynb", "pdf", 'zip', 'dat', 'csv','ui']
        self.extens = ['분류개수']
        #  분류 폴더 경로 지정
        self.pathlabel = QLabel(" 분류할 폴더 경로 지정 => ")
        self.pathedit = QLineEdit("C:\\protest1\\")
        #  정리될 폴더 경로 지정
        self.folderlabel = QLabel(" 정리될 폴더 경로 지정 => ")
        self.folderedit = QLineEdit("C:\\protest2\\")
        # 분류 방법
        self.cblabel = QLabel("분류 방법 : ")


        self.keylabel = QLabel(" 키워드 분류시 =>            ")
        self.keyedit = QLineEdit()
        self.keyedit.setText("띄어쓰기 기준")

        self.spaceitem1 = QLabel("  ")
        self.spaceitem2 = QLabel("  ")

        self.cb = QComboBox()
        self.cb.addItem('확장자별 분류')
        self.cb.addItem('날짜별 분류')
        self.cb.addItem('키워드별 분류')
        # OK 버튼
        self.okbutton = QPushButton("OK")
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
        self.setGeometry(100, 100, 920, 520)
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

        self.file_count_dict = {}
        for extension in self.extensions:
            for file in self.file_list:
                if file.endswith(extension):
                    if extension not in self.file_count_dict:
                        self.file_count_dict[extension] = [file]
                    else:
                        self.file_count_dict[extension].append(file)

        for yidx, y in enumerate(self.extens):
            for xidx, x in enumerate(self.extensions):
                try:
                    kk = len(list(self.file_count_dict.values())[xidx])
                    self.model.setData(self.model.index(xidx, yidx),kk)
                except:
                    self.model.setData(self.model.index(xidx, yidx),0)

        answer = ""
        for i in range(len(self.file_count_dict)):
            answer += f"{list(self.file_count_dict.keys())[i]} extension file : {len(list(self.file_count_dict.values())[i])}개 \n"
        self.tableView.setModel(self.model)
        self.resultlbl2.setText(answer)
        return

    # 생성날짜별 분류 함수
    def time_classify(self):
        self.model = QStandardItemModel(12, 3)
        self.years = ["2018년", "2019년", "2020년"]
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.years)
        self.model.setVerticalHeaderLabels(self.months)
        self.file_time_dict = {}
        for file in self.file_list:
            file_time = time.ctime(os.path.getctime(f"{self.file_path}/{file}"))
            times = file_time.split(" ")
            year = times[4]; month = times[1]; day = times[2];
            str_time = f"{year}_{month}_{day}"
            if str_time not in self.file_time_dict:
                self.file_time_dict[str_time] = [file]
            else:
                self.file_time_dict[str_time].append(file)
        self.file_time_dict = sorted(self.file_time_dict.items(), reverse=True)

        for yidx, y in enumerate(self.years):
            for xidx, x in enumerate(self.months):
                try:
                    kk = len(self.file_time_dict[xidx][1])
                    self.model.setData(self.model.index(xidx, yidx),kk)
                except:
                    self.model.setData(self.model.index(xidx, yidx),0)
        answer = ""
        for i in range(len(self.file_time_dict)):
            answer += f"{self.file_time_dict[i][0]} date created file : {len(self.file_time_dict[i][1])}개 \n"

        self.tableView.setModel(self.model)
        self.resultlbl2.setText(answer)
        return

    # 키워드별 분류 함수
    def keyword_classify(self):
        keyword_text = self.keyedit.text()
        self.keywords = keyword_text.split(" ")
        a = len(self.keywords)
        self.model = QStandardItemModel(a, 1)
        self.tableView.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.extens)
        self.model.setVerticalHeaderLabels(self.keywords)

        self.keyword_dict = {}
        for keyword in self.keywords:
            for file in self.file_list:
                if keyword in file:
                    if keyword not in self.keyword_dict:
                        self.keyword_dict[keyword] = [file]
                    else:
                        self.keyword_dict[keyword].append(file)

        for yidx, y in enumerate(self.extens): # 오류 있음 (찾는 파일이 0개일 때)
            for xidx, x in enumerate(self.keywords):
                try:
                    kk = len(list(self.keyword_dict.values())[xidx])
                    if kk == 0:
                        continue
                    self.model.setData(self.model.index(xidx, yidx),kk)
                except:
                    self.model.setData(self.model.index(xidx, yidx),0)

        answer = ""
        for i in range(len(self.keyword_dict)):
            answer += f"{list(self.keyword_dict.keys())[i]} keyword file : {len(list(self.keyword_dict.values())[i])}개 \n"

        self.tableView.setModel(self.model)
        self.resultlbl2.setText(answer)
        return

    # 폴더 분류 함수
    def folder_move(self):
        self.criterion = self.cb.currentText()
        self.folderpath = self.folderedit.text()
        self.folderedit.clear()  # 다음 연속해서 값을 받기위해 위젯 초기화

        # 확장자별 분류
        if self.criterion == "확장자별 분류":
            for extenstion in self.extensions:
                # 분류 폴더 생성
                dir = self.folderpath + "\\" + extenstion
                try:
                    dir = self.folderpath + "\\" + extenstion
                    os.makedirs(dir)
                    for file in self.file_list:
                        if file.endswith(extenstion):
                            shutil.copy(file, self.folderpath+"\\"+file)
                except:
                    print(f"Error: Creating directory. {dir}")

        # 생성 날짜별 분류
        elif self.criterion== "날짜별 분류":
            for key in self.file_time_dict:
                date = key[0]
                dir = self.folderpath + "\\" + date
                try:
                    os.makedirs(dir)
                    for file in self.file_list:
                        file_time = time.ctime(os.path.getctime(f"{self.file_path}/{file}"))
                        times = file_time.split(" ")
                        year = times[4];
                        month = times[1];
                        day = times[2];
                        str_time = f"{year} {month} {day}"
                        if str_time == date:
                            shutil.copy(file, self.folderpath+"/"+file)
                except:
                    print(f"Error: Creating directory. {dir}")

        # 키워드별 분류
        elif self.criterion == "키워드별 분류":
            for i in range(len(self.keyword_dict)):
                dir = self.folderpath + "\\" + list(self.keyword_dict.keys())[i]
                try:
                    os.makedirs(dir)
                    files = self.keyword_dict.values()[i]
                    for file in files:
                        shutil.copy(file, self.folderpath+"\\"+file) # self.file_path+"/"+
                except:
                    print(f"Error: Creating directory. {dir}")

        return

    def okClicked(self):
        # 1. 경로 폴더 가져오기.
        self.file_path = self.pathedit.text() # 지정된 폴더 경로 가져오기.
        self.pathedit.clear() # 다음 연속해서 값을 받기위해 위젯 초기화
        self.file_list = os.listdir(self.file_path) # 해당 지정 경로의 파일 리스트 가져오기.
        self.resultlbl1.setText(f"{self.file_path} 폴더 파일을 분류하겠습니다.")  #  분류할 폴더 위치 사용자 보여주기

        # 2. 폴더 지정 분류 기준으로 분류하기
        self.criterion = self.cb.currentText() # 분류기준 가져오기.
        if self.criterion == "확장자별 분류":
            self.ex_classify()

        elif self.criterion== "날짜별 분류":
            self.time_classify()

        elif self.criterion == "키워드별 분류":
            self.keyword_classify()

        # 3. 분류된 폴더 지정된 폴더로 분류하기
        self.folder_move()
        self.resultlbl3.setText(
            f"{self.file_path} 폴더의 파일 {len(self.file_list)}개를 {self.criterion}에 따라 \n \t 지정된 폴더 {self.folderpath}에 분류 완료하였습니다.")
        # 4. Table view showing
        if self.criterion== "날짜별 분류":
           pass

        return

if __name__ == '__main__':
    app = QApplication([])
    ex = main()
    ex.show()
    sys.exit(app.exec_())
