# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NovoEmprestimo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NovoEmprestimo(object):
    def setupUi(self, NovoEmprestimo):
        NovoEmprestimo.setObjectName("NovoEmprestimo")
        NovoEmprestimo.resize(504, 529)
        self.NovoEmprestimoText = QtWidgets.QLabel(NovoEmprestimo)
        self.NovoEmprestimoText.setGeometry(QtCore.QRect(30, 20, 277, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.NovoEmprestimoText.setFont(font)
        self.NovoEmprestimoText.setObjectName("NovoEmprestimoText")
        self.selectUser = QtWidgets.QComboBox(NovoEmprestimo)
        self.selectUser.setGeometry(QtCore.QRect(30, 110, 251, 31))
        self.selectUser.setEditable(False)
        self.selectUser.setCurrentText("")
        self.selectUser.setMaxVisibleItems(13)
        self.selectUser.setObjectName("selectUser")
        self.selectUserText = QtWidgets.QLabel(NovoEmprestimo)
        self.selectUserText.setGeometry(QtCore.QRect(40, 90, 141, 16))
        self.selectUserText.setObjectName("selectUserText")
        self.tabelaLivrosEmprestimo = QtWidgets.QTableWidget(NovoEmprestimo)
        self.tabelaLivrosEmprestimo.setGeometry(QtCore.QRect(50, 160, 381, 241))
        self.tabelaLivrosEmprestimo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaLivrosEmprestimo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaLivrosEmprestimo.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelaLivrosEmprestimo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelaLivrosEmprestimo.setObjectName("tabelaLivrosEmprestimo")
        self.tabelaLivrosEmprestimo.setColumnCount(3)
        self.tabelaLivrosEmprestimo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaLivrosEmprestimo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaLivrosEmprestimo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaLivrosEmprestimo.setHorizontalHeaderItem(2, item)
        self.selectBook = QtWidgets.QComboBox(NovoEmprestimo)
        self.selectBook.setGeometry(QtCore.QRect(30, 460, 241, 21))
        self.selectBook.setObjectName("selectBook")
        self.selectBookText = QtWidgets.QLabel(NovoEmprestimo)
        self.selectBookText.setGeometry(QtCore.QRect(40, 440, 141, 16))
        self.selectBookText.setObjectName("selectBookText")
        self.addBook = QtWidgets.QPushButton(NovoEmprestimo)
        self.addBook.setGeometry(QtCore.QRect(30, 490, 111, 32))
        self.addBook.setObjectName("addBook")
        self.finalizarEmprestimo = QtWidgets.QPushButton(NovoEmprestimo)
        self.finalizarEmprestimo.setGeometry(QtCore.QRect(360, 460, 131, 31))
        self.finalizarEmprestimo.setAutoFillBackground(False)
        self.finalizarEmprestimo.setAutoDefault(True)
        self.finalizarEmprestimo.setFlat(False)
        self.finalizarEmprestimo.setObjectName("finalizarEmprestimo")
        # self.removeBook = QtWidgets.QPushButton(NovoEmprestimo)
        # self.removeBook.setGeometry(QtCore.QRect(160, 490, 111, 32))
        # self.removeBook.setObjectName("removeBook")
        self.codEmprestimoInput = QtWidgets.QLineEdit(NovoEmprestimo)
        self.codEmprestimoInput.setGeometry(QtCore.QRect(340, 110, 113, 21))
        self.codEmprestimoInput.setObjectName("codEmprestimoInput")
        self.codEmprestimoText = QtWidgets.QLabel(NovoEmprestimo)
        self.codEmprestimoText.setGeometry(QtCore.QRect(330, 80, 151, 16))
        self.codEmprestimoText.setObjectName("codEmprestimoText")

        self.retranslateUi(NovoEmprestimo)
        QtCore.QMetaObject.connectSlotsByName(NovoEmprestimo)

        #Controle de Inputs
        #Cod Emprestimo
        regex=QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(regex)
        self.codEmprestimoInput.setValidator(validator)

    def retranslateUi(self, NovoEmprestimo):
        _translate = QtCore.QCoreApplication.translate
        NovoEmprestimo.setWindowTitle(_translate("NovoEmprestimo", "NovoEmprestimo"))
        self.NovoEmprestimoText.setText(_translate("NovoEmprestimo", "Novo Empréstimo"))
        self.selectUserText.setText(_translate("NovoEmprestimo", "Selecione um Usuário:"))
        item = self.tabelaLivrosEmprestimo.horizontalHeaderItem(0)
        item.setText(_translate("NovoEmprestimo", "Codigo"))
        item = self.tabelaLivrosEmprestimo.horizontalHeaderItem(1)
        item.setText(_translate("NovoEmprestimo", "Titulo"))
        item = self.tabelaLivrosEmprestimo.horizontalHeaderItem(2)
        item.setText(_translate("NovoEmprestimo", "Ano"))
        self.selectBookText.setText(_translate("NovoEmprestimo", "Selecione um Livro:"))
        self.addBook.setText(_translate("NovoEmprestimo", "Adicionar livro"))
        self.finalizarEmprestimo.setText(_translate("NovoEmprestimo", "Fazer empréstimo"))
        # self.removeBook.setText(_translate("NovoEmprestimo", "Remover livro"))
        self.codEmprestimoText.setText(_translate("NovoEmprestimo", "Codigo de Emprestimo:"))
