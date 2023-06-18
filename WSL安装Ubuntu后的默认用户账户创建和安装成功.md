# WSL安装Ubuntu后的默认用户账户创建和安装成功

有什么可以帮你的吗

## win10 安装Ubuntu后 Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: yc556
New password:
Retype new password:
passwd: password updated successfully
Installation successful!他的root密码是什么


在Ubuntu中，默认情况下是不设置root密码的。你可以使用sudo命令来执行需要root权限的操作，输入你所设置的UNIX用户的密码即可。如果你真的需要设置root密码，可以使用以下命令来修改：

sudo passwd root

然后会要求你输入新的root密码。

## yc556@yc2023:~$ su
Password:
su: Authentication failure


在WSL中，默认没有启用root用户的登录（类似于其他Unix/Linux系统）。尝试使用你创建的UNIX用户的密码来代替`su`命令，这个UNIX用户会拥有sudo权限，可以执行可以访问root权限的操作。例如，如果需要使用root权限执行某个命令，可以使用以下命令:

```
sudo command_name
```

或者，可以在使用`su`命令之前先通过`sudo su`切换为root用户。

如果你对默认没有启用root用户登录造成的WSL不同的安全性设置有任何疑问，可以查看WSL官方文档来了解详细信息。

## win10怎么进入Linux子系统


你可以通过以下步骤在Windows 10上进入Linux子系统：

1. 打开Windows 10的开始菜单，并在搜索框中输入“Microsoft Store”。

2. 在Microsoft Store中搜索“Linux”，并选择你喜欢的Linux发行版，例如Ubuntu、openSUSE、Kali Linux等等。

3. 安装所选的Linux发行版。安装过程可能需要一些时间，具体取决于你的网络速度。

4. 打开Windows 10的开始菜单，并在搜索框中输入“PowerShell”。

5. 右键单击“Windows PowerShell”，并选择“以管理员身份运行”。

6. 在Windows PowerShell中运行以下命令以启动你的Linux子系统：

```
wsl
```

7. 这将启动Linux子系统并打开一个Linux终端窗口，你现在可以在Linux中运行命令了。

注意：在Windows 10中安装Linux子系统可能需要开发人员模式启用。如果你还没有启用开发人员模式，可以按照以下步骤启用：

1. 打开Windows 10的开始菜单，并在搜索框中输入“设置”。

2. 选择“更新和安全”。

3. 选择“针对开发人员”，并选择“开发人员模式”。

4. 重启Windows 10。

## 「的ascll码


ASCII码是一种用于将字符编码为数字的标准编码方式。每个ASCII字符都有唯一的数字值，可以使用该值来表示该字符。例如，字母A的ASCII值为65，数字0的ASCII值为48。

如果你想查找一个字符的ASCII值，可以在编程语言中使用对应函数，比如在python中，使用`ord()`函数可以获取一个字符的ASCII码值，例如：

```
print(ord('A'))
```

输出结果为65。

反之，如果你知道一个ASCII值，并想知道它对应的字符是什么，可以使用对应编程语言提供的函数，例如在python中，可以使用`chr()`函数，如下所示：

```
print(chr(65))
```

输出结果为A。

## 「这个符号的ascII码


抱歉，你没有指定这个符号是什么，因此我无法告诉你它的ASCII码。请告诉我这个符号是什么或提供更多的上下文，我会尽力回答你的问题。

## 「

这个符号是一个空格，它的ASCII码是32。

## Linux怎么粘贴


在Linux系统中，可以使用鼠标中键或者组合键Ctrl+Shift+V来进行粘贴操作，具体方法如下：

1. 鼠标中键粘贴：
在Linux中，可以使用鼠标中键来进行粘贴操作。将鼠标光标放在你要复制的文本上，然后在你要粘贴的目标位置，使用鼠标中键（一般是按下鼠标滚轮的按钮）即可完成粘贴操作。

2. 组合键粘贴：
在大多数Linux发行版中，可以使用组合键Ctrl+Shift+V来进行粘贴操作。在你要粘贴的目标位置，先按下Ctrl+Shift，然后再按下V，在一些Linux系统中只需要按下Ctrl+V即可。

注意：这两种方法都是在命令行和图形界面都适用的。如果你在命令行界面下使用，那么只能使用第二种组合键粘贴方法。如果你在通过SSH远程登录到Linux系统中，那么只能使用第二种组合键粘贴方法。

## Command 'ifconfig' not found, but can be installed with:
sudo apt install net-tools

如果在 Linux 系统中运行 `ifconfig` 命令，但是显示 `Command 'ifconfig' not found` 错误信息，通常是因为缺少 `ifconfig` 命令的安装包。在大多数当前版本的 Linux 系统中，`ifconfig` 命令已被 `ip` 命令取代。可以尝试以下两种方法解决问题： 

