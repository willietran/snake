from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class Score(models.Model):
    player = models.ForeignKey(User, related_name='user')
    score = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    game_choices = (
        ('S', 'Snake'),
        ('M', 'Memory'),
    )

    game = models.CharField(max_length=1,
                            choices=game_choices,
                            default='S')

    def __unicode__(self):
        return u"{}".format(self.score)
    #
    # def get_highest_score(self):
    #     score =