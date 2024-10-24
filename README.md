# python"学习日志"web项目

本项目来自《Python编程：从入门到实践》第二版，是项目篇的第三个项目。项目代码是书中三章的集合，由于Django版本原因，有极少数改动。建议按照书中内容自行编写代码，遇到问题再参考本项目。

书籍地址: `https://pan.baidu.com/s/157cDUV4YM8b5wGUoQ9dQaw?pwd=i5z8`

提取码：i5z8

## 项目结构

`learning_log`,`learning_logs`,`users`,`manage.py`是文件的主要部分，包括项目的核心代码、数据库模型、用户模型、管理脚本。
其他文件与项目本身无关。

## 运行项目

安装的环境依赖在requirements.txt文件中(其中有一些不相关的库，也可以按照书中内容一步一步安装),使用`python install -r requirements.txt`命令安装依赖。

1. 进入项目目录，运行`python manage.py runserver`命令启动服务器。
2. 打开浏览器，访问`http://localhost:8000/`，进入登录页面。
3. 输入自定义的用户名和密码登录即可，主要分为admin和user两种角色，admin可以管理所有用户，user只能查看自己的学习记录。

## 注意事项

书中部署项目使用的Heroku在2022年不再提供免费服务，考虑到这只是一个入门的简单项目，不值得花钱部署，所以只能本地运行。不过代码中涉及到远程部署到Heroku的设置已完成。
如果要部署服务器上，选择其他heroku的替代产品，也可以自己租用云服务器实现，请参考其他网络教程。
