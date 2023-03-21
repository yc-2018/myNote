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









# ==玩转win==

### ==1.==我有一个应用demo.exe 每次开机用双击才能运行  有没有办法让这个应用在我开机的时候就自动运行

> 是的，有几种方法可以让应用程序在开机时自动运行：
>
> 1. **将应用程序的快捷方式添加到Windows启动文件夹中。要打开该文件夹，请按下Windows + R键，在运行对话框中输入shell:startup，然后按Enter键。将应用程序的快捷方式拖放到此文件夹中即可。**
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
>   >   复制代码MIT License
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
