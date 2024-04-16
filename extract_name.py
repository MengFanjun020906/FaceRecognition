import os

def extract_name(file_name):
    # 使用下划线分割文件名，并返回第一个部分

    return file_name.split('.')[0]

def main():
    folder_path = 'face_dataset'  # 替换为你的文件夹路径

    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    # 获取文件夹下所有文件
    files = os.listdir(folder_path)

    # 提取文件名中下划线前的部分并保存到数组
    extracted_names = [extract_name(file) for file in files]

    # 打印结果
    # for original_name, extracted_name in zip(files, extracted_names):
    #
    #  print(f"Original Name: {original_name}, Extracted Name: {extracted_name}")

    # 将提取的名字保存到数组
    global name_array
    name_array = extracted_names
    #print("Extracted Names Array:", name_array)

if __name__ == "__main__":
    main()

