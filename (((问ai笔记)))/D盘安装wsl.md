要在特定的目录（如 `D:\wsl`）上安装 WSL 分发，您可以使用 `wsl.exe` 命令在 `D:\wsl` 中创建一个新的 WSL 分发。请按照以下步骤操作：

1. 首先，请确保您已启用 WSL 功能并安装了 WSL 2。如果尚未设置，请参阅[官方文档 ↗](https://docs.microsoft.com/en-us/windows/wsl/install)以获取有关如何安装和设置 WSL 的详细信息。

2. 打开 PowerShell 或命令提示符（以管理员身份运行）。可以通过在开始菜单中搜索 "PowerShell" 或 "cmd"，然后右键点击结果并选择 "以管理员身份运行" 来实现。

3. 创建一个新目录 `D:\wsl` 作为 WSL 分发的安装位置：

   ```powershell
   mkdir D:\wsl
   ```

4. 现在，您需要从 Microsoft Store 下载 WSL 分发的 tarball 文件。以 Ubuntu 20.04 为例，从以下链接下载 tarball 文件：

   
   [https://aka.ms/wslubuntu2004 ↗](https://aka.ms/wslubuntu2004)
   

   请注意，如果您希望安装其他 WSL 分发，可能需要使用其他 tarball 下载链接。从上述链接下载 Ubuntu 20.04 tarball 文件并将其保存到 `D:\wsl` 文件夹中（例如，`D:\wsl\ubuntu-20.04.tar.gz`）。

5. 使用 `wsl.exe` 命令导入下载的 tarball 文件并将其安装到 `D:\wsl` 目录：

   ```powershell
   wsl.exe --import Ubuntu-20.04 D:\wsl\Ubuntu-20.04 D:\wsl\ubuntu-20.04.tar.gz
   ```
   
   请注意，您需要根据实际情况替换 `Ubuntu-20.04`（分发名称）和 `D:\wsl\ubuntu-20.04.tar.gz`（tarball 文件路径）。

完成这些步骤后，WSL 分发将安装在 `D:\wsl` 目录下。要启动新安装的分发，请在 PowerShell 或命令提示符中运行：

```powershell
wsl.exe -d Ubuntu-20.04
```

请根据实际情况替换 `Ubuntu-20.04` 为您安装的分发名称。现在，您可以在 `D:\wsl` 目录中使用新的 WSL 分发。

