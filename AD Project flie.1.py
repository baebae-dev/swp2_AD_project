import sys, os, shutil, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 변경사항 : 
#        
# 오류사항 : 분류는 되는데 윈도우 창에 숫자가 뜨지 않음(오류로 윈도우 창이 종료됨)

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.srcDir = "C:\\protest1\\"
        self.desDir = "C:\\protest2\\"
        self.year = ["2018", "2019", "2020"]
        self.years = ["2018년", "2019년","2020년"]
        self.month = ["{0:02}".format(x+1) for x in range(0,12)]
        self.months = ["{0:02}월".format(x+1) for x in range(0,12)]
        self.tv = QTableView(self)
        self.model = QStandardItemModel(12,3)
        self.btnRnd = QPushButton("랜덤파일생성 (200개)")
        self.btnClss1 = QPushButton("파일분류(시간대)")
        self.btnClss2 = QPushButton("파일분류(이름순)")
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
        hbox = QHBoxLayout()
        hbox.addWidget(self.btnClss1)
        hbox.addWidget(self.btnClss2)
        vbox.addLayout(hbox)
        vbox.addWidget(self.tv)
        self.setLayout(vbox)

    def setSlot(self):
        self.btnRnd.clicked.connect(self.rndCrtFile)
        self.btnClss1.clicked.connect(
            lambda s, srcDir = self.srcDir, desDir = self.desDir:
            self.ButtonTime(s, srcDir, desDir))

        self.btnClss2.clicked.connect(
            lambda s, srcDir=self.srcDir, desDir=self.desDir:
            self.ButtonName(s, srcDir, desDir))

    def ButtonTime(self, s, srcDir, desDir):
        fileList = os.listdir(srcDir)

        for name in fileList:
            y = name[5:9]+"년"
            m = name[10:12]+"월"

            export = desDir + y + '\\' + m
            if not os.path.isdir(export):
                os.makedirs(export)
            shutil.copyfile(srcDir + name, export + '\\' + name)

        for yidx, y in enumerate(self.years):
            for midx, m in enumerate(self.months):
                self.model.setData(self.model.index(midx, yidx),
                                   len(os.listdir(self.desDir + y + '\\' + m)))

    def ButtonName(self, s, srcDir, desDir): # 구현 아직 못함 ㅠ
        fileList = os.listdir(srcDir)

        for name in fileList:
            t = name[0:3]

            export = desDir + t
            if not os.path.isdir(export):
                os.makedirs(export)
            shutil.copyfile(srcDir + name, export + '\\' + name)

    def rndCrtFile(self):
        for i in range(200):
            y = random.randint(2018, 2020)
            m = random.randint(1,12)
            d = random.randint(1, 30)
            tmp = random.randrange(999)
            txd = ""
            for _ in range(4):                    # 파일의 이름을 기준으로 구분하는 방법?
                txd += chr(random.randint(97,122))
            f = open(self.srcDir + "{0}_{1}-{2:02}-{3:02}({4}).txt".format(txd, y, m, d, tmp), "w")
            # f = open(self.srcDir + "test_{0}-{1:02}-{2:02}({3}).txt".format(y, m, d, tmp), "w")
            f.close()

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())












