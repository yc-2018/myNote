# ==java问题==

### ==1.== java类名命名规范

> Java类名的命名规范一般遵循以下几点：
>
> 1. 类名要使用大写字母开头的驼峰命名法（即首字母大写，后面每个单词的首字母也要大写）。
>
> 2. 类名应该是一个名词或者名词短语，且具有描述性。
>
> 3. 如果类名由多个单词组成，那么这些单词之间应该没有下划线符号，而是采用驼峰命名法。
>
> 4. 类名不要使用Java关键字。
>
> 例如，如果你编写一个代表学生的类，你可以将它命名为"Student"。如果你编写一个代表图书馆的类，你可以将它命名为"Library"。
>
> ---
>
> **java方法命名规范**
>
> Java方法的命名规范一般遵循以下几点：
>
> 1. 方法名使用小写字母开头的驼峰命名法（即首字母小写，后面每个单词的首字母大写）。
>
> 2. 方法名应该是一个动词或者动词短语，且具有描述性。
>
> 3. 如果方法名由多个单词组成，那么这些单词之间应该没有下划线符号，而是采用驼峰命名法。
>
> 4. 方法名不要使用Java关键字。
>
> 例如，如果你编写一个计算两个数之和的方法，你可以将它命名为"calculateSum"。如果你编写一个检查字符串是否为空的方法，你可以将它命名为"isEmpty"。



### ==2.==Java中不常见的关键字

> Java有许多关键字，其中一些可能对初学者来说不太常见。以下是一些例子：
>
> 1. `transient`: 这个关键字用于声明一个对象的某些字段不应该被序列化。例如：
>
>    ```java
>    public class MyClass implements Serializable {
>        private transient int id; // 这个字段不会被序列化
>        private String name;
>    }
>    ```
>
> 2. `volatile`: 这个关键字用于表示一个变量可能会被多个线程同时修改，因此JVM会在每次访问该变量时都从主内存中读取其值，而不是从线程的本地缓存。例如：
>
>    ```java
>    public class MyThread extends Thread {
>        private volatile boolean running = true;
>
>        public void run() {
>            while (running) {
>                // do something
>            }
>        }
>
>        public void stopRunning() {
>            running = false;
>        }
>    }
>    ```
>
> 3. `strictfp`: 这个关键字用于指定一个类或方法必须严格遵守IEEE 754标准中定义的浮点运算规则。例如：
>
>    ```java
>    public strictfp class MyStrictClass {
>        // 所有的浮点运算都将严格遵守IEEE 754标准
>    }
>    ```
>
> 4. `synchronized`: 这个关键字用于指定一个方法或代码块在任何时候只能被一个线程访问。例如：
>
>    ```java
>    public class MyClass {
>        public synchronized void myMethod() {
>            // 这个方法在任何时候只能被一个线程访问
>        }
>    }
>    ```
>
> 以上就是一些可能对Java初学者来说不太常见的关键字。





# ==Spring boot 问题==

### ==1.==spring boot 项目一般分为几层

> Spring Boot项目通常被划分为以下几个层：
>
> 1. 控制器层(Controller Layer)：它是应用程序的入口，负责处理HTTP请求，并将响应返回给客户端。它主要包含处理HTTP请求的类和方法。
>
>    ---
>
> 2. 服务层(Service Layer)：它是业务逻辑的核心，封装了具体的业务逻辑。它主要包含接口和实现类，由控制器层调用。
>
>    ---
>
> 3. 数据访问层(Data Access Layer)：它主要负责与数据源进行交互，如数据库、缓存等。它包含实体类、DAO（Data Access Object）接口和实现类，以及ORM（Object-Relational Mapping）框架相关的配置等。
>
>    ---
> 4. 实体层(Entity Layer)：它包含了所有的实体类，负责定义对象模型的属性和对应的Getter/Setter方法。
>
>    ---
> 5. 配置层(Configuration Layer)：它包含了应用程序的配置信息，如数据库连接池、容器的配置等。
>
>    ---
>    这些层次的划分可以帮助开发人员将应用程序的不同部分清晰地分离开来，提高代码的可读性和可维护性。
>
>    > **这几层一般怎么排序**
>    >
>    > 一般情况下，这几个层次可以按照以下顺序排序：
>    >
>    > 1. 实体层(Entity Layer)：定义了对象模型的属性和对应的Getter/Setter方法。
>    > 2. 数据访问层(Data Access Layer)：负责与数据源进行交互，包含实体类、DAO接口和实现类等。
>    > 3. 服务层(Service Layer)：封装具体的业务逻辑，是控制器层调用的接口和实现类。
>    > 4. 控制器层(Controller Layer)：应用程序入口，处理HTTP请求，并将响应返回给客户端。
>    > 5. 配置层(Configuration Layer)：包含应用程序的配置信息，如数据库连接池、容器的配置等。
>    >
>    > 这样的排序可以使得整个应用程序的结构更加清晰明了，提高代码可读性和可维护性。

### ==2.==在springboot项目中 一般都有什么文件夹 

> 在Spring Boot项目中，常见的文件夹包括：
>
> 1. `src/main/java` - 存放Java源代码的目录。
> 2. `src/main/resources` - 存放应用程序资源文件（如配置文件、静态资源、国际化文件等）的目录。
> 3. `src/test/java` - 存放测试代码的目录。
> 4. `src/test/resources` - 存放测试所需资源文件的目录。
> 5. `target` - 存放编译后的类文件和构建产物的目录。
>
> 其中，`src/main/resources`是一个非常重要的目录，它通常有以下子目录：
>
> 1. `static` - 存放静态资源文件（如JavaScript、CSS、图片等）的目录。
> 2. `templates` - 存放模板文件（如Thymeleaf、FreeMaker等模板）的目录。
> 3. `application.yml`或`application.properties` - 应用程序的配置文件。
> 4. `i18n` - 存放国际化文件（如messages.properties、messages_zh_CN.properties等）的目录。
>
> 另外，还有一些常用的目录，例如：
>
> 1. `logs` - 存放应用程序日志文件的目录。
> 2. `db/migration` - 存放数据库迁移脚本的目录，用于版本控制和自动执行数据库升级脚本。
> 3. `docs` - 存放应用程序文档的目录，如API文档、用户手册等。
>
> 需要注意的是，以上只是一些常见的目录和文件，具体应用程序可能会有不同的结构和组织方式，根据实际情况灵活调整。
>
> ---
>
> 在`src/main/resources`目录下，除了前面提到的常见子目录外，还有一些其他的目录和文件：
>
> 1. `META-INF` - 存放应用程序的元数据（如MANIFEST.MF、spring.factories等）。
> 2. `public` - 存放公共资源文件的目录，这些资源可以被所有用户直接访问。
> 3. `resources` - 存放通用的资源文件的目录，包括图标、XML配置文件等。
> 4. `templates` - 存放模板文件的目录，通常与`src/main/resources/templates`目录是一致的。
>
> 另外，在Spring Boot应用程序中，我们也可以通过自定义配置文件来覆盖默认的配置，例如：
>
> - `application.yml`或`application.properties` - 应用程序的主配置文件。
> - `bootstrap.yml`或`bootstrap.properties` - 应用程序启动时加载的配置文件。
> - `application-{profile}.yml`或`application-{profile}.properties` - 带有指定 Spring 环境的配置文件，例如`application-dev.yml`、`application-prod.yml`等。
>
> 需要注意的是，这些自定义的配置文件必须放在`src/main/resources`目录下，并按照相应的命名规则进行命名。
>
> ---
>
> 除了前面提到的目录和文件之外，还有一些其他可能被用到的目录和文件：
>
> 1. `src/main/webapp` - 存放Web应用程序的静态资源文件（如HTML、JavaScript、CSS等）及WEB-INF目录下的JSP文件。
> 2. `src/main/filters` - 存放URL过滤器的目录。
> 3. `src/main/aspects` - 存放切面类的目录，用于AOP编程。
> 4. `src/main/scripts` - 存放脚本文件（如Python、Ruby等）的目录，用于自动化部署和管理。
> 5. `src/main/docker` - 存放Dockerfile文件和相关资源文件的目录，用于构建Docker镜像。
> 6. `src/main/bash` - 存放Bash脚本文件的目录，用于自动化部署和管理。
> 7. `.mvn` - 存放Maven Wrapper的配置文件，允许使用项目附带的Maven版本来构建项目，而不需要手动安装Maven。
>
> 当然，并不是所有的项目都需要上述目录和文件。具体情况要根据项目需求和开发者的习惯而定。
>
> ---
>
> 除了上述的目录和文件之外，还有一些在Spring Boot应用程序开发中常用的工具：
>
> 1. Lombok - 通过注解来简化Java代码，例如@Data、@Builder、@Slf4j等。
> 2. MapStruct - 一个对象映射框架，通过注解来生成类型安全的DTO映射器。
> 3. JUnit5 - 测试框架，支持参数化测试、动态测试、条件测试等。
> 4. Mockito - 用于Mock测试的框架，支持Mock对象、Stub方法、Verify验证等。
> 5. H2 Database - 嵌入式数据库，方便进行单元测试和集成测试。
>
> 这些工具可以有效地提高开发效率和测试质量，是Spring Boot应用程序开发中非常有价值的辅助工具。需要注意的是，使用这些工具前需要先引入相应的依赖。
>
> ---
>
> **如果是springboot web项目src/main/java里面包涵什么文件夹**
>
> 如果是Spring Boot Web应用程序，`src/main/java`中的目录结构通常会按照MVC（Model-View-Controller）模式来组织代码。以下是一个常见的MVC架构的目录结构：
>
> 1. `com.example.project` - 根目录。
> 2. `config` - 存放配置类的目录，例如Spring Security的配置、Swagger的配置等。
> 3. `controller` - 存放控制器类的目录，负责接收和处理HTTP请求，并返回响应数据。
> 4. `service` - 存放服务层类的目录，负责业务逻辑处理。
> 5. `dao`（或repository） - 存放数据访问层类的目录，负责与数据库进行交互，通常使用ORM框架（如MyBatis、Hibernate等）来简化操作。
> 6. `model`（或entity） - 存放实体类的目录，表示业务对象。
> 7. `exception` - 存放异常类的目录，例如自定义异常、全局异常处理器等。
> 8. `utils` - 存放工具类的目录，例如日期时间工具、系统参数工具等。
> 9. `dto`（或vo） - 存放数据传输对象（DTO）或值对象（VO）的目录，用于在不同层之间传递数据。
>
> 其中，`controller`、`service`和`dao`（或`repository`）是MVC三层的核心部分，负责完成Web应用程序的请求处理、业务逻辑处理和数据持久化等任务。其他目录都是为了更好地组织代码而设立的。需要注意的是，这只是一种常见的目录结构，具体实现方式可能因项目需求而有所不同。
>
> ---
>
>    > **怎么没有domain文件夹**
>    >
>    > 您提到的`domain`文件夹通常是用于存放领域模型（Domain Model）的目录，它是一种更加面向对象的设计方式。在Spring Boot应用程序中，我们可以使用`model`（或`entity`）目录来表示领域模型。
>    >
>    > 实际上，`model`（或`entity`）目录与`domain`目录的作用是类似的，都是用于存放业务对象的目录。不同之处在于，`model`（或`entity`）目录通常是与ORM框架（如MyBatis、Hibernate等）紧密相关的，而`domain`目录通常更加面向对象，强调领域驱动设计（DDD）的思想。
>    >
>    > 在具体实现时，可以根据项目需求和开发者的习惯选择是否创建`domain`目录，如果需要使用领域驱动设计的思想，则可以创建`domain`目录，并将领域模型放置在其中。
>
> ---
>
> >**pojo文件夹在什么时候用**
> >
> >POJO（Plain Old Java Object）文件夹通常用于存储Java类，这些类被设计为轻量级的数据传输对象。它们没有任何业务逻辑或其他复杂的处理逻辑，只是简单地保存数据的容器。
> >
> >通常情况下，POJO文件夹包含了应用程序的数据模型层，用于表示数据库中的表或其他数据源中的数据。这些Java类只包含属性和相应的getter/setter方法，以及一些简单的构造函数。
> >
> >使用POJO可以将数据从数据库中检索出来，并在Java应用程序中进行操作和处理。这种设计模式使得代码更加清晰、易于维护，也使得应用程序的开发速度更快，因为不需要处理过多的业务逻辑。
> >
> >总之，在Java应用程序中，POJO文件夹通常用于存储数据模型层的Java类。



### ==3.==如果用springboot写一个博客 一般都包涵哪些注解

> 使用SpringBoot编写博客应用程序时，一些常见的注解包括：
>
> 1. `@SpringBootApplication` - 这是一个复合注解，包含了`@Configuration`、`@EnableAutoConfiguration`和`@ComponentScan`等注解。它表示这是一个Spring Boot应用程序。
>
> 2. `@RestController` - 这个注解表明该控制器类处理HTTP请求，并且每个方法返回的数据都会通过`@ResponseBody`自动序列化到响应体中。
>
> 3. `@RequestMapping` - 这个注解用来映射URL和HTTP方法到控制器方法上。
>
> 4. `@RequestParam` - 用于将HTTP请求参数绑定到控制器方法的参数上。
>
> 5. `@PathVariable` - 用于将URL路径变量绑定到控制器方法的参数上。
>
> 6. `@Autowired` - 自动装配依赖项，使得代码更简洁。
>
> 7. `@Entity` - 表示该类是一个实体类。
>
> 8. `@Repository` - 标记数据访问组件，通常与`@Autowired`一起使用。
>
> 9. `@Service` - 在服务层中使用，标记业务逻辑组件。
>
> 10. `@ControllerAdvice` - 全局异常处理器，用于捕获控制器中抛出的异常并进行相应处理。
>
> 当然还有很多其他注解可以用于SpringBoot应用程序，具体使用哪些注解取决于应用程序需求和开发人员的喜好。
>
> 



### ==4.==能用表格表示springboot的注解关系吗

