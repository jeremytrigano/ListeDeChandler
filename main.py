import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget, QApplication

import json


def lireJson(name):
    with open(name) as json_file:
        data = json.load(json_file)
    return data

def ecrireJson(name, data):
    with open(name) as json_file:
        dataJson = json.load(json_file)
    dataJson['personne'].append(data)
    with open(name, 'w') as outfile:
        json.dump(dataJson, outfile)

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setObjectName("Form")
        self.resize(784, 588)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(60, 60, 651, 461))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.leNom = QtWidgets.QLineEdit(self.widget)
        self.leNom.setObjectName("leNom")
        self.horizontalLayout.addWidget(self.leNom)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lePrenom = QtWidgets.QLineEdit(self.widget)
        self.lePrenom.setObjectName("lePrenom")
        self.horizontalLayout_2.addWidget(self.lePrenom)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.leTel = QtWidgets.QLineEdit(self.widget)
        self.leTel.setObjectName("leTel")
        self.horizontalLayout_3.addWidget(self.leTel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.listWidget.addItem('<Nouveau>')
        # ajout item à partir de json
        jsonData = lireJson('repertoire.json')

        for elem in jsonData['personne']:
            self.listWidget.addItem(elem['nom'])

        self.listWidget.setCurrentRow(0)

        self.listWidget.currentItemChanged.connect(self.selectionItem)
        self.pushButton.clicked.connect(self.boutonOK)

    def selectionItem(self):
        jsonData = lireJson('repertoire.json')
        if self.listWidget.currentRow() == -1:
            return

        if self.listWidget.currentItem().text() == '<Nouveau>':
            self.leNom.setText("")
            self.lePrenom.setText("")
            self.leTel.setText("")
        else:
            selected = [elem for elem in jsonData['personne'] if elem['nom'] == self.listWidget.currentItem().text()]
            if len(selected) == 1:
                self.leNom.setText(selected[0]['nom'])
                self.lePrenom.setText(selected[0]['prenom'])
                self.leTel.setText(selected[0]['tel'])
            if len(selected) == 0:
                self.leNom.setText("")
                self.lePrenom.setText("")
                self.leTel.setText("")

    def boutonOK(self):
        jsonData = lireJson('repertoire.json')


        if self.listWidget.currentItem().text() != '<Nouveau>':
            for elem in jsonData['personne']:
                if elem['nom'] == self.listWidget.currentItem().text():
                    elem['nom'] = self.leNom.text()
                    elem['prenom'] = self.lePrenom.text()
                    elem['tel'] = self.leTel.text()
            with open('repertoire.json', 'w') as outfile:
                json.dump(jsonData, outfile)
        else:
            dataEntree = {"nom": self.leNom.text(), "prenom": self.lePrenom.text(), "tel": self.leTel.text()}
            ecrireJson('repertoire.json', dataEntree)

        # reset et création listWidget
        self.listWidget.clear()
        self.listWidget.addItem('<Nouveau>')
        # ajout item à partir de json
        jsonData = lireJson('repertoire.json')
        for elem in jsonData['personne']:
            self.listWidget.addItem(elem['nom'])

        self.listWidget.setCurrentRow(0)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Liste noms", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Nom", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Prenom", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Tel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "OK", None, -1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())