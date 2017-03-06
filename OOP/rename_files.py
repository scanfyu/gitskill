import os

def rename_files():
    # 1.从文件夹中获得文件名
    file_list = os.listdir(r"F:\OOP\prank")
    print(file_list)

    save_path = os.getcwd() #测试目前工作目录
    print("Current Working Directory is "+save_path)
    os.chdir(r"F:\OOP\prank")

    # 2.更改每个文件名
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0 1 2 3 4 5 6 7 8 9"))
        os.rename(file_name, file_name.translate(None, "0 1 2 3 4 5 6 7 8 9"))
    os.chdir(save_path)

rename_files()