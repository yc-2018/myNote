@echo off
REM 这是一个简单的批处理脚本，用于将用户输入的提交信息作为 Git 提交信息---陈光龙：公众号仰晨

git add *


:: 提示用户输入提交信息
echo 请输入提交信息:
set /p commit_message=


git commit -m "%commit_message%"
git push

echo =========================ikun:运行完成回车结束============================
set /p ikun=