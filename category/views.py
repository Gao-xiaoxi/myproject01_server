from flask import Blueprint, jsonify, request

from extensions import db
from models import Category
#定义蓝图
category_blue = Blueprint('category', __name__)

# 视图函数
@category_blue.route('/', methods=["GET"])
def get_all_category():
    """ 获取所有的类目 """
    # 全查询：可以理解为没有任何参数，不需要接收前端的数据，业务逻辑可以理解为，直接执行数据库的全查询
    category = Category.query.all()  # 返回是列表
    results = []
    for c in category:
        results.append(
            {
                'c_id': c.c_id,
                'name': c.c_name,
                'parent_id': c.parent_id,
                'is_parent': c.is_parent
            }
        )
    return jsonify({"code": "0", "results": results,  "msg": "操作成功"})

@category_blue.route('/parent', methods=["GET"])
def get_parent_category(is_parent=1):
    """ 查出所有的父类节点 """
    category = Category.query.filter_by(is_parent=is_parent)
    results = []
    for c in category:
        results.append(
            {
                'c_id': c.c_id,
                'name': c.c_name,
                'parent_id': c.parent_id,
                'is_parent': c.is_parent
            }
        )
    if len(results) > 0:
        return jsonify({"code": "0","results": results, "msg": "操作成功"})
    else:
        return jsonify({"code": "1", "results": [], "msg": "暂无数据"})

@category_blue.route('/child', methods=["POST"])
def get_child_category():
    """ 根据父类查出对应父类所有的子类节点 """
    name = request.json.get('name')  # 从前端获取父类名称(.http文件相当于模拟的前端数据)
    c_id = Category.query.filter_by(c_name=name)[0].c_id
    print('-------------')
    print(c_id)
    category = Category.query.filter_by(parent_id=c_id)
    results = []
    for c in category:
        results.append(
            {
                'c_id': c.c_id,
                'name': c.c_name,
                'parent_id': c.parent_id,
                'is_parent': c.is_parent
            }
        )
    if len(results) > 0:
        return jsonify({"code": "0","results": results, "msg": "操作成功"})
    else:
        return jsonify({"code": "1", "results": [], "msg": "暂无数据"})