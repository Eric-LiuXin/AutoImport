import os


class FileManager:
    # 获取当前路径下所有子文件夹
    @staticmethod
    def sub_dir(path):
        return [file for file in os.listdir(path) if os.path.isdir('\\'.join([path,file]))]

    # 获取当前路径下的非目录子文件
    @staticmethod
    def no_subdir_files(path):
        return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    # 获取当前路径下的非目录子文件,包含子目录下文件
    @staticmethod
    def inc_subdir_files(path):
        return [[os.path.join(root, file) for file in files] for root, dirs, files in os.walk(path)]

    # 获取当前路径下的所有指定文件类型的非目录子文件
    @staticmethod
    def no_subdir_type_files(path, type):
        all_file = list()
        for file in FileManager.no_subdir_files(path):
            arr = os.path.splitext(os.path.join(file))
            if arr[1] == type : all_file.append(arr[0])

        return all_file

    # 获取当前路径下的所有指定文件类型的非目录子文件,包含子目录下文件
    @staticmethod
    def inc_subdir_type_files(path, type):
        all_file = list()
        for files in FileManager.inc_subdir_files(path):
            for file in files:
                dir_name, file_name = os.path.split(file)
                arr = os.path.splitext(os.path.join(file_name))
                if arr[1] == type: all_file.append(arr[0])
        return all_file
