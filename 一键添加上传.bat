@echo off
REM ����һ���򵥵�������ű������ڽ��û�������ύ��Ϣ��Ϊ Git �ύ��Ϣ---�¹��������ں�����

git add *


:: ��ʾ�û������ύ��Ϣ
echo �������ύ��Ϣ:
set /p commit_message=


git commit -m "%commit_message%"
git push

echo =========================ikun:������ɻس�����============================
set /p ikun=