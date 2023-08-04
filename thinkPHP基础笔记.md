# ==1==.安装集成环境

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



### 域名重写

**==如果是通过phpEnv运行就要==**，如果是，命令行就不需要

没配：`http://demo.org/index.php/index/ikun`

配了：`http://demo.org/index/ikun`

![image-20230804174405719](https://gitee.com/yc556/md-pic/raw/master/image-20230804174405719.png)

> ```
> location ~* (runtime|application)/{
>     return 403;
> }
> location / {
>     if (!-e $request_filename){
>         rewrite  ^(.*)$  /index.php?s=$1  last;   break;
>     }
> }
> ```
>
> >1. location ~* (runtime|application)/{}: 对 runtime 和 application 目录,返回 403 禁止访问。
> >2. location / {}: 对所有的请求路径,如果请求的文件不存在,则重写到 index.php,参数为请求路径。
> >3. rewrite ^(.*)$ /index.php?s=$1 last; break;: 将路径重写到 index.php,参数命名为 s。
> >4. if (!-e $request_filename): 检查请求的文件是否存在,如果不存在则执行重写。
> >
> >所以这段 Nginx 配置的作用是:
> >
> >- 禁止直接访问 ThinkPHP 的 runtime 和 application 目录
> >- 如果请求的文件不存在,则将请求重写到 index.php 路由处理
> >
> >这是 ThinkPHP 项目部署时的典型 Nginx 配置,可以实现URL美化和保护系统目录。
> >
> >Nginx 的配置语言采用类似 DSL 的格式,通过 location、rewrite等指令来定义路由和重写规则。这段代码实现了针对 ThinkPHP 的重写配置。





# ==2.==thinkphp6命名规范

> `ThinkPHP6.0`遵循`PSR-2`命名规范和`PSR-4`自动加载规范，并且注意如下规范：
>
> ### 目录和文件
>
> - 目录使用小写+下划线；
> - 类库、函数文件统一以`.php`为后缀；
> - 类的文件名均以命名空间定义，并且命名空间的路径和类库文件所在路径一致；
> - 类（包含接口和Trait）文件采用驼峰法命名（首字母大写），其它文件采用小写+下划线命名；
> - 类名（包括接口和Trait）和文件名保持一致，统一采用驼峰法命名（首字母大写）；
>
> ### 函数和类、属性命名
>
> - 类的命名采用驼峰法（首字母大写），例如 `User`、`UserType`；
> - 函数的命名使用小写字母和下划线（小写字母开头）的方式，例如 `get_client_ip`；
> - 方法的命名使用驼峰法（首字母小写），例如 `getUserName`；
> - 属性的命名使用驼峰法（首字母小写），例如 `tableName`、`instance`；
> - 特例：以双下划线`__`打头的函数或方法作为魔术方法，例如 `__call` 和 `__autoload`；
>
> ### 常量和配置
>
> - 常量以大写字母和下划线命名，例如 `APP_PATH`；
> - 配置参数以小写字母和下划线命名，例如 `url_route_on` 和`url_convert`；
> - 环境变量定义使用大写字母和下划线命名，例如`APP_DEBUG`；
>
> ### 数据表和字段
>
> - 数据表和字段采用小写加下划线方式命名，并注意字段名不要以下划线开头，例如 `think_user` 表和 `user_name`字段，不建议使用驼峰和中文作为数据表及字段命名。



## PHP 关键词

| [__halt_compiler()](https://www.php.net/manual/zh/function.halt-compiler.php) | [abstract](https://www.php.net/manual/zh/language.oop5.abstract.php) | [and](https://www.php.net/manual/zh/language.operators.logical.php) | [array()](https://www.php.net/manual/zh/function.array.php)  | [as](https://www.php.net/manual/zh/control-structures.foreach.php) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [break](https://www.php.net/manual/zh/control-structures.break.php) | [callable](https://www.php.net/manual/zh/language.types.callable.php) | [case](https://www.php.net/manual/zh/control-structures.switch.php) | [catch](https://www.php.net/manual/zh/language.exceptions.php) | [class](https://www.php.net/manual/zh/language.oop5.basic.php#language.oop5.basic.class) |
| [clone](https://www.php.net/manual/zh/language.oop5.cloning.php) | [const](https://www.php.net/manual/zh/language.oop5.constants.php) | [continue](https://www.php.net/manual/zh/control-structures.continue.php) | [declare](https://www.php.net/manual/zh/control-structures.declare.php) | [default](https://www.php.net/manual/zh/control-structures.switch.php) |
| [die()](https://www.php.net/manual/zh/function.die.php)      | [do](https://www.php.net/manual/zh/control-structures.do.while.php) | [echo](https://www.php.net/manual/zh/function.echo.php)      | [else](https://www.php.net/manual/zh/control-structures.else.php) | [elseif](https://www.php.net/manual/zh/control-structures.elseif.php) |
| [empty()](https://www.php.net/manual/zh/function.empty.php)  | [enddeclare](https://www.php.net/manual/zh/control-structures.declare.php) | [endfor](https://www.php.net/manual/zh/control-structures.alternative-syntax.php) | [endforeach](https://www.php.net/manual/zh/control-structures.alternative-syntax.php) | [endif](https://www.php.net/manual/zh/control-structures.alternative-syntax.php) |
| [endswitch](https://www.php.net/manual/zh/control-structures.alternative-syntax.php) | [endwhile](https://www.php.net/manual/zh/control-structures.alternative-syntax.php) | [eval()](https://www.php.net/manual/zh/function.eval.php)    | [exit()](https://www.php.net/manual/zh/function.exit.php)    | [extends](https://www.php.net/manual/zh/language.oop5.basic.php#language.oop5.basic.extends) |
| [final](https://www.php.net/manual/zh/language.oop5.final.php) | [finally](https://www.php.net/manual/zh/language.exceptions.php) | [fn](https://www.php.net/manual/zh/functions.arrow.php)（从 PHP 7.4 开始） | [for](https://www.php.net/manual/zh/control-structures.for.php) | [foreach](https://www.php.net/manual/zh/control-structures.foreach.php) |
| [function](https://www.php.net/manual/zh/functions.user-defined.php) | [global](https://www.php.net/manual/zh/language.variables.scope.php) | [goto](https://www.php.net/manual/zh/control-structures.goto.php) | [if](https://www.php.net/manual/zh/control-structures.if.php) | [implements](https://www.php.net/manual/zh/language.oop5.interfaces.php) |
| [include](https://www.php.net/manual/zh/function.include.php) | [include_once](https://www.php.net/manual/zh/function.include-once.php) | [instanceof](https://www.php.net/manual/zh/language.operators.type.php) | [insteadof](https://www.php.net/manual/zh/language.oop5.traits.php#language.oop5.traits.conflict) | [interface](https://www.php.net/manual/zh/language.oop5.interfaces.php) |
| [isset()](https://www.php.net/manual/zh/function.isset.php)  | [list()](https://www.php.net/manual/zh/function.list.php)    | [match](https://www.php.net/manual/zh/control-structures.match.php)（从 PHP 8.0 开始） | [namespace](https://www.php.net/manual/zh/language.namespaces.php) | [new](https://www.php.net/manual/zh/language.oop5.basic.php#language.oop5.basic.new) |
| [or](https://www.php.net/manual/zh/language.operators.logical.php) | [print](https://www.php.net/manual/zh/function.print.php)    | [private](https://www.php.net/manual/zh/language.oop5.visibility.php) | [protected](https://www.php.net/manual/zh/language.oop5.visibility.php) | [public](https://www.php.net/manual/zh/language.oop5.visibility.php) |
| [readonly](https://www.php.net/manual/zh/language.oop5.properties.php#language.oop5.properties.readonly-properties)（自 PHP 8.1.0 起）* | [require](https://www.php.net/manual/zh/function.require.php) | [require_once](https://www.php.net/manual/zh/function.require-once.php) | [return](https://www.php.net/manual/zh/function.return.php)  | [static](https://www.php.net/manual/zh/language.variables.scope.php) |
| [switch](https://www.php.net/manual/zh/control-structures.switch.php) | [throw](https://www.php.net/manual/zh/language.exceptions.php) | [trait](https://www.php.net/manual/zh/language.oop5.traits.php) | [try](https://www.php.net/manual/zh/language.exceptions.php) | [unset()](https://www.php.net/manual/zh/function.unset.php)  |
| [use](https://www.php.net/manual/zh/language.namespaces.php) | [var](https://www.php.net/manual/zh/language.oop5.properties.php) | [while](https://www.php.net/manual/zh/control-structures.while.php) | [xor](https://www.php.net/manual/zh/language.operators.logical.php) | [yield](https://www.php.net/manual/zh/language.generators.php) |
| [yield from](https://www.php.net/manual/zh/language.generators.syntax.php#control-structures.yield.from) |                                                              |                                                              |                                                              |                                                              |

\* `readonly` 可用作函数名。

---

**编译时常量**

| [__CLASS__](https://www.php.net/manual/zh/language.constants.predefined.php) | [__DIR__](https://www.php.net/manual/zh/language.constants.predefined.php) | [__FILE__](https://www.php.net/manual/zh/language.constants.predefined.php) | [__FUNCTION__](https://www.php.net/manual/zh/language.constants.predefined.php) | [__LINE__](https://www.php.net/manual/zh/language.constants.predefined.php) | [__METHOD__](https://www.php.net/manual/zh/language.constants.predefined.php) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [__NAMESPACE__](https://www.php.net/manual/zh/language.namespaces.nsconstants.php) | [__TRAIT__](https://www.php.net/manual/zh/language.constants.predefined.php) |                                                              |                                                              |                                                              |                                                              |



# ==3.==开启调试模式

> 一、开启调试
>
> 在开发阶段,我们建议开启框架的调试模式。
>
> 1. 调试模式开启后,会牺牲一些执行效率,但大大提高了开发排错的能力。
>
> 2. 当项目部署到生产环境时,再关闭调试模式即可。
>
> 3. 安装好的 TP6 默认并没有开启调试,可以在域名后面胡乱输入字符回车。
>
> 4. 此时,页面只会提示:“页面错误,请稍后再试~”,表示调试未开启。
>
> 5. 通过命令行安装的 TP6.0,会自动在根目录生成一个 .env 文件。
>
> 6. ==这个 .env 文件是环境配置文件,我们只要删除前面的 .example 即可生效。==
>
> 7. ==此时,刷新页面,右下角会出现 Trace 调试小图标,说明调试开启了。==
>
> 8. ==查看 .env 文件,打开调试的环境变量为 APP_DEBUG = true,false 关闭。==
>
> 9. 那么,开启调试模式有哪些显著的优势呢?
>
>    a. 记录系统运行流程的执行过程;
>
>    b. 展示错误和调试信息,并开启日志记录;
>
>    c. 模板修改可以及时生效(不会被缓存干扰);
>
>    d. 启动右下角的 Trace 调试功能,更加强大;
>
>    e. 发生异常时,也会显示异常信息。
>
> 10. 当然,还有一种模式,就是关闭调试的时候,也可以显示简要的错误信息。
>
> 11. 首先 .env 文件设置 APP_DEBUG = false。
>
> 12. 然后,根目录下 config 的 app.php 最后一样设置为:'show_error_msg'=> true,
>



# ==4.==thinkPHP基础

## 4.1 默认方法

> 在ThinkPHP的控制器中,index()方法是一个特殊的默认方法。
>
> 如果URL中没有指定控制器方法,会自动调用index()方法。
>
> 例如:
>
> ```php
> namespace app\controller;
> 
> class Index
> {
>     public function index()
>     {
>         // 默认方法
>     }
> 
>     public function hello()
>     {
>        // 其他方法 
>     }
> }
> ```
>
> 那么:
>
> - 访问`/index/index` 会执行index()方法
>
> - 访问`/index`也会执行index()方法
>
>  index()方法不需要在URL中指定,是默认的方法。
>
> 这是因为index()这个方法名对应首页的概念,作为控制器的默认入口是合理的。
>
> 另外,默认方法名称可以在配置文件中修改:
>
> ```php
> 'controller' => [
>     'default_action' => 'otherMethod' 
> ]
> ```
>
> 这种默认方法的设计可以简化URL,同时也提高了系统的灵活性。
>
> 所以在开发ThinkPHP项目时,我们通常会把主要逻辑放在index()方法中,作为控制器的默认访问方法。





## 4.2 URL解析

1. ThinkPHP框架非常多的操作都是通过URL来实现的。

2. 多应用:http://serverName/index.php/应用/控制器/操作/参数/值...

3. 单应用:http://serverName/index.php/控制器/操作/参数/值...

4. 由于TP6默认是单应用模式,多应用需要作为扩展安装,避免混乱暂时搁置。 

5. http://serverName是域名地址,比如127.0.0.1:8000或localhost/tp6。

6. index.php这个文件,是根目录下public/下的index.php(入口文件)。

7. 控制器:app目录下有一个controller控制器目录的Test.php(控制器)。

8. Test.php控制器的类名也必须是class Test,否则错误。

9. 操作就是控制器类里面的方法,比如:index(默认免写)或hello(必写)。

10. 那么完整形式为:

a. http://localhost/tp6/public/index.php/test/hello/value/world

b. http://127.0.0.1:8000/index.php/test/hello/value/world

```php
class Test {

  public function index() {
    return "test"; 
  }

}
```

11. public/index.php 中的 index.php 可以省略,只要设置 URL 重写即可。
12. httpd.conf 配置文件中加载了 mod_rewrite.so 模块。
13. AllowOverride None 将None改为All,开启.htaccess文件的支持。
14. 此时,路径变更为:

http://localhost/tp6/public/test/hello/value/world
