import graphene
from graphene_django.types import DjangoObjectType
from .models import inventory


class invenType(DjangoObjectType):
    class Meta:
        model = inventory


class invenQuery(graphene.ObjectType):
    all_inven = graphene.List(invenType)
    date_inven = graphene.Field(all_inven, iDate=graphene.String(), bsnscd=graphene.String())


    def resolve_all_inven(self, info, **kwargs):
        return inventory.objects.all()

    def resolve_date_inven(self, info, iDate, bsnscd):
        return inventory.objects.filter(i_date__contains=iDate, bsnscd=bsnscd)