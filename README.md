# 基于决策树的下雪预测

注：本项目算法部分仅使用numpy，pandas，random，pickle库，为了对决策树加深理解所以并未使用其他机器学习库。

##  1.文件结构

本项目由三个部分组成，分别是数据部分，决策树训练部分，界面设计部分，其组成如下

└─决策树训练

&emsp; &emsp; CART.py   //CART算法实现及模型训练

 &emsp;&emsp;config.py   //参数设置

 &emsp;&emsp;data_read.py   //数据预处理以及数据集划分

&emsp;&emsp; main.py  //主执行函数

 &emsp;&emsp;vail_and_test.py   //验证和预测

 

└─数据及模型

 &emsp;&emsp;BTree.pickle   //决策树模型

&emsp;&emsp; data.csv

&emsp;&emsp; rate.csv

 &emsp;&emsp;test_data.csv  //测试数据集

 &emsp;&emsp;test_kunming.csv  //原始数据集

 

└─界面设计

 &emsp;&emsp;Ui_design.py   //各控件实现

&emsp;&emsp; WidgetMain.py   //主界面



## 2.数据处理

### 2.1 数据预处理



