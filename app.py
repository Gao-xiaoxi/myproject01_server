from flask import Flask, jsonify, request
from flask.views import MethodView
from extensions import db, cors
from goods.views import goods_blue
from category.views import category_blue
from models import Goods

app = Flask(__name__)

app.config.from_object('conf.Config')

db.init_app(app)
cors.init_app(app)
app.config["JSON_AS_ASCII"] = False

app.config["SQLALCHEMY_ECHO"] = True

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Goods.init_db()


@app.route('/')
def hello_world():
    return 'Hello World!'

# class GoodsApi(MethodView):
#     def get(self, good_id=''):
#         if not good_id:
#             goods: [Goods] = Goods.query.all()
#             print(Goods.query.all())
#             print(type(Goods.query.all()))
#             print(Goods.query.all()[0])
#             print(type(Goods.query.all()[0]))
#             results = [
#                 {
#                     'id': goods.id,
#                     'good_name': goods.good_name,
#                     'good_price': goods.good_price,
#                     'good_num': goods.good_num,
#                     'good_category': goods.good_category,
#                     'good_image': goods.good_image,
#                     'good_sell': goods.good_sell,
#                     'good_desc': goods.good_desc,
#                 } for goods in goods
#             ]
#             return {
#                 'status': 'success',
#                 'message': '数据查询成功',
#                 'results': results
#             }
#
# goods_view = GoodsApi.as_view('goods_api')
# app.add_url_rule('/goods/', view_func=goods_view, methods=['GET', ])

# goods: [Goods] = Goods.query.all()
# print(Goods.query.all())
# print(type(Goods.query.all()))
# print(Goods.query.all()[0])
# print(type(Goods.query.all()[0]))
# results = [
#     {
#         'id': goods.id,
#         'good_name': goods.good_name,
#         'good_price': goods.good_price,
#         'good_num': goods.good_num,
#         'good_category': goods.good_category,
#         'good_image': goods.good_image,
#         'good_sell': goods.good_sell,
#         'good_desc': goods.good_desc,
#     } for goods in goods
# ]

# @app.route("/goods/", methods=["GET"])
# def get_all_goods(): # 全查询：可以理解为没有任何参数，不需要接收前端的数据，业务逻辑可以理解为，直接执行数据库的全查询
#     goods = Goods.query.all() # 返回是列表
#     print(Goods.query.all())
#     results = []
#     for good in goods:
#         results.append(
#             {
#                 'id': good.id,
#                 'good_name': good.good_name,
#                 'good_price': good.good_price,
#                 'good_num': good.good_num,
#                 'good_category': good.good_category,
#                 'good_image': good.good_image,
#                 'good_sell': good.good_sell,
#                 'good_desc': good.good_desc,
#             }
#         )
#
#     return jsonify({"code": "0", "results": results, "msg": "操作成功"})

# @app.route("/goods/<int:id_>", methods=["GET"])
# def get_one_goods(id_): # 按条件查询查询：可以理解有参数，需要接收前端的数据，业务逻辑可以理解为，接收前端的数据，传给数据库，再执行执行数据库的查询
#     goods: [Goods] = Goods.query.filter_by(id=id_)
#     results = [
#         {
#             'id': goods.id,
#             'good_name': goods.good_name,
#             'good_price': goods.good_price,
#             'good_num': goods.good_num,
#             'good_category': goods.good_category,
#             'good_image': goods.good_image,
#             'good_sell': goods.good_sell,
#             'good_desc': goods.good_desc,
#         } for goods in goods
#     ]
#     print(type(results))
#     if int(id_) > 0 and len(results)>0:
#         return jsonify({"code": "0","results": results, "msg": "操作成功"})
#     else:
#         return jsonify({"code": "1", "results": [], "msg": "暂无数据"})

# @app.route("/goods/query", methods=["POST"])
# def query_goods():
#     print('------request----------')
#     print(request)
#     print('------request.json----------')
#     print(request.json)
#     id_ = request.json.get('id')
#     name = request.json.get('name')
#     print(id_)
#     print(name)
#     # id_ 从前端接收
#     goods: [Goods] = Goods.query.filter_by(id=id_, good_name=name)
#     print('------goods----------')
#     print(goods)
#     results = [
#         {
#             'id': goods.id,
#             'good_name': goods.good_name,
#             'good_price': goods.good_price,
#             'good_num': goods.good_num,
#             'good_category': goods.good_category,
#             'good_image': goods.good_image,
#             'good_sell': goods.good_sell,
#             'good_desc': goods.good_desc,
#         } for goods in goods
#     ]
#     print(type(results))
#     if int(id_) > 0 and len(results)>0:
#         return jsonify({"code": "0","results": results, "msg": "操作成功"})
#     else:
#         return jsonify({"code": "1", "results": [], "msg": "暂无数据"})

# 注册蓝图
app.register_blueprint(goods_blue, url_prefix='/goods')
app.register_blueprint(category_blue, url_prefix='/category')

if __name__ == '__main__':
    app.run()
