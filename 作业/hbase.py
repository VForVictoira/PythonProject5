import happybase
from thrift import Thrift

connection = happybase.Connection(host='localhost', port=9090)
connection.open()
print(connection.tables())
connection.close()