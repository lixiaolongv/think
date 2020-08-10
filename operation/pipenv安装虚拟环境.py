#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 1:11 下午
# @Author  : BruceLee
# @Site    : 
# @File    : pipenv安装虚拟环境.py

"""
pipenv install
为这个项目创建虚拟环境
pipenv shell
激活这个虚拟环境
pip list
查看虚拟环境所安装的包
exit
退出虚拟环境
pipenv uninstall
卸载包
pipenv graph
安装依赖包关系

pipenv --venv
查询当前的虚拟环境是哪个

pipenv --where
查询当前项目的绝对路径

状态码解析大全
308 -- Permanent Redirect 永久重定向
https://www.bookstack.cn/read/http-status-code/15.md
"""
"""
第一节：
重点1：flask必须保证URL的唯一性原则
@app.route('/hello/')
兼容访问地址：http://127.0.0.1:5000/hello/，最后的"/"，浏览器会做重定向的处理，其中请求是【"GET /hello HTTP/1.1" 308 -】
flask --- 必须保证唯一URL的原则，URL的末尾"/"加与不加，请求的链接不一致

重点2：开启调试模式，动态修改就可直接显示结果
app.run(debug=true)
重启后，服务显示：Debugger is active!且资源会reloading

重点3：路由的两种注册方法
第一种：@app.route('/hello')，一般使用装饰器，优雅
第二种：app.add_url_rule('/hello', view_func=hello)，基于类的视图（即插视图必须使用该视图）

重点4：部署生产环境时，IP地址如何指定
app.run(host='0.0.0.0', debug=True, port=81)
访问URL：http://192.168.1.2:81/hello
本机IP地址查询命令：ifconfig
192.168.1.2

重点5：约定常量都是大写的

重点6：导入配置的方法
# from yourapplication import default_config
app.config.from_object('config') 参数是模块的路径
from_object()，该方法必须要求config文件中的所有变量都是大写，谨记谨记！！！
DEBUG默认的值是false

重点7：为什么需要使用if __name__ == '__main__'，原因是只能在当前模块执行，导入或者部署到生产也不会执行

@app.route('/hello')
def hello():
    headers = {
        "content-type": "text/plain",
        "location": "http://www.bing.com"
    }
    response = make_response("<html></html>", 302)
    response.headers = headers
    return response

重点8：http请求的一般元素
status_code
content-type = text/html，默认的类型
http
header
最终返回的是：response对象

Content-Type 标头告诉客户端实际返回的内容的内容类型。
一般是指网页中存在的 Content-Type，用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件
常见的媒体格式类型如下：
text/html ： HTML格式
text/plain ：纯文本格式
text/xml ： XML格式
image/gif ：gif图片格式
image/jpeg ：jpg图片格式
image/png：png图片格式

Location:	
表示客户应当到哪里去提取文档。Location通常不是直接设置的，而是通过HttpServletResponse的sendRedirect方法，该方法同时设置状态代码为302


重点9：熟悉代码为什么需要重购？

重点10：熟悉怎样阅读代码，学会分层阅读即可，知道某个函数是做什么的即可，不需要具体阅读内部代码逻辑！

重点11：flask的路由机制有三层，分别是：url ----> endpoint ----> view_func【路由原理？？】
app.add_url_rule('/hello', view_func=hello, endpoint=hello), 当不传endpoint时，默认值是view_func
@app.route('/hello', endpoint=hello), 路由也可以传endpoint？？？

重点12：flask的蓝图结构：
第一层：APP
第二层：蓝图1，蓝图2，蓝图3
第三层：每个蓝图都对应相应的文档（静态文件，视图函数，模板）

1，视图函数需要注册到蓝图上，蓝图也需要注册到flask核心对象APP上

重点13：如何使一个模块变成包，请理解__init__.py 文件

不可变字典
to_dict()可以转变成最常用的字典

wtforms
验证层

7月31日：
1，买一本当前最新的Python书籍
2，看源代码
"""