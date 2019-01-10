from hbasedemo.demo1 import conn


client = conn()
scannerId = client.scannerOpen('user','zhangsan',[])   # 在指定表中，从指定行开始扫描，到表中最后一行结束，扫描指定列的数据。
result = client.scannerGet(scannerId)   # 根据ScannerID来获取结果
print(result[0].columns)
res = result[0].columns
for key,item in res.items():
    print(key)
    print(item.value)
    print('\n')