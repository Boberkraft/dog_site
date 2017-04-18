
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='files', static_url_path='')

@app.route('/')
def main_site():
    return render_template('index.html')

@app.route('/zamow')
def order():
    return render_template('order.html')


@app.route('/zamowienia', methods=['POST', 'GET'])
def orders():
    if request.form:
        add_to_base(request.form)

    with open('orders', encoding='utf-8') as ff:
        orders = []
        for line in ff:
            line = line.split('|X|')
            orders.append(dict(name=line[0], order=line[3]))

    return render_template('orders.html', orders=orders)


def add_to_base(form):
    name = form['name']
    email = form['email']
    phone = form['phone']
    order = form['order']

    with open('orders', 'a', encoding='utf-8') as ff:
        ff.write('{}|X|{}|X|{}|X|{}\n'.format(name, email, phone, order))

if __name__ == '__main__':
    app.run(host='192.168.1.17')
