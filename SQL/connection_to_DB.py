import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-I95AC83\SQLTEST' 
database = 'northwind' 
username = 'SA' 
password = 'espltdmh50' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("""
SELECT * FROM [Order Details]
WHERE ProductID IN
 (SELECT ProductID FROM PRODUCTS
  WHERE UnitsInStock > 40
  )
AND OrderID IN 
 (SELECT OrderID FROM Orders
  WHERE Freight > 50)
ORDER BY OrderID
;""") 

row = cursor.fetchone() # Запись данных в переменную построчно в виде кортежа
print('Вывод по одной строке таблицы')
for i in range(3):
  print(row)
  row = cursor.fetchone()
print('Вывод всего запроса целиком')
row = cursor.fetchall() # Запись всех данных в переменную в виде списка кортежей
print(row)