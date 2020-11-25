import graphene
import patitofeo.schema

class Query(patitofeo.schema.Query, graphene.ObjectType):
    pass
    
class Mutation(patitofeo.schema.Mutation, graphene.ObjectType,):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)