import os
import shutil  		# 删除非空文件夹


# 先尝试删除“博客md”文件夹 
try:
	shutil.rmtree('./博客md')
except FileNotFoundError:
	print("博客md 不存在  不用删除了")

# 兼容不同执行方式, 双击肯定是不用的,但是在GitHub Actions上在主目录执行,相对位置就错了
try:
    print(f'当前所在文件夹:{os.getcwd()}')
    os.chdir('./已整理笔记')
except:
    pass


# 执行py
os.system('python getBlogMd.py')
os.system('python getMdList.py')

print("=====完成重新生成博客=====")