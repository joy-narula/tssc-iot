from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5.QtCore import QDate, QTime, Qt, pyqtSlot, QTimer
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QRadioButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
import os
import time
import cv2 as cv
import numpy as np
import datetime
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
x = datetime.datetime.now()
print(type(x.strftime("%X")))
global button_number
button_number = 0
running_process = []
targets = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
class Window(QMainWindow):
   global button_number
   def __init__(self):
      super().__init__()
      title = "Start Station in PyQt5"
      top = 40
      left = 40
      width = 1000
      height = 700
      self.setWindowTitle('TCCS SMART IOT START STATION')
      self.setGeometry(top, left, width, height)
      self.MyUI()
   def b1_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 1
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
   def b2_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 2
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
         
   def b3_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 3
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
   def b4_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 4
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
   def b5_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 5
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
   def b6_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 6
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
   def b7_selected(self, selected):
      global button_number, label51
      if selected:
         button_number = 7
         label501.setText("<b> Set Target for Product </b>" + str(button_number))
   def MyUI(self):
      w = self
      label_date = QLabel(self)
      x = datetime.datetime.now()
      date_today = x.strftime("%x")
      label_date.setText("Date:" + date_today)
      label_date.resize(230,30)
      label_date.move(780, 35)
      label_date.setFont(QFont('Arial', 20))
      label_date.setStyleSheet("color: red")
      label = QLabel(w)
      label.setText("<b>STATION 1- START OF LINE</b>")
      label.resize(500,40)
      label.move(290, 30)
      label.setFont(QFont('Arial', 25))
      label1 = QLabel(w)
      label1.setText("<b>Select the Product</b>")
      label1.resize(500,40)
      label1.move(50, 100)
      label1.setFont(QFont('Arial', 25))

      label2 = QLabel(w)
      label2.setText("<b>Running Processes</b>")
      label2.resize(500,40)
      label2.move(650, 100)
      label2.setFont(QFont('Arial', 25))
      global label31, label32, label33, label34, label35, label36, label37, label38, label39, label310
      global label41, label42, label43, label44, label45, label46, label47, label48, label49, label410
      global label501, label51, label52, label53, label54, label55, label56, label57, label58, label59, label510 
      label31 = QLabel(w)
      label31.resize(200,40)
      label31.move(650, 150)
      label31.setFont(QFont('Arial', 20))
      label32 = QLabel(w)
      label32.resize(200,40)
      label32.move(650, 200)
      label32.setFont(QFont('Arial', 20))
      label33 = QLabel(w)
      label33.resize(200,40)
      label33.move(650, 250)
      label33.setFont(QFont('Arial', 20))
      label34 = QLabel(w)
      label34.resize(200,40)
      label34.move(650, 300)
      label34.setFont(QFont('Arial', 20))
      label35 = QLabel(w)
      label35.resize(200,40)
      label35.move(650, 350)
      label35.setFont(QFont('Arial', 20))
      label36 = QLabel(w)
      label36.resize(200,40)
      label36.move(650, 400)
      label36.setFont(QFont('Arial', 20))
      label37 = QLabel(w)
      label37.resize(200,40)
      label37.move(650, 450)
      label37.setFont(QFont('Arial', 20))
      label38 = QLabel(w)
      label38.resize(200,40)
      label38.move(650, 500)
      label38.setFont(QFont('Arial', 20))
      label39 = QLabel(w)
      label39.resize(200,40)
      label39.move(650, 550)
      label39.setFont(QFont('Arial', 20))
      label310 = QLabel(w)
      label310.resize(200,40)
      label310.move(650, 600)
      label310.setFont(QFont('Arial', 20))
      
      label41 = QLabel(w)
      label41.resize(200,40)
      label41.move(900, 150)
      label41.setFont(QFont('Arial', 20))
      label41.setStyleSheet("color: blue")
      label42 = QLabel(w)
      label42.resize(200,40)
      label42.move(900, 200)
      label42.setFont(QFont('Arial', 20))
      label42.setStyleSheet("color: blue")
      label43 = QLabel(w)
      label43.resize(200,40)
      label43.move(900, 250)
      label43.setFont(QFont('Arial', 20))
      label43.setStyleSheet("color: blue")
      label44 = QLabel(w)
      label44.resize(200,40)
      label44.move(900, 300)
      label44.setFont(QFont('Arial', 20))
      label44.setStyleSheet("color: blue")
      label45 = QLabel(w)
      label45.resize(200,40)
      label45.move(900, 350)
      label45.setFont(QFont('Arial', 20))
      label45.setStyleSheet("color: blue")
      label46 = QLabel(w)
      label46.resize(200,40)
      label46.move(900, 400)
      label46.setFont(QFont('Arial', 20))
      label46.setStyleSheet("color: blue")
      label47 = QLabel(w)
      label47.resize(200,40)
      label47.move(900, 450)
      label47.setFont(QFont('Arial', 20))
      label47.setStyleSheet("color: blue")
      label48 = QLabel(w)
      label48.resize(200,40)
      label48.move(900, 500)
      label48.setFont(QFont('Arial', 20))
      label48.setStyleSheet("color: blue")
      label49 = QLabel(w)
      label49.resize(200,40)
      label49.move(900, 550)
      label49.setFont(QFont('Arial', 20))
      label49.setStyleSheet("color: blue")
      label410 = QLabel(w)
      label410.resize(200,40)
      label410.move(900, 600)
      label410.setFont(QFont('Arial', 20))
      label410.setStyleSheet("color: blue")

      label51 = QLabel(w)
      label51.resize(100,40)
      label51.move(800, 150)
      label51.setFont(QFont('Arial', 12))
      label51.setStyleSheet("color: green")
      label52 = QLabel(w)
      label52.resize(100,40)
      label52.move(800, 200)
      label52.setFont(QFont('Arial', 12))
      label52.setStyleSheet("color: green")
      label53 = QLabel(w)
      label53.resize(100,40)
      label53.move(800, 250)
      label53.setFont(QFont('Arial', 12))
      label53.setStyleSheet("color: green")
      label54 = QLabel(w)
      label54.resize(100,40)
      label54.move(800, 300)
      label54.setFont(QFont('Arial', 12))
      label54.setStyleSheet("color: green")
      label55 = QLabel(w)
      label55.resize(100,40)
      label55.move(800, 350)
      label55.setFont(QFont('Arial', 12))
      label55.setStyleSheet("color: green")
      label56 = QLabel(w)
      label56.resize(100,40)
      label56.move(800, 400)
      label56.setFont(QFont('Arial', 12))
      label56.setStyleSheet("color: green")
      label57 = QLabel(w)
      label57.resize(100,40)
      label57.move(800, 450)
      label57.setFont(QFont('Arial', 12))
      label57.setStyleSheet("color: green")
      label58 = QLabel(w)
      label58.resize(100,40)
      label58.move(800, 500)
      label58.setFont(QFont('Arial', 12))
      label58.setStyleSheet("color: green")
      label59 = QLabel(w)
      label59.resize(100,40)
      label59.move(800, 550)
      label59.setFont(QFont('Arial', 12))
      label59.setStyleSheet("color: green")
      label510 = QLabel(w)
      label510.resize(100,40)
      label510.move(800, 600)
      label510.setFont(QFont('Arial', 12))
      label510.setStyleSheet("color: green")

      b1 = QRadioButton(w)
      b1.setChecked(False)
      b1.setText("Product 1")
      b1.resize(200,30)
      b1.move(50, 170)
      b1.setFont(QFont('Arial', 20))
      b1.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b1.toggled.connect(self.b1_selected)
   
      b2 = QRadioButton(w)
      b2.setChecked(False)
      b2.setText("Product 2")
      b2.resize(200,30)
      b2.move(50, 240)
      b2.setFont(QFont('Arial', 20))
      b2.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b2.toggled.connect(self.b2_selected)
      b3 = QRadioButton(w)
      b3.setChecked(False)
      b3.setText("Product 3")
      b3.resize(200,30)
      b3.move(50, 310)
      b3.setFont(QFont('Arial', 20))
      b3.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b3.toggled.connect(self.b3_selected)
      b4 = QRadioButton(w)
      b4.setChecked(False)
      b4.setText("Product 4")
      b4.resize(200,30)
      b4.move(50, 380)
      b4.setFont(QFont('Arial', 20))
      b4.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b4.toggled.connect(self.b4_selected)
      b5 = QRadioButton(w)
      b5.setChecked(False)
      b5.setText("Product 5")
      b5.resize(200,30)
      b5.move(50, 450)
      b5.setFont(QFont('Arial', 20))
      b5.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b5.toggled.connect(self.b5_selected)
      b6 = QRadioButton(w)
      b6.setChecked(False)
      b6.setText("Product 6")
      b6.resize(200,30)
      b6.move(50, 520)
      b6.setFont(QFont('Arial', 20))
      b6.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b6.toggled.connect(self.b6_selected)
      b7 = QRadioButton(w)
      b7.setChecked(False)
      b7.setText("Product 7")
      b7.resize(200,30)
      b7.move(50, 590)
      b7.setFont(QFont('Arial', 20))
      b7.setStyleSheet("QRadioButton::indicator""{""width : 25px;""height : 25px;""}")
      b7.toggled.connect(self.b7_selected)
      button = QPushButton(w)
      button.setText("START TIMER")
      button.setFont(QFont('Arial', 23))
      button.resize(250,250)
      button.move(250, 170)
      button.setStyleSheet("background-color: #0c940c");
      button.clicked.connect(self.on_start_button)
      button1 = QPushButton(w)
      button1.setText("UNDO \n LAST")
      button1.setFont(QFont('Arial', 15))
      button1.resize(100,250)
      button1.move(530, 170)
      button1.setStyleSheet("background-color: #b02920");
      button1.clicked.connect(self.on_undo_last_confirm)
      label501 = QLabel(w)
      label501.resize(330,40)
      label501.move(250, 450)
      label501.setFont(QFont('Arial', 20))
      label501.setText("<b> Set Target for Product </b>" + str(button_number))
      global line_edit
      line_edit = QLineEdit("", self)
      line_edit.resize(150,50)
      line_edit.move(250, 500)
      button51 = QPushButton(w)
      button51.setText("OK")
      button51.setFont(QFont('Arial', 15))
      button51.resize(50,50)
      button51.move(420, 500)
      button51.setStyleSheet("background-color: #0c940c");
      button51.clicked.connect(self.confirm_target)
      button52 = QPushButton(w)
      button52.setText("Reset Targets")
      button52.setFont(QFont('Arial', 15))
      button52.resize(140,50)
      button52.move(490, 500)
      button52.setStyleSheet("background-color: #b02920");
      button52.clicked.connect(self.reset_target)
      label61 = QLabel(w)
      label61.resize(330,40)
      label61.move(250, 560)
      label61.setFont(QFont('Arial', 20))
      label61.setText("<b> Broadcast Information </b>")
      global line_edit2
      line_edit2 = QLineEdit("", self)
      line_edit2.resize(310,50)
      line_edit2.move(250, 610)
      button61 = QPushButton(w)
      button61.setText("OK")
      button61.setFont(QFont('Arial', 15))
      button61.resize(50,50)
      button61.move(580, 610)
      button61.setStyleSheet("background-color: #0c940c");
      button61.clicked.connect(self.broadcast_done)
      x = datetime.datetime.now()
      global label_time
      label_time = QLabel(self)
      time_now = x.strftime("%X")
      label_time.setText(time_now)
      label_time.resize(300,40)
      label_time.move(400, 100)
      label_time.setFont(QFont('Arial', 25))
      label_time.setStyleSheet("color: red")
      timer = QTimer(self)
      timer.timeout.connect(self.update_time)
      timer.start(1000)
   def broadcast_done(self):
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Warning)
      msg.setText("Broadcast Done")
      msg.setWindowTitle("Broadcast")
      msg.setStandardButtons(QMessageBox.Ok)
      retval = msg.exec_()
   def reset_target(self):
      if button_number != 0:
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Warning)
         msg.setText("Do you really want to RESET?")
         msg.setWindowTitle("Confirm RESET")
         msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
         msg.buttonClicked.connect(self.on_reset_final)
         retval = msg.exec_()
   def on_reset_final(self, i):
      button_pressed = i.text()
      if button_pressed == "&OK":
         global targets
         targets = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
   def confirm_target(self):
      global targets
      if button_number != 0:
         value = int(line_edit.text())
         if targets[button_number-1][0] == 0:
            targets[button_number-1][0] = value
            sucess1 = QMessageBox()
            sucess1.setIcon(QMessageBox.Information)
            sucess1.setText("Tasks for product " + str(button_number) + ": " + str(value))
            sucess1.setWindowTitle("SUCCESS")
            sucess1.setStandardButtons(QMessageBox.Ok)
            retval2 = sucess1.exec_()         
         else:
            error1 = QMessageBox()
            error1.setIcon(QMessageBox.Critical)
            error1.setText("Finish the remaining task first")
            error1.setWindowTitle("ERROR")
            error1.setStandardButtons(QMessageBox.Ok)
            retval1 = error1.exec_()
         print(targets)
         
   def update_time(self):
      x = datetime.datetime.now()
      time_now = x.strftime("%X")
      label_time.setText(time_now)
      for i in range(len(running_process)):
         diff = datetime.datetime.now().replace(microsecond=0) - running_process[i][1].replace(microsecond = 0)
         #print(diff, type(diff), diff.total_seconds())
         j = i+1
         if j == 1:
            label41.setText(str(diff))
         if j == 2:
            label42.setText(str(diff))
         if j == 3:
            label43.setText(str(diff))
         if j == 4:
            label44.setText(str(diff))
         if j == 5:
            label45.setText(str(diff))
         if j == 6:
            label46.setText(str(diff))
         if j == 7:
            label47.setText(str(diff))
         if j == 8:
            label48.setText(str(diff))
         if j == 9:
            label49.setText(str(diff))
         if j == 10:
            label410.setText(str(diff))
   def on_start_button(self):
      global running_process
      x = datetime.datetime.now()
      time_now = x.strftime("%X")
      label_time.setText(time_now)
      if button_number > 0:
         print("Button Number", button_number)
         
         #print(running_process)
         if targets[button_number-1][0] != 0:
            targets[button_number-1][1] += 1
            running_process.append([button_number, x, targets[button_number-1][1], targets[button_number-1][0]])
         else:
            running_process.append([button_number, x, 0, 0])

         for i in range(len(running_process)):
            j = i+1
            if j == 1:
               label51.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 2:
               label52.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 3:
               label53.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 4:
               label54.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 5:
               label55.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 6:
               label56.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 7:
               label57.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 8:
               label58.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 9:
               label59.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 10:
               label510.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))

                     
               
            j = i+1
            if j == 1:
               label31.setText("Product " + str(running_process[i][0]))
            if j == 2:
               label32.setText("Product " + str(running_process[i][0]))
            if j == 3:
               label33.setText("Product " + str(running_process[i][0]))
            if j == 4:
               label34.setText("Product " + str(running_process[i][0]))
            if j == 5:
               label35.setText("Product " + str(running_process[i][0]))
            if j == 6:
               label36.setText("Product " + str(running_process[i][0]))
            if j == 7:
               label37.setText("Product " + str(running_process[i][0]))
            if j == 8:
               label38.setText("Product " + str(running_process[i][0]))
            if j == 9:
               label39.setText("Product " + str(running_process[i][0]))
            if j == 10:
               label310.setText("Product " + str(running_process[i][0]))
            x = datetime.datetime.now()
            time_now = x.strftime("%X")
            label_time.setText(time_now)
            diff = datetime.datetime.now().replace(microsecond=0) - running_process[i][1].replace(microsecond = 0)
            #print(diff, type(diff), diff.total_seconds())
            j = i+1
            if j == 1:
               label41.setText(str(diff))
            if j == 2:
               label42.setText(str(diff))
            if j == 3:
               label43.setText(str(diff))
            if j == 4:
               label44.setText(str(diff))
            if j == 5:
               label45.setText(str(diff))
            if j == 6:
               label46.setText(str(diff))
            if j == 7:
               label47.setText(str(diff))
            if j == 8:
               label48.setText(str(diff))
            if j == 9:
               label49.setText(str(diff))
            if j == 10:
               label410.setText(str(diff))
         if targets[button_number-1][1] == targets[button_number-1][0] != 0:
            print("Target Done")
            sucess_tar1 = QMessageBox()
            sucess_tar1.setIcon(QMessageBox.Information)
            sucess_tar1.setText("Target Met")
            sucess_tar1.setWindowTitle("SUCCESS")
            sucess_tar1.setStandardButtons(QMessageBox.Ok)
            retval_tar2 = sucess_tar1.exec_() 
            targets[button_number-1][0] = 0
            targets[button_number-1][1] = 0
            
      else:
         print("No button Selected")
   def on_undo_last_confirm(self):
      if len(running_process) > 0:
         msg = QMessageBox()
         msg.setIcon(QMessageBox.Warning)
         msg.setText("Do you really want to UNDO?")
         msg.setWindowTitle("Confirm Undo")
         msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
         msg.buttonClicked.connect(self.on_undo_last)
         retval = msg.exec_()
      
   def on_undo_last(self, i):
      button_pressed = i.text()
      global running_process
      if button_pressed == "&OK" and len(running_process) > 0:
         print(running_process[-1:])
         button_number = running_process[-1:][0][0]
         if targets[button_number-1][0] != 0:
            targets[button_number-1][1] -= 1
         
         running_process = running_process[:-1]
         label31.setText("")
         label32.setText("")
         label33.setText("")
         label34.setText("")
         label35.setText("")
         label36.setText("")
         label37.setText("")
         label38.setText("")
         label39.setText("")
         label310.setText("")
         label41.setText("")
         label42.setText("")
         label43.setText("")
         label44.setText("")
         label45.setText("")
         label46.setText("")
         label47.setText("")
         label48.setText("")
         label49.setText("")
         label410.setText("")
         label51.setText("")
         label52.setText("")
         label53.setText("")
         label54.setText("")
         label55.setText("")
         label56.setText("")
         label57.setText("")
         label58.setText("")
         label59.setText("")
         label510.setText("")
         for i in range(len(running_process)):
            j = i+1
            if j == 1:
               label31.setText("Product " + str(running_process[i][0]))
            if j == 2:
               label32.setText("Product " + str(running_process[i][0]))
            if j == 3:
               label33.setText("Product " + str(running_process[i][0]))
            if j == 4:
               label34.setText("Product " + str(running_process[i][0]))
            if j == 5:
               label35.setText("Product " + str(running_process[i][0]))
            if j == 6:
               label36.setText("Product " + str(running_process[i][0]))
            if j == 7:
               label37.setText("Product " + str(running_process[i][0]))
            if j == 8:
               label38.setText("Product " + str(running_process[i][0]))
            if j == 9:
               label39.setText("Product " + str(running_process[i][0]))
            if j == 10:
               label310.setText("Product " + str(running_process[i][0]))
            x = datetime.datetime.now()
            time_now = x.strftime("%X")
            label_time.setText(time_now)
            diff = datetime.datetime.now().replace(microsecond=0) - running_process[i][1].replace(microsecond = 0)
            #print(diff, type(diff), diff.total_seconds())
            j = i+1
            if j == 1:
               label41.setText(str(diff))
            if j == 2:
               label42.setText(str(diff))
            if j == 3:
               label43.setText(str(diff))
            if j == 4:
               label44.setText(str(diff))
            if j == 5:
               label45.setText(str(diff))
            if j == 6:
               label46.setText(str(diff))
            if j == 7:
               label47.setText(str(diff))
            if j == 8:
               label48.setText(str(diff))
            if j == 9:
               label49.setText(str(diff))
            if j == 10:
               label410.setText(str(diff))
                  
            if j == 1:
               label51.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 2:
               label52.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 3:
               label53.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 4:
               label54.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 5:
               label55.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 6:
               label56.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 7:
               label57.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 8:
               label58.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 9:
               label59.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))
            if j == 10:
               label510.setText(str(running_process[i][2]) + " / " + str(running_process[i][3]))

   
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
