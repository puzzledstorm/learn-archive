## 1.centos7联网
```
https://blog.csdn.net/gengkui9897/article/details/108017531
```
## 2.换yum源
```
https://blog.csdn.net/xiaojin21cen/article/details/84726193
https://blog.csdn.net/XuHang666/article/details/82994389
```
## 3.安装ssh
```
yum list installed | grep openssh-server

yum install openssh-server -y

启动ssh
service sshd start
systemctl start sshd.service


重启OpenSSH服务
service sshd restart
设置开机启动
systemctl enable sshd.service

修改配置
vim /etc/ssh/sshd_config

Port=22  设置SSH的端口号是22(默认端口号为22)

Protocol 2  启用SSH版本2协议

ListenAddress 192.168.0.222  设置服务监听的地址

DenyUsers   user1 user2 foo  拒绝访问的用户(用空格隔开)

AllowUsers  root osmond vivek  允许访问的用户(用空格隔开)

PermitRootLogin  no  禁止root用户登陆

PermitEmptyPasswords no  用户登陆需要密码认证

PasswordAuthentication  yes  启用口令认证方式

https://blog.csdn.net/wang704987562/article/details/72722263
```
## 4.vim
```
yum install vim -y
```
