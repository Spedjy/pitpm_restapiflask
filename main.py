from flask import *

app = Flask(__name__)

#Создание массивов для хранения юзеров
users = []
#Создание массивов для хранения музыки
musics = []


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
        "DELETE(music) - " + "<a href='http://localhost:3005/api/musics/0'>" + "http://localhost:3005/api/musics/0" + "</a>" + "<br>" 
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

#Метод для редактирования юзеров
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

#Создание текста для 404 ошибки
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Ошибка': 'Не найдено'}), 404)

#Ну и стандартная строчка для запуска кода
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3005)



