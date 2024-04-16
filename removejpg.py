def remove_extension(file_name):
    if file_name.endswith('.jpg'):
        return file_name[:-4]  # 去掉后缀'.jpg'
    else:
        return file_name

# if __name__ == "__main__":
#     file_name = "example.jpg"
#     file_name_without_extension = remove_extension(file_name)
#     print("File name without extension:", file_name_without_extension)
