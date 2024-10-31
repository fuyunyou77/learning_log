# python"学习日志"web项目

本项目来自《Python编程：从入门到实践》第二版，是项目篇的第三个项目。项目代码是书中三章的集合，由于Django版本原因，有极少数改动。建议按照书中内容自行编写代码，遇到问题再参考本项目。

代码写完之后发现这书有第三版，代码本身的结构没有大的变动，本项目仍具有参考价值，具体变化参考书中的修订记录。

更建议按照第三版内容学习。

两版书籍的下载地址：<a href="https://pan.baidu.com/s/1wXJZYXXLUcWr4nU5CzKi9Q?pwd=lvso">百度网盘下载</a>
提取码：lvso

## 项目结构

`learning_log`,`learning_logs`,`users`,`manage.py`是文件的主要部分，包括项目的核心代码、数据库模型、用户模型、管理脚本。
其他文件与项目本身无关。

## 运行项目

安装的环境依赖在requirements.txt文件中(其中有一些不相关的库，也可以按照书中内容一步一步安装),使用`python install -r requirements.txt`命令安装依赖。

1. 进入项目目录，运行`python manage.py runserver`命令启动服务器。
2. 打开浏览器，访问`http://localhost:8000/`，进入登录页面。
3. 输入自定义的用户名和密码登录即可，主要分为admin和user两种角色，admin可以管理所有用户，user只能查看自己的学习记录。

<mark>注意</mark>:详细的环境配置请查看<a href="https://github.com/fuyunyou77/alien_invasion/blob/master/python%E5%85%A5%E9%97%A8%E9%A1%B9%E7%9B%AE%E9%85%8D%E7%BD%AE.md">python入门项目配置文件</a>

## 注意事项

1. 在第二版书中，django版本为2.x,如果下载的是最新版本的django，可能有些代码需要修改，具体在分享的书籍中用黄色高亮标记出来了，阅读时请注意。第三版书籍则没有这个问题。

2. 第二版书中部署项目使用的Heroku在2022年不再提供免费服务。不论按照那本书籍的代码进行学习，最后部署项目请参照第三版的教程，其中使用的是platform.sh，需要掌握科学上网的方法，而且较为繁琐。

## 关于platform的部署

<mark>注意:以下教程在我自认为部署过程中是没有问题的，但最后部署到平台上使用平台给的链接访问时，会返回502错误，原因未知，可能是平台的问题，总之还是写下来，希望能帮到大家。最后部署完成生成的几个访问连接，放在文件最后了，但是访问不了</mark>

首先按照书中的教程，把响应的配置文件添加上（.yaml文件）,然后按下面的步骤进行部署：

1. 注册一个platform.sh账号
  进入platform.sh网站，点击右上角的“free trail”按钮注册一个账号。
  <mark>注意</mark>：一定要选择“free trail”按钮注册，否则会要钱。
  <br>

2. 下载platform CLI
  这个CLI有多种方式下载，可以选择自己喜欢的下载方式，比如直接下载安装包，也可以使用命令行输入命令下载。详情请参照：<a href="https://docs.platform.sh/gettingstarted/cli.html#download-the-platform-cli">platform CLI下载</a>

  我使用的是scoop下载,因此需要先安装scoop(这就是套娃😅)，<a href="https://muxiner.github.io/using-scoop/">scoop安装点这里</a>或者<a href="https://github.com/ScoopInstaller/Install#for-admin%20for%20details.">查看官方文档</a>。
  
  简单说一下scoop吧：
  scoop是一个windows下的软件包管理器，类似于linux下的apt-get、yum等。
  scoop默认安装在c盘，但是我不喜欢安装在c盘，使用如下方法可自定义安装路径。
  
  打开powershell，输入以下命令：
  
  ```powershell
    #先安装scoop安装脚本
    irm get.scoop.sh -outfile 'install.ps1' 
    #通过脚本安装scoop
    .\install.ps1 -ScoopDir '自己希望的安装路径' -ScoopGlobalDir '以后使用scoop安装的全局软件的路径'
    #查看是否安装成功
    scoop version
  ```  

  ![20241031153939](https://fuyunyou-note.oss-cn-wuhan-lr.aliyuncs.com/typora-user-images/20241031153939.png)

  确认scoop安装成功后，然后就可以下载platform CLI了，输入以下命令：

  ```powershell
    scoop bucket add platformsh https://github.com/platformsh/homebrew-tap.git
    scoop install platform
  ```

  等待下载完成即可。

3. 登录platform：(建议挂代理)
  书中写的是直接输入`platform login`，但是应该先输入`platform`命令，然后选择登录，输入账号密码登录。

    * 登陆时还可能遇到问题：找你要验证,如下所示
    [0] SMS message
    [1] whatsapp message
    [2] call

    选第一项，收sms验证码，但是国内手机号收不到，挂代理也不行。
    所以需要SMS短信代收，<a href="https://zh.receive-sms.cc/">代收网站点这里</a>。截止到2024年10月还能用，但是不保证长期有效。
    如果失效，这里有个github项目收集了很多SMS代收网站：<a href="https://github.com/nhitoshi60/sms-reception">其他代收网站</a>。但很多都没用，自己慢慢试吧。

登录成功如下所示：

![20241031160722](https://fuyunyou-note.oss-cn-wuhan-lr.aliyuncs.com/typora-user-images/20241031160722.png)

以上步骤完成后，可以按照书中的`plattform create`教程进行。

but！！！ 别急还有变动😣😣😣。

直接使用`platform create`命令创建项目时，还会有以下的问题，我没有截图。

第一种：大意是说要想创建project，必须先创建一个organization，按照命令行的指引来注册一个organization就行了。

第二种：在注册organization时，这个organization必须要有billing，而我没有billing，所以报错。
这意味着注册账号时没有选择“free trail”，要找你要钱了。需要用另外的账号重新注册。

到这里，按照树上的教程创建project，push，获取url，就可以了。

给出的链接如下所示：
（四个连接全部指向同一个网站）
  [0] `https://master-7rqtwti-54c6qbvhvgyts.ca-1.platformsh.site/`
  [1] `https://www.master-7rqtwti-54c6qbvhvgyts.ca-1.platformsh.site/`
  [2] `http://master-7rqtwti-54c6qbvhvgyts.ca-1.platformsh.site/`
  [3] `http://www.master-7rqtwti-54c6qbvhvgyts.ca-1.platformsh.site/`

最后的最后，折腾了那么多，结果会报502的错，气死人了。但是还是写出来了，希望在一些问题上能起到参考作用，就算没人看，也能喂给ai。