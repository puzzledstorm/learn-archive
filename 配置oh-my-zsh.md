## 1.下载安装
```
git地址: https://github.com/ohmyzsh/ohmyzsh
直接安装: sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
安装不了可以使用github镜像的链接
镜像有这两个
github.com.cnpmjs.org
hub.fastgit.org
```
## 2.修改主题
```
vim ~/.zshrc
更换主题
找到ZSH_THEME="robbyrussell"改成ZSH_THEME="agnoster"
```

## 3.配置自动补全
```
1. zsh-autosuggestions,incr
有两种,我这里用incr
网址:https://mimosa-pudica.net/zsh-incremental.html
可以下载之后在~/.oh-my-zsh/plugins目录下创建文件夹incr,然后把sh脚本放进去
linux直接:
mkdir ~/.oh-my-zsh/plugins/incr
cd ~/.oh-my-zsh/plugins/incr
wget https://mimosa-pudica.net/src/incr-0.2.zsh

2. 生效
echo 'source ~/.oh-my-zsh/plugins/incr/incr*.zsh' >> ~/.zshrc
source ~/.zshrc
```

## 4.还有一些奇怪的问题需要解决
比如重复显示的问题,上次解决了,有记录

