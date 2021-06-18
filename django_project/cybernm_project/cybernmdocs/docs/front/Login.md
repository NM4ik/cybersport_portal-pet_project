## Авторизация

**URL** : `LogIn/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : IsAuthenticated

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

## Success URL

**If user == admin** : `administration/`

## Профиль

**URL** : `administration/`

**Method** : `GET`, `PUT`, `DELETE`, `POST`, `PATCH`,

**Auth required** : YES

**Permissions required** : IsAdmin

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

