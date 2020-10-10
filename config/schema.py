import graphene
from analysis.schema import CHReportQuery,DTReportQuery
from api.schema import invenQuery
#from analysis.schema import CMAnalysisQuery, CHAnalysisStepQuery


class Query(
    CHReportQuery,
    DTReportQuery,
    invenQuery,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
