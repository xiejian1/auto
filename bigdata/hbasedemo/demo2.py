from hbasedemo.demo1 import conn

from hbase.ttypes import ColumnDescriptor

#定义列簇
client = conn()
column1 = ColumnDescriptor(name='department')
column2 = ColumnDescriptor(name='role')
column3 = ColumnDescriptor(name='account')
column4= ColumnDescriptor(name='job')
#创建表
client.createTable('cyit',[column1,column2,column3,column4])
print(client.getTableNames())