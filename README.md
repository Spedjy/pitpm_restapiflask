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

9. GET(book) - http://localhost:3005/api/books

![GETbooks](https://user-images.githubusercontent.com/98220684/205609626-ebaff5aa-bd06-4a71-b1d8-4c2ac9396061.png)

Данные о книге, 200

10. POST(book) - http://localhost:3005/api/books

{
    "title": "title",
    "author": "author",
    "genre": "genre",
    "numofpages": "numofpages",
    "year": "year"
}

![POSTbook](https://user-images.githubusercontent.com/98220684/205610048-6dc7d1ac-98b5-4204-b1e9-7258e65e01df.png)

Книга добавлена, 201

11. PUT(book) - http://localhost:3005/api/books/0

{
    "title":"title1"
}

![PUTbook](https://user-images.githubusercontent.com/98220684/205610327-268295a1-90b2-4729-9c4c-6f4ff3543d05.png)

Книга отредактирована, 200

12. DELETE(book) - http://localhost:3005/api/books/0

![DELETEbook](https://user-images.githubusercontent.com/98220684/205610426-318af7e4-f3f9-460d-803e-6f34803fc9fc.png)

Книга успешно удалена, 200

13. GET(car) - http://localhost:3005/api/cars

![GETcars](https://user-images.githubusercontent.com/98220684/205610860-212a07fc-bab2-4101-9972-0171124b7d88.png)


Данные о машине, 200

14. POST(car) - http://localhost:3005/api/cars

{
    "name": "name",
    "brand": "brand",
    "color": "color",
    "speed": "speed",
    "year": "year"
}

![POSTcar](https://user-images.githubusercontent.com/98220684/205610883-de85d614-10cb-48a5-9ec8-4a18f78c86a3.png)


Машина добавлена, 201

15. PUT(car) - http://localhost:3005/api/cars/0

{
    "brand": "brand1"
}

![PUTcar](https://user-images.githubusercontent.com/98220684/205610903-4b15ddf5-c093-4b6f-b0e7-2b86bd9f8b89.png)

Машина отредактирована, 200

16. DELETE(car) - http://localhost:3005/api/cars/0

![DELETEcar](https://user-images.githubusercontent.com/98220684/205610923-5f2291c1-2cd6-4163-bde3-e0981c086397.png)

Машина успешно удалена, 200




