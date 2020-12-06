from PyQt5 import QtCore, QtGui, QtWidgets
import DBconnection_cars, time

class Car:
  def __init__(self, id, year, model, miles, maker):
    self.__id = id
    self.__year = year
    self.__model = model
    self.__miles = miles
    self.__maker = maker
    #self.__id = 0
    #self.__year = 0
    #self.__model = ''
    #self.__miles = 0
    #self.__maker = ''

  def set_id (self, ids):
      self.__id = ids

  def set_year (self, year):
      self.__year = year

  def set_model (self, model):
    self.__model = model

  def set_miles (self, miles):
    self.__miles = miles

  def set_maker (self, maker):
    self.__maker = maker
  
  def get_id(self):
      return self.__id

  def get_year(self):
    return self.__year

  def get_model(self):
    return self.__model
  
  def get_miles(self):
    return self.__miles
  
  def get_maker(self):
    return self.__maker

def get_inventory(self):
  param = 'all'
  DBconnection_cars.retrieve_data ('NULL', param, self)


def initialize_DB(self):
  DBconnection_cars.initialize(self)

def clean_text_boxes(self):
        self.text__VIN_number.setText("")
        self.text_car_year.setText("")
        self.text_car_model.setText("")
        self.text_car_miles.setText("")
        self.text_car_maker.setText("")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(799, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 360, 731, 341))
        self.groupBox.setObjectName("groupBox")
        self.My_pushButton_search = QtWidgets.QPushButton(self.groupBox)
        self.My_pushButton_search.setGeometry(QtCore.QRect(590, 40, 93, 28))
        self.My_pushButton_search.setObjectName("My_pushButton_search")
        self.My_pushButton_search.clicked.connect(self.button_search_clicked)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 631, 181))
        #self.tableWidget.setRowCount(3)
        #self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.clicked.connect(self.tableWidget_clicked)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 0, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setItem(0, 1, item)
        self.My_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.My_comboBox.setGeometry(QtCore.QRect(350, 40, 201, 22))
        self.My_comboBox.setObjectName("My_comboBox")
        self.My_comboBox.addItem("")
        #self.My_comboBox.addItem("")
        #self.My_comboBox.addItem("")
        self.My_radiobutton_maker = QtWidgets.QRadioButton(self.groupBox)
        self.My_radiobutton_maker.setGeometry(QtCore.QRect(50, 30, 91, 21))
        self.My_radiobutton_maker.setChecked(True)
        self.My_radiobutton_maker.setObjectName("my_radiobutton_maker")
        self.My_radiobutton_maker.clicked.connect(self.My_radiobutton_maker_clicked)
        self.My_radiobutton_model = QtWidgets.QRadioButton(self.groupBox)
        self.My_radiobutton_model.setGeometry(QtCore.QRect(50, 60, 95, 21))
        self.My_radiobutton_model.setChecked(False)
        self.My_radiobutton_model.setObjectName("my_radiobutton_model")
        self.My_radiobutton_model.clicked.connect(self.My_radiobutton_model_clicked)
        self.My_radiobutton_year = QtWidgets.QRadioButton(self.groupBox)
        self.My_radiobutton_year.setGeometry(QtCore.QRect(50, 90, 95, 21))
        self.My_radiobutton_year.setObjectName("my_radiobutton_year")
        self.My_radiobutton_year.clicked.connect(self.My_radiobutton_year_clicked)
        self.My_radiobutton_all = QtWidgets.QRadioButton(self.groupBox)
        self.My_radiobutton_all.setGeometry(QtCore.QRect(50, 120, 95, 21))
        self.My_radiobutton_all.setObjectName("my_radiobutton_all")
        self.My_radiobutton_all.clicked.connect(self.My_radiobutton_all_clicked)
        self.text__VIN_number = QtWidgets.QLineEdit(self.centralwidget)
        self.text__VIN_number.setGeometry(QtCore.QRect(190, 60, 280, 22))
        self.text__VIN_number.setObjectName("text__VIN_number")
        self.text_car_year = QtWidgets.QLineEdit(self.centralwidget)
        self.text_car_year.setGeometry(QtCore.QRect(190, 110, 280, 22))
        self.text_car_year.setObjectName("text_car_year")
        self.text_car_model = QtWidgets.QLineEdit(self.centralwidget)
        self.text_car_model.setGeometry(QtCore.QRect(190, 160, 280, 22))
        self.text_car_model.setObjectName("text_car_model")
        self.text_car_miles = QtWidgets.QLineEdit(self.centralwidget)
        self.text_car_miles.setGeometry(QtCore.QRect(190, 210, 280, 22))
        self.text_car_miles.setObjectName("text_car_miles")
        self.text_car_maker = QtWidgets.QLineEdit(self.centralwidget)
        self.text_car_maker.setGeometry(QtCore.QRect(190, 260, 280, 22))
        self.text_car_maker.setObjectName("text_car_maker")
        self.My_pushButton_insert = QtWidgets.QPushButton(self.centralwidget)
        self.My_pushButton_insert.setGeometry(QtCore.QRect(590, 60, 93, 28))
        self.My_pushButton_insert.setObjectName("My_pushButton_insert")
        self.My_pushButton_insert.clicked.connect(self.button_insert_clicked) #insert click action
        self.My_pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.My_pushButton_update.setEnabled(False)
        self.My_pushButton_update.setGeometry(QtCore.QRect(590, 110, 93, 28))
        self.My_pushButton_update.setObjectName("My_pushButton_update")
        self.My_pushButton_update.clicked.connect(self.button_update_clicked)
        self.My_pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.My_pushButton_delete.setEnabled(False)
        self.My_pushButton_delete.setGeometry(QtCore.QRect(590, 160, 93, 28))
        self.My_pushButton_delete.setObjectName("My_pushButton_delete")
        self.My_pushButton_delete.clicked.connect(self.button_delete_clicked)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 50, 80, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_VIN_number = QtWidgets.QLabel(self.layoutWidget)
        self.label_VIN_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_VIN_number.setObjectName("label_VIN_number")
        self.verticalLayout.addWidget(self.label_VIN_number)
        self.label_car_year = QtWidgets.QLabel(self.layoutWidget)
        self.label_car_year.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_car_year.setObjectName("label_car_year")
        self.verticalLayout.addWidget(self.label_car_year)
        self.label_car_model = QtWidgets.QLabel(self.layoutWidget)
        self.label_car_model.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_car_model.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_car_model.setObjectName("label_car_model")
        self.verticalLayout.addWidget(self.label_car_model)
        self.label_car_miles = QtWidgets.QLabel(self.layoutWidget)
        self.label_car_miles.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_car_miles.setObjectName("label_car_miles")
        self.verticalLayout.addWidget(self.label_car_miles)
        self.label_car_maker = QtWidgets.QLabel(self.layoutWidget)
        self.label_car_maker.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_car_maker.setObjectName("label_car_maker")
        self.verticalLayout.addWidget(self.label_car_maker)
        self.status_frame = QtWidgets.QFrame(self.centralwidget)
        self.status_frame.setGeometry(QtCore.QRect(20, 710, 731, 31))
        self.status_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_frame.setLineWidth(1)
        self.status_frame.setObjectName("status_frame")
        self.status_label1 = QtWidgets.QLabel(self.status_frame)
        self.status_label1.setGeometry(QtCore.QRect(10, 9, 41, 16))
        self.status_label1.setObjectName("status_label1")
        self.status_label2 = QtWidgets.QLabel(self.status_frame)
        self.status_label2.setGeometry(QtCore.QRect(60, 7, 661, 20))
        self.status_label2.setText("")
        self.status_label2.setObjectName("status_label2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInitialize = QtWidgets.QAction(MainWindow)
        self.actionInitialize.setObjectName("actionInitialize")
        self.menuDatabase.addAction(self.actionInitialize)
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.actionInitialize.triggered.connect(self.initialize_menu)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def tableWidget_clicked(self):
        self.status_label2.setText("")
        r = self.tableWidget.currentRow()
        item = self.tableWidget.item(r, 0)
        self.text__VIN_number.setText(item.text()) 
        self.text__VIN_number.setDisabled(True)
        item = self.tableWidget.item(r, 1)
        self.text_car_year.setText(item.text()) 
        item = self.tableWidget.item(r, 2)
        self.text_car_model.setText(item.text()) 
        item = self.tableWidget.item(r, 3)
        self.text_car_miles.setText(item.text()) 
        item = self.tableWidget.item(r, 4)
        self.text_car_maker.setText(item.text()) 
        self.My_pushButton_update.setEnabled(True)
        self.My_pushButton_delete.setEnabled(True)

    def initialize_menu(self):
        initialize_DB(self)
        

    def button_search_clicked(self):
        self.status_label2.setText("")
        if self.My_radiobutton_maker.isChecked():
          param = 'maker'
        elif self.My_radiobutton_model.isChecked():
          param = 'model'
        elif self.My_radiobutton_year.isChecked():
          param = 'year'
        elif self.My_radiobutton_all.isChecked():
          param = 'all'
        data = self.My_comboBox.itemText(self.My_comboBox.currentIndex())
        DBconnection_cars.retrieve_data(data, param, self)
        self.text__VIN_number.setDisabled(False)
        clean_text_boxes(self)


    def button_insert_clicked(self):
        self.status_label2.setText("")
        my_car = Car(self.text__VIN_number.text(), self.text_car_year.text(),self.text_car_model.text(),self.text_car_miles.text(), self.text_car_maker.text())
        DBconnection_cars.insert_data (my_car.get_id(), my_car.get_year(), my_car.get_model(), my_car.get_miles(), my_car.get_maker(), self)
        get_inventory(self)
        clean_text_boxes(self)
        self.My_pushButton_update.setEnabled(False)
        self.My_pushButton_delete.setEnabled(False)
        

    def button_delete_clicked(self):
        param = 'carId'
        del_car = self.text__VIN_number.text()
        DBconnection_cars.delete_data (del_car, param, self)
        get_inventory(self)
        clean_text_boxes(self)
        self.text__VIN_number.setDisabled(False)
        self.My_pushButton_update.setEnabled(False)
        self.My_pushButton_delete.setEnabled(False)

    def button_update_clicked(self):
        my_car = Car(self.text__VIN_number.text(), self.text_car_year.text(),self.text_car_model.text(),self.text_car_miles.text(), self.text_car_maker.text())
        DBconnection_cars.update_data(my_car.get_id(), my_car.get_year(), my_car.get_model(), my_car.get_miles(), my_car.get_maker(), self)
        get_inventory(self)
        clean_text_boxes(self)
        self.text__VIN_number.setDisabled(False)
        self.My_pushButton_update.setEnabled(False)
        self.My_pushButton_delete.setEnabled(False)

    def My_radiobutton_maker_clicked(self):
        self.status_label2.setText("")
        param = 'maker'
        DBconnection_cars.fill_combo_box(param, self)

    def My_radiobutton_model_clicked(self):
        self.status_label2.setText("")
        param = 'model'
        DBconnection_cars.fill_combo_box(param, self)

    def My_radiobutton_year_clicked(self):
        self.status_label2.setText("")
        param = 'year'
        DBconnection_cars.fill_combo_box(param, self)
        

    def My_radiobutton_all_clicked(self):
        self.status_label2.setText("")
        self.My_comboBox.clear()
        self.My_comboBox.addItem("")
        self.My_comboBox.setItemText(0, "All inventory...")
        self.My_comboBox.setItemData(0, "all")
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Car Inventory App"))
        self.groupBox.setTitle(_translate("MainWindow", "Search"))
        self.My_pushButton_search.setText(_translate("MainWindow", "Search"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.My_comboBox.setItemText(0, _translate("MainWindow", "Select..."))
        self.My_radiobutton_maker.setText(_translate("MainWindow", "By Maker"))
        self.My_radiobutton_model.setText(_translate("MainWindow", "By Model"))
        self.My_radiobutton_year.setText(_translate("MainWindow", "By Year"))
        self.My_radiobutton_all.setText(_translate("MainWindow", "All"))
        self.My_pushButton_insert.setText(_translate("MainWindow", "Insert"))
        self.My_pushButton_update.setText(_translate("MainWindow", "Update"))
        self.My_pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.label_VIN_number.setText(_translate("MainWindow", "VIN:"))
        self.label_car_year.setText(_translate("MainWindow", "Year:"))
        self.label_car_model.setText(_translate("MainWindow", "Model:"))
        self.label_car_miles.setText(_translate("MainWindow", "Miles:"))
        self.label_car_maker.setText(_translate("MainWindow", "Maker:"))
        self.status_label1.setText(_translate("MainWindow", "Status:"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.actionInitialize.setText(_translate("MainWindow", "Initialize"))
        
        get_inventory(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    