# lung_seg_vision0
> 肺部CT扫描图像可视化结果：

![plan](/数据可视化//3D.png)

## 肺结节检测
**1.预处理**

* 将注视文件转化为image mask文件： run  ./dataprocess/LUNA_mask_extraction.py
* 分析CT图像获取切片的厚度，宽度和位置： run  ./dataprocess/dataAnaly.py
* 生成3D训练和测试数据集：run ./dataprocess/data3dprepare.py
* 将肺结节数据和mask保存到csv文件 run ./dataprocess/utils.py
* 获取所有分割数据集的绝对路径 run ./dataprocess/data/dataset_dir.py
