import sys, os, shutil, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 변경사항 : 윈도우 창의 환경 개선(글자 나타내기),
#           파일에 랜덤이름을 붙여넣기 + 년도별로 구분까지 할 수 있다.
# 오류사항 : 분류는 되는데 윈도우 창에 숫자가 뜨지 않음(오류로 윈도우 창이 종료됨)

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.srcDir = "C:\\protest1\\"
        self.desDir = "C:\\protest2\\"
        self.year = ["2018", "2019", "2020"]
        self.years = [" 2018년 ", " 2019년 "," 2020년 "]
        self.month = ["{0:02}".format(x+1) for x in range(0,12)]
        self.months = [" {0}월 ".format(x+1) for x in range(0,12)]
        self.tv = QTableView(self)
        self.model = QStandardItemModel(12,3)
        self.btnRnd = QPushButton("랜덤파일생성 (100개)")
        self.btnClss = QPushButton("파일분류")
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300, 300, 450, 600)
        self.setWindowTitle("파일 식별기")

        self.tv.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.years)
        self.model.setVerticalHeaderLabels(self.months)
        vbox = QVBoxLayout()
        vbox.addWidget(self.btnRnd)
        vbox.addWidget(self.btnClss)
        vbox.addWidget(self.tv)
        self.setLayout(vbox)

    def setSlot(self):
        self.btnRnd.clicked.connect(self.rndCrtFile)
        self.btnClss.clicked.connect(
            lambda s, srcDir = self.srcDir, desDir = self.desDir:
            self.classify(s, srcDir, desDir))

    def classify(self, s, srcDir, desDir):
        fileList = os.listdir(srcDir)

        for name in fileList:
            y = name[5:9]
            m = name[10:12]

            export = desDir + y + "/" + m
            if not os.path.isdir(export):
                os.makedirs(export)
            shutil.copyfile(srcDir + name, export + "/" + name)

        for yidx, y in enumerate(self.year):    # 오류사항 2
            for midx, m in enumerate(self.month):
                self.model.setData(self.model.index(midx, yidx),
                                   len(os.listdir(self.desDir + y + "/" + m))) # 오류사항 1

    def rndCrtFile(self):
        for i in range(100):
            y = random.randint(2018, 2020)
            m = random.randint(1,12)
            d = random.randint(1, 30)
            tmp = random.randrange(999)
            # txd = ""
            # for _ in range(4):                    # 파일의 이름을 기준으로 구분하는 방법?
            #     txd += chr(random.randint(97,122))
            # f = open(self.srcDir + "{0}_{1}-{2:02}-{3:02}({4}).txt".format(txd, y, m, d, tmp), "w")
            f = open(self.srcDir + "test_{0}-{1:02}-{2:02}({3}).txt".format(y, m, d, tmp), "w")
            f.close()

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())












