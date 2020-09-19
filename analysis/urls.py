from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('help/', views.help, name="help"),
    path('intelligence', views.intelligence, name="intelligence"),

    path('analysis', views.analysis, name="analysis"),
    url('analysis_generate', views.analysis_generate, name="analysis_generate"),
    url('analysis_view', views.analysis_view, name="analysis_view"),
    url('analysis_detail', views.analysis_detail, name="analysis_detail"),
    url('analysis_step', views.analysis_step, name="analysis_step"),
    url('analysis_run', views.analysis_run, name="analysis_run"),
    url('analysis_update', views.analysis_update, name="analysis_update"),
    url('analysis_toggle', views.analysis_toggle, name="analysis_toggle"),
    url('analysis_upload', views.analysis_upload, name="analysis_upload"),
    url('analysis_metawrite', views.analysis_metawrite, name="analysis_metawrite"),
    url('analysis_metaread', views.analysis_metaread, name="analysis_metaread"),
    url('analysis_metaupload', views.analysis_metaupload, name="analysis_metaupload"),
    url('analysis_metasave', views.analysis_metasave, name="analysis_metasave"),

    url('analysis_code', views.analysis_code, name="analysis_code"),
    url('analysisfile_update', views.analysisfile_update, name="analysisfile_update"),

    url('analysis_data', views.analysis_data, name="analysis_data"),
    url('data_column_generate', views.data_column_generate, name="data_column_generate"),
    url('data_columndelete', views.data_columndelete, name="data_columndelete"),
    url('data_columncopy', views.data_columncopy, name="data_columncopy"),
    url('data_table_generate', views.data_table_generate, name="data_table_generate"),

    url('step_generate', views.step_generate, name="step_generate"),
    url('step_update', views.step_update, name="step_update"),

    url('analysis_report', views.analysis_report, name="analysis_report"),
    url('report_generate', views.report_generate, name="report_generate"),
    url('report_edit', views.report_edit, name="report_edit"),
    url('reportedit_section', views.reportedit_section, name="reportedit_section"),
    url('report_update', views.report_update, name="report_update"),
    url('report_sectionimage_upload', views.report_sectionimage_upload, name="report_sectionimage_upload"),
    url('reportedit_delete', views.reportedit_delete, name="reportedit_delete"),
    url('reportedit_write', views.reportedit_write, name="reportedit_write"),

    url('reporting', views.reporting, name="reporting"),
    url('report_release', views.report_release, name="report_release"),
    url('report_view', views.report_view, name="report_view"),
    url('reportcmt_create', views.reportcmt_create, name="reportcmt_creat"),

    url('blabla', views.whatever, name='hello'),
    url('subtest', views.subtest, name='subtest'),
    url('dbtest', views.dbtest, name='dbtest'),

]
