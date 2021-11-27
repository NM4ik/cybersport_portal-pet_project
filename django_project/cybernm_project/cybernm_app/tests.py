from unittest import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from .logic import desc
from .models import news
from .models import discipline
from .serializers import newsListSeriallizer, disciplineListSeriallizer


class CyberTestCase(APITestCase):  # Тест создания новостей
    def test_get(self):
        self.news_1 = news.objects.create(name='testNews', description='TestDesc')
        self.news_2 = news.objects.create(name='testNews2', description='TestDesc2')
        url = 'http://127.0.0.1:8000/Allnews/'

        response = self.client.get(url)
        serializer_data = newsListSeriallizer([self.news_1, self.news_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # проверка ответа сервера
        self.assertEqual(serializer_data, response.data)  # manyTrue - для списка(массива)


class NewsSerializerTest(TestCase):  # Тестирование сериалайзера
    def test_ok(self):
        self.news_1 = news.objects.create(name='testNews', description='')
        self.news_2 = news.objects.create(name='testNews2', description='')
        data = newsListSeriallizer([self.news_1, self.news_2], many=True).data
        expect_data = [
            {
                'name': 'testNews',
                'description': '',
            },
            {
                'name': 'testNews2',
                'description': '',
            }
        ]
        self.assertEqual(expect_data, data)


class LogicTestCase(TestCase):
    def test_logic_more(self):
        result1 = desc(4, 5, 1)
        self.assertEqual((-0.25, -1), result1)

    def test_logic_less(self):
        result = desc(16, 3, 1)
        self.assertEqual("Корень не найден, так как дискриминант меньше нуля", result)

    def test_logic_zero(self):
        result = desc(4, 4, 1)
        self.assertEqual(-0.5, result)


class DisciplineTestCase(APITestCase):  # Тест создания новостей
    def test_discipline(self):
        self.discipline_1 = discipline.objects.create(discipline_id=25, discipline_name='testdesc',
                                                      match_seatsnumber=10, type='sh',
                                                      description='')
        self.discipline_2 = discipline.objects.create(discipline_id=26, discipline_name='testdesc2',
                                                      match_seatsnumber=11, type='sh',
                                                      description='')
        url = 'http://127.0.0.1:8000/Alldisciplines/'

        response = self.client.get(url)
        serializer_data = disciplineListSeriallizer([self.discipline_1, self.discipline_2], many=True).data
        # serializer_data = disciplineListSeriallizer(self.discipline_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)  # проверка ответа сервера
        self.assertEqual(serializer_data, response.data)  # manyTrue - для списка(массива)

class DisciplineSerializerTest(TestCase):  # Тестирование сериалайзера
    def test_discipline_serializer(self):
        self.discipline_1 = discipline.objects.create(discipline_id=25, discipline_name='testdesc',
                                                      match_seatsnumber=10, type='sh',
                                                      description='')
        self.discipline_2 = discipline.objects.create(discipline_id=26, discipline_name='testdesc2',
                                                      match_seatsnumber=11, type='sh',
                                                      description='')
        data = disciplineListSeriallizer([self.discipline_1, self.discipline_2], many=True).data
        expect_data = [
            {
                'discipline_id': '25.00',
                'name': 'testdesc',
                'match_seatsnumber': '10.00',
                'type': 'sh',
                'description': '',
            },
            {
                'discipline_id': '26.00',
                'name': 'testdesc2',
                'match_seatsnumber': '11.00',
                'type': 'sh',
                'description': '',
            }
        ]
        self.assertEqual(expect_data, data)
