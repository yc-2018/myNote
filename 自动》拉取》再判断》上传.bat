@echo off
:: ���ڿ��ƻ�����������չ��Ϊ
setlocal enabledelayedexpansion  


:: �ı䵱ǰ�Ĺ���Ŀ¼     :: /dѡ���������ڸı乤��Ŀ¼ʱ�������������л���
cd /d E:\Users\Dell\Desktop\�ʼ�


:: ��ȡ���µı��
git pull
:: %ERRORLEVEL%��һ����������������洢���һ��ִ�е�������˳�״̬�����ȼ���ͨ������£��������ɹ�ִ�У�%ERRORLEVEL%���ᱻ����Ϊ0�����������ᱻ����Ϊ����ֵ��
IF %ERRORLEVEL% NEQ 0 (
    echo "Git pullʧ��"
    exit /b %ERRORLEVEL%
)

:: ����ļ�
git add *
:: ����Ƿ����ļ������
git status | findstr /C:"Changes to be committed"
IF %ERRORLEVEL% EQU 0 (
    :: ������ļ�����ӣ��ύ���
    git commit -m "�Զ�����"
    :: ���commit�Ƿ�ɹ�
    git log -1 | findstr /C:"�Զ�����"
    IF %ERRORLEVEL% EQU 0 (
        :: ���commit�ɹ������ͱ��
        git push
        IF %ERRORLEVEL% NEQ 0 (
            echo "Git pushʧ��"
            timeout /t 5
            exit /b %ERRORLEVEL%
        )
    ) ELSE (
        echo "Git commitʧ��"
        timeout /t 5
        exit /b %ERRORLEVEL%
    )
) ELSE (
    echo "û���ļ�����ӣ�ʧ�ܵ�man"
    timeout /t 5
    exit /b %ERRORLEVEL%
)