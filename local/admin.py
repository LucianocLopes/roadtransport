from django.contrib import admin

from .models import Country, City, State, Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    '''Admin View for Address'''

    list_display = ('address','district', 'city', 'zip_code','create', 'create_by', 'modified')
    exclude = ('create_by',)

    def save_model(self,request,obj,form,change):
        obj.create_by = request.user
        obj.save()

class AddressInline(admin.TabularInline):
    '''Tabular Inline View for Address'''

    model = Address
    exclude = ('create_by',)
    ordering = ('zip_code',)
    min_num = 1
    max_num = 0
    extra = 1



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    '''Admin View for City'''

    list_display = ('name','state', 'create', 'create_by', 'modified')
    inlines = [
        AddressInline,
    ]
    exclude = ('create_by',)

    def save_model(self,request,obj,form,change):
        obj.create_by = request.user
        obj.save()

class CityInline(admin.TabularInline):
    '''Tabular Inline View for City'''

    model = City
    exclude = ('create_by',)
    ordering = ('name',)
    min_num = 1
    max_num = 0
    extra = 1


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    '''Admin View for State'''

    list_display = ('name','country', 'create', 'create_by', 'modified')
    inlines = [
        CityInline,
    ]
    exclude = ('create_by',)

    def save_model(self,request,obj,form,change):
        obj.create_by = request.user
        obj.save()

class StateInline(admin.TabularInline):
    '''Tabular Inline View for City'''

    model = State
    exclude = ('create_by',)
    ordering = ('name',)
    min_num = 1
    max_num = 0
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    '''Admin View for Country'''

    list_display = ('name','create', 'create_by', 'modified')
    inlines = [
        StateInline,
    ]
    exclude = ('create_by',)

    def save_model(self,request,obj,form,change):
        obj.create_by = request.user
        obj.save()

