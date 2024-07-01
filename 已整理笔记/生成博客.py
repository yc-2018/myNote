import os
import shutil  		# 删除非空文件夹


# 先尝试删除“博客md”文件夹 
try:
	shutil.rmtree('./博客md')
except FileNotFoundError:
	print("博客md 不存在  不用删除了")

# 执行py
os.system('python getBlogMd.py')
os.system('python getMdList.py')

print("=====完成重新生成博客=====")