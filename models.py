from extensions import db
from util import constants


class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    good_name = db.Column(db.String(255), nullable=False)
    good_price = db.Column(db.Float, nullable=False)
    good_num = db.Column(db.Integer, nullable=False)
    good_category = db.Column(db.String(255))
    good_image = db.Column(db.String(255))
    good_sell = db.Column(db.String(255))
    good_desc = db.Column(db.String(255))

    @staticmethod
    def init_db():
        rets = [
            (1, '商品名称1', 1.1, 1, '商品类目1', '', '商品卖点1', '商品描述1'),
            (2, '商品名称1', 2.1, 2, '商品类目2', '', '商品卖点2', '商品描述2')
        ]
        for ret in rets:
            goods = Goods()
            goods.id = ret[0]
            goods.good_name = ret[1]
            goods.good_price = ret[2]
            goods.good_num = ret[3]
            goods.good_category = ret[4]
            goods.good_image = ret[5]
            goods.good_sell = ret[6]
            goods.good_desc = ret[7]
            db.session.add(goods)
        db.session.commit()

class Category(db.Model):
    __tablename__ = 'category'
    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(255), nullable=False)
    parent_id = db.Column(db.Integer)
    is_parent = db.Column(db.SmallInteger, default=constants.CategoryIsParent.C_IS_PARENT.value)

    @staticmethod
    def init_db():
        rets = [
            (10, '文具类', 0, 1),
            (11, '本子', 10, 0)
        ]
        for ret in rets:
            category = Category()
            category.c_id = ret[0]
            category.c_name = ret[1]
            category.c_parent_id = ret[2]
            category.c_is_parent = ret[3]
            db.session.add(category)
        db.session.commit()
