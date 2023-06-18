from django.contrib import admin
from .models import form_1, form_2, form_3,form_5, verification0

# Register your models here.
@admin.register(form_1)      #    Pour enregistrer le form ici


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'number', 'age', 'state')


# Register your models here.
@admin.register(form_2)      #    Pour enregistrer le form ici


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'state')

# Register your models here.
@admin.register(form_3)      #    Pour enregistrer le form ici


class UserAdmin(admin.ModelAdmin):
    list_display = ('jour', 'nom', 'sept_heure', 'huit_heure', 'neuf_heure', 'dix_heure', 'onze_heure', 'douze_heure', 'treize_heure', 'quatorze_heure', 'quinze_heure', 'seize_heure', 'dix_sept_heure', 'dix_huit_heure', 'dix_neuf_heure')

# Register your models here.
@admin.register(form_5)      #    Pour enregistrer le form ici


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'occupate')


# Register your models here.
@admin.register(verification0)      #    Pour enregistrer le form ici


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'jour_choisi',)
