from django.db import models

# Create your models here.
class File(models.Model):
    STARTED = 0
    IN_PROCESS = 1
    ERROR = 2
    SUCCESS = 3
    STATUS_FILE_CHOICES = [
        (STARTED, 'Iniciado'),
        (IN_PROCESS, 'Procesando'),
        (ERROR, 'Error'),
        (SUCCESS, 'Finalizado')
    ]
    user_name = models.TextField()
    internal_name = models.TextField()
    report_internal_name = models.TextField()
    date = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_FILE_CHOICES, default=STARTED)   

    class Meta:
        db_table = 'file'

class Document(models.Model):

    file = models.ForeignKey(File, models.DO_NOTHING)
    first_name = models.CharField(max_length=160)
    last_name = models.CharField(max_length=160)
    fiscal_number = models.CharField(max_length=15)
    sex = models.CharField(max_length=1)
    

    class Meta:
        db_table = 'document'

class Site(models.Model):
    
    document = models.ForeignKey(Document, models.DO_NOTHING)
    url = models.TextField()
    glossary = models.TextField()

    class Meta:
        db_table = 'site'
