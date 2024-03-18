from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('main.html', **context)

@app.route('/clothes/')
def clothes():
    title = {'title': 'Категории одежды'}
    _clothes = [
    {"name": "Рубашка", "price": 2000, "descr": "Классическая белая рубашка"},
    {"name": "Кофта", "price": 3400, "descr": "Серая кофта с длинным рукавом"},
    {"name": "Джинсы", "price": 3700, "descr": "Синие зауженные джинсы"}
]
    return render_template('product.html', **title, products = _clothes)

@app.route('/shoes/')
def shoes():
    title = {'title': 'Категории обуви'}
    _shoes = [{"name": "Туфли", "price": 3500, "descr": "Классические черные туфли"},
              {"name": "Сандали", "price": 2500, "descr": "Бежевые открытые сандали"},
              {"name": "Кроссовки", "price": 4500, "descr": "Спортивные с эластичной подошвой кроссовки"}
]
    return render_template('product.html', **title, products = _shoes)

@app.route('/jackets/')
def jackets():
    title = {'title': 'Категории верхней одежды'}
    _jackets = [{"name": "Пуховик", "price": 10000, "descr": "Теплая зимний пуховик"},
              {"name": "Пальто", "price": 13000, "descr": "Демисезонное пальто"},
              {"name": "Ветровка", "price": 6000, "descr": "Спортивная легкая ветровка"}
]
    return render_template('product.html', **title, products = _jackets)

if __name__ == '__main__':
    app.run(debug=True)