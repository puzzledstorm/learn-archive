## 在flask接口中控制一个线程的启动和停止,demo
### demo代码
```
# Python program killing threads using stop flag
import threading
import time
from flask import Flask, redirect, url_for, request, session

result = []
stop_threads = False
app = Flask(__name__)


class R:
    def __init__(self):
        pass

    def run(self, stop):
        i = 0
        while True:
            i = i + 1
            time.sleep(1)
            result.append(i)
            print(f'thread running {i}')
            if stop():
                break


def do_some(s):
    r = R()
    r.run(s)


def do_stop():
    global stop_threads
    stop_threads = True


def do_reset():
    global stop_threads, result
    result = []
    stop_threads = False


def main():
    time.sleep(0.0001)
    do_stop()
    print('thread killed')


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        do_reset()
        t1 = threading.Thread(target=do_some, args=(lambda: stop_threads,))
        t1.start()
        return {"start": "ok"}


@app.route('/stop', methods=['GET', 'POST'])
def stop():
    if request.method == 'GET':
        do_stop()
        print(result)
        print('thread killed')
        return {"stop": "ok"}


if __name__ == '__main__':
    # main()
    # print(result)
    app.run()

```

### demo测试, test.http
```
###
GET http://127.0.0.1:5000/start

###
GET http://127.0.0.1:5000/stop
```

```
"C:\puzzle\softwareInstall\Program Files\Python39\python.exe" D:\DProject\puzzle\repository\ferfull\face\test\data\d2.py 
 * Serving Flask app 'd2'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [21/Jun/2023 14:03:17] "GET /start HTTP/1.1" 200 -
thread running 1
thread running 2
thread running 3
thread running 4
127.0.0.1 - - [21/Jun/2023 14:03:22] "GET /stop HTTP/1.1" 200 -
[1, 2, 3, 4]
thread killed
thread running 5
127.0.0.1 - - [21/Jun/2023 14:03:29] "GET /start HTTP/1.1" 200 -
thread running 1
thread running 2
thread running 3
thread running 4
thread running 5
thread running 6
thread running 7
127.0.0.1 - - [21/Jun/2023 14:03:36] "GET /stop HTTP/1.1" 200 -
[1, 2, 3, 4, 5, 6, 7]
thread killed
thread running 8
```
## 参考
```
杀死线程的方法，选择最简单的和最合适的
https://zhuanlan.zhihu.com/p/142781154
```
