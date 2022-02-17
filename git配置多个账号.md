## 参考链接
```
https://finisky.github.io/multiplegithubaccountsononemachine/
https://www.jianshu.com/p/b15f2b5d87c6
https://blog.csdn.net/argleary/article/details/100638560
```


### [文章来源](https://finisky.github.io/multiplegithubaccountsononemachine/)
在同一机器上对不同repo使用不同的github账号是个常见需求。举个例子，repo1托管在github账号x1下，而repo2托管在账号x2下，如何方便地在同一机器上使用不同账号自动git push到对应的远端？比较直接的做法是在不同repo目录下使用git config配置用户名，但这样有两个问题：

每个repo都要配置一遍比较繁琐
有些情况下无法配置。比如使用 hexo-deployer-git 部署Hexo网站时，.deploy_git目录是动态生成的，而所用的git账户和远端url修改不便。
于是，我们可以借用SSH config文件来把不同github账号与repo联系起来。在SSH config中定义多个不同的host项即可，然后在访问github时，使用一个虚拟host作为别名代替真正的主机名github.com即可。

生成SSH Key
直接按步骤来即可： # Generating a new SSH key and adding it to the ssh-agent
```
$ ssh-keygen -t ed25519 -C "your_email@example.com"

Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/user/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user/.ssh/id_ed25519
Your public key has been saved in /home/user/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256: xxx your_email@example.com
Add your SSH private key to the ssh-agent:

$ ssh-add ~/.ssh/id_ed25519
Identity added: /home/user/.ssh/id_ed25519 (your_email@example.com)
```
添加公钥到GitHub账户
按Tutorial步骤来，点点鼠标复制粘贴即可： # Adding a new SSH key to your GitHub account

拷贝公钥:
```
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 xxxx your_email@example.com
```
然后把公钥通过GitHub配置页添加至账户: Profile Photo -> Settings -> SSH and GPG keys -> New SSH keys

编辑SSH Config
这是最重要的的部分，编辑 ~/.ssh/config （不存在则创建一个）:
```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa

Host githubx1
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_x1

Host githubx2
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_x2
 ```
各字段的解释：
```
Host: 主机别名，也是每段定义项的名字，将来用这个别名来指代所用的用户名及私钥
HostName: 要登录的远端主机名 (对github来说就是github.com)
User: SSH连接所用的用户名 (对github来说就是git)
IdentityFile: 上面生成的私钥
假设上面示例文件中的私钥和账户对应关系如下:

id_rsa -> main@example.com
id_rsa_x1 -> x1@example.com
id_rsa_x2 -> x2@example.com
```
一个repo的远端url大概长这样:
```
git@github.com:finisky/TextCNN.git
```
对于无SSH config或上面的示例配置，使用上面url (github.com) 进行访问时，使用的是账户main@example.com。如果我们想用x1@example.com来访问此repo，需要将它的主机名改一下，与SSH config中的配置相对应：
```
git@githubx1:finisky/TextCNN.git
```
测试连接
验证上面配置是否生效也很简单，使用下面命令测试即可：
```
$ ssh -T git@githubx1
Hi x1! You've successfully authenticated, but GitHub does not provide shell access.

$ ssh -T git@githubx2
Hi x2! You've successfully authenticated, but GitHub does not provide shell access.

$ ssh -T wrongusername@githubx2
wrongusername@github.com: Permission denied (publickey).
```
如果登录成功，Hi之后会显示对应登录账户的GitHub用户名。