> 可以，下面是一个简单的表格，展示了Spring Boot中一些常见注解之间的关系：
>
> | 注解名                 | 作用                        | 细节                                                         |
> | ---------------------- | --------------------------- | ------------------------------------------------------------ |
> | @SpringBootApplication | 标记主类                    | 复合注解，包含@Configuration，@EnableAutoConfiguration和@ComponentScan等注解 |
> | @RestController        | 标记控制器类                | 处理HTTP请求，并自动序列化返回结果到响应体中                 |
> | @RequestMapping        | 映射 URL 和 HTTP 方法       | 可以设置请求路径、请求方法、请求参数、响应类型等             |
> | @RequestParam          | 绑定请求参数到方法参数      | 可以设置参数名、是否必须等                                   |
> | @PathVariable          | 绑定 URL 中的变量到方法参数 | 可以设置变量名、是否必须等                                   |
> | @Autowired             | 自动装配依赖项              | 可以使用在属性、构造函数或者 setter 方法上                   |
> | @Entity                | 标记实体类                  | 表示该类对应数据库中的一张表                                 |
> | @Repository            | 标记数据访问组件            | 通常与@Autowired一起使用                                     |
> | @Service               | 标记业务逻辑组件            | 在服务层中使用                                               |
> | @ControllerAdvice      | 全局异常处理器              | 可以捕获控制器中抛出的异常并进行相应处理                     |
>
> 注意，这只是一个示例表格，实际使用中可能会根据具体需求使用不同的注解。
>
> 除了上面提到的注解，还有一些常用的注解可以在Spring Boot应用中使用。以下是一些常见的注解及其作用：
>
> | 注解名            | 作用                                                |
> | ----------------- | --------------------------------------------------- |
> | @Component        | 标记组件类，通用的注解                              |
> | @Configuration    | 标记配置类                                          |
> | @Bean             | 将方法返回值注册为一个 Bean                         |
> | @Profile          | 按照不同的环境（如开发、测试、生产）定义不同的 Bean |
> | @Value            | 注入配置文件中的属性值                              |
> | @Qualifier        | 根据 Bean 名称或别名进行注入                        |
> | @EnableScheduling | 开启定时任务                                        |
> | @Scheduled        | 定义定时任务                                        |
> | @Async            | 标识异步方法                                        |
>
> 需要注意的是，注解的具体作用和用法要根据具体情况而定，以上表格仅仅列出了一些比较常见的注解，并不能代表全部。
>
> 另外，在Spring Boot中还有一些用于处理Web请求、数据库操作等方面的注解，这里简单介绍一下：
>
> | 注解名           | 作用                             |
> | ---------------- | -------------------------------- |
> | @GetMapping      | 处理 GET 请求                    |
> | @PostMapping     | 处理 POST 请求                   |
> | @PutMapping      | 处理 PUT 请求                    |
> | @DeleteMapping   | 处理 DELETE 请求                 |
> | @PatchMapping    | 处理 PATCH 请求                  |
> | @RequestBody     | 将请求体中的数据绑定到方法参数上 |
> | @ResponseBody    | 将方法返回值序列化为响应体       |
> | @PathVariable    | 用于获取 URL 路径中的变量        |
> | @RequestParam    | 用于获取请求参数                 |
> | @PageableDefault | 用于设置分页默认参数             |
> | @Transactional   | 标记事务方法                     |
>
> 这些注解常常与其他注解一起使用，可以大幅度减少编写代码的工作量，提高开发效率。需要说明的是，这些注解都是Spring框架提供的，与Spring Boot本身并没有直接关联，但在Spring Boot应用程序中也可以自由地使用它们。
>
> 除了上面提到的注解外，Spring Boot还有一些用于集成其他框架或库的注解，例如：
>
> | 注解名                        | 作用                  |
> | ----------------------------- | --------------------- |
> | @EnableJpaRepositories        | 开启 JPA 数据访问     |
> | @EntityScan                   | 扫描实体类            |
> | @EnableBatchProcessing        | 开启批处理            |
> | @EnableCaching                | 开启缓存支持          |
> | @EnableAsync                  | 开启异步执行          |
> | @EnableWebSocketMessageBroker | 开启 WebSocket 聊天室 |
> | @EnableSwagger2               | 开启 Swagger API 文档 |
>
> 这些注解可以让我们更方便地集成其他框架或库，并在Spring Boot应用程序中使用它们。需要注意的是，使用这些注解前需要先引入相应的依赖。



# ==关于服务器==

### ==1.==有什么工具可以进行端口映射

