from flask import *

app = Flask(__name__)

#Создание массива для хранения юзеров
users = []
#Создание массива для хранения музыки
musics = []
#Создание массива для хранение книг
books = []
#Создание массива для хранения машин
cars = []


#Создание класса, который будет хранить записи юзеров
class User(object):
    def __init__(self, name, surname, patronomyc, email, password):
        self.name = name
        self.surname = surname
        self.patronomyc = patronomyc
        self.email = email
        self.password = password

#Создание класса, который будет хранить записи музыки
class Music(object):
    def __init__(self, title, executor, genre, duration, rating):
        self.title = title
        self.executor = executor
        self.genre = genre
        self.duration = duration
        self.rating = rating

#Создание класса, который будет хранить записи книг
class Book(object):
    def __init__(self, title, author, genre, numofpages, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.numofpages = numofpages
        self.year = year

#Создание класса, который будет хранить записи машин
class Car(object):
    def __init__(self, name, brand, color, speed, year):
        self.name = name
        self.brand = brand
        self.color = color
        self.speed = speed
        self.year = year

@app.route('/', methods=['GET'])
def mainpage():
    return (
        "GET(users) - " + "<a href='http://localhost:3005/api/users'>" + "http://localhost:3005/api/users" + "</a>" + "<br>" +
        "POST(users) - " + "<a href='http://localhost:3005/api/users'>" + "http://localhost:3005/api/users" + "</a>" + "<br>" +
        "PUT(users) - " + "<a href='http://localhost:3005/api/users'>" + "http://localhost:3005/api/users" + "</a>" + "<br>" +
        "DELETE(users) - " + "<a href='http://localhost:3005/api/users'>" + "http://localhost:3005/api/users" + "</a>" + "<br>" +
        "GET(music) - " + "<a href='http://localhost:3005/api/musics'>" + "http://localhost:3005/api/musics" + "</a>" + "<br>" +
        "POST(music) - " + "<a href='http://localhost:3005/api/musics'>" + "http://localhost:3005/api/musics" + "</a>" + "<br>" +
        "PUT(music) - " + "<a href='http://localhost:3005/api/musics/0'>" + "http://localhost:3005/api/musics/0" + "</a>" + "<br>" +
        "DELETE(music) - " + "<a href='http://localhost:3005/api/musics/0'>" + "http://localhost:3005/api/musics/0" + "</a>" + "<br>" +
        "GET(books) - " + "<a href='http://localhost:3005/api/books'>" + "http://localhost:3005/api/books" + "</a>" + "<br>" +
        "POST(books) - " + "<a href='http://localhost:3005/api/books'>" + "http://localhost:3005/api/books" + "</a>" + "<br>" +
        "PUT(books) - " + "<a href='http://localhost:3005/api/books/0'>" + "http://localhost:3005/api/books/0" + "</a>" + "<br>" +
        "DELETE(books) - " + "<a href='http://localhost:3005/api/books/0'>" + "http://localhost:3005/api/books/0" + "</a>" + "<br>" +
        "GET(cars) - " + "<a href='http://localhost:3005/api/cars'>" + "http://localhost:3005/api/cars" + "</a>" + "<br>" +
        "POST(cars) - " + "<a href='http://localhost:3005/api/cars'>" + "http://localhost:3005/api/cars" + "</a>" + "<br>" +
        "PUT(cars) - " + "<a href='http://localhost:3005/api/cars/0'>" + "http://localhost:3005/api/cars/0" + "</a>" + "<br>" +
        "DELETE(cars) - " + "<a href='http://localhost:3005/api/cars/0'>" + "http://localhost:3005/api/cars/0" + "</a>" + "<br>"
    )

#Метод получения всех юзеров, пытался сделать для каждого отдельно дополнительно, но что-то пошло не так
@app.route('/api/users/', methods=['GET'])
def get_users():

    user = ''
    u = ''
    num = 0
    for i in users:
        num += 1
        user = "<b>" + "Имя: " + "</b>" + i.name + ", " + "<br>" + "<b>" + "Фамилия: " + "</b>" + i.surname + ", " + "<br>" + "<b>" + "Отчество: " + "</b>" + i.patronomyc + ", " + "<br>" + "<b>" + "Адрес электронной почты: " + "</b>" + i.email + ", " + "<br>" + "<b>" + "Пароль: " + "</b>" +  i.password
        u += "<b>" + "<u>" + f"Пользователь {num}: " + "</u>" + "</b>" + "<br>" + user + "<br>" + "<br>"
    return u, 200

#Не работает, хз почему, но это и не нужно, для себя пытался сделать
@app.route('/api/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = list(filter(lambda u: u['id'] == user_id, users))
    if user == None:
        abort(404)
    return jsonify({'user': user[0]})

#Метод получения всей музыки
@app.route('/api/musics/', methods=['GET'])
def get_musics():
    music = ''
    u = ''
    num = 0
    for i in musics:
        num += 1
        music = "<b>" + "Название трека: " + "</b>" + i.title + ", " + "<br>" + "<b>" + "Исполнитель: " + "</b>" + i.executor + ", " + "<br>" + "<b>" + "Жанр: " + "</b>" + i.genre + ", " + "<br>" + "<b>" + "Длительность: " + "</b>" + i.duration + ", " + "<br>" + "<b>" + "Рейтинг: " + "</b>" +  i.rating
        u += "<b>" + "<u>" + f"Трек {num}: " + "</u>" + "</b>" + "<br>" + music + "<br>" + "<br>"
    return u, 200

#Метод получения всех книг
@app.route('/api/books/', methods=['GET'])
def get_books():
    book = ''
    u = ''
    num = 0
    for i in books:
        num += 1
        book = "<b>" + "Название книги: " + "</b>" + i.title + ", " + "<br>" + "<b>" + "Автор книги: " + "</b>" + i.author + ", " + "<br>" + "<b>" + "Жанр: " + "</b>" + i.genre + ", " + "<br>" + "<b>" + "Количество страниц: " + "</b>" + i.numofpages + ", " + "<br>" + "<b>" + "Год издания: " + "</b>" +  i.year
        u += "<b>" + "<u>" + f"Книга {num}: " + "</u>" + "</b>" + "<br>" + book + "<br>" + "<br>"
    return u, 200

#Метод получения всех машин
@app.route('/api/cars/', methods=['GET'])
def get_cars():
    car = ''
    u = ''
    num = 0
    for i in cars:
        num += 1
        car = "<b>" + "Модель машины: " + "</b>" + i.name + ", " + "<br>" + "<b>" + "Марка машины: " + "</b>" + i.brand + ", " + "<br>" + "<b>" + "Цвет машины: " + "</b>" + i.color + ", " + "<br>" + "<b>" + "Максимальная скорость машины: " + "</b>" + i.speed + ", " + "<br>" + "<b>" + "Год выпуска машины: " + "</b>" +  i.year
        u += "<b>" + "<u>" + f"Машина {num}: " + "</u>" + "</b>" + "<br>" + car + "<br>" + "<br>"
    return u, 200

#Метод создания новых юзеров
@app.route('/api/users', methods=['POST'])
def create_user():
    rqst = request.get_json()
    name = None
    surname = None
    patronomyc = None
    email = None
    password = None

    if rqst:
        if 'name' in rqst:
            name = rqst['name']
        else:
            return 'Не обнаружено поле "name"', 403
        if 'surname' in rqst:
            surname = rqst['surname']
        else:
            return 'Не обнаружено поле "surname"', 403
        if 'patronomyc' in rqst:
            patronomyc = rqst['patronomyc']
        else:
            return 'Не обнаружено поле "patronomyc"', 403
        if 'email' in rqst:
            email = rqst['email']
        else:
            return 'Не обнаружено поле "email"', 403
        if 'password' in rqst:
            password = rqst['password']
        else:
            return 'Не обнаружено поле "password"', 403
    else:
        return 'Данных недостаточно', 403
    if name and surname and patronomyc and email and password:
        user = User(name, surname, patronomyc, email, password)
        users.append(user)
        return 'Пользователь создан', 201

#Первая попытка в метод пут, не получилось, решил переделать по другому
'''
@app.route('/api/put/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = list(filter(lambda u: u['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'surname' in request.json and type(request.json['surname']) != str:
        abort(400)
    if 'patronomyc' in request.json and type(request.json['patronomyc']) != str:
        abort(400)
    if 'email' in request.json and type(request.json['email']) != str:
        abort(400)
    if 'password' in request.json and type(request.json['password']) != str:
        abort(400)
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['surname'] = request.json.get('surname', user[0]['surname'])
    user[0]['patronomyc'] = request.json.get('patronomyc', user[0]['patronomyc'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['password'] = request.json.get('password', user[0]['password'])
    return jsonify({'user': user[0]})
'''

#Метод создания новой музыки
@app.route('/api/musics', methods=['POST'])
def create_music():
    rqst = request.get_json()
    title = None
    executor = None
    genre = None
    duration = None
    rating = None

    if rqst:
        if 'title' in rqst:
            title = rqst['title']
        else:
            return 'Не обнаружено поле "title"', 403
        if 'executor' in rqst:
            executor = rqst['executor']
        else:
            return 'Не обнаружено поле "executor"', 403
        if 'genre' in rqst:
            genre = rqst['genre']
        else:
            return 'Не обнаружено поле "genre"', 403
        if 'duration' in rqst:
            duration = rqst['duration']
        else:
            return 'Не обнаружено поле "duration"', 403
        if 'rating' in rqst:
            rating = rqst['rating']
        else:
            return 'Не обнаружено поле "rating"', 403
    else:
        return 'Данных недостаточно', 403
    if title and executor and genre and duration and rating:
        music = Music(title, executor, genre, duration, rating)
        musics.append(music)
        return 'Трек добавлен', 201

#Метод добавления новых книг
@app.route('/api/books', methods=['POST'])
def create_book():
    rqst = request.get_json()
    title = None
    author = None
    genre = None
    numofpages = None
    year = None

    if rqst:
        if 'title' in rqst:
            title = rqst['title']
        else:
            return 'Не обнаружено поле "title"', 403
        if 'author' in rqst:
            author = rqst['author']
        else:
            return 'Не обнаружено поле "author"', 403
        if 'genre' in rqst:
            genre = rqst['genre']
        else:
            return 'Не обнаружено поле "genre"', 403
        if 'numofpages' in rqst:
            numofpages = rqst['numofpages']
        else:
            return 'Не обнаружено поле "numofpages"', 403
        if 'year' in rqst:
            year = rqst['year']
        else:
            return 'Не обнаружено поле "year"', 403
    else:
        return 'Данных недостаточно', 403
    if title and author and genre and numofpages and year:
        book = Book(title, author, genre, numofpages, year)
        books.append(book)
        return 'Книга добавлена', 201

#Метод добавления новых машин
@app.route('/api/cars', methods=['POST'])
def create_car():
    rqst = request.get_json()
    name = None
    brand = None
    color = None
    speed = None
    year = None

    if rqst:
        if 'name' in rqst:
            name = rqst['name']
        else:
            return 'Не обнаружено поле "name"', 403
        if 'brand' in rqst:
            brand = rqst['brand']
        else:
            return 'Не обнаружено поле "brand"', 403
        if 'color' in rqst:
            color = rqst['color']
        else:
            return 'Не обнаружено поле "color"', 403
        if 'speed' in rqst:
            speed = rqst['speed']
        else:
            return 'Не обнаружено поле "speed"', 403
        if 'year' in rqst:
            year = rqst['year']
        else:
            return 'Не обнаружено поле "year"', 403
    else:
        return 'Данных недостаточно', 403
    if name and brand and color and speed and year:
        car = Car(name, brand, color, speed, year)
        cars.append(car)
        return 'Машина добавлена', 201

#Метод для редактирования юзеров
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if len(users) == 0 or len(users) == None:
        abort(404)
    rqst = request.get_json()
    if rqst:
        if 'name' in rqst:
            users[user_id].name = rqst['name']
        if 'surname' in rqst:
            users[user_id].surname = rqst['surname']
        if 'patronomyc' in rqst:
            users[user_id].patronomyc = rqst['patronomyc']
        if 'email' in rqst:
            users[user_id].email = rqst['email']
        if 'password' in rqst:
            users[user_id].password = rqst['password']
    else:
        return "Недостаточно данных", 403
    return "Пользователь успешно отредактирован", 200

#Метод для редактирования музыки
@app.route('/api/musics/<int:music_id>', methods=['PUT'])
def update_music(music_id):
    if len(musics) == 0 or len(musics) == None:
        abort(404)
    rqst = request.get_json()
    if rqst:
        if 'title' in rqst:
            musics[music_id].title = rqst['title']
        if 'executor' in rqst:
            musics[music_id].executor = rqst['executor']
        if 'genre' in rqst:
            musics[music_id].genre = rqst['genre']
        if 'duration' in rqst:
            musics[music_id].duration = rqst['duration']
        if 'rating' in rqst:
            musics[music_id].rating = rqst['rating']
    else:
        return "Недостаточно данных", 403
    return "Трек успешно отредактирован", 200

#Метод для редактирования книг
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if len(books) == 0 or len(books) == None:
        abort(404)
    rqst = request.get_json()
    if rqst:
        if 'title' in rqst:
            books[book_id].title = rqst['title']
        if 'author' in rqst:
            books[book_id].author = rqst['author']
        if 'genre' in rqst:
            books[book_id].genre = rqst['genre']
        if 'numofpages' in rqst:
            books[book_id].numofpages = rqst['numofpages']
        if 'year' in rqst:
            books[book_id].year = rqst['year']
    else:
        return "Недостаточно данных", 403
    return "Книга успешно отредактирована", 200

#Метод для редактирования машин
@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    if len(cars) == 0 or len(cars) == None:
        abort(404)
    rqst = request.get_json()
    if rqst:
        if 'name' in rqst:
            cars[car_id].name = rqst['name']
        if 'brand' in rqst:
            cars[car_id].brand = rqst['brand']
        if 'color' in rqst:
            cars[car_id].color = rqst['color']
        if 'speed' in rqst:
            cars[car_id].speed = rqst['speed']
        if 'year' in rqst:
            cars[car_id].year = rqst['year']
    else:
        return "Недостаточно данных", 403
    return "Машина успешно отредактирована", 200

#Тоже что-то не работает, ошибка, с которой я пытался разобраться очень много времени, пришлось переделывать
'''
@app.route('/api/delete/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = list(filter(lambda u: u['name'] == user_id, users))
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})
'''

#Метод для удаления юзеров по айдишнику
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if len(users) == 0 or len(users) == None:
        abort(404)
    users.pop(user_id)
    return "Пользователь успешно удален", 200

#Метод для удаления треков по айдишнику
@app.route('/api/musics/<int:music_id>', methods=['DELETE'])
def delete_music(music_id):
    if len(musics) == 0 or len(musics) == None:
        abort(404)
    musics.pop(music_id)
    return "Трек успешно удален", 200

#Метод для удаления книг по айдишнику
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if len(books) == 0 or len(books) == None:
        abort(404)
    books.pop(book_id)
    return "Кнмга успешно удалена", 200

#Метод для удаления машин по айдишнику
@app.route('/api/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    if len(cars) == 0 or len(cars) == None:
        abort(404)
    cars.pop(car_id)
    return "Машина успешно удалена", 200

#Создание текста для 404 ошибки
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Ошибка': 'Не найдено'}), 404)

#Ну и стандартная строчка для запуска кода
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3005)



