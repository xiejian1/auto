import requests
import json
import psutil
import  socket
import datetime

class GetCpu():

    def cpu(self):

        mem = psutil.virtual_memory()
        total = mem.total
        used = mem.used
        free = mem.free
        percent = mem.percent

        return {
            "total":total,
            "used":used,
            "free":free,
            "percent":percent,
        }

    #获取主机的ip地址
    def get_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()

        finally:
            s.close()

        return ip[0]

    #获取部署的爬虫项目
    def get_project(self):

        host = 'http://139.159.140.183:'
        port = 6880
        url = host+str(port)+'/listprojects.json'
        response = requests.get(url=url)
        data = json.loads(response.text)
        projects = data["projects"]

        return projects

    def run(self):
        cpu = self.cpu()
        ip = self.get_ip()
        projects = self.get_project()
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'total':cpu['total'],
            'used':cpu['used'],
            'free':cpu['free'],
            'percent':cpu['percent'],
            'ip':ip,
            'spiders':projects,
            'time':time,
        }
        headers = {
            'content-type': 'application/json',
        }
        content = requests.post(url='http://139.159.140.183:8090/monitor/get_cpu/', data=json.dumps(data), headers=headers)
        print(content.text)


if __name__ == '__main__':

    cpu = GetCpu()
    print(cpu.get_project())