1. 使用 `ip` 命令代替 `ifconfig`
   可以在终端中使用 `ip addr` 命令来查看网络设置信息。`ip` 命令支持的功能更丰富，而且在许多 Linux 系统上已经成为默认网络配置工具。

2. 安装 `ifconfig` 命令
   如果你仍然需要使用 `ifconfig` 命令，可以根据提示使用命令 `sudo apt install net-tools` 安装 `net-tools` 包。在安装完毕后，应该可以找到 `ifconfig` 命令并正常运行了。

## ip命令怎么用


`ip` 命令是 Linux 下一个非常重要的网络工具，用来查看与配置网络接口和路由表等。以下是一些常见的 `ip` 命令的用法：

1. 查看网络接口的信息

   使用 `ip a` 或 `ip addr show` 命令来查看网络接口的详细信息，包括接口名称、IP地址、MAC地址等等。

2. 配置网络接口的信息

   使用 `ip addr add` 命令来配置指定网络接口的IP地址和掩码。例如，要将接口 `eth0` 的IP地址设置为 `192.168.1.100/24`：`sudo ip addr add 192.168.1.100/24 dev eth0`

3. 查看路由表

   使用 `ip route` 或 `ip r` 命令来查看当前系统的路由表信息，包括目标网络、网关、出口接口等等。

4. 添加路由

   使用 `ip route add` 命令添加一条新的路由项，指明数据包要走的目标网络和网关地址。例如，要添加一条到 `192.168.2.0/24` 网络的路由，下一跳为 `192.168.1.1`：

   `sudo ip route add 192.168.2.0/24 via 192.168.1.1 dev eth0`

5. 删除路由

   使用 `ip route del` 命令删除路由表中的一条路由项。例如，要删除一条到 `192.168.2.0/24` 网络的路由，下一跳为 `192.168.1.1`：

   `sudo ip route del 192.168.2.0/24 via 192.168.1.1`

以上是 `ip` 命令的常见用法，使用 `man ip` 命令或者 `ip --help` 命令可以查看完整的帮助文档。

## xshell怎么连接win的Linux子系统


要使用 Xshell 连接 Windows 的 WSL (Windows Subsystem for Linux)，可以使用以下步骤：

1. 打开 Windows 系统的 Linux 子系统

   首先，你需要在 Windows 设置中启用 WSL，并安装所需的 Linux 操作系统。

2. 打开 Xshell 应用程序

   打开 Xshell 应用程序，并创建一个新会话。

3. 配置会话参数

   在新会话中，配置以下参数：

   - 协议：SSH
   - 主机名：localhost
   - 端口号：默认为 22
   - 用户名：在 Linux 子系统中创建的用户名
   - 认证方式：密码认证

4. 启用 X11 转发

   在 Xshell 会话的选项卡中找到 "SSH" 选项，然后选择 "X11" 选项卡。启用 "转发 X11 会话" 选项，并配置正确的 X display 地址（一般为 localhost:0.0）。

5. 连接 Linux 子系统

   单击 "连接" 按钮，连接到 Linux 子系统。在连接过程中，你将需要输入密码以进行身份验证。

连接成功后，你就可以在 Xshell 中操作 Linux 子系统了。

## 启用 X11 转发找不到


如果你在 Xshell 选项卡中找不到 "SSH" -> "X11" 选项，那么可能是因为 X11 转发功能没有打开。可以按照以下步骤打开 X11 转发：

1. 安装 X11

   确保你已经安装了 X11 服务器，在 Windows 中安装 Xming 或者 VcXsrv。可以在官方网站上下载并安装。

2. 在 Linux 子系统中安装并配置 X11 环境

   在 Linux 子系统中安装 X11 工具和库。可以在 Linux 中打开终端，并使用以下命令安装 X11：

   ```
   sudo apt install x11-apps
   ```

   安装完成后，运行以下命令配置 X11：

   ```
   export DISPLAY=:0.0
   ```

   这个命令将配置 X11 在 localhost 上启用，默认显示端口为 0.0。

3. 启用 X11 转发

   打开 Xshell，并在新建的会话中选择 "SSH" -> "隧道" 选项卡。在 "本地隧道" 中添加以下信息：

   - 本地地址：127.0.0.1
   - 本地端口：6000
   - 远程地址：localhost
   - 远程端口：6000

   然后单击 "添加" 按钮创建隧道。最后，在 "SSH" -> "高级" 选项卡中启用 "启用 X11 转发"。

4. 连接到 Linux 子系统

   最后，连接到 Linux 子系统，并在终端中启动需要使用 X11 的应用程序。例如，可以在终端中运行 X11 图形界面下的应用程序 `xclock`，并在 Xming 中查看窗口是否正常显示。

