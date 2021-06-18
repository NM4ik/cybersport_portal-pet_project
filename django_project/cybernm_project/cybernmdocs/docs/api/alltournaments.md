Выводит информацию обо всех турнирах

**URL** : `Alltournaments/`

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
        "tournament_id": 1,
        "status": "run",
        "limitation": "8-10lvl",
        "tournament_image": null,
        "name": "IEM SUMMER 2021",
        "seats_number": 8,
        "prize": "20000000$",
        "start_date": "2021-06-30",
        "end_date": "2021-07-31",
        "discipline_id": 1,
        "employee_id": 1,
        "players": [
            2,
            146,
            152
        ]
    },
    {
        "tournament_id": 2,
        "status": "run",
        "limitation": "5-8lvl",
        "tournament_image": "http://127.0.0.1:8000/media/e3036_X4Kmq1j_slY0mYm.png",
        "name": "Katowice Masters",
        "seats_number": 8,
        "prize": "10000000$",
        "start_date": "2021-06-14",
        "end_date": "2021-06-20",
        "discipline_id": 2,
        "employee_id": 1,
        "players": [
            152,
            153
        ]
    },
    {
        "tournament_id": 3,
        "status": "finished",
        "limitation": "8-10lvl",
        "tournament_image": "http://127.0.0.1:8000/media/Rectangle_596_ZK7iUtu.jpg",
        "name": "FIFA CHAMPION MAJOR",
        "seats_number": 64,
        "prize": "PLAYSTATION 6",
        "start_date": "2021-06-07",
        "end_date": "2021-06-14",
        "discipline_id": 4,
        "employee_id": 1,
        "players": [
            146,
            151
        ]
    },
    {
        "tournament_id": 4,
        "status": "announced",
        "limitation": "8-10lvl",
        "tournament_image": null,
        "name": "DOTA 2 CHAMPION CUP",
        "seats_number": 10,
        "prize": "30000000$",
        "start_date": "2021-06-22",
        "end_date": "2021-06-28",
        "discipline_id": 3,
        "employee_id": 1,
        "players": [
            2
        ]
    }
]
```