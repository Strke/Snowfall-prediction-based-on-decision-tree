# 基于决策树的下雪预测

注：本项目算法部分仅使用numpy，pandas，random，pickle库，为了对决策树加深理解所以并未使用其他机器学习库。

##  1.文件结构

本项目由三个部分组成，分别是数据部分，决策树训练部分，界面设计部分，其组成如下

└─决策树训练

 CART.py   //CART算法实现及模型训练

 config.py   //参数设置

 data_read.py   //数据预处理以及数据集划分

 main.py  //主执行函数

 vail_and_test.py   //验证和预测

 

└─数据及模型

 BTree.pickle   //决策树模型

 data.csv

 rate.csv

 test_data.csv  //测试数据集

 test_kunming.csv  //原始数据集

 

└─界面设计

 Ui_design.py   //各控件实现

 WidgetMain.py   //主界面



## 2.数据处理

### 2.1 数据预处理



