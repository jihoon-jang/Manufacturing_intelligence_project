from django.db import models

# Create your models here.
class inventory(models.Model):
    i_no = models.AutoField(db_column='id', primary_key=True)
    bsnscd = models.CharField(db_column='bsnscd', max_length=255)
    measures = models.CharField(db_column='measures', max_length=255)
    i_date = models.CharField(db_column='yyyymmdd', max_length=1024)
    i_init = models.IntegerField(db_column='inv_init', default=0)
    i_close = models.IntegerField(db_column='inv_close', default=0)
    i_input = models.IntegerField(db_column='inv_input', default=0)
    i_output = models.IntegerField(db_column='inv_output', default=0)
    i_rate = models.FloatField(db_column='inv_rate', default=0)
    i_predict = models.FloatField(db_column='invrate_predict', default=0)

    class Meta:
        managed = False
        db_table = 'inventory2009'