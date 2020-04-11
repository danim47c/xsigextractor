from PySide2 import QtWidgets as qtw, QtCore as qtc

from PySide2.QtCore import Qt

from sys import argv as sys_argv, exit as sys_exit
from traceback import format_exc

from xml.etree import ElementTree as et

from base64 import b64decode

from os import fsencode, fsdecode
from os.path import exists as file_exists

from ui import Ui_MainWindow


move_path = lambda path, to: '/'.join(path.decode().split('/')[:-1] + [to]).encode()


class MainWindow(qtw.QMainWindow):
  def __init__(self):
    super().__init__()

    self.ui = Ui_MainWindow()

    self.ui.setupUi(self)


    self.ui.browseButton.clicked.connect(self.browseButton)
    self.ui.extractButton.clicked.connect(self.extractButton)

    self.path = ''

    self.last_path = '.'

  def browseButton(self):

    self.path, _ = qtw.QFileDialog.getOpenFileName(
      self,
      'Browse .XSIG',
      self.last_path,
      '.XSIG File (*.xsig)'
    )

    if self.path == '': return

    self.ui.browseLine.setText(self.path)

    self.ui.extractButton.setEnabled(True)

  def extractButton(self):
    if self.path == '': self.ui.extractButton.setEnabled(False); return

    try:
      path = fsencode(self.path)

      xsigFile = et.parse(path)
      xsigBackup = xsigFile

      doc = xsigFile.getroot()

      for node in doc:

        if 'Id' in node.attrib and node.attrib['Id'].startswith('fichero'):

          xmlFilename = node.attrib['FileName']
          xmlPath = move_path(path, xmlFilename)

          with open(xmlPath, 'wb') as saveFile: saveFile.write(b64decode(node.text.encode()))

          xmlFile = et.parse(xmlPath)
          xmlDoc = xmlFile.getroot()
          
          documento = xmlDoc[-1][0][0]
          pdfFilename = self.path.split('/')[-1].split('.')[0] + '.pdf'
          
          with open(move_path(xmlPath, pdfFilename), 'wb') as saveFile: saveFile.write(b64decode(documento[3].text.encode()))

          documento[3].text = 'Extracted to ' + pdfFilename

          xmlFile.write(xmlPath)

      xsigFile.write(path)
    
    except Exception:
      xsigBackup.write(path)

      msg = qtw.QMessageBox()
      msg.setIcon(qtw.QMessageBox.Critical)
      msg.setText("Error while extracting .XSIG")
      msg.setInformativeText('\n'.join(format_exc().split('\n')[:-1]))
      msg.setWindowTitle("Critical error")
      msg.exec_()

    else:
      self.last_path = '/'.join(self.path.split('/')[:-1])

      msg = qtw.QMessageBox.about(
        self,
        'Extracted successfully',
        '.XSIG was extracted successfully'
      )





if __name__ == '__main__':

  app = qtw.QApplication(sys_argv)
  
  mainwindow = MainWindow()

  mainwindow.show()

  ex = app.exec_()

  from icon import stop

  stop()

  sys_exit(ex)


