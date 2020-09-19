from django.db import models

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, TIMESTAMP
metadata =  MetaData()

class CMAnalysis(models.Model):
    a_no = models.AutoField(db_column='a_no', primary_key=True)
    a_title = models.CharField(db_column='a_title', max_length=255)
    a_note = models.TextField(db_column='a_note', )
    a_owner = models.IntegerField(db_column='a_owner', default=1)
    a_date = models.DateTimeField(db_column='a_date', )
    a_count = models.IntegerField(db_column='a_count', default=0)
    usage_flag = models.CharField(db_column='usage_flag', max_length=10)
    analysis_cnt = models.IntegerField(db_column='analysis_cnt', default=0)
    reporting_cnt = models.IntegerField(db_column='reporting_cnt', default=0)
    type_no = models.IntegerField(db_column='type_no', default=0)
    type_desc = models.CharField(db_column='type_desc', max_length=255)

    class Meta:
        managed = False
        db_table = 'cm_analysis'

    def __str__(self):
        return "분석 제목 : " + self.a_title + ", 주관자 : " + self.a_owner


#    a_no = models.IntegerField(db_column='a_no', default=0)
#   a_no = models.ForeignKey(CMAnalysis, on_delete=models.CASCADE)
class CHAnalysisStep(models.Model):
    step_no = models.AutoField(db_column='step_no', primary_key=True)
    a_no = models.IntegerField(db_column='a_no', default=0)
    step_title = models.CharField(db_column='step_title', max_length=255)
    upload_url = models.CharField(db_column='upload_url', max_length=1024)
    upload_file = models.CharField(db_column='upload_file', max_length=1024)
    upload_cnt = models.IntegerField(db_column='upload_cnt', default=0)
    analysis_cnt = models.IntegerField(db_column='analysis_cnt', default=0)
    datatable_in = models.CharField(db_column='datatable_in', max_length=255)
    datatable_out = models.CharField(db_column='datatable_out', max_length=255)
    datain_cnt = models.IntegerField(db_column='datain_cnt', default=0)
    dataout_cnt = models.IntegerField(db_column='dataout_cnt', default=0)
    step_date = models.DateTimeField(db_column='step_date', )
    tablein_flag = models.CharField(db_column='tablein_flag', max_length=10)
    tableout_flag = models.CharField(db_column='tableout_flag', max_length=10)
    usage_flag = models.CharField(db_column='usage_flag', max_length=10)

    class Meta:
        managed = False
        db_table = 'ch_analysis_step'

    def __str__(self):
        return "분석 단계 : " + self.step_title + ", 파일 : " + self.upload_url

class CHUploadHistory(models.Model):
    h_no = models.AutoField(db_column='h_no', primary_key=True)
    a_no = models.IntegerField(db_column='a_no', default=0)
    step_no = models.IntegerField(db_column='step_no', default=0)
    upload_url = models.CharField(db_column='upload_url', max_length=1024)
    upload_file = models.CharField(db_column='upload_file', max_length=1024)
    file_name = models.CharField(db_column='file_name', max_length=1024)
    file_size = models.IntegerField(db_column='file_size', default=0)
    h_datetime = models.DateTimeField(db_column='h_datetime', )

    class Meta:
        managed = False
        db_table = 'ch_uploadhistory'

    def __str__(self):
        return "업로드 경로 : " + self.upload_url

class CHAnalysisHistory(models.Model):
    h_no = models.AutoField(db_column='h_no', primary_key=True)
    a_no = models.IntegerField(db_column='a_no', default=0)
    step_no = models.IntegerField(db_column='step_no', default=0)
    upload_url = models.CharField(db_column='upload_url', max_length=1024)
    upload_file = models.CharField(db_column='upload_file', max_length=255)
    success_flag = models.CharField(db_column='success_flag', max_length=10)
    h_date = models.DateTimeField(db_column='h_date', )

    class Meta:
        managed = False
        db_table = 'ch_analysis_history'

    def __str__(self):
        return "실행파일 경로 : " + self.upload_url


