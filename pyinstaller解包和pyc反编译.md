## 1.pyinstaller解包
使用[pyinstxtractor.py](https://github.com/extremecoders-re/pyinstxtractor/blob/master/pyinstxtractor.py)

https://github.com/extremecoders-re/pyinstxtractor
## 2.反编译pyc
[Decompyle++ ](https://github.com/zrax/pycdc)

有大佬build过，直接下载用

https://github.com/TheHellTower/decompyle-builds/releases

软件直接下载

https://github.com/TheHellTower/decompyle-builds/releases/download/build-29-Jun-2023-bb54b27/pycdc.exe

## 3.由于有很多pyc文件，而且还没有直接输出到文件，我写了一个转换脚本
```python
import glob
import sys
import os
import subprocess

save_dir = "pys"
os.makedirs(save_dir, exist_ok=True)

original_stdout = sys.stdout

pycs = glob.glob("*.pyc")
for pyc in pycs:
    py_file_path = os.path.join(save_dir, pyc[:-1])
    with open(py_file_path, 'w') as py_file:
        sys.stdout = py_file
        # os.system(f"pycdc.exe {pyc}")
        # subprocess.call(f"pycdc.exe {pyc}")
        cmd = f"pycdc.exe {pyc}"
        # returns output as byte string
        returned_output = subprocess.check_output(cmd)
        # using decode() function to convert byte string to string
        print(returned_output.decode())

# Restore stdout
sys.stdout = original_stdout
```

## 4.参考
```
https://blog.csdn.net/loovelj/article/details/107364022
https://github.com/extremecoders-re/pyinstxtractor
https://github.com/zrax/pycdc
https://github.com/TheHellTower/decompyle-builds
https://github.com/linyiLYi/street-fighter-ai/blob/master/main/train.py
https://www.digitalocean.com/community/tutorials/python-system-command-os-subprocess-call
```
