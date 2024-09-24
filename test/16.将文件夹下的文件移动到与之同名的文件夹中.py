#######################################################################
# 将文件夹下的文件移动到与之同名的文件夹中
# 现在将 "要移动的文件夹" 中所有的子文件夹中的文件，对应复制或者移动到 “目标文件夹(同名的)” 中的子文件夹。
#
######################################################################
import os
import shutil


is_move_or_copy = 0  #1  # 1代表移动 ，0代表复制

# 指定目标和源文件夹的路径
# 现在将源文件夹中所有的子文件夹中的文件，对应复制在目标文件夹中的子文件夹。
# 如果目标文件夹中没有“原文件夹”中的目录，那么会在目标文件夹中新增一个类，并打印出来。

# 源文件夹  要移动的文件夹
folder_src = r"E:\00.Data\03_canhe_datasets\19_Canhe_padding_9_23"

# 移动到哪里  “目标文件夹”  移动目的地
folder_dist = r"E:\00.Data\03_canhe_datasets\19_1_Canhe_kuochong_9_23"




# 如果说源文件夹下的某个文件夹的名字   在    目标文件夹下不存在与之同名的文件夹，那么就将这个文件移动到这个路径下并保存
#add_folder = r""



# 获取"要移动的文件夹"文件夹下所有的子文件夹 #subfolders_src是个列表，保存folder_src路径下所有子文件夹的全路径
subfolders_src = [f.path for f in os.scandir(folder_src) if f.is_dir()]
print(subfolders_src)
count_add_folder = 0
# 遍历源文件夹下的所有子文件夹
for subfolder_src in subfolders_src:
    # 获取子文件夹的名字
    subfolder_name = os.path.basename(subfolder_src)

    # 构造目标文件夹下对应的子文件夹路径
    subfolder_dist = os.path.join(folder_dist, subfolder_name)

    if os.path.exists(subfolder_dist) :
        #print("没有新增类别")
        pass
    else :
        # 确保目标文件夹下的子文件夹存在
        os.makedirs(subfolder_dist, exist_ok=True)
        count_add_folder += 1
        print(f" 新增类别 {count_add_folder:<4} folder: {subfolder_name}")


    # 遍历源文件夹下当前子文件夹的所有文件
    for filename in os.listdir(subfolder_src):
        # 构造完整的文件路径
        file_path_src = os.path.join(subfolder_src, filename)
        file_path_dist = os.path.join(subfolder_dist, filename)

        if is_move_or_copy: # 移动
            shutil.move(file_path_src, file_path_dist)
        else:# 复制文件
            shutil.copy2(file_path_src, file_path_dist)

print()
print(f"total {len(subfolders_src)} folder ")
print("-----> done！<-----")