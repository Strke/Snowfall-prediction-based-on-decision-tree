from CART import Cart
from data_read import data_load_clean, load_data, split_tt
from vail_and_test import vail_model, test_model
from config import choose_feature

if __name__ == "__main__":
    # 只保留k个特征
    k = choose_feature
    data, pos, neg = data_load_clean(k)
    # 有数据了就加载数据，节省时间
    # data = load_data()
    # 划分测试集和训练集
    train_set, vail_set, test_set = split_tt(data, pos, neg)
    cart = Cart(train_set)
    #cart.train_model()
    #print(cart.model)
    #cart.save_model(cart.model)
    Btree = cart.load_model()
    #print(Btree)
    vail_model(Btree, vail_set)
    vail_model(Btree, test_set)
    # test_model(test_set, Btree)
    # 需要输入的特征为平均气压，日最低气压，平均气温，日最低气温，平均相对湿度，
    # 最大风速，日照时数，平均地表气温，日最低地表气温
    
