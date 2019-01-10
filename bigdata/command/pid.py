import psutil

pids = psutil.pids()
rediscn = 0
mysqlcn = 0
mongocn = 0
for id in pids:
    p = psutil.Process(id)
    if p.name() == 'redis-server':
        name = p.name().split('-')[0]
        print(name)
        print(p.exe())
        print(p.cwd())
        print(p.status())
        rediscn = rediscn+1
    elif p.name() == 'mysqld':
        name = 'mysql'
        print(name)
        print(p.exe())
        print(p.cwd())
        print(p.status())
        mysqlcn = mysqlcn+1
        print(mysqlcn)
    elif p.name() == 'mongod':
        name = 'mongodb'
        print(name)
        print(p.exe())
        print(p.cwd())
        print(p.status())
        mongocn = mongocn+1
        print(mongocn)