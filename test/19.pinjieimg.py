import sys
import os
import numpy as np
import cv2

# pt_src = r"E:\00.Data\03.jdw\32\07_15_result\save_result_exp_128_default_\all"
trt_src_1=r"E:\00.Data\03.jdw\32\32"
trt_src_2=r"E:\00.Data\03.jdw\32\07_15_result\master_32\all"
# trt_src_3=r"E:\00.Data\03.jdw\32\07_15_result\save_result_exp_1024_haveNEG_best\all"
# trt_src_4=r"E:\00.Data\03.jdw\32\07_15_result\save_result_exp_1024_noneNEG_3_best\all"

save_path=r"E:\00.Data\03.jdw\32\07_15_result\master_32\all_duibi"

img_names=os.listdir(trt_src_1)
for img in img_names:
    try :
        # pt_img_path = os.path.join(pt_src,img)
        trt_src_1_path = os.path.join(trt_src_1,img)
        trt_src_2_path = os.path.join(trt_src_2, img)
        # trt_src_3_path = os.path.join(trt_src_3,img)
        # trt_src_4_path = os.path.join(trt_src_4, img)

        # pt_img =cv2.imread(pt_img_path)
        trt_img_1 = cv2.imread(trt_src_1_path)
        trt_img_2 = cv2.imread(trt_src_2_path)
        # trt_img_3 = cv2.imread(trt_src_3_path)
        # trt_img_4 = cv2.imread(trt_src_4_path)

        # final_img = np.concatenate((pt_img,trt_img_1,trt_img_2,trt_img_3,trt_img_4),axis=1)
        final_img = np.concatenate((trt_img_1, trt_img_2), axis=1)
        cv2.imshow("final_img",final_img)

        #cv2.imwrite(os.path.join(save_path,img),final_img)
        cv2.waitKey(1)
    except  Exception as error:
        print("error--->",error)
        continue