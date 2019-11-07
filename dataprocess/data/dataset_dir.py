# 获取所有分割数据集的绝对路径
import os
import pandas as pd


seg_img_path="E:\ylhe\LUNA-16\segmentation\Image/"
seg_img = "./Segmentation3DImage.csv"
seg_mask_path="E:\ylhe\LUNA-16\segmentation\Mask/"
seg_mask = "./Segmentation3DMask.csv"

def get_all_path(rootdir, df_path):
    """
    获取文件夹下的所有文件路径
    rootdir：是当前目录
    return：返回当前目录下所有的文件绝对路径
    """
	df = pd.DataFrame()
    path_list = []
    all_path = os.listdir(rootdir)
    for i in range(0,len(all_path)):
        path = os.path.join(rootdir, all_path[i])
        path_list.append(path)
    path_list = get_all_path(rootdir)
	df["path_list"] = path_list
	df.to_csv(df_path, index = False)
	
get_all_path(seg_img_path, seg_img)
get_all_path(seg_mask_path, seg_mask)

