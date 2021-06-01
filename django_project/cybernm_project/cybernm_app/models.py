from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class discipline(models.Model):
    discipline_id = models.IntegerField(primary_key=True)
    discipline_name = models.CharField(max_length=30)
    discipline_image = models.ImageField(verbose_name="Картинка для игры", blank=True, null=True)
    match_seatsnumber = models.IntegerField()
    type = models.CharField(max_length=25)
    description = models.TextField()


class employee(AbstractUser):
    employee_id = models.IntegerField(primary_key=True)
    employee_image = models.ImageField(verbose_name="Картинка для сотрудника", blank=True, null=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    post = models.CharField(max_length=20)


class player(models.Model):
    nickname = models.CharField(max_length=30, primary_key=True)
    player_image = models.ImageField(verbose_name="Картинка для игрока", blank=True, null=True)
    discipline_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=25)
    email = models.CharField(max_length=50)


class tournament(models.Model):
    tournament_status = (
        ('a', 'анонсирован'),
        ('r', 'проводится'),
        ('e', 'закончен'),
    )
    status = models.CharField(choices=tournament_status, max_length=20)
    tournament_id = models.IntegerField(primary_key=True)
    tournament_image = models.ImageField(verbose_name="Картинка для турнира", blank=True, null=True)
    name = models.CharField(max_length=45)
    seats_number = models.IntegerField()
    prize = models.CharField(max_length=45)
    tournament_limitation = (
        ('f15', '1-5lvl'),
        ('f58', '5-8lvl'),
        ('f810', '8-10lvl'),
    )
    limitation = models.CharField(choices=tournament_limitation, max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    discipline_id = models.ForeignKey(discipline, on_delete=models.CASCADE, null=True, related_name='discipline_id_fk',
                                      verbose_name='Дисциплина')
    employee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                    related_name='tournament_employee_id_fk',
                                    verbose_name='Сотрудник')
    players = models.ManyToManyField(player, null=True, blank=True, verbose_name="игроки",
                                     related_name="tournament_player")





class tournament_participation(models.Model):
    """
    Участие на турнире
      """
    status_types = (
        ('w', 'на рассмотрении'),
        ('a', 'принят'),
        ('o', 'отклонен'),
    )
    status = models.CharField(choices=status_types, max_length=20)
    participation_id = models.IntegerField()
    reason = models.CharField(max_length=100)
    nickname = models.ForeignKey(player, on_delete=models.CASCADE, null=True, related_name='nickname_fk',
                                 verbose_name='Ник игрока')
    tournament_id = models.ForeignKey(tournament, on_delete=models.CASCADE, null=True,
                                      related_name='tournament_id_participation_fk',
                                      verbose_name='Номер турнира')


class news(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.TextField(verbose_name="Новостной текст")
    image = models.ImageField(verbose_name="Картинка для новости")
    employee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                    related_name='employeers_id_fk',
                                    verbose_name='Сотрудник')