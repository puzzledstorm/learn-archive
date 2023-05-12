# win11下WSL2使用Docker搭建gitlab

## 1.拉镜像，启动容器
```
docker pull gitlab/gitlab-ce:latest
docker run --detach --hostname localhost --publish 443:443 --publish 80:80 --publish 22:22 --name gitlab --volume /home/huo/gitlab/config:/etc/gitlab --volume /home/huo/gitlab/logs:/var/log/gitlab --volume /home/huo/gitlab/data:/var/opt/gitlab -m 3g  gitlab/gitlab-ce:latest 
```

## 2.进入容器，修改管理员root用户密码
```
docker exec -it gitlab /bin/bash 

root@123:/# gitlab-rails console -e production
--------------------------------------------------------------------------------
 Ruby:         ruby 2.7.2p137 (2020-10-01 revision 5445e04352) [x86_64-linux]
 GitLab:       14.0.5 (25fc1060aff) FOSS
 GitLab Shell: 13.19.0
 PostgreSQL:   12.6
--------------------------------------------------------------------------------
Loading production environment (Rails 6.1.3.2)
irb(main):001:0> user=User.where(id:1).first
=> #<User id:1 @root>
irb(main):002:0> user.password='12345678fF!'
=> "12345678fF!"
irb(main):003:0> user.password_confirmation='12345678fF!'
=> "12345678fF!"
irb(main):004:0> user.save!
Enqueued ActionMailer::MailDeliveryJob (Job ID: 89e9421a-8a23-4789-8833-d063410200cc) to Sidekiq(mailers) with arguments: "DeviseMailer", "password_change", "deliver_now", {:args=>[#<GlobalID:0x00007f5e32c89168 @uri=#<URI::GID gid://gitlab/User/1>>]}
=> true
irb(main):005:0> exit
```

## 3.可选，映射windows ip的 8088 端口到 WSL2的ip的 80 端口,不想映射直接进入wsl2，直接使用ip a命令查看ip,在浏览器输入查询出的ip（192.168.183.43，这是我查出我的ip）就行。
```
netsh interface portproxy add v4tov4 listenport=8088 listenaddress=0.0.0.0 connectport=80 connectaddress=192.168.183.43
```
这步骤做完之后，可以浏览器输入http://localhost:8088/ 访问, 不做也可以直接http://192.168.183.43 访问。

## 参考
```
https://blog.51cto.com/u_15127505/3444297
https://blog.csdn.net/Yxc19950122/article/details/126728247
```
