import os


def count_images_in_subfolders(source_folder):
    # 支持的图片格式
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    # 初始化一个字典来存储结果
    results = {}

    # 遍历source_folder下的所有子文件夹
    for subdir, dirs, files in os.walk(source_folder):
        # 获取当前文件夹的名称
        folder_name = os.path.basename(subdir)
        if folder_name == 'source':
            continue  # 如果是source文件夹本身，则跳过

        # 计算当前文件夹中的图片数量
        image_count = sum(1 for f in files if os.path.splitext(f)[1].lower() in image_extensions)
        results[folder_name] = image_count

        # 打印结果表格
    print("Folder Name\tImage Count")
    for folder, count in results.items():
        #print(f"{folder}\t\t{count}")
        print(f"{folder:<35}\t\t{count:<5}")
        # if count< 3000:
        #     print(f"{folder:<35} 数量 {count:<5}")



    # 调用函数


source_folder = r'E:\00.Data\03_canhe_datasets\19_1_Canhe_kuochong_9_23'  # 指定source文件夹的路径
count_images_in_subfolders(source_folder)