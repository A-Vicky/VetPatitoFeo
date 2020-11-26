import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from patitofeo.models import Employee, Owner, Pet, Appointment

class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = ['first_name', 'specialty']
        interfaces = (relay.Node,)

class OwnerNode(DjangoObjectType):
    class Meta:
        model = Owner
        filter_fields = ['first_name', 'first_lname', 'email', 'phone']
        interfaces = (relay.Node,)
        
class PetNode(DjangoObjectType):
    class Meta:
        model = Pet
        filter_fields = ['first_name', 'last_name', 'breed', 'owner']
        interfaces = (relay.Node,)
        
class AppointmentNode(DjangoObjectType):
    class Meta:
        model = Appointment
        filter_fields = ['date', 'pet', 'profesional']
        interfaces = (relay.Node,)

class EmployeeModel(DjangoObjectType):
    class Meta:
        model = Employee
    
class NewEmployee(graphene.Mutation):
    new = graphene.Field(EmployeeModel)
    
    class Arguments:
        firstName = graphene.String(required=True)
        middleName = graphene.String(required=True)
        firstLname = graphene.String(required=True)
        secondLname = graphene.String(required=True)
        email = graphene.String(required=True)
        specialty = graphene.String(required=True)
        
    def mutate(self, info, firstName, middleName, firstLname, secondLname, email, specialty):
        
        new = Employee(first_name=firstName, middle_name=middleName,first_lname=firstLname,second_lname=secondLname, email=email, specialty=specialty)
        new.save()
        
        return NewEmployee(new=new)

class PetModel(DjangoObjectType):
    class Meta:
        model = Pet
    
class NewPet(graphene.Mutation):
    new = graphene.Field(PetModel)
    
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        breed = graphene.String(required=True)
        colors = graphene.String(required=True)
        behavior = graphene.String(required=True)
        age = graphene.Int(required=True)
        ownerid = graphene.Int(required=True)
        
    def mutate(self, first_name, last_name, breed, colors, behaviour, age, ownerid):
        owner = Owner.objects.get(id=ownerid)
        new = Pet(first_name=first_name, last_name=last_name,breed=breed,colors=colors, behavior=behaviour,age=age,owner=owner)
        new.save()
    
        return NewPet(new=new)

class OwnerModel(DjangoObjectType):
    class Meta:
        model = Owner
        
class NewOwner(graphene.Mutation):
    new = graphene.Field(OwnerModel)
    
    class Arguments:
        first_name = graphene.String(required=True)
        middle_name = graphene.String(required=True)
        first_lname = graphene.String(required=True)
        second_lname = graphene.String(required=True)
        address = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        
    def mutate(self, first_name, middle_name, first_lname, second_lname, address, email, phone):
        new = Owner(first_name=first_name, middle_name=middle_name,first_lname=first_lname,second_lname=second_lname, address=address,email=email,phone=phone)
        new.save()
        
        return NewOwner(new=new)
        
class AppointmentModel(DjangoObjectType):
    class Meta:
        model = Appointment
        
class NewAppointment(graphene.Mutation):
    new = graphene.Field(AppointmentModel)
    
    class Arguments:
        petid = graphene.Int(required=True)
        profesionalid = graphene.Int(required=True)
        description = graphene.String(required=True)
        comments = graphene.String(required=True)
        
    def mutate(self, petid, profesionalid, description, comments):
        pet = Pet.objects.get(id=id)
        employee = Employee.objects.get(id=id)
        new = Appointment(pet=pet,profesional=employee,description=description,comments=comments)
        new.save()
        
        return NewOwner(new=new)
        
class Query(graphene.ObjectType):
    employee = relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)

    owner = relay.Node.Field(OwnerNode)
    all_owners = DjangoFilterConnectionField(OwnerNode)
    
    pet = relay.Node.Field(PetNode)
    all_pets = DjangoFilterConnectionField(PetNode)

    appointment = relay.Node.Field(AppointmentNode)
    all_appointments = DjangoFilterConnectionField(AppointmentNode)
    
class Mutation(graphene.ObjectType):
    create_pet = NewPet.Field()
    
    create_owner = NewOwner.Field()
    
    create_appointment = NewAppointment.Field()
    
    create_employee = NewEmployee.Field()