class CSMetaData(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    step_no = models.IntegerField(db_column='step_no', default=0)
    inout_flag = models.CharField(db_column='inout_flag', max_length=10)
    column_name = models.CharField(db_column='column_name', max_length=255)
    column_type = models.CharField(db_column='column_type', max_length=255)
    order_no = models.IntegerField(db_column='order_no', default=0)

    class Meta:
        managed = False
        db_table = 'cs_meta_data'

    def __str__(self):
        return "분석Meta 데이터 항목 : " + self.column_name

# SQLAlchemy용
csmetadata2 = Table('cs_meta_data', metadata,
             Column('id', Integer, primary_key=True),
             Column('step_no', Integer),
             Column('inout_flag', String(10)),
             Column('column_name', String(255)),
             Column('column_type', String(255)),
             Column('order_no', Integer),
             )

class CHReport(models.Model):
    r_no = models.AutoField(db_column='r_no', primary_key=True)
    a_no = models.IntegerField(db_column='a_no', default=0)
    report_title = models.CharField(db_column='report_title', max_length=1024)
    report_note = models.CharField(db_column='report_note', max_length=4096)
    detail_cnt = models.IntegerField(db_column='detail_cnt', default=0)
    char_cnt = models.IntegerField(db_column='char_cnt', default=0)
    comment_cnt = models.IntegerField(db_column='comment_cnt', default=0)
    r_date = models.DateTimeField(db_column='r_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10)
    member_id = models.CharField(db_column='member_id', max_length=20)
    img_url = models.CharField(db_column='img_url', max_length=20)
    release_flag = models.CharField(db_column='release_flag', max_length=10)

    class Meta:
        managed = False
        db_table = 'ch_report'

    def __str__(self):
        return "분석 Report : " + self.report_title

class CHReportDetail(models.Model):
    rh_no = models.AutoField(db_column='rh_no', primary_key=True)
    r_no = models.IntegerField(db_column='r_no', default=0)
    s_type = models.CharField(db_column='s_type', max_length=10)
    s_title = models.CharField(db_column='s_title', max_length=1024)
    s_note = models.CharField(db_column='s_note', max_length=4096)
    s_note_post = models.CharField(db_column='s_note_post', max_length=4096)
    s_note_special = models.CharField(db_column='s_note_special', max_length=4096)
    img_url = models.CharField(db_column='img_url', max_length=1024)
    s_date = models.DateTimeField(db_column='s_date', )
    display_flag = models.CharField(db_column='display_flag', max_length=10)
    usage_flag = models.CharField(db_column='usage_flag', max_length=10)

    class Meta:
        managed = False
        db_table = 'ch_report_detail'

    def __str__(self):
        return "Report 상세 : " + self.s_title

class CMType(models.Model):
    type_no = models.AutoField(db_column='type_no', primary_key=True)
    cat_no = models.IntegerField(db_column='cat_no', default=0)
    cat_desc = models.CharField(db_column='cat_desc', max_length=255)
    type_desc = models.CharField(db_column='type_desc', max_length=1024)
    order_no = models.IntegerField(db_column='order_no', default=0)

    class Meta:
        managed = False
        db_table = 'cm_type'

    def __str__(self):
        return "분석 유형 : " + self.type_desc


class Person(models.Model):
    name = models.CharField(db_column='name', max_length=255)

    class Meta:
        managed = True
        db_table = 'cm_person'

class CHReportComment(models.Model):
    c_no = models.AutoField(db_column='c_no', primary_key=True)
    r_no = models.IntegerField(db_column='r_no', )
    comment_descript = models.CharField(db_column='comment_descript', max_length=255)
    c_date = models.DateTimeField(db_column='c_date', )
    c_count = models.IntegerField(db_column='c_count', default=0)
    image_url = models.CharField(db_column='image_url', max_length=255)

    class Meta:
        managed = False
        db_table = 'ch_report_comment'

    def __str__(self):
        return "Comment : " + self.comment_descript