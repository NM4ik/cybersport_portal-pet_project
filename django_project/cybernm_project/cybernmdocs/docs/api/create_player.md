Создание игрока

Форма для создания игрока

**URL** : `Addplayer/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : IsAuthenticated

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "user_id": 156,
        "password": "pbkdf2_sha256$216000$ZEmHlh7jGXyg$5I3qMlEJeaREtOtWH1NG2K0kFVx4b+qBvYSCTNzxa9c=",
        "last_login": "2021-06-15T09:01:25.520906Z",
        "is_superuser": false,
        "username": "newuser",
        "first_name": "akwdqkwd",
        "last_name": "jnasdnasd",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-06-15T08:50:13.998476Z",
        "nickname": "example-player",
        "user_image": null,
        "email": "aaaa@bk.ru",
        "post": null,
        "social_link": "vk.com",
        "birth_date": "2021-06-09",
        "city": "Moscow",
        "role": "Sniper",
        "groups": [],
        "user_permissions": []
    }
]
```