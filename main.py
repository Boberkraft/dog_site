
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
        #  ktoś przysłał formularz. Pewnie to są zamówienia
        add_to_base(request.form)  # zapisz w pliku

    orders = get_orders()  # odczytaj zamówienia z pliku

    return render_template('orders.html', orders=orders)  # zrenderuj stronkę


def add_to_base(form):
    """Dodaje zamówienie do pliku"""
    # pobiera z requestu niezbędne rzeczy.
    # Jeżeli jakiegoś nie będzie to trudno
    name = form['name']
    email = form['email']
    phone = form['phone']
    order = form['order']

    # otwórz plik orders w trybie append 'a' czyli dodawaj na końcu pliku
    with open('orders', 'a', encoding='utf-8') as ff:
        # wygeneruj wiersz do zapisania
        temp = '{}|X|{}|X|{}|X|{}'.format(name, email, phone, order)
        ff.write(temp + '\n')  # dopisz do końca pliku

def get_orders():
    """Wczytuje zamówienia z pliku"""
    # otwórz plik o nazwie orders
    with open('orders', encoding='utf-8') as ff:
        orders = []
        for line in ff:
            # dla każdej linii w pliku
            line = line.split('|X|')  # rozerwij wiersz w  miejscach '|X|'
            orders.append(dict(name=line[0], order=line[3]))  # zachowaj tylko 1 i 4 część wiersza
    return orders  # zwróc zamówienia

if __name__ == '__main__':
    app.run()
