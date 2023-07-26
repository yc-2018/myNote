@echo off
:: 用于控制环境变量的扩展行为
setlocal enabledelayedexpansion  


:: 改变当前的工作目录     :: /d选项允许你在改变工作目录时跨驱动器进行切换。
cd /d E:\Users\Dell\Desktop\笔记


:: 拉取最新的变更
git pull
:: %ERRORLEVEL%是一个环境变量，它会存储最后一次执行的命令的退出状态或错误等级。通常情况下，如果命令成功执行，%ERRORLEVEL%将会被设置为0，否则它将会被设置为非零值。
IF %ERRORLEVEL% NEQ 0 (
    echo "Git pull失败"
    exit /b %ERRORLEVEL%
)

:: 添加文件
git add *
:: 检查是否有文件被添加
git status | findstr /C:"Changes to be committed"
IF %ERRORLEVEL% EQU 0 (
    :: 如果有文件被添加，提交变更
    git commit -m "自动备份"
    :: 检查commit是否成功
    git log -1 | findstr /C:"自动备份"
    IF %ERRORLEVEL% EQU 0 (
        :: 如果commit成功，推送变更
        git push
        IF %ERRORLEVEL% NEQ 0 (
            echo "Git push失败"
            timeout /t 5
            exit /b %ERRORLEVEL%
        )
    ) ELSE (
        echo "Git commit失败"
        timeout /t 5
        exit /b %ERRORLEVEL%
    )
) ELSE (
    echo "没有文件被添加，失败的man"
    timeout /t 5
    exit /b %ERRORLEVEL%
)