如果你没有找到 "SSH" -> "X11" 选项，可能是因为 X11 转发功能没有打开或者需要升级 Xshell 到支持 X11 转发的版本。

## Host 'localhost' resolved to ::1.
Connecting to ::1:22...
Host 'localhost' resolved to 127.0.0.1.
Connecting to 127.0.0.1:22...
Could not connect to 'localhost' (port 22): Connection failed.

Type `help' to learn how to use Xshell prompt.


根据这段错误提示信息，Xshell 可以解析 "localhost" 主机名并尝试连接到端口 22，但连接失败了。这个问题可能是由于以下原因导致的：

1. SSH 服务没有启动

   确认 SSH 服务已经在 Linux 子系统中启动。可以在 Linux 子系统中运行以下命令来检查：

   ```
   sudo service ssh status
   ```

   如果 SSH 服务未启动，可以使用以下命令将其启动：

   ```
   sudo service ssh start
   ```

2. 防火墙阻止了连接

   如果 Linux 系统上的防火墙设置了限制，可能会阻止 SSH 连接。请确保防火墙允许 SSH 协议通过，或者在连接之前暂时关闭防火墙。

3. SSH 配置错误

   如果 SSH 配置有误，也可能导致连接失败。可以检查 Linux 子系统中 SSH 的配置文件 `/etc/ssh/sshd_config`，确保以下配置项被正确设置：

   ```
   Port 22
   ListenAddress 0.0.0.0
   ```

   其中，`Port` 配置项指定 SSH 服务监听的端口号为 22，`ListenAddress` 配置项指定 SSH 服务监听的地址为 0.0.0.0（即监听所有的网络接口）。

4. X11 转发配置错误

   如果使用了 X11 转发，确认 X11 转发已经正确启用。可以检查 Xshell 会话设置中的 "SSH" -> "高级" 选项卡，确保已经启用了 "启用 X11 转发" 选项。

5. 连接地址错误

   如果在 Xshell 中使用的连接地址不是本机，请确认连接地址是否正确，应该填写 Linux 子系统的 IP 地址。

## yc556@yc2023:/mnt/c/Users/Administrator$ sudo service ssh start
ssh: unrecognized service


如果你运行 `sudo service ssh start` 命令启动 SSH 服务时出现 "ssh: unrecognized service" 错误，可能是因为 SSH 服务并没有被安装在你的 Linux 子系统中，因此系统无法识别 `ssh` 服务名。

要安装 SSH 服务，请使用以下命令：

```
sudo apt-get update
sudo apt-get install openssh-server
```

安装完成后，可以使用 `sudo service ssh start` 命令启动 SSH 服务。同时，为了避免出现类似问题，可以使用以下命令检查 SSH 服务是否运行：

```
sudo service ssh status
```

确保 SSH 服务正在运行并且没有出现错误。

## xshlle和cmd运行wsl有什么不一样

在 Windows 10 上，有多种方式可以运行 WSL (Windows Subsystem for Linux)，包括使用图形界面的 Terminal 应用和命令行界面的 PowerShell、CMD 和 Xshell 等。不同的方式会对 WSL 的运行环境和性能产生影响，下面简要介绍 Xshell 和 CMD 运行 WSL 的不同之处：

1. 用户体验

   Xshell 是一个 Windows 下的 SSH 客户端，提供了图形化的用户界面和方便的操作功能，使得连接到 Linux 主机变得更加便捷。由于 Xshell 显示的是一个独立的窗口，所以用户可以非常灵活地调整连接窗口大小和位置，而不会干扰其他应用程序窗口的布局。

   而 CMD 则只提供了纯文本的控制台界面，用户需要手动输入命令来与 WSL 交互。这种方式比较适合熟悉命令行操作的用户，但是不够直观，需要花费更多的时间和精力来完成一些常见的操作。

2. 兼容性

   Xshell 支持常见的 SSH 协议和密钥认证方式，因此可以与大多数 Linux 发行版兼容。同时，Xshell 还支持 X11 转发和 SFTP 等功能，可以方便地上传和下载文件，或者运行需要 X11 支持的应用程序。

   CMD 则只提供了基础的命令行当作控制台，缺少许多图形化的工具和功能，需要使用其他工具进行补充。

3. 性能

   Xshell 针对 SSH 连接进行了优化，使用了更快的加密算法和压缩机制，因此可以和 Linux 主机建立更快速和稳定的连接。与之相比，CMD 运行 WSL 时，可能会受到 Windows 系统磁盘读写速度、网络传输速度等因素的影响，导致运行速度较慢。

综上所述，Xshell 相对于 CMD 更加方便易用，同时具有更广泛的兼容性和更好的性能，也可以提供一些图形化的工具和功能。但是如果你熟练于使用命令行操作，CMD 可能更适合你。