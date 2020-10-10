import graphene
from graphene_django.types import DjangoObjectType
from .models import inventory


class invenType(DjangoObjectType):
    class Meta:
        model = inventory


class invenQuery(graphene.ObjectType):
    all_inven = graphene.List(invenType)
#    DTReport = graphene.Field(all_DTReports, rNo=graphene.Int())


    def resolve_all_inven(self, info, **kwargs):
        return inventory.objects.all()

#    def resolve_DTReport(self, info, rNo):
#        return CHReportDetail.objects.filter(r_no=rNo)