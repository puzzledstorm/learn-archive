##  1.git地址
```
https://github.com/wkentaro/labelme
```
## 2.在centos8中安装labelme
```
安装了anconda

# python3
conda create --name=labelme python=3.8
source activate labelme
pip install labelme
# 运行安装labelme之后会自动安装相关依赖
------------------------
Successfully installed Pillow-9.0.0 PyQt5-5.15.6 PyQt5-Qt5-5.15.2 PyQt5-sip-12.9.0 
PyYAML-6.0 cycler-0.11.0 imgviz-1.4.1 kiwisolver-1.3.2 labelme-4.6.0 
matplotlib-3.2.2 numpy-1.22.0 packaging-21.3 pyparsing-3.0.6 
python-dateutil-2.8.2 qtpy-2.0.0 six-1.16.0 termcolor-1.1.0
```
## 3.还是在windows下打包labelme吧，linux下我没有找到合适的方法，打包出来的是可执行文件，但是windows下又不能用。
```
1.下载anconda3,我已经下载了，略
2. git clone https://github.com/wkentaro/labelme.git
3. conda create --name labelme python==3.6.0
activate labelme
查看有几个python虚拟环境，conda env list
4. 安装upx
https://upx.github.io/
当然是win64了
wget https://github.com/upx/upx/releases/download/v3.96/upx-3.96-win64.zip
把解压出来的upx.exe放到C:\Windows\System32目录下，
或者我认为添加环境变量应该也可以，懒得试了。
5. pyinstaller 文档： https://pyinstaller.readthedocs.io/en/stable/operating-mode.html
6.进入labelme python虚拟环境
进入labelme的代码目录
# Build the standalone executable
pip install .
pip install pyinstaller
pyinstaller labelme.spec
dist/labelme --version
```
