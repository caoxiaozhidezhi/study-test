# _*_ coding:utf-8 _*_

"""
1、房子（House）有户型、总面积和家具名称列表,新房子没有任何家具
2、家具（HouseItem）有名字和占地面积，其中,
    席梦思（bed）占地4平米,
    衣柜（chest）占地2平米,
    餐桌（table）占地1.5平米
3、将以上三件家具添加到房子中
4、打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
"""


class HouseItem(object):
    """家具信息"""

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "【%s】占地%.2f" % (self.name, self.area)


# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed, chest, table)
print("")


class House(object):
    """docstring for House"""

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f【剩余：%.2f】\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        # 添加家具
        """
        需求说明：
        1、判断家具的面积是否超过剩余面积，如果超过，提示不能添加这件家具；
        2、将家具的名称追加到家具名称列表中
        3、用房子的 剩余面积 - 家具面积
        """
        print("要添加%s" % item)
        if item.area > self.free_area:
            print("%s的面积太大了，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


# 创建房子对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
