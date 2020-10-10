import graphene
from graphene_django.types import DjangoObjectType
from .models import CHReport, CHReportDetail


class CHReportType(DjangoObjectType):
    class Meta:
        model = CHReport

class CHReportDetailType(DjangoObjectType):
    class Meta:
        model = CHReportDetail

class CHReportQuery(graphene.ObjectType):
    all_CHReports = graphene.List(CHReportType)
    CHReport = graphene.Field(CHReportType, rNo=graphene.Int())

    def resolve_all_CHReports(self, info, **kwargs):
        return CHReport.objects.all()

    def resolve_CHReport(self, info, rNo):

        return CHReport.objects.get(pk=rNo)


class DTReportQuery(graphene.ObjectType):
    all_DTReports = graphene.List(CHReportDetailType)
    DTReport = graphene.Field(all_DTReports, rNo=graphene.Int())


    def resolve_all_DTReports(self, info, **kwargs):
        return CHReportDetail.objects.all()

    def resolve_DTReport(self, info, rNo):
        return CHReportDetail.objects.filter(r_no=rNo)