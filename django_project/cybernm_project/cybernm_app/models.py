from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=30)
    user_image = models.ImageField(verbose_name="Картинка для сотрудника", blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    social_link = models.CharField(max_length=50, verbose_name="Ссылка на соц. сети", blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=25, blank=True, null=True)


class discipline(models.Model):
    game_type = (
        ('st', 'strategy'),
        ('sh', 'shooter'),
        ('sm', 'simulator'),
    )
    discipline_name = models.CharField(max_length=50)
    discipline_id = models.AutoField(primary_key=True)
    discipline_image = models.ImageField(verbose_name="Картинка для игры", blank=True, null=True)
    match_seatsnumber = models.IntegerField()
    type = models.CharField(choices=game_type, max_length=50)
    description = models.TextField()


class tournament(models.Model):
    tournament_status = (
        ('a', 'announced'),
        ('r', 'run'),
        ('e', 'finished'),
    )
    status = models.CharField(choices=tournament_status, max_length=20)
    tournament_id = models.AutoField(primary_key=True)
    tournament_image = models.ImageField(verbose_name="image for tournament", blank=True, null=True)
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
                                      verbose_name='discipline')
    employee_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                    related_name='tournament_employee_id_fk',
                                    verbose_name='employee')
    players = models.ManyToManyField(User, null=True, blank=True, verbose_name="players",
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
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='nickname_fk',
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
