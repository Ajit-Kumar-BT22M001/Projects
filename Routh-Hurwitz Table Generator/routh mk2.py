from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem
from routh_hurwitz import RouthHurwitz, ToLaTeX, exprArrToStrArr

class RouthApp(QWidget):
    def __init__(self):
        super().__init__()

        self.polynomial = []
        self.routhArray = []
        self.latexRouthArray = []

        self.initUI()

    def initUI(self):
        # create widgets
        titleLabel = QLabel('<h1>Routh-Hurwitz App</h1>')
        introLabel = QLabel('Enter the coefficients of the polynomial separated by commas in ascending order of degree.')
        polynomialLabel = QLabel('Polynomial:')
        self.polynomialInput = QLineEdit()

        computeButton = QPushButton('Compute')
        computeButton.clicked.connect(self.computeRouthArray)

        self.latexOutput = QTextEdit()
        self.latexOutput.setReadOnly(True)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Coefficients', 'Even Terms', 'Odd Terms'])

        # layout widgets
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(polynomialLabel)
        inputLayout.addWidget(self.polynomialInput)

        outputLayout = QVBoxLayout()
        outputLayout.addWidget(computeButton)
        outputLayout.addWidget(self.latexOutput)
        outputLayout.addWidget(self.tableWidget)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(introLabel)
        mainLayout.addLayout(inputLayout)
        mainLayout.addLayout(outputLayout)

        # set main layout
        self.setLayout(mainLayout)

        # set window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Routh-Hurwitz App')
        self.show()
    
    def computeRouthArray(self):
        polynomialText = self.polynomialInput.text()
        polynomialArr = polynomialText.split(',')
        polynomialArr = [x.strip() for x in polynomialArr]

        try:
            self.routhArray = RouthHurwitz(polynomialArr)

            # clear and set up table widget
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(len(self.routhArray[0]))
            self.tableWidget.setRowCount(len(self.routhArray))
            self.tableWidget.setHorizontalHeaderLabels([''] * len(self.routhArray[0]))
            self.tableWidget.setVerticalHeaderLabels([''] * len(self.routhArray))

            # populate table widget
            for i in range(len(self.routhArray)):
                for j in range(len(self.routhArray[i])):
                    item = QTableWidgetItem(str(self.routhArray[i][j]))
                    self.tableWidget.setItem(i, j, item)
        except Exception as e:
            self.tableWidget.clear()
            self.tableWidget.setRowCount(1)
            item = QTableWidgetItem('Error: ' + str(e))
            self.tableWidget.setItem(0, 0, item)


if __name__ == '__main__':
    app = QApplication([])
    ex = RouthApp()
    app.exec_()
