import sqlite3, time
from PyQt5 import QtCore, QtGui, QtWidgets
con = sqlite3.connect('My_inventory.db')
my_cursor = con.cursor ()

def initialize(self):
  try:
    sql = 'DROP TABLE IF EXISTS CARS_INVENTORY'
    sql2 = 'CREATE TABLE CARS_INVENTORY (carId INTEGER(5) NOT NULL PRIMARY KEY, year int(4) NOT NULL, model CHAR(10) NOT NULL, miles int(6), maker CHAR (15))'
    my_cursor.execute(sql)
    my_cursor.execute(sql2)
    con.commit
    self.status_label2.setText('---DB Initialized---')
    for i in range (self.tableWidget.rowCount(), -1, -1):
      self.tableWidget.removeRow(i)       


  except Exception as e:
    self.status_label2.setText(str(e))
    con.rollback

def insert_data (carId, year, model, miles, maker, self):
   
  try:
    rec = (int(carId), int(year), model, int(miles), maker)	
    sql = 'INSERT INTO CARS_INVENTORY VALUES (?, ?, ?, ?, ?)'
    my_cursor.execute(sql, rec)
    con.commit()
    self.status_label2.setText("New record inserted")

  except Exception as e:
    self.text__VIN_number.setDisabled(False)
    self.status_label2.setText(str(e) + ". VIN, year & miles should be integers.")
    #print ('Error :', e)
    con.rollback()
 

def delete_data (data, param, self):
  #rec = (carId, year, model, miles, maker)	
  sql = 'DELETE FROM CARS_INVENTORY WHERE CARS_INVENTORY.' + param + '=' + data
  try:
    my_cursor.execute(sql)
    con.commit()
    sql = 'SELECT * FROM CARS_INVENTORY WHERE CARS_INVENTORY.carId =' + data
    my_cursor.execute(sql)
    records = my_cursor.fetchone()
    #print(records)
    if not records:
      self.status_label2.setText('No records for that VIN number. The car was either deleted or you type an inexistent VIN number.')
      #print('No records for that VIN number. The car was either deleted or you type an inexistent VIN number.')
    else:
      self.status_label2.setText('The VIN number is still in the system.')
      #print ('The VIN number is still in the system.')
  except Exception as e:
    self.status_label2.setText(e)
    #print ('Error3 :', e)
    con.rollback()

def fill_combo_box(param, self):
  sql = 'SELECT DISTINCT ' + param + ' FROM CARS_INVENTORY ORDER BY ' + param + ' ASC'
  my_cursor.execute(sql)
  records = my_cursor.fetchall()
  self.My_comboBox.clear()
  c = 0
  for record in records:
    #print(records)
    #print(str(record[c]))
    self.My_comboBox.addItem("")
    self.My_comboBox.setItemText(c, str(record[0]))
    c += 1
  #print(records)


def update_data(carId, year, model, miles, maker, self):
  sql = 'UPDATE CARS_INVENTORY SET year =' + str(year) + ', model =\'' + model + '\', miles =' + str(miles) + ', maker =\'' + maker + '\' WHERE carId =' + str(carId)
  try:
    my_cursor.execute(sql)
    con.commit()
    self.status_label2.setText("Record updated")
  except Exception as e:
    self.status_label2.setText(str(e) + ". Year & miles should be integers.")
    #print ('Error :', e)
    con.rollback()
    
def retrieve_data (data, param, self):
  if param == 'year':
    sql = 'SELECT * FROM CARS_INVENTORY WHERE CARS_INVENTORY.' + param + '=' + "'" + data + "'"
  elif param == 'maker':
    sql = 'SELECT * FROM CARS_INVENTORY WHERE CARS_INVENTORY.' + param + '=' + "'" + data + "'"
  elif param == 'model':
    sql = 'SELECT * FROM CARS_INVENTORY WHERE CARS_INVENTORY.' + param + '=' + "'" + data + "'"
  elif param == 'all':
    sql = 'SELECT * FROM CARS_INVENTORY ORDER BY CarId ASC'
  try:
    #item = self.QtWidgets.QTableWidgetItem()
    my_cursor.execute(sql)
    records = my_cursor.fetchall()
    if len(records) > 0:
      c = 0
      self.tableWidget.setRowCount(len(records))
      self.tableWidget.setColumnCount(5)
      for record in records:
        if c < len(records):
          for j in range (0, self.tableWidget.columnCount()):
             #Crea un elemento de QtWidget
            item = QtWidgets.QTableWidgetItem() 
            item.setFlags(QtCore.Qt.ItemIsEnabled) #prevent the user from editing the table
            item.setBackground(QtGui.QColor('light yellow')) #set the background color
            item.setForeground(QtGui.QColor('blue')) #set the foreground color
            #item.setFont(QtGui.)
            font = QtGui.QFont()
            #font.setBold(True)
            font.setPointSize(9)
            item.setFont(font)
            self.tableWidget.setItem(c, j, item)
            #self.tableWidget.resizeColumnsToContents() 
            self.tableWidget.setHorizontalHeaderLabels(['VIN','Year', 'Model', 'Miles','Maker'])
            
            item1 = self.tableWidget.item (c, j)
            item1.setText(str(record[j])) 
            #font1 = QtGui.QFont()
            #font1.setBold(True)
            #font1.setPointSize(12)
            #item1.setFont(font1) 
            #item1.setForeground(QtGui.QColor('blac'))        
            #print(str(i) + ',' + str(j))
          c += 1  
        
      #return record
    else:
      self.status_label2.setText('--No records found--')
      self.tableWidget.removeRow(0) #delete the table row when deleting the last element in DB
      #print('--No records found--')
      #return record
  except Exception as e:
    if str(e) == 'no such table: CARS_INVENTORY':
      initialize(self)
    else:
      self.status_label2.setText(e)
    
    #print ('<<DB could be empty or no records return for that query>>')
  