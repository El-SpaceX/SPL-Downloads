from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube, Playlist, exceptions
from os import rename, path
from tkinter import filedialog as fd

val_dir = ''


class Ui_MainWindow(object):

    def ShowMessageError(self, message, * colors):
            
        self.LabelFrameMessage.setText(message)
        self.FrameMessage.setStyleSheet("background-color: rgb({}, {}, {});".format(* colors))
        self.FrameMessage.show()

    def HideMessageError(self):
        self.FrameMessage.hide()


    def get_directory(self):
        global val_dir
        val_dir = fd.askdirectory(initialdir='/',title ='Selecione uma pasta')

    def download(self):
        global val_dir
        mp3_extension = False
        if self.comboBox.currentText() == 'AUDIO':
            mp3_extension = True
        
        if val_dir == '':
            val_dir = path.dirname(path.realpath(__file__))
        url=self.InputURL.text()
        try:
            if '/playlist?' in url:
                playlist = Playlist(url)
                for video in playlist:
                    yt = YouTube(video)
                    if mp3_extension:
                       file = yt.streams.filter(only_audio=True)[0].download(val_dir)
                       name, extension = path.splitext(file)
                       rename(file, (name+'.mp3'))
                    else:
                        yt.streams.get_highest_resolution().download(val_dir)
            else:
                yt = YouTube(url)
                if mp3_extension:
                       file = yt.streams.filter(only_audio=True)[0].download(val_dir)
                       name, extension = path.splitext(file)
                       rename(file, (name+'.mp3'))
                else:
                    yt.streams.get_highest_resolution().download(val_dir)

        except exceptions.RegexMatchError:
            self.ShowMessageError('Digite uma URL válida.', 232, 26, 19)
        except:
            self.ShowMessageError('ERRO ao se conectar com a API', 232, 26, 19)
        else:
            self.ShowMessageError('Download concluído com sucesso', 6, 128, 0)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 550)
        MainWindow.setMaximumSize(QtCore.QSize(700, 550))
        
        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.InputURL = QtWidgets.QLineEdit(self.frame)
        self.InputURL.setGeometry(QtCore.QRect(50, 200, 461, 31))
        self.InputURL.setTabletTracking(False)
        self.InputURL.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"background-color: rgb(34, 34, 34);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-position: center;\n"
"color: rgb(200, 200, 200);")
        self.InputURL.setText("")
        self.InputURL.setClearButtonEnabled(True)
        self.InputURL.setObjectName("InputURL")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(410, 290, 81, 31))
        self.comboBox.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"background-color: rgb(34, 34, 34);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-position: center;\n"
"color: rgb(200, 200, 200);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.DownloadButton = QtWidgets.QPushButton(self.frame)
        self.DownloadButton.setGeometry(QtCore.QRect(160, 280, 221, 41))
        self.DownloadButton.setAcceptDrops(False)
        self.DownloadButton.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"background-color: rgb(34, 34, 34);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"background-position: center;\n"
"color: rgb(200, 200, 200);")
        self.DownloadButton.setCheckable(True)
        self.DownloadButton.setObjectName("DownloadButton")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(510, 210, 31, 21))
        self.toolButton.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"background-color: rgb(34, 34, 34);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-position: center;\n"
"color: rgb(200, 200, 200);")
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 40, 241, 41))
        self.label.setStyleSheet("font: 87 32pt \"Segoe UI Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 631, 81))
        self.label_2.setStyleSheet("font: 87 11pt \"Segoe UI Black\";")
        self.label_2.setObjectName("label_2")
        self.FrameMessage = QtWidgets.QFrame(self.frame)
        self.FrameMessage.setGeometry(QtCore.QRect(50, 230, 461, 21))
        self.FrameMessage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameMessage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameMessage.setObjectName("FrameMessage")
        self.LabelFrameMessage = QtWidgets.QLabel(self.FrameMessage)
        self.LabelFrameMessage.setGeometry(QtCore.QRect(130, 0, 201, 21))
        self.LabelFrameMessage.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.LabelFrameMessage.setObjectName("LabelFrameMessage")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPL Downloads"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico')) 
        self.InputURL.setPlaceholderText(_translate("MainWindow", "Digite a URL do vídeo"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VIDEO"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AUDIO"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Instruções"))
        self.label_2.setText(_translate("MainWindow", "1 - Digite a URL do vídeo/playlist no campo abaixo.\n"
"2 - Escolha o local onde será salvo o arquivo clicando no botão de resistencia(\"...\").\n"
"3 - Escolhao o formato a ser salvo(VIDEO ou AUDIO).\n"
"4 - Clice no botão \"download\" para baixar o arquivo."))

        #Ocult message error
        self.FrameMessage.hide()

        #Clicked
        self.toolButton.clicked.connect(self.get_directory)
        self.DownloadButton.clicked.connect(self.HideMessageError)
        self.DownloadButton.clicked.connect(self.download)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
