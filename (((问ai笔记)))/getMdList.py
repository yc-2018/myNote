import os
import json

def scan_md_folder(path):
    """
    扫描指定路径下的第一层文件夹和对应的 .md 文件
    
    :param path: 要扫描的路径
    :return: 包含文件夹和 .md 文件列表的嵌套列表
    """
    result = []

    # 获取第一层文件夹，排除以点开头的文件夹
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f)) and not f.startswith('.')]

    for folder in folders:
        folder_path = os.path.join(path, folder)
        
        # 获取文件夹下的 .md 文件列表，排除以点开头的文件
        md_files = [f for f in os.listdir(folder_path) if f.endswith('.md') and not f.startswith('.')]
        
        # 将文件夹名和对应的 .md 文件列表作为一个子列表添加到结果列表中
        result.append([folder] + md_files)

    return result

def save_to_json(data, output_file):
    """
    将数据保存为 JSON 文件
    
    :param data: 要保存的数据
    :param output_file: 输出的 JSON 文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # 将数据写入文件，设置 ensure_ascii=False 以支持非 ASCII 字符，indent=2 以美化 JSON 格式
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    # 设置要扫描的 md 文件夹路径
    md_folder_path = './博客md'  # 替换为你的 md 文件夹路径
    
    # 设置输出的 JSON 文件名
    output_file = './博客md/mdList.json'

    # 扫描 md 文件夹，获取文件夹和 .md 文件列表
    md_list = scan_md_folder(md_folder_path)
    
    # 将结果保存到 JSON 文件中
    save_to_json(md_list, output_file)

    print(f'扫描完成，结果已保存到 {output_file} 文件中。')
