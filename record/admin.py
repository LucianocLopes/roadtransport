from django.contrib import admin

from .models import Business, Person


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    '''Admin View for Business'''

    list_display = ('id','name', 'fantasy_name', 'cnpj_number', 'create_by', 'create', 'modified')
    exclude = ('create_by','record_type')

    def save_model(self,request,obj,form,change):
        obj.create_by = request.user
        obj.record_type = 'B'
        obj.save()


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''

    list_display = ('id','first_name', 'last_name', 'cpf_number', 'create_by', 'create', 'modified')
    exclude = ('create_by','record_type')

    def save_model(self,request,obj,form,change):
        obj.create_by = request.user
        obj.record_type = 'P'
        obj.save()