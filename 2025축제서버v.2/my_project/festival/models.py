from django.db import models

class Information(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    vote = models.IntegerField(null=True, blank= True)

    class Meta:
        db_table = 'information'  # 데이터베이스 테이블 이름 지정
        verbose_name = 'Information'  # 모델의 단수 이름
        verbose_name_plural = 'Informations'  # 모델의 복수 이름

class Participant(models.Model):
    participant1 = models.CharField(max_length=100)
    participant2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.participant1}, {self.participant2}"

    class Meta:
        db_table = 'participant'  # 데이터베이스 테이블 이름 지정
        verbose_name = 'Participant'  # 모델의 단수 이름
        verbose_name_plural = 'Participants'  # 모델의 복수 이름