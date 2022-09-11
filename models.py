from extensions import db

class Goods(db.Model):
    __tablename__ = 'goods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    good_name = db.Column(db.String(255), nullable=False)
    good_price = db.Column(db.Float, nullable=False)
    good_num = db.Column(db.Integer, nullable=False)
    good_category = db.Column(db.String(255), nullable=False)
    good_image = db.Column(db.String(255))
    good_sell = db.Column(db.String(255), nullable=False)
    good_desc = db.Column(db.String(255), nullable=False)

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
