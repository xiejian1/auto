from hbasedemo.demo1 import conn


client = conn()
result = client.get('user','lisi','account:password')
print(result)
print(result[0].value)
# result = client.getVer('user', 'lisi', 'userid:id', numVersions = 2)
# # print(result[0].value)
print('\n')
allcf = client.getColumnDescriptors('user')  # 获取表的所有列族
print('test表的列族',allcf)