import psutil

mem = psutil.virtual_memory()
print("总的内存"+str(mem.total))
print("已使用的内存："+str(mem.used))
print("空闲的内存"+str(mem.free))
print("内存使用占比："+str(mem.percent))
print('\n')
print(mem)
