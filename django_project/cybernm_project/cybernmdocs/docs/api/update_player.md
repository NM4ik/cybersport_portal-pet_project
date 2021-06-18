Редактирование игрока

форма для редактирования игрока

**URL** : `Updateplayer/<pk>/`

**Method** : `PATCH`, `PUT`

**Auth required** : YES

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "user_id": 153,
        "password": "123123qweqwe",
        "last_login": null,
        "is_superuser": false,
        "username": "NM4ik",
        "first_name": "Nikita",
        "last_name": "Mikhailov",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2021-06-14T22:17:34Z",
        "nickname": "NM",
        "user_image": null,
        "email": "n.mikhailov55@gmail.com",
        "post": "player",
        "social_link": "https://vk.com/nmihailov89",
        "birth_date": "2021-06-14",
        "city": "Saint-Petersburg",
        "role": "Sniper",
        "groups": [],
        "user_permissions": []
    }
]
```