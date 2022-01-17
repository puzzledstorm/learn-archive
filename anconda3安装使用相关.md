## 1.安装
```
略
```

## 2.一些问题
```
使用conda命令
eval "$(/root/anaconda3/bin/conda shell.bash hook)"
eval "$(/root/anaconda3/bin/conda shell.zsh hook)"

查到的一些理解:
eval "$(shell-command)" will run shell-command and feed its output to the shell as a command to execute.
A hook in this context is a mechanism to attach custom actions to some event processed by a software.

It will eval the result/output from the subcommand.
For example, eval "$(echo echo test)" will output test.
(Reproduced here with modified formatting.)
```

## 3.conda换源
```
恢复默认源：
conda config --remove-key channels
换源：
(清华源)
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
(中科大源)
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/'
显示url
conda config --set show_channel_urls yes

```
## 4.conda命令
```
conda --help
conda info查看信息
```
