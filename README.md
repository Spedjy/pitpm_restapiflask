1. GET(user) - http://localhost:3005/api/users

 ![GETusers](https://user-images.githubusercontent.com/98220684/205493606-3310c780-c20c-472d-b672-fef05137f8cb.png)
 
 Данные пользователей, 200
 
 2. POST(user) - http://localhost:3005/api/users
 
 {
    "name": "Александр",
    "surname": "Жирков",
    "patronomyc": "Дмитриевич",
    "email": "magnus134545@yandex.ru",
    "password": "qwerty12345"
}

![POSTusers](https://user-images.githubusercontent.com/98220684/205493647-795be08f-485f-4635-af4f-93233c8b23ba.png)

Пользователь создан, 201

3. PUT(user) - http://localhost:3005/api/users/0

{
    "name": "Матвей"
}

![PUTusers](https://user-images.githubusercontent.com/98220684/205493676-7a7d1621-0e9e-4735-9412-cab2d6898dfb.png)

Пользователь отредактирован, 200

4. DELETE(user) - http://localhost:3005/api/users/0

![DELETEusers](https://user-images.githubusercontent.com/98220684/205493694-5e1b11e5-7dc2-43d5-b47d-d50e7a3deed3.png)

Пользователь успешно удалён, 200

5. GET(music) -  http://localhost:3005/api/musics

![GETmusic](https://user-images.githubusercontent.com/98220684/205493779-e3d24162-8b18-448c-b53a-0d23b81354e0.png)

Данные трека, 200

6. POST(music) - http://localhost:3005/api/musics

{
    "title": "After Dark",
    "executor": "Mr.Kitty",
    "genre": "Альтернативная музыка/Инди",
    "duration": "4:17",
    "rating": "12/10"
}

![POSTmusic](https://user-images.githubusercontent.com/98220684/205493794-1a7b5876-a40f-45d8-bbd5-c6b7c09822e9.png)

Трек добавлен, 201

7. PUT(music) - http://localhost:3005/api/musics/0

{
    "title":"123"
}

![PUTmusic](https://user-images.githubusercontent.com/98220684/205493881-63effecd-907f-443b-b4b7-4d30b7567230.png)

Трек отредактирован, 200

8. DELETE(music) - http://localhost:3005/api/musics/0

![DELETEmusic](https://user-images.githubusercontent.com/98220684/205493888-2541f582-1487-4599-8b70-3b22d6eb2102.png)

Трек успешно удалён, 200


