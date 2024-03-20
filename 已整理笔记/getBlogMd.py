import os

# 定义一个函数来处理文件夹和文件名中不允许的字符
def sanitize_name(name):
    for ch in ['\\', '/', ':', '*', '?', '"', '<', '>', '|', '+', '%', '!', '@']:
        name = name.replace(ch, ' ')
    return name.replace('==', ' ').strip()

# 定义读取和解析Markdown文件的函数
def parse_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    sections = {}
    current_section = None
    current_file = None
    content_accumulator = []
    for line in lines:
        if line.startswith('# '):  # 标题1，用作文件夹名
            if current_section is not None and current_file is not None:
                sections[current_section][current_file] = '\n'.join(content_accumulator)
            current_section = sanitize_name(line.strip().lstrip('# '))
            sections[current_section] = {}
            current_file = None
            content_accumulator = []
        elif line.startswith('## '):  # 标题2，用作md文件名和内容的开始
            if current_section is not None and current_file is not None:
                sections[current_section][current_file] = '\n'.join(content_accumulator)
            current_file = sanitize_name(line.strip().lstrip('## ')) + '.md'
            content_accumulator = [line.strip()]
        elif current_file is not None:
            content_accumulator.append(line.rstrip())
    
    # 保存最后一部分的内容
    if current_section is not None and current_file is not None:
        sections[current_section][current_file] = '\n'.join(content_accumulator)
    
    return sections

# 创建文件夹和文件的函数
def create_folders_and_files(sections, base_path='博客md'):
    base_path = sanitize_name(base_path)
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    for section, files in sections.items():
        section_path = os.path.join(base_path, section)
        if not os.path.exists(section_path):
            os.makedirs(section_path)
        for file_name, content in files.items():
            file_path = os.path.join(section_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

# 主逻辑
def main():
    md_file = '问chat笔记.md'
    sections = parse_markdown_file(md_file)
    create_folders_and_files(sections)

if __name__ == '__main__':
    main()
