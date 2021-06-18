Выводит информацию обо всех дисциплинах

**URL** : `Alldisciplines/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "discipline_id": 1,
        "discipline_name": "Counter:Strike Global Offensive",
        "discipline_image": "http://127.0.0.1:8000/media/Rectangle_594_E2JJSwX.jpg",
        "match_seatsnumber": 10,
        "type": "sh",
        "description": "The most popular shooter"
    },
    {
        "discipline_id": 2,
        "discipline_name": "Valorant",
        "discipline_image": "http://127.0.0.1:8000/media/Rectangle_597_3V4SoGX.jpg",
        "match_seatsnumber": 10,
        "type": "sh",
        "description": "Shooter like a Counter-Strike : Global Offensive"
    },
    {
        "discipline_id": 3,
        "discipline_name": "DOTA 2",
        "discipline_image": "http://127.0.0.1:8000/media/Rectangle_595_y26FhLy.jpg",
        "match_seatsnumber": 10,
        "type": "st",
        "description": "The most popular strategy"
    },
    {
        "discipline_id": 4,
        "discipline_name": "FIFA 2020",
        "discipline_image": "http://127.0.0.1:8000/media/Rectangle_596_Pi5zRuf.jpg",
        "match_seatsnumber": 2,
        "type": "sm",
        "description": "The most popular football simulator"
    }
]
```