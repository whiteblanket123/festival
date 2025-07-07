from django.db import models

class Information(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    vote = models.IntegerField(null=True, blank= True)

    class Meta:
        db_table = 'information'  # 데이터베이스 테이블 이름 지정
        verbose_name = 'Information'  # 모델의 단수 이름
        verbose_name_plural = 'Informations'  # 모델의 복수 이름

        # 인덱스 정의
        indexes = [
            # name과 number 컬럼에 대한 다중 컬럼 인덱스
            # name: 인덱스 이름 (선택 사항, 없으면 장고가 자동 생성)
            models.Index(fields=['name', 'number'], name='idx_information_name_number'),
            
            # vote 컬럼에 대한 단일 컬럼 인덱스
            models.Index(fields=['vote'], name='idx_information_vote'),
        ]

class Participant(models.Model):
    participant1 = models.CharField(max_length=100)
    participant2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.participant1}, {self.participant2}"

    class Meta:
        db_table = 'participant'  # 데이터베이스 테이블 이름 지정
        verbose_name = 'Participant'  # 모델의 단수 이름
        verbose_name_plural = 'Participants'  # 모델의 복수 이름