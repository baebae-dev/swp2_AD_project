import sys, os, shutil, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.srcDir = "/Users/baeyuna/Documents/univ/swp2/ad/files/"
        self.desDir = "/Users/baeyuna/Documents/univ/swp2/ad/files/"
        self.year = ["2019", "2020", "2021"]
        self.month = ["{0:02}".format(x+1) for x in range(0,12)]
        self.tv = QTableView(self)
        self.model = QStandardItemModel(12,3)
        self.btnRnd = QPushButton("랜덤파일생성(1000)")
        self.btnClss = QPushButton("파일분류")
        self.setUi()
        self.setSlot()

    def setUi(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("QTableView")

        self.tv.setModel(self.model)
        self.model.setHorizontalHeaderLabels(self.year)
        self.model.setVerticalHeaderLabels(self.month)
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

        for yidx, y in enumerate(self.year):
            for midx, m in enumerate(self.month):
                self.model.setData(self.model.index(midx, yidx),
                                   len(os.listdir(self.desDir + y+ "/" + m)))

    def rndCrtFile(self):
        for i in range(1000):
            y = random.randint(2019, 2021)
            m = random.randint(1,12)
            d = random.randint(1, 30)
            tmp = random.randrange(9999)
            f = open(self.srcDir + "test_{0}-{1:02}-{2:02}({3}).txt".format(y, m, d, tmp), "w")
            f.close()

app = QApplication([])
ex = main()
ex.show()
sys.exit(app.exec_())












