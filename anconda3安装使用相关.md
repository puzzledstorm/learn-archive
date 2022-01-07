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

