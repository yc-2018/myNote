# 1.安装集成环境

https://www.phpenv.cn/download.html

![image-20230801163146827](https://gitee.com/yc556/md-pic/raw/master/image-20230801163146827.png)



## 安装PHP依赖管理工具Composer



![image-20230801163306350](https://gitee.com/yc556/md-pic/raw/master/image-20230801163306350.png)



### 安装ThinkPHP`6.0`

> https://www.kancloud.cn/manual/thinkphp6_0/1037481



切换到你的WEB根目录下面并执行下面的命令（这里的`tp`目录名你可以任意更改，这个目录就是我们后面会经常提到的应用根目录。）

```php
composer create-project topthink/think tp
```

就会生产一个项目，目录名就是tp

> **测试运行**
>
> 进入`tp`下运行
>
> ```
> php think run
> ```
>
> 在浏览器中输入地址：
>
> ```
> http://localhost:8000/
> ```
>
> 会看到欢迎页面。恭喜你，现在已经完成`ThinkPHP6.0`的安装！
>
> 如果你本地80端口没有被占用的话，也可以直接使用
>
> ```
> php think run -p 80
> ```
>
> 然后就可以直接访问：
>
> ```
> http://localhost/
> ```
>
> ==实际部署中，应该是绑定域名访问到`public`目录，确保其它目录不在WEB目录下面。==
