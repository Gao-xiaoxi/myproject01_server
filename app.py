from flask import Flask
from flask.views import MethodView
from extensions import db, cors
from models import Goods

app = Flask(__name__)

app.config.from_object('conf.Config')

db.init_app(app)
cors.init_app(app)

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Goods.init_db()


@app.route('/')
def hello_world():
    return 'Hello World!'

class GoodsApi(MethodView):
    def get(self, good_id=''):
        if not good_id:
            goods: [Goods] = Goods.query.all()
            results = [
                {
                    'id': goods.id,
                    'good_name': goods.good_name,
                    'good_price': goods.good_price,
                    'good_num': goods.good_num,
                    'good_category': goods.good_category,
                    'good_image': goods.good_image,
                    'good_sell': goods.good_sell,
                    'good_desc': goods.good_desc,
                } for goods in goods
            ]
            return {
                'status': 'success',
                'message': '数据查询成功',
                'results': results
            }

goods_view = GoodsApi.as_view('goods_api')
app.add_url_rule('/goods/', view_func=goods_view, methods=['GET', ])

if __name__ == '__main__':
    app.run()
