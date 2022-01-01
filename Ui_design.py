from PyQt5 import QtCore, QtWidgets
from CART import load_model
from PyQt5.QtWidgets import QWidget, QFileDialog, QTableWidgetItem
import numpy as np
from vail_and_test import run


class Ui_Form(QWidget):
    def setupUi(self, Form):
        # self.data
        self.model = load_model()
        print(self.model)
        Form.setObjectName("Form")
        Form.resize(678, 574)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 250, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.load)
        self.TableWidget = QtWidgets.QTableWidget(Form)
        self.TableWidget.setGeometry(QtCore.QRect(140, 20, 531, 221))
        self.TableWidget.setObjectName("TableView")
        self.TableWidget.setHorizontalHeaderLabels(["输入栈", "剩余输入串", "所用表达式", "动作"])
        self.TableWidget.horizontalHeader().setSectionsClickable(False)
        self.TableWidget_2 = QtWidgets.QTableWidget(Form)
        self.TableWidget_2.setGeometry(QtCore.QRect(20, 330, 531, 221))
        self.TableWidget_2.setObjectName("TableView_2")
        self.TableWidget_3 = QtWidgets.QTableWidget(Form)
        self.TableWidget_3.setGeometry(QtCore.QRect(570, 330, 91, 221))
        self.TableWidget_3.setObjectName("TableView_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(590, 300, 61, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "开始预测"))
        self.pushButton_2.setText(_translate("Form", "导入excel"))
        self.label.setText(_translate("Form", "预测结果"))

    def predict(self):
        result = []
        n, m = np.shape(self.data)
        for i in range(n):
            result.append(run(self.data[i, :], self.model, 0))
        self.TableWidget_2.setHorizontalHeaderLabels(["平均气压", "日最低气压", "平均气温",
                                                      "日最低气温", "平均相对湿度", "最大风速", "日照时数", "平均地表气温", "日最低地表气温"])
        self.TableWidget_2.setColumnCount(m)
        self.TableWidget_2.setRowCount(n)
        for row in range(n):
            for column in range(m):
                self.TableWidget_2.setItem(row, column, QTableWidgetItem(str(self.data[row, column])))
        self.TableWidget_3.setColumnCount(1)
        self.TableWidget_3.setRowCount(n)
        for row in range(n):
            self.TableWidget_3.setItem(row, 0, QTableWidgetItem(result[row]))

    def load(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Excel (*.csv *.xlsx *.xls);;Text files (*.txt);;XML files (*.xml);;all file(*)")
        with open(fileName, encoding='utf-8') as f:
            data = np.loadtxt(f, delimiter=",")
        data_n, data_m = np.shape(data)
        self.data = data
        print(data)
        self.TableWidget.setHorizontalHeaderLabels(['平均气压', '日最低气压', '平均气温', '日最低气温', '平均相对湿度', '最大风速', '日照时数', '平均地表气温', '日最低地表气温' ])
        self.TableWidget.setColumnCount(data_m)
        self.TableWidget.setRowCount(data_n)
        print(data_n, data_m)
        for row in range(data_n):
            for column in range(data_m):
                self.TableWidget.setItem(row, column, QTableWidgetItem(str(data[row, column])))
