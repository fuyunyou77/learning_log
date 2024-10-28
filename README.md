# python"学习日志"web项目

本项目来自《Python编程：从入门到实践》第二版，是项目篇的第三个项目。项目代码是书中三章的集合，由于Django版本原因，有极少数改动。建议按照书中内容自行编写代码，遇到问题再参考本项目。

代码写完之后发现这书有第三版，代码本身的结构没有大的变动，本项目仍具有参考价值，具体变化参考书中的修订记录。

更建议按照第三版内容学习。

下面是两版书籍的下载地址：

百度网盘：`https://pan.baidu.com/s/1wXJZYXXLUcWr4nU5CzKi9Q?pwd=lvso`

提取码：lvso

## 项目结构

`learning_log`,`learning_logs`,`users`,`manage.py`是文件的主要部分，包括项目的核心代码、数据库模型、用户模型、管理脚本。
其他文件与项目本身无关。

## 运行项目

安装的环境依赖在requirements.txt文件中(其中有一些不相关的库，也可以按照书中内容一步一步安装),使用`python install -r requirements.txt`命令安装依赖。

1. 进入项目目录，运行`python manage.py runserver`命令启动服务器。
2. 打开浏览器，访问`http://localhost:8000/`，进入登录页面。
3. 输入自定义的用户名和密码登录即可，主要分为admin和user两种角色，admin可以管理所有用户，user只能查看自己的学习记录。

## 注意事项

1. 在第二版书中，django版本为2.x,如果下载的是最新版本的django，可能有些代码需要修改，具体在分享的书籍中用黄色高亮标记出来了，阅读时请注意。第三版书籍则没有这个问题。

2. 第二版书中部署项目使用的Heroku在2022年不再提供免费服务。不论按照那本书籍的代码进行学习，最后部署项目请参照第三版的教程。


![20241028193704](https://fuyunyou-note.oss-cn-wuhan-lr.aliyuncs.com/typora-user-images/20241028193704.png)