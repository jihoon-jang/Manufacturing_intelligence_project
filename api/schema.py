import graphene
from graphene_django.types import DjangoObjectType
from .models import inventory


class invenType(DjangoObjectType):
    class Meta:
        model = inventory


class invenQuery(graphene.ObjectType):
    all_inven = graphene.List(invenType)
    date_inven = graphene.Field(all_inven, bsnscd=graphene.String())


    def resolve_all_inven(self, info, **kwargs):
        return inventory.objects.all()

    def resolve_date_inven(self, info, bsnscd):
        return inventory.objects.filter(bsnscd=bsnscd)