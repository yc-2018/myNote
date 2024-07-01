import os
import shutil  		# 删除非空文件夹
import subprocess	# 执行其他py


# 先尝试删除“博客md”文件夹 
try:
	shutil.rmtree('./博客md')
except FileNotFoundError:
	print("博客md 不存在  不用删除了")
		

# 执行 getBlogMd.py
subprocess.run(["python", "getBlogMd.py"], check=True)

# 执行 getMdList.py
subprocess.run(["python","getMdList.py"], check=True)

print("=====完成重新生成博客=====")