> 有很多工具可以进行端口映射，以下是几个常见的工具：
>
> 1. Ngrok：这是一个非常流行的端口映射工具，它可以将本地端口暴露到公网上，从而方便远程访问。
> 2. FRP：这是一款基于Go语言开发的高性能的反向代理工具，它可以将内网服务映射到公网上。
> 3. Nginx：这是一款常用的Web服务器，它还可以用来进行端口映射，通过配置Nginx反向代理实现端口映射。
> 4. Haproxy：这是一款高性能的TCP/HTTP负载均衡器，也可以用来进行端口映射。
>
> 以上是几个常用的端口映射工具，每个工具都有其特点和适用场景，需要根据实际需求选择使用。
>
>    > ---
>    >
>    > **springboot项目怎么用Nginx来暴露端口**
>    >
>    > 要通过Nginx来暴露Spring Boot项目的端口，需要进行以下步骤：
>    >
>    > 1. 安装Nginx，并确保Nginx服务已启动。
>    >
>    > 2. 在Nginx配置文件中添加一个反向代理规则。在Ubuntu系统上，配置文件位于`/etc/nginx/sites-available/default`。
>    >
>    >    打开该文件并添加以下内容：
>    >
>    >    ```shell
>    >    server {
>    >        listen 80;
>    >        server_name yourdomain.com;
>    >        location / {
>    >            proxy_pass http://localhost:8080;
>    >            proxy_set_header X-Real-IP $remote_addr;
>    >            proxy_set_header Host $host;
>    >            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
>    >        }
>    >    }
>    >    ```
>    >
>    >    此配置将所有来自yourdomain.com域名的HTTP请求转发到本地Spring Boot应用程序的8080端口。这里还设置了一些HTTP头，以便将客户端的真实IP地址传递给Spring Boot应用程序。
>    >
>    > 3. 保存并关闭文件，然后重新加载Nginx配置文件。在Ubuntu系统上，可以使用以下命令重新加载Nginx配置文件：
>    >
>    >    ```shell
>    >    sudo systemctl reload nginx
>    >    ```
>    >
>    > 4. [现在可以从Internet浏览器中访问yourdomain.com](http://xn--internetyourdomain-7o22a05g1no92gjumlleb09ozw8auxzjqrld45e.com/)，就可以看到已经代理到Spring Boot应用程序的内容。
>    >
>    > 注意：在上述配置中，我们假设您已经将Spring Boot应用程序部署在本地服务器上，并且正在监听端口8080。如果您的应用程序正在运行其他端口，请相应地更改Nginx配置文件中的端口号和代理端口号。



### ==2.==怎么把服务器当vpn

> 将服务器作为VPN服务器需要进行以下几个步骤：
>
> 1. 安装VPN服务器软件：可以选择安装一些开源或商业的VPN服务器软件，例如OpenVPN、SoftEther等。
> 2. 配置VPN服务器：安装完VPN服务器软件后，需要对其进行配置，包括设置认证方式、网络协议、加密方式、IP地址池等参数。具体配置方法可以参考相关软件的文档。
> 3. 授权用户访问VPN：配置完成后，你需要添加用户并授权他们使用VPN。这通常涉及到创建用户名和密码，并分配VPN访问权限。
> 4. 连接VPN：在客户端上安装VPN客户端软件，并输入VPN服务器的IP地址和登录凭据，即可连接到VPN服务器。此时，你的电脑的网络流量将被路由到VPN服务器并通过VPN连接传输。
>
> 需要注意的是，在配置VPN服务器时需要遵循安全的最佳实践，确保所有的数据都得到了充分的保护和加密。同时也要遵守当地的法律法规以及互联网服务提供商（ISP）的使用政策，以免违反相关规定导致不必要的法律风险。
>
> ---
>
> **v2rayN**
>
> v2rayN是一款基于V2Ray协议的Windows客户端程序，用于代理网络连接并实现VPN功能。它具有使用简单、界面友好、配置灵活等特点，适合普通用户使用。
>
> 以下是v2rayN的使用步骤：
>
> 1. 下载v2rayN客户端程序：你可以从v2rayN的官方网站（https://github.com/2dust/v2rayN/releases）下载最新版本的v2rayN客户端程序，并安装到电脑上。
> 2. 配置v2rayN客户端：打开v2rayN客户端程序，点击“服务器”按钮，添加你的VPN服务器和配置信息。这里需要注意，你需要先有一个可用的V2Ray服务器，或者购买V2Ray服务提供商的服务。
> 3. 连接VPN：在v2rayN客户端程序中选择你要使用的VPN服务器，并点击“连接”按钮。此时，你的电脑将会通过VPN连接到服务器，并使用该服务器进行访问互联网。
>
> 需要注意的是，在使用v2rayN时，你需要遵循当地的法律法规及服务条款，并确保VPN连接的稳定性和安全性。同时也需要注意隐私保护，例如不要访问敏感信息或使用未知来源的第三方应用程序。
>
> ---
>
> **什么是可用的V2Ray服务器**
>
> V2Ray是一种网络协议，用于代理网络连接并实现VPN功能。为了使用V2Ray协议，你需要有一个可用的V2Ray服务器，或者购买V2Ray服务提供商的服务。
>
> 可用的V2Ray服务器在构建和使用中具有以下特点：
>
> 1. 稳定性：可用的V2Ray服务器应该能够提供高度稳定的网络连接，避免因服务器故障或其他问题导致的服务中断。
> 2. 速度：与VPN相关的速度是非常重要的，因此可用的V2Ray服务器应该能够提供快速的网络连接速度，以保证用户能够流畅地访问互联网。
> 3. 隐私保护：V2Ray的目标之一是保护用户的隐私和身份安全，因此可用的V2Ray服务器应该能够提供安全的数据传输和加密服务。
> 4. 支持性：V2Ray是一个开源项目，拥有广泛的社区支持和开发人员支持。因此，可用的V2Ray服务器应该能够支持各种不同的客户端和操作系统，并提供易于使用的API和配置文件。
>
> 如果你想寻找可用的V2Ray服务器，可以通过搜索引擎或论坛等渠道查询相关信息，并评估其稳定性、速度、隐私保护和支持性等方面的特点。同时也需要注意当地的法律法规及服务条款，确保自己的合法权益和使用安全。
>
> ---
>
> **使用v2rayN  服务器需要阿里云服务器需要配置什么**
>
> 要配置一个阿里云服务器用于v2rayN，您需要执行以下步骤：
>
> 1. 创建一个阿里云ECS实例。
> 2. 在安全组规则中设置允许传入的TCP流量的端口范围。默认情况下，v2ray使用的端口是10000-65535之间的任意端口，因此您可以选择将所有TCP端口打开或只打开这个范围。
> 3. 安装v2rayN到您的本地计算机上，并按照v2rayN的指南，将其连接到您的阿里云服务器。
> 4. 在阿里云服务器上安装和配置v2ray服务和相应的协议（例如VMess）以及相关的加密方式（如TLS）。
> 5. 配置v2rayN以与您的阿里云服务器进行通信，并确保所有配置文件正确。
>
> 请注意，这只是v2rayN和阿里云服务器之间通信的基本配置。您还需要考虑其他因素，如服务器性能、网络稳定性和安全性等。
>
> ---
>
> **服务器上怎么安装和配置v2ray服务和相应的协议**
>
> 要在服务器上安装和配置v2ray服务和相应的协议，您可以按照以下步骤进行操作：
>
> 1. 在服务器上安装v2ray，可以使用以下命令：
>
> ```shell
> bash <(curl -L -s https://install.direct/go.sh)
> ```
>
> 这将下载并安装v2ray。
>
> 1. 安装完成后，您需要编辑v2ray的配置文件。配置文件通常位于`/etc/v2ray/config.json`。
> 2. 打开配置文件，您将看到一个JSON格式的文本。在此文件中，您需要定义v2ray服务器的监听端口、协议、传输层安全（TLS）等信息。例如，以下是一个VMess协议的示例配置：
>
> ```json
> {
>   "inbounds": [
>     {
>       "port": 10086, // 监听端口
>       "protocol": "vmess", // 协议类型
>       "settings": {
>         "clients": [
>           {
>             "id": "b831381d-6324-4d53-ad4f-8cda48b30811", // UUID
>             "level": 1,
>             "alterId": 64
>           }
>         ]
>       },
>       "streamSettings": {
>         "network": "tcp",
>         "security": "tls",
>         "tlsSettings": {
>           "certificates": [
>             {
>               "certificateFile": "/path/to/cert.pem",
>               "keyFile": "/path/to/key.pem"
>             }
>           ]
>         }
>       }
>     }
>   ],
>   "outbounds": [
>     {
>       "protocol": "freedom",
>       "settings": {}
>     }
>   ]
> }
> ```
>
> 1. 配置完成后，保存文件并重启v2ray服务，以使更改生效。
>
> 以上是基本的v2ray服务和协议配置示例，具体的配置取决于您所需的协议和网络环境。如果您不熟悉v2ray的配置文件语法，请参考v2ray官方文档或寻求专业人士的帮助。





### ==3.==怎么向公网暴露本机的80端口

> 要向公网暴露本机的80端口，您需要进行以下步骤：
>
> 1. 确保您的网络拥有一个公网IP地址，您可以通过访问“https://www.whatismyip.com/”等网站来获取该IP地址。
>
> 2. 确认您的路由器是否开启了端口转发功能，如果没有，请参考您的路由器说明书按照规定方法进行设置。
>
> 3. 在路由器中设置端口转发。将路由器的外部公网IP地址绑定到本地网络中服务器或设备的内部IP地址的80端口上。这通常可以在路由器的"端口映射"或"端口转发"选项下找到。
>
> 4. 确认您的防火墙是否已正确配置，允许外部请求通过80端口进入您的服务器或设备。
>
> 5. 最后，测试您的设置。您可以使用一个在线端口检查工具来验证您的80端口是否已成功开放。
>
> 请注意，在向公网暴露您的端口之前， 公网安全性问题必须得到重视。 您应谨慎权衡可能带来的风险，并采取适当的安全措施来确保您的系统和数据的安全。
>
> 
>
> **水星路由器怎么开启了端口转发功能**
>
> >以下是在水星路由器上开启端口转发功能的步骤：
> >
> >1. 登录水星路由器管理页面。一般情况下，您可以在浏览器地址栏中输入路由器的管理页面地址，例如：“192.168.1.1”。
> >
> >2. 在管理页面中，选择“高级设置”选项，然后找到“端口转发”或“虚拟服务器”选项。
> >
> >3. 单击“添加规则”按钮，然后选择“TCP/UDP”协议，并输入要开放的端口号。
> >
> >4. 输入您希望所在局域网的设备的IP地址来指定目标设备。
> >
> >5. 将规则的状态切换为“已启用”，单击“保存”以保存设置并应用于路由器。
> >
> >请注意，在向公网暴露您的端口之前， 公网安全性问题必须得到重视。 您应谨慎权衡可能带来的风险，并采取适当的安全措施来确保您的系统和数据的安全。



# ==玩转win==

### ==1.==我有一个应用demo.exe 每次开机用双击才能运行  有没有办法让这个应用在我开机的时候就自动运行

> 是的，有几种方法可以让应用程序在开机时自动运行：
>
> 1. ==**将应用程序的快捷方式添加到Windows启动文件夹中。要打开该文件夹，请按下Windows + R键，在运行对话框中输入shell:startup，然后按Enter键。将应用程序的快捷方式拖放到此文件夹中即可。**==
> 2. 使用Windows任务计划程序。打开任务计划程序（按下Windows + R键，输入taskschd.msc并按Enter键），然后创建一个新任务。在“触发器”选项卡中，选择“开始任务时”并选择“开机”作为触发器。在“操作”选项卡中，指定要启动的应用程序。完成后，单击“确定”以保存任务。
> 3. 编辑注册表。请注意，更改注册表可能会对系统产生负面影响，因此请确保备份您的注册表并小心进行操作。要编辑注册表，请按下Windows + R键，输入regedit并按Enter键。在注册表编辑器中，导航到HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run。右键单击空白处，选择“新建 > 字符串值”，然后为其命名并将路径指定为应用程序。
>
> 这些方法都可以使您的应用程序在开机时自动运行。





### ==2.==我还有一个应用d.exe 每次要双击才能运行，我想有一个快捷键也能运行 win10能做到吗

> 是的，你可以使用 Windows 的快捷键功能来实现这个目标。以下是在 Windows 10 中创建快捷键以运行应用程序的步骤：
>
> 1. 打开 D:\ 目录，找到 d.exe 应用程序文件。
> 2. 右键单击该文件，并选择“发送到” -> “桌面 (快捷方式)”。
> 3. 在桌面上找到新创建的快捷方式，右键单击它，并选择“属性”。
> 4. 在“属性”窗口中，切换到“快捷键”选项卡。
> 5. 在“快捷键”栏中，输入你想要使用的快捷键组合。例如，你可以按下“Ctrl + Alt + D”作为快捷键。
> 6. 点击“应用”按钮，然后点击“确定”按钮。
>
> 现在，每当你按下你设定的快捷键组合时，d.exe 应用程序将会自动运行。



### ==3.==win10 系统的win键+另外一个按键的快捷键全部列出来

> 以下是在Windows 10系统中可以使用的Win键组合快捷键列表：
>
> 1. Win键：打开或关闭开始菜单。
> 2. Win + A：打开操作中心。
> 3. Win + B：将焦点移动到任务栏上，并选择第一个可用的应用程序。
> 4. Win + C：启用Cortana语音助手。
> 5. Win + D：显示桌面并最小化所有窗口。
> 6. Win + E：打开文件资源管理器。
> 7. Win + F：打开反馈中心。
> 8. Win + G：打开游戏栏。
> 9. Win + H：打开语音输入。
> 10. Win + I：打开设置。
> 11. Win + J：切换跟随鼠标指针的焦点模式。
> 12. Win + K：打开“连接”框，以连接到无线投影或其他外部设备。
> 13. Win + L：锁定电脑。
> 14. Win + M：最小化所有窗口。
> 15. Win + N：打开“通知”面板。
> 16. Win + O：锁定屏幕方向。
> 17. Win + P：打开投影选项。
> 18. Win + Q：打开Cortana进行语音搜索。
> 19. Win + R：打开“运行”对话框。
> 20. Win + S：打开Windows搜索。
> 21. Win + T：在任务栏上循环浏览应用程序。
> 22. Win + U：打开辅助功能管理器。
> 23. Win + V：循环浏览通知。
> 24. Win + W：打开Windows Ink Workspace。
> 25. Win + X：打开高级用户菜单。
> 26. Win + Y：打开语音输入工具。
> 27. Win + Z：打开应用程序条。
>
> 以上是部分常见的Win键组合快捷键。



### ==4.== 免安装软件 删除时怎么清理数据

> 免安装软件一般不会在计算机上留下太多系统文件和注册表项，因此删除后对系统的影响较小。如果想彻底清理数据，可以按照以下步骤：
>
> 1. 打开软件所在的安装目录，查看是否有创建的文件或文件夹，如果有，直接删除即可。
> 2. 检查是否在注册表中留下了相关的记录，可以在开始菜单中的“运行”中输入“regedit”打开注册表编辑器，搜索软件的名称，删除相关项。
> 3. 清理软件留下的临时文件，可以在开始菜单中的“运行”中输入“%temp%”打开临时文件夹，找到软件创建的临时文件夹，将其删除即可。
> 4. 建议使用专业的卸载工具，如Revo Uninstaller等来卸载应用程序，这种工具可以检测程序遗留的文件和注册表项，并帮助用户清理。
>
> ---
>
> >**用专门的清理软件清理注册表 免安装的会被处理掉吗**
> >
> >使用清理软件清理注册表时，免安装软件也会被处理掉。清理软件通常会扫描整个计算机的注册表，找出与其相关的所有记录，并根据用户选择进行清理。因此，即使免安装软件在计算机中没有留下任何安装记录，但是如果它们曾经在计算机上使用过，那么其相关的注册表记录也会被清理软件检测到并清理掉。我们建议使用专业的清理软件时要小心谨慎，确保只删除不需要的记录，以免不需要的记录被误删导致系统出现问题。
>
> ---
>
> >**用专门的清理软件清理注册表 会先判断的免安装的软件是否存在 还是会直接被处理掉**
> >
> >清理软件一般是根据注册表中的键值来判断软件是否存在，而不是根据软件的安装位置。因此，即使免安装软件没有留下相关的安装记录，但如果在注册表中有相关的键值，则也会被判断为存在并被进行处理。不过，一些较为智能的清理软件会提供排除列表或者不处理某些键值的选项，可以对特定的免安装软件进行保护和排除。



### ==5.== 用cmd查看Wi-Fi密码

> 您可以在计算机中查找已连接的Wi-Fi密码。可以打开命令提示符窗口（CMD）并使用以下命令：netsh wlan show profile，然后输入以下命令来查看Wi-Fi密码：netsh wlan show profile name=[Wifi名称] key=clear。
>
> 例如，如果你想查看名字为“test”的Wi-Fi密码，应输入以下命令：
>
> ```
> netsh wlan show profile name=test key=clear
> ```
>
> ![image-20230405233509440](./问chat笔记.assets/image-20230405233509440.png)
>
> > 在Windows系统中，保存WiFi网络的文件通常存储在" C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces "目录下。每个以太网接口和无线接口都有一个对应的文件夹来存储其已连接的网络信息。你可以找到与你当前连接的Wi-Fi网络相关的文件夹，并打开XML文件来查看该网络的详细信息，包括名称、加密类型和密码(加密了)。请注意，访问此目录需要管理员权限。
> >
> > 
>





### ==6.== 非应用放win10磁贴

**（不依靠第三方工具）**

> 不使用第三方工具在 Windows 10 的开始菜单磁贴中放置非应用快捷方式的方法有限。然而，您可以尝试以下方法：
>
> 1. 在桌面或文件夹中找到您想添加到开始菜单的非应用程序快捷方式（例如，文件、文件夹或可执行文件）。
>
> 2. 右键单击快捷方式，然后选择「创建快捷方式」。
>
> 3. 打开文件资源管理器，然后导航到以下文件夹：
>
>    ```shell
>    %APPDATA%\Microsoft\Windows\Start Menu\Programs
>    ```
>
>    您可以通过快速将上述路径粘贴到文件资源管理器的地址栏并按 Enter 键来访问此文件夹。
>
> 4. 将刚刚创建的快捷方式复制或移动到此文件夹。您可以为快捷方式重命名，以便在开始菜单中更容易识别。
>
> 5. 现在，打开开始菜单，找到新添加的快捷方式，然后右键单击它。选择「固定到开始」。这将在开始菜单的磁贴部分添加一个新磁贴。
>
> 请注意，这种方法不允许自定义磁贴的外观。磁贴将显示默认的图标和名称。



### ==7.== 端口转发（wsl地址转发到本地端口）

> **打开端口转发**
>
> ````bash
> netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=2345 connectaddress=172.23.72.37 connectport=80
> ````
>
> 该命令是将Windows本机的2345端口转发到WSL环境的172.23.72.37地址的80端口。
>
> >其中:
> >
> >- listenaddress和listenport需要与添加规则时指定的IP地址和端口对应,比如本例是0.0.0.0和2345。
> >- 如果不指定listenaddress,默认删除与指定端口相关的所有规则。
> >- 如果不指定任何参数,会删除所有端口转发规则。
>
> **关闭从2345端口到WSL 80端口的转发规则,命令是**
>
> ````bash
> netsh interface portproxy delete v4tov4 listenaddress=0.0.0.0 listenport=2345
> ````
>
> >删除规则后,用netsh interface portproxy show v4tov4可以查看当前机器所有端口转发规则,确认规则已删除。
> >
> >此外,也可以直接**重启机器**,重启后所有自定义端口转发规则都**会失效**。
> >
> >通过删除或重启就可以关闭不需要的端口转发了。



### ==8.== win打开指定端口给局域网访问（命令）

如果cmd不行就用Windows PowerShell(管理员)

> ```bash
> netsh advfirewall firewall add rule name="Open Port 2345" dir=in action=allow protocol=TCP localport=2345
> ```
>
> >这个命令在Windows入站防火墙添加了一个规则,允许TCP 2345端口的入站连接。
> >
> >你可以根据需要调整几个参数:
> >
> >- name - 规则的名字,可以自定义。
> >- protocol - 协议,可以是TCP、UDP或ANY。
> >- localport - 端口号,这里是2345。
> >
> >一个允许TCP和UDP的完整命令如下:
> >
> >```bash
> >netsh advfirewall firewall add rule name="Open Port 2345" dir=in action=allow protocol=TCP localport=2345
> >netsh advfirewall firewall add rule name="Open Port 2345" dir=in action=allow protocol=UDP localport=2345
> >```
> >
> >>添加规则后,可以用以下命令查看现有入站规则:
> >>
> >>```bash
> >>netsh advfirewall firewall show rule name=all
> >>```
> >>
> >>删除规则可以用delete参数:
> >>
> >>```bash
> >>netsh advfirewall firewall delete rule name="Open Port 2345"
> >>```
> >>
> >>netsh firewall提供了完整的命令行方式来管理Windows防火墙,非常方便。你可以根据实际需要调整规则。





### ==9.== CMD改颜色

> 使用 `color` 命令来更改文本和背景的颜色。这个命令的一般格式是 `color XY`，其中 `X` 和 `Y` 都是从 0 到 F 的十六进制数字。`X` 代表背景颜色，`Y` 代表文本颜色。
>
> >例如，如果你想将文本颜色改为亮绿色，并保持背景颜色不变，你可以输入 `color 0A`。这里，`0` 代表黑色背景，`A` 代表亮绿色文本。
> >
> >>注意：不允许，字体颜色和背景色一样，否则不生效；
> >>
> >>​			如果只提供一个值，`color` 命令将只更改文本颜色；
>
> ```basic
> 0 = 黑色       8 = 灰色
> 1 = 蓝色       9 = 亮蓝色
> 2 = 绿色       A = 亮绿色
> 3 = 蓝绿色     B = 亮蓝绿色
> 4 = 红色       C = 亮红色
> 5 = 紫色       D = 亮紫色
> 6 = 黄色       E = 亮黄色
> 7 = 白色       F = 亮白色
> ```





# ==开源许可证==

> **MIT 许可证、Apache 许可证、GPL 许可证**
>
>   >   MIT 许可证、Apache 许可证和 GPL 许可证都是常见的开源软件许可证。
>   >
>   >   1. MIT 许可证：MIT 许可证是一种宽松的许可证，允许代码被自由地使用、修改和再分发，只要在代码中包含原始许可证和版权声明即可。MIT 许可证适用于大多数类型的应用程序和库，也非常适合商业软件。
>   >   2. Apache 许可证：Apache 许可证也是一种宽松的许可证，允许代码被自由地使用、修改和再分发，但要求在代码中包含原始许可证和版权声明，并且明确指出任何变更的部分。同时，Apache 许可证还涉及特定的专利授权条款，帮助保护贡献者和用户的知识产权。
>   >   3. GPL 许可证：GPL 许可证是一种相对严格的许可证，要求采用 GPL 许可证授权的代码必须公开源代码，并且任何基于该代码的派生作品也必须采用相同的协议授权。因此，如果你以 GPL 许可证授权的代码为基础开发自己的软件，那么你也必须遵守 GPL 许可证的规定，即公开你的源代码并采用 GPL 许可证授权。
>   >
>   >   总之，这三种许可证各有特点，选择哪种许可证取决于项目的性质和要求。需要开源软件作者谨慎选择适当的许可证，并在发布代码前仔细阅读许可证文本，并理解其限制和规定。
>
> ---
>
> **GitHub 上怎么编写MIT 许可证**
>
>   >   如果你想在 GitHub 上创建一个使用 MIT 许可证的开源项目，可以按照以下步骤编写许可证文件：
>   >
>   >   1. 创建 LICENSE 文件：在 GitHub 仓库的根目录下创建一个名为 LICENSE 的文件。
>   >   2. 拷贝许可证文本：从 MIT 许可证模板中复制许可证文本，然后将其粘贴到 LICENSE 文件中。MIT 许可证文本如下：
>   >
>   >   ```shell
>   >   MIT License
>   >   
>   >   Copyright (c) [year] [author]
>   >   
>   >   Permission is hereby granted, free of charge, to any person obtaining a copy 
>   >   of this software and associated documentation files (the "Software"), to deal 
>   >   in the Software without restriction, including without limitation the rights 
>   >   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
>   >   copies of the Software, and to permit persons to whom the Software is furnished 
>   >   to do so, subject to the following conditions:
>   >   
>   >   The above copyright notice and this permission notice shall be included in 
>   >   all copies or substantial portions of the Software.
>   >   
>   >   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
>   >   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
>   >   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
>   >   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
>   >   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
>   >   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN 
>   >   THE SOFTWARE.
>   >   ```
>   >
>   >   1. 修改许可证内容：将其中的 [year] 和 [author] 替换为自己的年份和作者信息。
>   >   2. 提交代码并发布项目：将 LICENSE 文件提交到 GitHub 仓库中，并发布项目。这样，其他用户就可以查看你的代码，并了解你的许可证类型和使用条件。
>   >
>   >   需要注意的是，在使用许可证时应该严格遵守许可证的规定，包括版权声明、免责声明、限制条件等。否则可能会侵犯知识产权或者造成法律风险。建议在使用许可证前仔细阅读许可证文本，并咨询专业律师的意见。





# ==CSS相关==

## ==1.== Emmet 语法

> Emmet是一个流行的编程插件，用于使用简洁的缩写语法快速生成HTML和CSS代码。Emmet的语法主要受到了CSS选择器的启发，使用了类似的语法结构。
>
> 以下是一些基本的Emmet语法：
>
> - `>` : 子元素
> - `+` : 兄弟元素
> - `#` : ID
> - `.` : 类名
> - `[]` : 属性
> - `*` : 复制元素
> - `()` : 分组
> - `^` : 上升一级
> - `{}` : 文本内容
>
> 例如，以下的Emmet缩写：
>
> ```
> div#header>ul.nav>li*4>a{Link $}
> ```
>
> 将会扩展为：
>
> ```html
> <div id="header">
>     <ul class="nav">
>         <li><a>Link 1</a></li>
>         <li><a>Link 2</a></li>
>         <li><a>Link 3</a></li>
>         <li><a>Link 4</a></li>
>     </ul>
> </div>
> ```
>
> 在上述Emmet缩写中，`div#header`代表一个具有ID为"header"的div元素，`ul.nav`代表一个具有类名"nav"的ul元素，`li*4`代表四个li元素，`a{Link $}`代表一个链接，其文本内容为"Link "后跟一个数字，这个数字会在每次复制时增加。
>
> 请注意，不同的编辑器可能需要不同的方式来使用Emmet，一般来说，你需要先输入Emmet缩写，然后通过某种快捷键（比如Tab键）来扩展这个缩写。
>
> ---
>
> **==黑马：==**
>
> 



## ==2.== 复合属性的例子

> 1. `background`：设置背景的颜色、图像、位置和是否重复。
>
> ```css
> background: #ff0000 url("image.jpg") no-repeat fixed center;
> ```
> 在这个例子中，`#ff0000` 是背景颜色，`url("image.jpg")` 是背景图像，`no-repeat` 指定背景图像不重复，`fixed` 指定背景图像固定（不随内容滚动），`center` 指定背景图像的位置。
>
> 2. ==`font`==：设置字体的样式、变体、粗细、大小、行高和字体家族。
>
> ```css
> font: italic bold 1.2em/1.5em Georgia, serif;
> ```
> 在这个例子中，`italic` 是字体样式，`bold` 是字体粗细，`1.2em` 是字体大小，`1.5em` 是行高，`Georgia, serif` 是字体家族。
>
> 3. `margin` 和 `padding`：同时设置上、右、下、左的边距或内边距。
>
> ```css
> margin: 10px 20px 30px 40px;
> padding: 10px 20px 30px 40px;
> ```
> 在这两个例子中，四个值分别代表上、右、下、左的边距或内边距。
>
> 4. `list-style`：设置列表项的标记类型、位置和图像。
>
> ```css
> list-style: circle inside url("marker.gif");
> ```
> 在这个例子中，`circle` 是标记类型，`inside` 是标记位置，`url("marker.gif")` 是标记图像。
>
> 当然，以下是更多的CSS复合属性的例子：
>
> 5. `outline`：设置轮廓的宽度、样式和颜色。
>
> ```css
> outline: 2px dotted blue;
> ```
> 在这个例子中，`2px` 是轮廓的宽度，`dotted` 是轮廓的样式，`blue` 是轮廓的颜色。
>
> 6. ==`border-radius`==：设置元素的边框圆角。
>
> ```css
> border-radius: 25px 50px;
> ```
> 在这个例子中，`25px` 是左上角和右下角的边框半径，`50px` 是右上角和左下角的边框半径。
>
> 7. ==`transition`==：设置元素的过渡效果。
>
> ```css
> transition: margin-left 2s ease-in-out 1s;
> ```
> 在这个例子中，`margin-left` 是应用过渡效果的CSS属性，`2s` 是过渡效果的持续时间，`ease-in-out` 是过渡效果的速度曲线，`1s` 是过渡效果的延迟。
>
> 8. `text-decoration`：设置文本的装饰线样式、颜色和类型。
>
> ```css
> text-decoration: underline red wavy;
> ```
> 在这个例子中，`underline` 是装饰线的样式，`red` 是装饰线的颜色，`wavy` 是装饰线的类型。
>
> 9. `box-shadow`：该属性用于在一个元素的框架周围应用一种或多种阴影效果。
>
> ```css
> box-shadow: 10px 5px 5px black;
> ```
> 在这个例子中，`10px` 是阴影的水平偏移量，`5px` 是阴影的垂直偏移量，第二个 `5px` 是阴影的模糊距离，`black` 是阴影的颜色。
>
> 10. `flex`：这是一个用于设置 `flex-grow`, `flex-shrink` 和 `flex-basis` 的简写属性。
>
> ```css
> flex: 1 0 auto;
> ```
> 在这个例子中，`1` 是 `flex-grow` 的值，`0` 是 `flex-shrink` 的值，`auto` 是 `flex-basis` 的值。
>
> 11. `grid-column` 和 `grid-row`：这是用于设置 `grid-column-start` / `grid-column-end` 和 `grid-row-start` / `grid-row-end` 的简写属性。
>
> ```css
> grid-column: 1 / 3;
> grid-row: 2 / 4;
> ```
> 在这个例子中，`grid-column: 1 / 3;` 表示网格项从网格的第一列开始，到第三列结束。`grid-row: 2 / 4;` 表示网格项从网格的第二行开始，到第四行结束。
>
> 12. `columns`：这是一个用于设置 `column-width` 和 `column-count` 的简写属性。
>
> ```css
> columns: 100px 3;
> ```
> 在这个例子中，`100px` 是列宽，`3` 是列数。
>
> CSS的复合属性可以让你的代码更简洁，更易于维护，但在使用它们时，你需要确保你理解了每个组成部分的含义以及它们的默认值。





## ==3.==伪类选择器:active对div不起作用

> 伪类选择器 `:active` 通常用于匹配鼠标按下但尚未释放时的元素。它最常用于链接（`a`标签），但它可以用于任何可交互的元素。
>
> 对于 `div` 元素，`:active` 伪类默认是不起作用的，因为 `div` 通常被视为非交互式元素。然而，你可以通过设置某些 CSS 属性（如 `tabindex`）使 `div` 元素变得可以交互，从而使 `:active` 伪类起作用。
>
> 例如：
>
> ```html
> <div id="myDiv" tabindex="0">Click me</div>
> ```
>
> ```css
> #myDiv:active {
>  background-color: yellow;
> }
> ```
>
> 在这个例子中，当你点击 `div` 元素并保持鼠标按下状态时，背景色会变为黄色。
>
> 请注意，虽然这种方法可以让 `:active` 伪类在 `div` 上起作用，但在一般情况下，我们不建议在非交互式元素上使用 `:active` 伪类，因为这可能会导致可访问性问题。在大多数情况下，你应该只在链接和按钮等交互式元素上使用 `:active` 伪类。
>
> ---
>
> 在HTML中，`:active`伪类通常用于标识用户正在与之交互的元素。以下是一些常用于`:active`伪类的HTML元素：
>
> - `<a>`：链接元素。这是最常用`:active`伪类的元素。当用户点击链接时，链接会变为活动状态，直到用户释放鼠标按钮。
>
> - `<button>`：按钮元素。当用户点击按钮时，按钮会变为活动状态，直到用户释放鼠标按钮。
>
> - `<input>`：输入元素。特别是`type="button"`、`type="submit"`和`type="reset"`的输入元素，它们在用户点击时会变为活动状态。
>
> 除了这些元素，也可以通过添加`tabindex`属性（例如`tabindex="0"`）来使几乎任何HTML元素支持`:active`伪类。然而，应注意只在必要时这样做，因为这可能会影响到网站的可访问性。在大多数情况下，你应该只在链接和按钮等交互式元素上使用`:active`伪类。
>
> >---
> >
> >**链接伪类选择器以及它们的推荐顺序：**
> >
> >1. `:link`：该伪类选择器匹配所有未访问过的链接。通常将其放在首位。
> >2. `:visited`：该伪类选择器匹配所有已访问过的链接。由于浏览器安全策略限制，对于:visited 仅能修改颜色属性，并且只有当前页面所包含URL才可以更改为其他颜色值。
> >3. `:hover`：该伪类选择器匹配鼠标悬停在链接上时的状态。
> >4. `:active`：该伪类选择器匹配鼠标点击并按住不松开时显示出来的状态。
> >5. `:focus`：该伪类选择器匹配获得焦点时（例如通过键盘导航）显示出来的状态。



# ==js问题==

### ==1.==js判断中 哪些非布尔类的值会是false

> 在JavaScript中，以下值将被视为“falsy”，也就是假的：
>
> - false
> - 0
> - -0
> - 0n (BigInt)
> - "" (空字符串)
> - null
> - undefined
> - NaN
>
> 除了以上列出的值之外，其他所有值都将被视为“truthy”，也就是真的。
>
> >---
> >
> >**上文“falsy”和“truthy”是什么意思**
> >
> >在JavaScript中，“falsy”和“truthy”是两个布尔值的概念，分别表示一个值在逻辑上被视为假或者真。
> >
> >一个“falsy”值在逻辑上被视为假。JavaScript中有七种“falsy”值：false、0、-0、""（空字符串）、null、undefined和NaN。如果一个值不是这些“falsy”值，那么它就是“truthy”，也就是在逻辑上被视为真。
> >
> >需要注意的是，“falsy”和“truthy”只是用于描述一个值在逻辑上被视为真还是假，并不意味着该值本身是布尔类型。在JavaScript中，任何值都可以被强制转换为布尔值，例如通过使用双重否定运算符“!!”，即“!!value”。所以说，一个“falsy”值在被强制转换为布尔值时会变成false，而一个“truthy”值则会变成true。

### ==2.== document.querySelectorAll()和document.getElementsByClassName();的区别是什么

> `document.querySelectorAll()`和`document.getElementsByClassName()`都是用于在Document对象中查找特定元素的方法，但它们有以下几个区别：
>
> 1. 返回值类型不同：`document.querySelectorAll()`返回的是一个NodeList对象，而`document.getElementsByClassName()`返回的是一个HTMLCollection对象。
>
> 2. 参数的写法不同：`document.querySelectorAll()`可以接受更复杂的选择器作为参数，例如类似CSS选择器的语法，而`document.getElementsByClassName()`只接受一个类名字符串作为参数。
>
> 3. 元素查找的范围不同：`document.querySelectorAll()`可以在整个文档中查找元素，而`document.getElementsByClassName()`只能在调用它的元素的子节点中查找元素。
>
> 4. 兼容性问题不同：`document.querySelectorAll()`支持IE8及以上版本，而`document.getElementsByClassName()`只支持IE9及以上版本。
>
> 因此，如果需要根据多个条件来查找元素，或者需要跨越整个文档查找元素，应该使用`document.querySelectorAll()`；如果只需要根据类名查找元素，并且不需要兼容IE9及以下版本，可以使用`document.getElementsByClassName()`。



### ==3.==给谷歌浏览器导出来的书签.html 添加样式和脚本 让它和导航栏的书签有一样的效果 写一个完整的demo

>  正在为您搜索：如何给谷歌浏览器导出的书签添加样式和脚本、如何让导出的书签和导航栏的书签有一样的效果、书签.html样式和脚本的完整demo
>
> 以下是一个完整的demo，实现了给谷歌浏览器导出来的书签.html添加样式和脚本，让它和导航栏的书签有一样的效果：
>
> ```html
> <!DOCTYPE html>
> <html>
> <head>
> 	<meta charset="UTF-8">
> 	<title>My Bookmarks</title>
> 	<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.4.1/css/bootstrap.min.css">
> 	<style>
> 		body {
> 			padding: 20px;
> 		}
> 		.bookmark {
> 			margin-bottom: 10px;
> 		}
> 		.bookmark .title {
> 			padding: 5px 10px;
> 			background-color: #f2f2f2;
> 			font-weight: bold;
> 			cursor: pointer;
> 		}
> 		.bookmark .content {
> 			display: none;
> 			padding: 5px 10px;
> 		}
> 		.bookmark .content a {
> 			display: block;
> 			padding: 2px 0;
> 			color: #333;
> 		}
> 	</style>
> </head>
> <body>
> 	
> 	<div class="container">
> 		
> 		<div class="row">
> 			<div class="col-md-6">
> 				<div class="bookmark">
> 					<div class="title">Bookmark Folder 1</div>
> 					<div class="content">
> 						<a href="https://www.google.com">Google</a>
> 						<a href="https://www.baidu.com">Baidu</a>
> 						<a href="https://www.taobao.com">Taobao</a>
> 					</div>
> 				</div>
> 			</div>
> 			<div class="col-md-6">
> 				<div class="bookmark">
> 					<div class="title">Bookmark Folder 2</div>
> 					<div class="content">
> 						<a href="https://www.github.com">Github</a>
> 						<a href="https://www.microsoft.com">Microsoft</a>
> 						<a href="https://www.apple.com">Apple</a>
> 					</div>
> 				</div>
> 			</div>
> 		</div>
> 		
> 	</div>
> 
> 	<script src="https://cdn.staticfile.org/jquery/3.5.1/jquery.min.js"></script>
> 	<script src="https://cdn.staticfile.org/popper.js/1.16.0/umd/popper.min.js"></script>
> 	<script src="https://cdn.staticfile.org/twitter-bootstrap/4.4.1/js/bootstrap.min.js"></script>
> 	<script>
> 		$(function() {
> 			$('.bookmark .title').click(function() {
> 				$(this).siblings('.content').slideToggle();
> 			});
> 		});
> 	</script>
> 
> </body>
> </html>
> ```
>
> 在这个demo中，我们使用了Bootstrap库来提供样式和布局，并使用jQuery库来实现交互效果。我们首先定义了一个.bookmark的样式类，用于设置整个书签的样式，其中包含一个.title类和一个.content类，用于分别表示书签标题和书签内容。
>
> 接着我们使用了Bootstrap的网格系统，将两个书签放在同一行内，每个书签占据页面宽度的一半。
>
> 我们使用jQuery库来实现展开/折叠功能，当用户单击书签的标题时就可以切换其下方内容的可见性。
>
> 最后，我们引入了所需的库文件，并将我们的JavaScript脚本放在页面底部以确保文档完全加载后再执行。
>
> 以上是一个简单的demo，您可以下载并根据自己的需求对其进行修改。



### ==4.== 异步问题

> - ~~**我要在https://www.jianfast.com/网站上用js拿到下面网页内容打印在控制台: https://www.douyin.com/user/MS4wLjABAAAAcOogp8WSlLvXNTPUg9b9brwWXQj76F9qeckY4T4w3kOzyuAMP-BFj2SbGqwIYwSZ?vid=7219194157544377637 请求方法: GET 返回 第一个<p class="iQKjW6dr">到页面**~~
>
>   你可以使用以下代码来获取页面内容并打印在控制台中:
>
>   ```javascript
>   fetch('https://www.douyin.com/user/MS4wLjABAAAAcOogp8WSlLvXNTPUg9b9brwWXQj76F9qeckY4T4w3kOzyuAMP-BFj2SbGqwIYwSZ?vid=7219194157544377637')
>     .then(response => response.text())
>     .then(text => {
>       let parser = new DOMParser();
>       let doc = parser.parseFromString(text, 'text/html');
>       let element = doc.querySelector('.iQKjW6dr');
>       console.log(element.textContent);
>     });
>   ```
>
>   请注意，这段代码可能不适用于所有网站，因为某些网站可能会阻止跨域请求。此外，如果页面结构发生变化，选择器也可能需要相应地进行更改。
>
>   ---
>
>   《如果报错《这个错误信息表明你的请求被CORS策略阻止了。CORS（跨域资源共享）是一种安全机制，它允许浏览器向不同域的服务器发送请求。然而，服务器需要在响应中包含一个`Access-Control-Allow-Origin`头，以指示浏览器允许来自特定域的请求。
>
>   在你的情况下，`https://www.douyin.com`服务器没有返回一个`Access-Control-Allow-Origin`头，所以浏览器阻止了你的请求。
>
>   有几种方法可以解决这个问题。一种方法是使用一个CORS代理，它会在你的请求和目标服务器之间充当中介，并在响应中添加适当的CORS头。另一种方法是在服务器端配置CORS策略，以允许来自你的域的请求。
>
>   请注意，更改服务器端的CORS策略需要对服务器有管理权限。》》
>
>   
>
> ---
>
> - **fetch是什么**
>
>   `fetch()`是一个JavaScript函数，它提供了一种简单的方法来获取网络资源。它返回一个`Promise`，该`Promise`在资源可用时解析为一个`Response`对象。你可以使用`Response`对象的方法来检查响应的状态和获取响应的内容。
>
>   例如，你可以使用`response.text()`方法来获取响应的文本内容，或者使用`response.json()`方法来获取响应的JSON内容。
>
>   下面是一个简单的例子，它使用`fetch()`函数从网络上获取一个JSON文件，并在控制台中打印出它的内容:
>
>   ```javascript
>   fetch('<URL>')
>     .then(response => response.json())
>     .then(data => console.log(data));
>   ```
>
>   请注意，由于`fetch()`返回一个`Promise`，所以你需要使用`.then()`方法来处理响应。你也可以使用`async/await`语法来简化代码。
>
>   ---
>
>   >**用js爬https://www.jianfast.com/ 来个简单的demo**
>   >
>   >下面是一个简单的JavaScript爬虫示例，它使用`fetch()`函数从`https://www.jianfast.com/`获取页面内容，并使用`DOMParser`来解析HTML并提取页面标题:
>   >
>   >```javascript
>   >fetch('https://www.jianfast.com/')
>   >  .then(response => response.text())
>   >  .then(text => {
>   >    let parser = new DOMParser();
>   >    let doc = parser.parseFromString(text, 'text/html');
>   >    let title = doc.querySelector('title').textContent;
>   >    console.log(title);
>   >  });
>   >```
>   >
>   >请注意，这段代码可能不适用于所有网站，因为某些网站可能会阻止跨域请求。此外，如果页面结构发生变化，选择器也可能需要相应地进行更改。
>   >
>   >---
>   >
>   >**对于阻止跨域请求的网站应该怎么做呢**
>   >
>   >如果你遇到了阻止跨域请求的网站，你可以考虑使用以下方法之一来解决这个问题:
>   >
>   >1. **使用CORS代理**: 你可以使用一个CORS代理服务器，它会在你的请求和目标服务器之间充当中介，并在响应中添加适当的CORS头。这样，浏览器就可以接收到来自目标服务器的响应，而不会被CORS策略阻止。
>   >
>   >2. **在服务器端配置CORS策略**: 如果你有权访问目标服务器，你可以在服务器端配置CORS策略，以允许来自你的域的请求。这样，当浏览器向目标服务器发送请求时，服务器会在响应中包含一个`Access-Control-Allow-Origin`头，指示浏览器允许来自你的域的请求。
>   >
>   >3. **使用其他语言或工具**: 如果上述方法都不可行，你可以考虑使用其他语言（如Python或Ruby）或工具（如`curl`或`wget`）来获取网页内容。这些语言和工具通常不受浏览器的CORS策略限制，因此可以更容易地获取跨域资源。
>   >
>   >请注意，在使用爬虫程序获取网页内容时，请确保遵守网站的服务条款，并尊重服务器的资源限制。
>
>   ---
>
>   **那可以用<iframe>嵌入https://www.jianfast.com/ 再在<iframe>里面请求。可以应对跨域请求吗**
>
>   > 不行，使用`<iframe>`嵌入其他网站的内容并不能解决跨域请求的问题。即使你在`<iframe>`中嵌入了其他网站的内容，你仍然无法从父页面中访问`<iframe>`中的内容，除非两个页面都同意通过`postMessage` API进行通信。
>   >
>   > 此外，许多网站会使用`X-Frame-Options` HTTP头来阻止其他网站在`<iframe>`中嵌入它们的内容。这意味着，即使你尝试在`<iframe>`中嵌入其他网站的内容，浏览器也可能会阻止这种行为。
>   >
>   > 总之，使用`<iframe>`嵌入其他网站的内容并不能解决跨域请求的问题。你需要使用其他方法（如CORS代理或服务器端配置）来解决这个问题。
>   >
>   > >---
>   > >
>   > >**我想知道如何使用postMessage API进行通信。**
>   > >
>   > >`postMessage` API允许不同来源的窗口之间进行安全的通信。这意味着你可以使用`postMessage` API在`<iframe>`和父页面之间，或者在不同标签页之间传递消息。
>   > >
>   > >下面是一个简单的例子，它演示了如何在父页面和`<iframe>`之间使用`postMessage` API进行通信:
>   > >
>   > >**父页面:**
>   > >
>   > >```html
>   > ><iframe src="iframe.html" id="my-iframe"></iframe>
>   > >
>   > ><script>
>   > >  let iframe = document.querySelector('#my-iframe');
>   > >
>   > >  // 向iframe发送消息
>   > >  iframe.contentWindow.postMessage('Hello from parent!', '*');
>   > >
>   > >  // 监听来自iframe的消息
>   > >  window.addEventListener('message', event => {
>   > >    console.log('Received message from iframe:', event.data);
>   > >  });
>   > ></script>
>   > >```
>   > >
>   > >**iframe页面 (`iframe.html`):**
>   > >
>   > >```html
>   > ><script>
>   > >  // 监听来自父页面的消息
>   > >  window.addEventListener('message', event => {
>   > >    console.log('Received message from parent:', event.data);
>   > >
>   > >    // 向父页面发送消息
>   > >    event.source.postMessage('Hello from iframe!', event.origin);
>   > >  });
>   > ></script>
>   > >```
>   > >
>   > >在上面的例子中，父页面使用`postMessage`方法向`<iframe>`发送了一条消息。然后，`<iframe>`页面监听`message`事件，并在收到消息时向父页面发送一条回复。
>   > >
>   > >请注意，在使用`postMessage` API时，你应该始终验证消息的来源和数据，以确保通信的安全性。
>   > >
>   > >---
>   > >
>   > >**我想知道如何验证postMessage API中消息的来源和数据。**
>   > >
>   > >在使用`postMessage` API时，验证消息的来源和数据是非常重要的，以确保通信的安全性。下面是一些验证消息来源和数据的方法:
>   > >
>   > >1. **验证消息来源**: 当你监听`message`事件时，你可以检查`event.origin`属性来确定消息的来源。这个属性包含了发送消息的窗口的来源（即协议、主机名和端口）。你应该始终验证`event.origin`是否与你期望的来源匹配，以防止接收到来自不受信任来源的消息。
>   > >
>   > >2. **验证消息数据**: 在处理收到的消息时，你应该始终验证消息数据的格式和内容是否符合预期。例如，你可以检查数据是否为预期的类型（如字符串或对象），并验证数据中包含的字段是否符合预期。这样可以防止处理不符合预期的数据，从而提高应用程序的安全性。
>   > >
>   > >下面是一个简单的例子，它演示了如何在接收到`postMessage`消息时验证消息来源和数据:
>   > >
>   > >```javascript
>   > >window.addEventListener('message', event => {
>   > >  // 验证消息来源
>   > >  if (event.origin !== '<URL>') {
>   > >    console.log('Received message from unexpected origin:', event.origin);
>   > >    return;
>   > >  }
>   > >
>   > >  // 验证消息数据
>   > >  if (typeof event.data !== 'object' || !event.data.myField) {
>   > >    console.log('Received unexpected message data:', event.data);
>   > >    return;
>   > >  }
>   > >
>   > >  // 处理消息
>   > >  console.log('Received message:', event.data.myField);
>   > >});
>   > >```
>   > >
>   > >在上面的例子中，我们首先检查了`event.origin`属性，以确保消息来自预期的来源。然后，我们检查了消息数据的格式和内容，以确保它符合预期。只有当这些检查都通过时，我们才会处理收到的消息。



### ==5.== 现在好多要页面都不用通过事件绑定元素了，那是怎么知道点击了那个元素的并做出不同的反应的

> 现在很多网页使用事件代理（Event Delegation）来处理这种情况。事件代理利用了事件冒泡（Event Bubbling）的原理，将事件监听器添加到父元素上，而不是直接添加到目标子元素上。当子元素触发事件时，事件会冒泡到父元素，然后在父元素的事件监听器中处理事件。
>
> 要实现这种方法，你可以按照以下步骤操作：
>
> 1. 为父元素添加事件监听器。
> 2. 在事件监听器的回调函数中，检查事件的目标元素（`event.target`）。
> 3. 根据目标元素的属性或其他信息（如类名、ID等），判断是哪个子元素被点击，并执行相应的操作。
>
> 以下是一个简单的例子，展示了如何使用事件代理处理点击事件：
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Event Delegation Example</title>
> </head>
> <body>
>     <div id="parent">
>         <button class="child">Button 1</button>
>         <button class="child">Button 2</button>
>         <button class="child">Button 3</button>
>     </div>
> 
>     <script>
>         document.getElementById('parent').addEventListener('click', function(event) {
>             const target = event.target;
> 
>             if (target.classList.contains('child')) {
>                 alert('Clicked: ' + target.textContent);
>             }
>         });
>     </script>
> </body>
> </html>
> ```
>
> 在这个例子中，我们将事件监听器添加到了ID为`parent`的父元素上。当用户点击按钮时，我们检查事件的目标元素是否包含`child`类，并根据点击的按钮弹出相应的提示信息。
>
> 这种方法的优势在于可以减少事件监听器的数量，提高性能。此外，即使在事件监听器绑定之后动态添加子元素，事件代理依然有效，无需为新添加的子元素重新绑定事件。
>
> **解释上面的script是什么意思**
>
> >这段代码是注册了parent元素的点击事件监听器。当parent元素或其子元素被点击时,会触发这个事件监听器。
> >
> >在监听器的回调函数中,它会获取被点击的目标元素target。
> >
> >然后它会检查这个目标元素target是否具有class名为child的class。如果有,则会弹出一个警告框,显示被点击元素的textContent。
> >
> >所以简而言之,这段代码检测parent元素或其子元素的点击,如果点击的是拥有class="child"的子元素,则会弹出一个警告框显示那个元素的文本。

### ==6.== JSONP夸域调用

> 你好！这是一个JSONP（JSON with Padding）跨域请求的示例。在这个例子中，你正在使用百度的搜索建议API。
>
> 首先，让我们分析这个URL：
>
> ```
> https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?jsoncallback=jQuery18002568176207224737_1681129677419&wd=%E4%BD%A0%E5%B9%B2%E5%98%9B&cb=keydata&_=1681129959331
> ```
>
> 这个URL包含以下参数：
>
> - `jsoncallback`: 用于指定回调函数名称，这里的回调函数名称是`jQuery18002568176207224737_1681129677419`。
> - `wd`: 搜索词，这里是经过URL编码的“你干嘛”。
> - `cb`: 可选参数，可以自定义回调函数的参数名称。在这个例子中，回调函数的参数名称为`keydata`。
> - `_`: 时间戳，用于缓存防止。这个参数的值通常是当前时间的毫秒数。
>
> 这是一个简单的JSONP跨域请求示例。为了使这个例子完整，我将展示一个HTML页面，里面包含一个JavaScript代码片段，用于发起这个JSONP请求并处理返回的数据：
>
> ```html
> <!DOCTYPE html>
> <html lang="zh-CN">
> <head>
>     <meta charset="UTF-8">
>     <title>JSONP 跨域调用示例</title>
>     <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
> </head>
> <body>
>     <h1>搜索建议</h1>
>     <input type="text" id="search" placeholder="输入搜索词">
>     <ul id="suggestions"></ul>
> 
>     <script>
>         //这个是报错修复方法
> 		function keydata(data) {
>             $('#suggestions').empty();
>             $.each(data.s, function(index, suggestion) {
>                 $('#suggestions').append('<li>' + suggestion + '</li>');
>             });
>         }
>         
>         //GPT4 给的方法
>         $(document).ready(function() {
>             $('#search').on('input', function() {
>                 var searchWord = $(this).val();
>                 var url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?jsoncallback=?&wd=' + encodeURIComponent(searchWord) + '&cb=keydata';
> 
>                 $.getJSON(url, function(keydata) {
>                     $('#suggestions').empty();
>                     $.each(keydata.s, function(index, suggestion) {
>                         $('#suggestions').append('<li>' + suggestion + '</li>');
>                     });
>                 });
>             });
>         });
>     </script>
> </body>
> </html>
> ```
>
> 在这个例子中，当用户在文本框中输入搜索词时，页面将发送JSONP请求并处理返回的搜索建议数据。这是一个完整的JSONP跨域请求示例。
>
> **上面报错**（修复了）
>
> 在这个示例中,跨域服务器返回的 JSON 数据中带有一个 keydata callback 函数名,但是在当前页面这个函数未定义,所以报错 Uncaught ReferenceError: keydata is not defined。
>
> 修复方法很简单,我们只需要在页面中提前定义这个 callback 函数即可:
>
> ```html
> <script>
> function keydata(data) {
>     // Use data
> } 
> </script>
> ```
>
> 这样,当跨域 JS 资源加载完毕,调用 keydata 函数时,就不会报错了。
>
> **==GPT3回答 JSONP夸域调用==**
>
> ```html
> <!DOCTYPE html>
> <html>
> <head>
>     <meta charset="UTF-8">
>     <title>JSONP Demo</title>
> </head>
> <body>
>   <p id="result"></p>
> 
>   <script>
> 	  //Claude+修复bug方法
> 	  function keydata(data) {
>     handleResponse(data.s[0]);
>   }
> 	  //gpt3直接运行报错方法
>     function handleResponse(response) {
>       document.getElementById('result').textContent = response;
>     }
> 
>     const script = document.createElement('script');
>     script.src = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?jsoncallback=jQuery18002568176207224737_1681129677419&wd=%E4%BD%A0%E5%B9%B2%E5%98%9B&cb=keydata&_=1681129959331';
>     document.body.appendChild(script);
>   </script>
> </body>
> </html>
> ```
>





### ==7.== 油猴来获取跨域请求html/text类型

>  正在为您搜索：页面https://www.jianfast.com/通过油猴来获取跨域请求html/text类型可以吗、帮我写一个demo
>
> 根据知识来源[1]中描述，"简法主页"是一个可以自定义搜索引擎的网站，并且没有提到它允许跨域请求，因此无法确切判断它是否可以通过油猴来获取跨域请求html/text类型。如果您要获取百度主页（https://www.baidu.com/）的html/text类型响应，可以使用以下代码作为参考：
>
> ```javascript
> // ==UserScript==
> // @name     Get Baidu HTML by Cross-Domain Request
> // @version  1
> // @grant    GM_xmlhttpRequest
> // ==/UserScript==
> 
> GM_xmlhttpRequest({
>     method: 'GET',
>     url: 'https://www.baidu.com/',
>     onload: function(response) {
>         console.log(response.responseText);
>     }
> });
> ```
>
> 这个油猴脚本会在安装后向百度主页发送一个GET请求，然后通过控制台输出响应文本。需要注意的是，有些网站可能不允许跨域请求，这时候就不能通过油猴获取跨域请求的html/text。
>
> 
>
>  **GM_xmlhttpRequest是？**
>
> >`GM_xmlhttpRequest`是一个特定于油猴（Tampermonkey）的XMLHttpRequest对象，用于发起跨域http/https请求和获取响应[[1](https://www.tampermonkey.net/documentation.php#_gm_xmlhttprequest)]。该对象并非标准浏览器内置的XMLHttpRequest对象，而是油猴为了方便脚本编写者进行跨域请求而提供的一个扩展。与普通的XMLHttpRequest对象相比，`GM_xmlhttpRequest`的使用方法基本相同，但它可以处理跨域请求、包括对https协议的支持，并提供更方便的回调函数，如onload、onerror等。另外需要注意的是，一些高保护级别的Chrome浏览器（如Google Chrome 87及以上版本）已经禁止了GM_xmlhttpRequest的使用，如果需要使用跨域请求，请使用GM.fetch()函数[[2](https://www.jianshu.com/p/f880878c1398)]。
>
> 
>
> **这段代码放在油猴里面会，进入页面是运行一次还是一直运行的**
>
> >```	javascript
> >    GM_xmlhttpRequest({
> >        method: 'GET',
> >        url: 'https://www.douyin.com/user/MS4wLjABAAAAcOogp8WSlLvXNTPUg9b9brwWXQj76F9qeckY4T4w3kOzyuAMP-BFj2SbGqwIYwSZ?vid=7219194157544377637',
> >        onload: function(response) {
> >            //console.log(response.responseText);
> >            // 处理返回结果
> >            let data = response.responseText;
> >            let parser = new DOMParser();
> >            let doc = parser.parseFromString(data, "text/html");
> >            let element = doc.querySelector("p.iQKjW6dr");
> >            document.getElementsByClassName("site-title")[0].innerText=element.textContent;
> >        }
> >```
> >
> >>该代码片段只会在页面加载时运行一次
> >
> > 
> >
> >**报错（不影响使用）Unchecked runtime.lastError: The message port closed before a response was received.**
> >
> >>这个错误是由于Chrome浏览器对于扩展的代码执行时间做了限制，如果超过了一定时间（通常为10秒），则会被认为是未响应的代码，从而被Chrome自动终止。当您尝试在油猴脚本中请求一个较慢的URL时，可能会遇到这个错误。解决这个问题的方法有：
> >>
> >>1. 缩短代码执行时间：优化您的代码，尽量减少需要花费大量时间的操作和网络请求，从而缩短代码执行时间。
> >>
> >>2. 延长超时时间：在油猴脚本中使用GM.xmlHttpRequest()发起请求时，可以设置timeout属性来延长请求的超时时间。例如：
> >>
> >>   ```javascript
> >>   GM.xmlHttpRequest({
> >>      method: "GET",
> >>      url: "https://www.example.com",
> >>      headers: {
> >>         "User-Agent": "Mozilla/5.0", //模拟浏览器请求
> >>         "Accept-Language": "zh-CN,zh;q=0.9" //设置接受语言
> >>      },
> >>      timeout: 20000, //延长请求超时时间（单位：毫秒）
> >>      onload: function(response) {
> >>          console.log(response.responseText);
> >>      }
> >>   });
> >>   ```
> >>
> >>   在上述代码中，timeout属性设置为20000，即20秒，表示请求的超时时间为20秒。如果在20秒内请求没有得到响应，将会触发onerror回调函数。
> >>
> >>3. 禁用油猴的自动更新：在某些情况下，油猴的自动更新会导致脚本执行时间过长，从而触发上述错误。您可以禁用油猴的自动更新功能，在油猴的设置中关闭“自动更新脚本”选项。
> >>



# ==Linux相关==

## ==1.==shell的常用命令

> 在 Linux 和 Unix-like 系统中，`shell` 是一个命令行界面，用于与操作系统进行交互。它允许用户执行各种命令来完成任务，如创建和管理文件、文件夹，运行程序，管理进程等。下面是一些常用的 shell 命令：
>
> 1. `ls`：列出目录中的文件和文件夹。
>
>    例如：`ls` 或 `ls /etc`
>
> 2. `cd`：切换当前工作目录。
>
>    例如：`cd /var/log`
>
> 3. `pwd`：显示当前工作目录的绝对路径。
>
> 4. `mkdir`：创建一个新的目录。
>
>    例如：`mkdir my_new_directory`
>
> 5. `rmdir`：删除一个空目录。
>
>    例如：`rmdir my_empty_directory`
>
> 6. `rm`：删除文件或目录。
>
>    例如：`rm myfile.txt` 或 `rm -r my_directory`
>
> 7. `cp`：复制文件或目录。
>
>    例如：`cp source.txt destination.txt` 或 `cp -r source_directory destination_directory`
>
> 8. `mv`：移动或重命名文件或目录。
>
>    例如：`mv old_name.txt new_name.txt` 或 `mv file.txt target_directory`
>
> 9. `cat`：输出文件内容到标准输出。
>
>    例如：`cat myfile.txt`
>
> 10. `grep`：在文件中搜索指定的文本模式。
>
>     例如：`grep "search_pattern" myfile.txt`
>
> 11. `find`：在目录中搜索文件。
>
>     例如：`find / -name myfile.txt`
>
> 12. `tar`：创建或提取 tar 归档文件。
>
>     例如：`tar -czvf archive.tar.gz my_directory` 或 `tar -xzvf archive.tar.gz`
>
> 13. `wget`：从网络上下载文件。
>
>     例如：`wget https://example.com/myfile.txt`
>
> 14. `curl`：与服务器进行数据传输。
>
>     例如：`curl -O https://example.com/myfile.txt`
>
> 15. `chmod`：更改文件或目录的权限。
>
>     例如：`chmod 755 myfile.txt`
>
> 16. `chown`：更改文件或目录的所有者和/或所属组。
>
>     例如：`chown user:group myfile.txt`
>
> 
>
> 这些只是 shell 命令的一部分，你可以在各种 Linux 和 Unix-like 系统中使用这些命令完成各种任务。每个命令都有许多选项和参数，可以根据需要调整命令的行为。要查看命令的详细信息和可用选项，请使用 `man` 命令查看命令的手册页，例如：`man ls`。
>
> 继续为您介绍更多的 shell 命令：
>
> 
>
> 17. `tail`：查看文件的末尾部分。
>
>     例如：`tail myfile.txt` 或 `tail -n 20 myfile.txt`（查看最后20行）
>
> 18. `head`：查看文件的开头部分。
>
>     例如：`head myfile.txt` 或 `head -n 20 myfile.txt`（查看前20行）
>
> 19. `sort`：对文件内容进行排序。
>
>     例如：`sort myfile.txt`
>
> 20. `uniq`：从排序后的文件中删除重复行。
>
>     例如：`sort myfile.txt | uniq`
>
> 21. `diff`：比较两个文件的差异。
>
>     例如：`diff file1.txt file2.txt`
>
> 22. `nano`、`vim`、`vi`、`emacs`：命令行文本编辑器。
>
>     例如：`nano myfile.txt` 或 `vim myfile.txt` 或 `vi myfile.txt` 或 `emacs myfile.txt`（根据你的喜好选择编辑器）
>
> 23. `du`：查看文件或目录占用的磁盘空间。
>
>     例如：`du -sh my_directory`
>
> 24. `df`：查看磁盘空间使用情况。
>
>     例如：`df -h`
>
> 25. `ps`：查看当前运行的进程。
>
>     例如：`ps aux`
>
> 26. `kill`：关闭进程。
>
>     例如：`kill 12345`（其中12345是进程ID）
>
> 27. `top`、`htop`：实时查看系统进程、内存和CPU使用情况。
>
>     例如：`top` 或 `htop`（需要先安装htop）
>
> 28. `uptime`：显示系统运行时间、负载和登录用户数。
>
> 29. `ping`：检查网络连接和延迟。
>
>     例如：`ping example.com`
>
> 30. `traceroute`：查看数据包在网络中的传输路径。
>
>     例如：`traceroute example.com`
>
> 31. `ssh`：通过安全 Shell（SSH）远程登录到其他计算机。
>
>     例如：`ssh user@example.com`
>
> 32. `scp`：通过安全 Shell（SSH）在计算机之间复制文件。
>
>     例如：`scp myfile.txt user@example.com:/target/directory`
>
> 33. `crontab`：管理定时任务。
>
>     例如：`crontab -e`（编辑定时任务）或 `crontab -l`（列出当前用户的所有定时任务）
>
> 
>
> 这只是 shell 命令的一部分，实际上还有许多其他命令和功能。要查看命令的详细信息和可用选项，请使用 `man` 命令查看命令的手册页，例如：`man tail`。熟练掌握这些命令可以帮助您更高效地完成许多系统管理和文件操作任务。
>
> 
>
> 以下是更多有用的 shell 命令：
>
> 34. `touch`：创建一个空文件或更新文件的访问和修改时间。
>
>     例如：`touch newfile.txt`
>
> 35. `ln`：创建一个指向文件或目录的硬链接或符号链接。
>
>     例如：`ln -s target.txt symlink.txt`（创建一个符号链接）
>
> 36. **`alias`：为命令创建别名。**
>
>     **例如：`alias ll='ls -la'`（创建一个名为 ll 的别名，用于显示详细的文件列表）**
>
> 37. `history`：显示命令历史记录。
>
> 38. `zip`、`unzip`：创建和解压 ZIP 归档文件。
>
>     例如：`zip archive.zip file1.txt file2.txt` 或 `unzip archive.zip`
>
> 39. `awk`：用于文本处理和数据提取的编程语言。
>
>     例如：`awk '{print $1}' myfile.txt`（输出文件中的第一列）
>
> 40. `sed`：流式编辑器，用于对输入文本进行基本文本转换。
>
>     例如：`sed 's/old/new/g' input.txt > output.txt`（将 input.txt 中的所有'old'替换为'new'，并将结果写入 output.txt）
>
> 41. `cut`：从文件的每一行中删除一部分文本。
>
>     例如：`cut -f 1,3 -d , myfile.csv`（显示文件中的第1和第3列）
>
> 42. `paste`：将多个文件的对应行连接在一起。
>
>     例如：`paste file1.txt file2.txt`
>
> 43. `wc`：统计文件中的行数、字数和字节数。
>
>     例如：`wc myfile.txt`
>
> 44. `bg`：将一个暂停的前台进程放到后台继续运行。
>
>     例如：`bg` 或 `bg %1`（其中 %1 是暂停的作业ID）
>
> 45. `fg`：将一个后台进程放到前台继续运行。
>
>     例如：`fg` 或 `fg %1`（其中 %1 是后台作业ID）
>
> 46. `jobs`：显示当前的作业（后台或暂停的进程）列表。
>
> 47. `nohup`：在后台运行命令，并在终端关闭时使其保持运行。
>
>     例如：`nohup my_command &`
>
> 48. `screen`、`tmux`：终端复用器，可以在一个终端窗口中运行多个会话。
>
>     例如：`screen` 或 `tmux`（需要先安装相应的软件包）
>
> 49. `mount`：挂载文件系统。
>
>     例如：`mount /dev/sdb1 /mnt/my_drive`
>
> 50. `umount`：卸载文件系统。
>
>     例如：`umount /mnt/my_drive`
>
> 这仅仅是 shell 命令的一部分，实际上还有许多其他命令和功能。要查看命令的详细信息和可用选项，请使用 `man` 命令查看命令的手册页，例如：`man touch`。熟练掌握这些命令可以帮助您更高效地完成许多系统管理和文件操作任务。



## ==2.==win10子系统（WLS）

**怎么进去**

> 1. 打开“开始”菜单，然后在搜索框中输入“cmd”或“命令提示符”，按回车键打开命令提示符。
>
> 2. 在命令提示符中输入`wsl`，然后按回车键。这将启动默认的WSL发行版（例如，Ubuntu）。
>
> 3. 您还可以直接从“开始”菜单运行已安装的WSL发行版。只需在“开始”菜单中找到对应的WSL发行版（例如，Ubuntu），点击它以启动终端。
>
> 4. > 如果您想要运行特定的WSL发行版，您可以在命令提示符中输入以下命令，其中`<发行版名称>`是您希望运行的WSL发行版的名称（例如，`Ubuntu-20.04`）：
>    >
>    > ```shell
>    > wsl -d <发行版名称>
>    > ```
>
>    如果您不确定已安装了哪些WSL发行版，可以在命令提示符中输入以下命令查看可用的WSL发行版列表：
>
>    ```shell
>    wsl --list --verbose
>    ```

---



### **忘记root密码**

> 1. 打开Windows命令提示符（cmd）或PowerShell。
>
> 2. 先列出您的WSL发行版，以找到您要重置密码的发行版的名称。在命令提示符或PowerShell中输入以下命令：
>
>    ```shell
>    wsl --list
>    ```
>
>    这将显示您已安装的WSL发行版列表。
>
>    
>
> 3. 假设您要重置的发行版名称为`Ubuntu-20.04`（请根据实际情况替换为您的发行版名称），使用以下命令以root用户身份启动WSL发行版：
>
>    ```shell
>    wsl -u root -d Ubuntu-20.04
>    ```
>
>    这将以root权限打开WSL终端。
>
>    > 如果默认发行版是`Ubuntu`
>    >
>    > ```shell
>    > wsl -u root
>    > ```
>
> 4. 现在，您可以使用`passwd`命令重置您的用户密码。将`<your-username>`替换为您的用户名（例如，yc556）：
>
>    ```shell
>    passwd <your-username>
>    ```
>
>    按照提示输入新密码，然后再次输入以确认。
>
>    
>
> 5. 完成密码重置后，输入`exit`退出WSL终端。
>
> 现在，您应该已经成功重置了WSL用户密码。尝试使用新密码登录或运行`sudo`命令。



### WSL文件夹移到D盘

（==还没试过==）

> 要将WSL（Windows Subsystem for Linux）的默认安装位置更改为D盘，您需要创建一个符号链接（symlink）来将WSL默认路径重定向到D盘。请遵循以下步骤：
>
> 1. 首先确保WSL未运行。在PowerShell（以管理员身份运行）中输入以下命令停止WSL服务：
>
>    ```
>    wsl --shutdown
>    ```
>
> 2. 接下来，将现有的WSL文件夹移到D盘。在PowerShell中输入以下命令（请根据实际情况替换`<D:\your\desired\path>`）：
>
>    ```
>    Move-Item "$env:USERPROFILE\AppData\Local\Packages" "<D:\your\desired\path>"
>    ```
>
>    例如，如果您希望将文件夹移动到D盘上的`WSL`文件夹中，可以使用以下命令：
>
>    ```
>    Move-Item "$env:USERPROFILE\AppData\Local\Packages" "D:\WSL"
>    ```
>
> 3. 创建一个指向新位置的符号链接。在PowerShell中输入以下命令（请根据实际情况替换`<D:\your\desired\path>`）：
>
>    ```
>    New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\AppData\Local\Packages" -Target "<D:\your\desired\path>"
>    ```
>
>    例如，如果您将文件夹移动到了D盘上的`WSL`文件夹中，可以使用以下命令：
>
>    ```
>    New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\AppData\Local\Packages" -Target "D:\WSL"
>    ```
>
> 完成以上步骤后，WSL将使用D盘上的新路径作为默认存储位置。
>
> 请注意，这个方法仅适用于将整个`Packages`文件夹（包括所有WSL发行版）移动到D盘。如果您只想将特定的WSL发行版移动到D盘，可以考虑使用`wsl --export`和`wsl --import`命令。





### 这么看wsl是1还是2

> 要确定您正在使用的是 WSL 1 还是 WSL 2，您可以在 Windows 命令提示符或 PowerShell 中运行以下命令：
>
> ```bash
> wsl.exe --list --verbose
> ```
>
> 或者使用简写：
>
> ```bash
> wsl -l -v
> ```
>
> 这将显示一个列表，其中包括已安装的 Linux 发行版以及每个发行版所使用的 WSL 版本。输出可能类似于以下内容：
>
> ```
>   NAME                   STATE           VERSION
> * Ubuntu                 Running         2
>   Debian                 Stopped         1
> ```
>
> 在这个示例中，我们可以看到 Ubuntu 发行版正在运行，并使用 WSL 2，而 Debian 发行版已停止，并使用 WSL 1。在您的系统上，版本号可能与此不同。



### wsl 怎么停止

> 在 Windows Subsystem for Linux（WSL）中，你可以使用以下方法来停止 WSL：
>
> 1. **使用命令行停止特定的 WSL 发行版：** 如果你知道要停止的 WSL 发行版的名称，可以使用以下命令来停止它：
>
>     ```bash
>     wsl --terminate <distribution-name>
>     ```
>
>     这里的 `<distribution-name>` 应该被替换为你要停止的 WSL 发行版的名称。例如，如果你要停止名为 "Ubuntu" 的 WSL 发行版，你可以运行以下命令：
>
>     ```bash
>     wsl --terminate Ubuntu
>     ```
>
> 2. **停止所有的 WSL 发行版：** 如果你想要停止所有正在运行的 WSL 发行版，你可以使用以下命令：
>
>     ```bash
>     wsl --shutdown
>     ```
>
>     这个命令会停止所有的 WSL 发行版和 WSL 2 的虚拟机。
>
> 这些命令都应该在 Windows 的命令提示符或 PowerShell 中执行。
>
> 请注意，当你停止一个 WSL 发行版时，所有在该发行版中运行的进程都会被终止，所有未保存的数据都会丢失。因此，你应该在运行这些命令之前保存所有的工作。



## ==3.==关于开启ssh

> 非gpt4解决：https://www.tinymind.net.cn/articles/da5b6aecd85361  但是gpt4也解决了要先打开ssh的问题
>
> 在腾讯云上拿到的Ubuntu主机分配给的用户是ubuntu用户，并不是root用户，而阿里云上拿到的Ubuntu主机分配给的用户就是root用户。如果没有root用户权限做事情会变得麻烦，每次做什么都要sudo一下，下面介绍怎么设置root用户的ssh登录：
>
> ### 1、设置root密码，可以修改成和ubuntu用户一样，方便记忆。先使用ubuntu用户ssh登录腾讯云，然后执行命令
>
> ```
> sudo passwd root
> ```
>
> 接着输入root密码，屏幕不会像Windows那样出现星号，输完密码敲回车键就可以了，要输入两次密码。
>
> ### 2、修改ssh登录的配置，即/etc/ssh/sshd_config文件，修改为允许root登录，可以执行命令
>
> ```
> sudo vim /etc/ssh/sshd_config
> ```
>
> 这里的sudo前缀不可少，否则接下来的修改无法保存。进入vim编辑，用方向键向下滚动找到PermitRootLogin这项，按下insert键进入插入模式，将PermitRootLogin后面的prohibit-password改为yes，再按下Esc键，然后依次按下:键(英文冒号键)、w键和q键，最后按下回车键，保存修改成功。
>
> ### 3、重启ssh服务使刚才的ssh配置的修改生效，执行命令
> ```
> sudo service ssh restart
> ```
>
> >---
> >
> >#### ==问gpt4==
> >
> >>[C:\~]$ 
> >
> >>Connecting to 172.23.72.37:22...
> >>Could not connect to '172.23.72.37' (port 22): Connection failed.
> >
> >>Type `help' to learn how to use Xshell prompt.
> >>==为什么会这样==
> >
> >>这个错误可能是由于几个原因造成的：
> >
> >>1. **SSH服务未启动**：在WSL中，你需要确保SSH服务已经启动。你可以通过运行`service ssh start`来启动SSH服务。
> >
> >>2. **防火墙阻止了连接**：你的防火墙可能阻止了对端口22的连接。你需要检查你的防火墙设置，确保它允许对端口22的连接。
> >
> >>3. **WSL和Xshell不在同一网络**：你需要确保WSL和Xshell在同一网络中。如果它们在不同的网络中，那么你可能无法建立连接。
> >
> >>4. **端口22被其他服务占用**：如果端口22被其他服务占用，那么你可能无法通过这个端口连接到WSL。你可以通过运行`netstat -tuln`来查看哪些端口正在被使用。
> >
> >>如果以上都无法解决问题，你可能需要查看更详细的错误信息，或者尝试使用其他工具（如PuTTY）进行连接，看看是否能成功。
> >
> >>==能连接了，但是我的密码是123456，但是在xshell里面显示SSH服务器拒绝了密码。请再试一次==
> >
> >>如果你确定你的密码是正确的，但是SSH服务器仍然拒绝你的密码，那么可能是因为SSH配置文件中禁止了密码认证。
> >
> >>你可以按照以下步骤检查并修改你的SSH配置：
> >
> >>1. 在WSL中，打开SSH配置文件。你可以使用`nano`或`vi`等文本编辑器打开它。命令是`sudo nano /etc/ssh/sshd_config`或`sudo vi /etc/ssh/sshd_config`。
> >
> >>2. 在配置文件中，找到==`PasswordAuthentication`==这一行。如果这一行的值是`no`，那么就意味着禁止了密码认证。你需要将它改为`yes`。
> >
> >>3. 保存并关闭配置文件。
> >
> >>4. 重新启动SSH服务。命令是
> >>
> >>   ```
> >>   sudo service ssh restart
> >>   ```
> >>
> >>   
> >
> >>现在，你应该可以使用密码连接到SSH服务器了。如果你仍然无法连接，那么可能需要检查你的用户名是否正确，或者是否有其他的SSH配置问题。
> >
> >>==执行命令sudo nano /etc/ssh/sshd_config 修改后无法esc ：qw==
> >
> >>你使用的是`nano`编辑器，而不是`vi`或`vim`编辑器，所以退出和保存文件的命令是不同的。
> >
> >>在`nano`编辑器中，你可以按下`Ctrl+X`来退出编辑器。然后，如果你对文件进行了修改，它会询问你是否要保存修改。你可以按下`Y`来保存修改，然后按下`Enter`来确认文件名。
> >
> >>所以，如果你在`nano`编辑器中修改了文件，你应该按下`Ctrl+X`，然后按下`Y`，最后按下`Enter`来保存修改并退出编辑器。
> >
> >

### 安装ssh

Ubuntu 自带了一个名为 OpenSSH 的 SSH 客户端和服务器软件包。在大多数情况下，您无需额外安装。

**SSH 客户端**

在默认情况下，Ubuntu 包含了 OpenSSH 客户端，您可以使用 `ssh` 命令连接到远程服务器。要验证您的系统上是否已经安装了 SSH 客户端，您可以在终端中运行：

```bash
ssh -V
```

此命令应返回 SSH 版本信息。如果没有安装 SSH 客户端，您可以通过以下命令安装：

```bash
sudo apt update
sudo apt install openssh-client
```

**SSH 服务器**

对于 SSH 服务器（允许其他人使用 SSH 连接到您的计算机），它不会在默认情况下安装。如果您想在您的 Ubuntu 系统上设置 SSH 服务器，您可以通过以下命令安装 OpenSSH 服务器：

```bash
sudo apt update
sudo apt install openssh-server
```

安装完成后，SSH 服务器将自动启动并运行。您可以通过以下命令检查 SSH 服务器的状态：

```bash
sudo systemctl status ssh
```

现在，您的 Ubuntu 系统应该可以接受来自其他计算机的 SSH 连接。确保在防火墙中允许 SSH 端口（默认为 22）。如果您使用的是 `ufw` 防火墙，可以使用以下命令允许 SSH：

```bash
sudo ufw allow ssh
```

#### 如果启动不了头大报错就先卸载重装

> 如果您的 SSH 配置文件变得混乱，重新安装 SSH 服务以恢复默认配置文件是一个有效的解决方案。以下是在 Ubuntu/Debian 系统上卸载和重新安装 OpenSSH 服务器的步骤：
>
> 1. 首先，卸载 OpenSSH 服务器：
>
>   ```bash
>    sudo apt-get remove --purge openssh-server
>   ```
> 
> 2. 清除相关的配置文件和数据：
> 
>   ```bash
>    sudo rm -rf /etc/ssh
>   ```
> 
> 3. 更新软件包列表：
> 
>   ```bash
>    sudo apt-get update
>   ```
> 
> 4. 重新安装 OpenSSH 服务器：
> 
>   ```bash
>    sudo apt-get install openssh-server
>   ```
> 
> 重新安装完成后，您将获得一个全新的 `/etc/ssh/sshd_config` 默认配置文件。您可以根据需要对其进行修改。完成修改后，请确保运行 `sudo sshd -t` 命令以检查配置文件的语法和有效性。最后，重新启动 SSH 服务以应用新配置：
> 
> ```bash
> sudo systemctl restart ssh
> ```
> 
> 现在，您应该拥有一个干净的 SSH 配置文件，并且 SSH 服务应该可以正常运行。如果您在执行这些步骤后仍然遇到问题，请提供有关错误的详细信息，以便我可以为您提供更多帮助。





## ==4.==关于Ubuntu环境改为中文

> 要将 WSL（Windows Subsystem for Linux）的默认语言更改为中文，您需要更新系统的语言环境。以下是一种方法，适用于基于 Debian 和 Ubuntu 的 WSL 发行版（如 Ubuntu、Kali Linux、Debian 等）：
>
> 1. **更新软件包列表**：
>
>    首先，更新软件包列表以确保您可以安装最新版本的软件包：
>
>    ```bash
>    sudo apt update
>    ```
>
> 2. **安装中文语言包**：
>
>    使用以下命令安装中文语言包：
>
>    ```bash
>    sudo apt install -y locales
>    sudo apt install -y language-pack-zh-hans language-pack-zh-hans-base
>    ```
>
> 3. **配置系统区域设置**：
>
>    使用以下命令配置系统区域设置：
>
>    ```bash
>    sudo dpkg-reconfigure locales
>    ```
>
>    在出现的界面中，使用上下箭头选择 `zh_CN.UTF-8`，然后按空格键选中它。接下来，按回车键继续。在下一个界面中，选择 `zh_CN.UTF-8` 作为默认区域设置。
>
> 4. **更新环境变量**：
>
>    打开文件 `~/.bashrc` 或 `~/.profile`（具体取决于您的系统配置），在文件末尾添加以下内容：
>
>    ```bash
>    export LANG=zh_CN.UTF-8
>    export LANGUAGE=zh_CN:zh
>    export LC_ALL=zh_CN.UTF-8
>    ```
>
>    保存并关闭文件。
>
>    >**再次检查环境变量**：
>    >
>    >运行以下命令，检查当前环境变量是否已设置为中文：
>    >
>    >```bash
>    >echo $LANG
>    >echo $LANGUAGE
>    >echo $LC_ALL
>    >```
>    >
>    >如果这些变量现在显示为中文设置，请注意，并非所有命令和程序都会根据系统语言自动更改为中文。某些程序可能需要单独配置才能使用中文界面。
>    >
>    >>如果运行结构为↓则是成功
>    >>
>    >>`yc556@yc2023:/mnt/c/Users/Administrator$ echo $LANG`
>    >>**`zh_CN.UTF-8`**
>    >>`yc556@yc2023:/mnt/c/Users/Administrator$ echo $LANGUAGE`
>    >>**`zh_CN:zh`**
>    >>`yc556@yc2023:/mnt/c/Users/Administrator$ echo $LC_ALL`
>    >>**`zh_CN.UTF-8`**
>
> 5. **应用更改**：
>
>    要使更改生效，重新启动 WSL 或运行以下命令：
>
>    ```bash
>    source ~/.bashrc
>    ```
>
>    或者：
>
>    ```bash
>    source ~/.profile
>    ```
>
> 现在，您的 WSL 系统应该使用中文作为默认语言。但请注意，并非所有命令和程序都会根据系统语言自动更改为中文。某些程序可能需要单独配置才能使用中文界面。
>
> ​	    **重启 WSL**：
>
> ​	**如果**更改仍未生效，请尝试关闭 WSL，然后重新启动它。要关闭 WSL，请运行以下命令：
>
> ```bash
> exit
> ```
>
> 然后，在 Windows 中重新启动 WSL。

==6.==安装ssh

**root@yc2023:~# service ssh start**
**`Failed to start ssh.service: Unit ssh.service not found.`**

> 您遇到的问题是尝试启动 SSH 服务时，系统找不到 `ssh.service`。这通常意味着 SSH 服务未安装或安装不完整。以下是在不同操作系统上安装并启动 SSH 服务的方法：
>
> **对于 Ubuntu/Debian 系统：**
>
> 1. 首先，确保安装了 `openssh-server` 软件包。使用以下命令安装：
>
>    ```bash
>    sudo apt update
>    sudo apt install openssh-server
>    ```
>
> 2. 安装完成后，使用以下命令启动 SSH 服务：
>
>    ```bash
>    sudo systemctl start ssh
>    ```
>
> 3. 若要在系统启动时自动启动 SSH 服务，请运行：
>
>    ```bash
>    sudo systemctl enable ssh
>    ```
>
> **对于 CentOS/RHEL 系统：**
>
> 1. 首先，确保安装了 `openssh-server` 软件包。使用以下命令安装：
>
>    ```bash
>    sudo yum install openssh-server
>    ```
>
> 2. 安装完成后，使用以下命令启动 SSH 服务：
>
>    ```bash
>    sudo systemctl start sshd
>    ```
>
> 3. 若要在系统启动时自动启动 SSH 服务，请运行：
>
>    ```bash
>    sudo systemctl enable sshd
>    ```
>
> 根据您提供的错误信息，看起来您可能在使用 Ubuntu/Debian 系统。请按照上述说明进行操作，如果问题仍然存在，请提供更多详细信息，以便我们为您提供更好的支持。



## ==5.==改变提示符颜色

> **注意每个用户都是不一样的文件，所以每个用户可以有不一样的颜色**
>
> 如果你想将提示符(`ikun@yc2023`)变为绿色，你可以在你的bash配置文件（通常是 `~/.bashrc` 或 `~/.bash_profile`）中添加或修改 `PS1` 变量的值。这里是一个例子，它将提示符设置为绿色：
>
> ```bash
> PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\w\$ '
> ```
>
> 在这个例子中，`\033[01;32m` 是开始设置为绿色的转义序列，`\033[00m` 是重置颜色的转义序列。
>
> 同样，要使改变生效，你需要重新加载bash配置文件。你可以关闭并重新打开终端，或者在终端中运行以下命令：
>
> ```bash
> source ~/.bashrc
> ```
>
> 或者(Ubuntu 是上面其他暂时不知道)
>
> ```bash
> source ~/.bash_profile
> ```
>
> 记住，不同的系统可能使用不同的bash配置文件，你可能需要调整上述命令以适应你的系统。如果你使用的是其他类型的Shell（例如zsh），你可能需要修改其他文件（例如 `~/.zshrc`）。
>
> ---
>
> 在终端中，你可以使用ANSI转义码来设置文本颜色。下面是一些常用的颜色和相应的ANSI转义码：
>
> - 黑色：`0;30`
>
> - 红色：`0;31`
>
> - 绿色：`0;32`
>
> - 黄色：`0;33`
>
> ```bash
>   PS1='\[\033[0;33m\]\u@\h\[\033[00m\]:\w\$ '
> ```
>
> - 蓝色：`0;34`
>
> - 紫色：`0;35`
>
> - 青色：`0;36`
>
> - 白色：`0;37`
>
> 如果你想使用更亮的颜色，可以将前缀从 `0` 改为 `1`。例如，亮红色的代码是 `1;31`。
>
> 这是一个示例，将提示符设置为亮紫色：
>
> ```bash
> PS1='\[\033[01;35m\]\u@\h\[\033[00m\]:\w\$ '
> ```



## ==6.== （多个）选择默认py

> `sudo update-alternatives --config python3`
>
> 然后给你选，0123...



# ==Git问题==

## ==1.== git怎么对已管理的文件夹取消管理

> 要让 Git 取消对已管理文件夹的跟踪，您需要执行以下步骤：
>
> 1. **将文件夹添加到 `.gitignore` 文件**：
>
>    在项目根目录下，打开或创建一个名为 `.gitignore` 的文件。然后，将需要取消管理的文件夹添加到此文件中。假设您想取消对 `untracked_folder/` 文件夹的管理，可以将以下内容添加到 `.gitignore` 文件：
>
>    ```gitignore
>    untracked_folder/
>    ```
>
>    请注意，末尾的斜杠表示这是一个文件夹。添加文件夹名称后，保存并关闭 `.gitignore` 文件。
>
> 2. **从 Git 仓库中删除文件夹**：
>
>    虽然已将文件夹添加到了 `.gitignore` 文件中，但它仍在 Git 仓库中。要从仓库中删除文件夹（但保留在工作目录中），请执行以下命令：
>
>    ```bash
>    git rm -r --cached untracked_folder/
>    ```
>
>    这将会从 Git 的索引中移除 `untracked_folder/` 及其下的所有文件和子文件夹，但它们仍会保留在您的工作目录中。
>
> 3. **提交更改**：
>
>    最后，您需要提交这些更改：
>
>    ```bash
>    git commit -m "从版本控制中删除未跟踪的文件夹"
>    ```
>
> 现在，`untracked_folder/` 及其下的所有文件和子文件夹将不再受 Git 管理。
>
> >如果要取消对单个文件的跟踪，您不需要使用 `-r` 选项，因为它是用于递归地处理文件夹的。您可以使用以下命令来取消对文件的跟踪：
> >
> >```
> >git rm --cached 文件名
> >```





## ==2.== Git 使用代理

> 如果你的网络环境有限制，如在某些公司网络或地区网络中，可能无法直接访问 GitHub，你可能需要配置 Git 使用代理来连接 GitHub。
>
> 你可以使用如下命令来配置 Git 使用 HTTP 或 HTTPS 代理：
>
> ```bash
> # 设置 http 代理
> git config --global http.proxy 'http://127.0.0.1:2334'
> 
> # 设置 https 代理
> git config --global https.proxy 'https://127.0.0.1:2334'
> ```
>
> 请将其中的 `proxyserver` 和 `port` 替换为你的代理服务器的地址和端口。
>
> 如果你的代理服务器需要用户名和密码，可以这样设置：
>
> ```bash
> git config --global http.proxy 'http://username:password@proxyserver:port'
> git config --global https.proxy 'https://username:password@proxyserver:port'
> ```
>
> 其中的 `username` 和 `password` 是你的代理服务器的用户名和密码。
>
> 如果你想取消代理设置，可以使用如下命令：
>
> ```bash
> git config --global --unset http.proxy
> git config --global --unset https.proxy
> ```
>
> 以上命令全局设置了 Git 的代理服务器，如果你只想针对特定的仓库设置代理，可以去掉 `--global` 选项，在仓库的目录下运行这些命令。
>
> >以下是设置仓库级别 http 和 https 代理的命令：
> >
> >```bash
> ># 设置 http 代理
> >git config http.proxy 'http://127.0.0.1:2334'
> >
> ># 设置 https 代理
> >git config https.proxy 'https://127.0.0.1:2334'
> >```
> >如果你想移除这些代理设置，你可以运行 `git config --unset http.proxy` 和 `git config --unset https.proxy`。




# ==docker问题==

## ==1.== 理解docker

> **镜像就像是预装了应用程序的“轻量级操作系统”，而容器就像是运行在这种“轻量级操作系统”上的一个应用程序。**
>
> >- **镜像（Image）**: 镜像可以被视为一个只读的模板，包含了运行一个应用所必需的代码、库、环境变量和配置文件。你可以将它想象成预装了应用程序和配置的操作系统映像，但并不包含操作系统本身的全部功能和文件。镜像可以被用来创建 Docker 容器。
> >
> >- **容器（Container）**: 容器是镜像的运行实例。你可以将它类比为一个运行的应用程序，它运行在自己的隔离环境中，并具有自己的文件系统。尽管容器可以访问主机系统的资源，但它并不具备操作系统的全部功能。例如，容器不能运行自己的内核或启动其它的容器。
> >
> >  
> >
> >  **他们之间的关系**
> >
> >  ```gherkin
> >  Docker
> >  |
> >  |-- 镜像1
> >  |    |-- 容器1.1
> >  |    |-- 容器1.2
> >  |    |-- 容器1.3
> >  |
> >  |-- 镜像2
> >  |    |-- 容器2.1
> >  |    |-- 容器2.2
> >  |
> >  |-- 微服务应用
> >  |    |-- 服务A (运行在容器1.1)
> >  |    |-- 服务B (运行在容器1.2 和 容器2.1)
> >  |    |-- 服务C (运行在容器2.2)
> >  ```
>
> ---
>
> **一个镜像只能放一个应用吗**
>
> 在 Docker 中，推荐的做法是每个镜像只包含一个应用及其依赖。这样做的优点是可以保持镜像的体积小，使得管理和部署变得更加简单，并且可以提高安全性。此外，将每个应用放在单独的容器中，可以使得每个应用都在隔离的环境中运行，并且可以独立地扩展和管理每个应用。
>
> 然而，这并不是一个硬性规定。一个 Docker 镜像中确实可以包含多个应用，只要这些应用的文件都包含在镜像的文件系统中，并且镜像的启动命令能够启动所有需要的进程。但是，这种做法并不常见，也不推荐，因为这样会使得镜像的管理变得复杂，也可能会增加镜像的体积。
>
> 所以，虽然技术上可以在一个 Docker 镜像中包含多个应用，但是在大多数情况下，每个镜像应该只包含一个应用及其依赖。







# ==py问题==

## ==1.==TOML在py中怎么用

> 在 Python 中使用 TOML（Tom's Obvious, Minimal Language），您需要安装一个 TOML 库，例如 `toml` 或 `tomli`。这些库允许您解析 TOML 文件并将其内容转换为 Python 数据结构，例如字典。相反，您还可以将 Python 数据结构转换为 TOML 格式的字符串。
>
> 我将向您展示如何使用 `tomli` 库。首先，使用以下命令安装 `tomli`：
>
> ```bash
> pip install tomli
> ```
>
> 安装完成后，您可以按照以下示例使用 `tomli`：
>
> ### 1. 从 TOML 文件读取
>
> 假设您有一个名为 `config.toml` 的 TOML 文件，内容如下：
>
> ```toml
> [database]
> host = "localhost"
> port = 5432
> user = "myuser"
> password = "mypassword"
> ```
>
> 要在 Python 中解析此文件，您可以执行以下操作：
>
> ```python
> import tomli
> 
> # 读取 TOML 文件
> with open("config.toml", "r", encoding="utf-8") as file:
>     config = tomli.load(file)
> 
> # 访问配置数据
> host = config["database"]["host"]
> port = config["database"]["port"]
> user = config["database"]["user"]
> password = config["database"]["password"]
> 
> print(host, port, user, password)
> ```
>
> ### 2. 将 Python 数据结构转换为 TOML
>
> 假设您有一个 Python 字典，您想将其转换为 TOML 格式并将其保存到文件中：
>
> ```python
> import tomli
> 
> config = {
>     "database": {
>         "host": "localhost",
>         "port": 5432,
>         "user": "myuser",
>         "password": "mypassword",
>     }
> }
> 
> # 将 Python 字典转换为 TOML 字符串
> toml_string = tomli.dumps(config)
> 
> # 将 TOML 字符串写入文件
> with open("config_new.toml", "w", encoding="utf-8") as file:
>     file.write(toml_string)
> ```
>
> 这将创建一个名为 `config_new.toml` 的文件，其中包含字典的 TOML 表示。



# ==其他问题==

## ==1.==临时邮箱

> 美国临时邮件网站提供一次性或临时电子邮件地址，以帮助用户避免垃圾邮件和保护隐私。以下是一些受欢迎的临时邮件网站：
>
> 1. **Temp Mail** (https://temp-mail.org/zh/)
>    提供临时、安全、匿名、免费、一次性的电子邮件地址。
>
> 2. **10 Minute Mail** (https://10minutemail.com)
>    提供一个随机生成的临时电子邮件地址，有效期为10分钟，可延长时间。
>
> 3. **Mailinator** (https://www.mailinator.com)
>    提供免费的公共临时电子邮件地址，无需注册，但收件箱对所有人可见。
>
> 4. **Guerrilla Mail** (https://www.guerrillamail.com)
>    提供自定义用户名的临时邮件地址，有效期为1小时，可接收和发送邮件。
>
> 5. **ThrowAwayMail** (https://www.throwawaymail.com)
>    提供一个新的临时邮件地址，只要在浏览器中保留页面，邮件地址将保持有效。
>
> 请注意，临时邮件服务可能不适用于所有情况，有时会被一些网站和服务识别并拒绝接受。尽管如此，它们在一些场景下仍然是非常有用的工具，特别是在需要保护隐私或避免垃圾邮件时。





## ==2.== v2rayN绕过大陆还是有跑到代理去的

>  版本有点旧，新版界面变化有点大但核心点还是没有变的
>
> ![img](https://img-blog.csdnimg.cn/17d980c5006c4bb79d0fa3c8e712d228.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)编辑
>
>  ![img](https://img-blog.csdnimg.cn/c63398b28ff64052b2b81cf3b80450b8.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)
>
>  <img src="https://img-blog.csdnimg.cn/c0884614d81f4961864d69d01c4ff475.png" alt="img" style="zoom:33%;" />![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)
>
>  ↑双击进去
>
> 
>
> **注意，这里有个坑，它是按排序来的，我试过代理在最前面直连都不会走就直接走代理了，所以一定要先把直连放最前面**
>
> ![img](https://img-blog.csdnimg.cn/5df0048ce77d4735a14a28848810a814.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)
>
>  然后一路确定就好了
>
> 
>
>  ![img](https://img-blog.csdnimg.cn/fb8098b5e6b04438aefd7311c801a527.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)
>
> 
>
> ![img](https://img-blog.csdnimg.cn/dd5bdc0640ad4140a4ef8e8940ddbefa.jpeg)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)
>
>  ![img](https://img-blog.csdnimg.cn/f8edf2dca5bf481f9afeb0731f7906d6.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)
