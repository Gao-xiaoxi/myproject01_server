from flask import Blueprint, jsonify, request

from models import Goods
#定义蓝图
goods_blue = Blueprint('goods', __name__)

# 视图函数
@goods_blue.route('/', methods=["GET"])
def get_all_goods():
    """ 获取所有的商品 """
    # 全查询：可以理解为没有任何参数，不需要接收前端的数据，业务逻辑可以理解为，直接执行数据库的全查询
    goods = Goods.query.all()  # 返回是列表
    results = []
    for good in goods:
        results.append(
            {
                'id': good.id,
                'good_name': good.good_name,
                'good_price': good.good_price,
                'good_num': good.good_num,
                'good_category': good.good_category,
                'good_image': good.good_image,
                'good_sell': good.good_sell,
                'good_desc': good.good_desc,
            }
        )
    return jsonify({"code": "0", "results": results, "msg": "操作成功"})

@goods_blue.route('/query', methods=["POST"])
def query_goods():
    """ 根据条件查询商品 """
    id_ = request.json.get('id') #从前端获取
    good_name = request.json.get('good_name') #从前端获取
    if id_ and good_name:
        goods = Goods.query.filter_by(id=id_, good_name=good_name)
    elif id_ and not(good_name):
        goods = Goods.query.filter_by(id=id_)
    elif not(id_) and good_name:
        goods = Goods.query.filter_by(good_name=good_name)
    else:
        goods = Goods.query.all()  # 返回是列表
    results = []
    for good in goods:
        results.append(
            {
                'id': good.id,
                'good_name': good.good_name,
                'good_price': good.good_price,
                'good_num': good.good_num,
                'good_category': good.good_category,
                'good_image': good.good_image,
                'good_sell': good.good_sell,
                'good_desc': good.good_desc,
            }
        )
    if len(results) > 0:
        return jsonify({"code": "0","results": results, "msg": "操作成功"})
    else:
        return jsonify({"code": "1", "results": [], "msg": "暂无数据"})