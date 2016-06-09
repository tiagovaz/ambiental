# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#### ADDRESS #########

@python_2_unicode_compatible
class Neighborhood(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=150
    )

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=150
    )

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=150
    )

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(
        verbose_name="Nome",
        max_length=150
    )

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Address(models.Model):
    """
    Address for organization, persons and properties
    """
    number = models.CharField(
        verbose_name="Número",
        max_length=10
    )

    street = models.CharField(
        verbose_name="Rua",
        max_length=50
    )

    complement = models.CharField(
        verbose_name="Complemento",
        max_length=150,
        blank=True
    )

    postal_code = models.CharField(
        verbose_name="CEP",
        max_length=10,
        blank=True
    )

    neighborhood = models.ForeignKey(
        'Neighborhood',
        verbose_name="Bairro"
    )

    city = models.ForeignKey(
        'City',
        verbose_name="Cidade",
        default=1
    )

    state = models.ForeignKey(
        'State',
        verbose_name="Estado",
        default=1
    )

    country = models.ForeignKey(
        'Country',
        verbose_name="País",
        default=1
    )

    longitude = models.FloatField(
        verbose_name="Longitude",
        null=True,
        blank=True
    )

    latitude = models.FloatField(
        verbose_name="Latitude",
        null=True,
        blank=True
    )

    def get_full_address_html(self):
        return u"%s, %s, %s <br> %s %s" % \
               (self.street, self.number, self.city, self.state, self.postal_code)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return u"%s %s, %s" % \
               (self.number, self.street, self.city)

######## END ADDRESS ###########

@python_2_unicode_compatible
class Company(models.Model):
    """The main class for Ambiental."""
    cnpj = models.CharField("CNPJ", max_length=200)
    civil_name = models.CharField("Razão social", blank=True, max_length=200)
    commercial_name = models.CharField('Nome fantasia', null=True, blank=True, max_length=200)
    phone_main = models.CharField("Telefone 1", max_length=50)
    phone_secondary = models.CharField("Telefone 2", max_length=50)
    whatsapp = models.CharField("Whatsapp", max_length=50)
    logo = models.ImageField(upload_to = 'logos', null=True, blank=True, verbose_name='Logomarca')
    contact_person = models.CharField("Contato", max_length=200)
    email = models.EmailField("Email", max_length=254)
    website = models.CharField("Website", max_length=254)
    twitter = models.CharField("Twitter", max_length=254)
    facebook = models.CharField("Facebook", max_length=254)
    partnership = models.ManyToManyField("Partnership", verbose_name="Parceria")
    address = models.ForeignKey("Address", verbose_name="Endereço")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.commercial_name

@python_2_unicode_compatible
class Partnership(models.Model):
    description = models.CharField("Tipo de parceria", max_length=200)
    start_date = models.DateField()

    class Meta:
        verbose_name = "Parceria"
        verbose_name_plural = "Parcerias"

    def __str__(self):
        return self.description

class EquipmentType(models.Model):
    description = models.CharField(
        verbose_name="Descrição",
        max_length=500
    )

    class Meta:
        verbose_name = "Tipo de equipamento"

    def __str__(self):
        return self.description

class Inventary(models.Model):
    type = models.ForeignKey("EquipmentType",
        verbose_name="Tipo de equipamento"
    )

    local = models.ForeignKey("Company",
                             verbose_name="Local"
                             )
    quantity = models.IntegerField(
        verbose_name="Quantidade",
    )

    deliverd_date = models.DateField("Data de entrega")
    return_date = models.DateField("Data de retorno")

    class Meta:
        verbose_name = "Inventário"

    def __str__(self):
        return "%s %s em %s" % (self.quantity, self.type, self.local)

class Trip(models.Model):
    start_date = models.DateTimeField("Data/hora de saída")
    end_date = models.DateTimeField("Data/hora de chegada")
    distance_travelled = models.FloatField("Deslocamento")
    distance_unity = models.ForeignKey("Unity",
                             verbose_name="Unidade"
                             )
    class Meta:
        verbose_name = "Deslocamento"

    def __str__(self):
        return u"Deslocamento de %f (%s) em %s h com saida as %s" % (self.distance_travelled, self.distance_unity, (self.end_date-self.start_date), self.start_date)

class Unity(models.Model):
    name = models.CharField("Nome", max_length=20)
    abreviation = models.CharField("Abreviação", max_length=10)

    class Meta:
        verbose_name = "Unidade de medida"

    def __str__(self):
        return self.name

class Collect(models.Model):
    trip = models.ForeignKey("Trip",
        verbose_name="Deslocamento"
    )
    date = models.DateField("Data")
    partner = models.ForeignKey("Company",
                             verbose_name="Parceiro"
                             )
    quantity = models.FloatField(
        verbose_name="Quantidade",
    )
    collect_unity = models.ForeignKey("Unity",
                                       verbose_name="Unidade"
                                       )
    class Meta:
        verbose_name = "Coleta"

    def __str__(self):
        return "Coleta de %f (%s) de %s em %s" % (self.quantity, self.collect_unity.abreviation, self.partner, self.date)

class Sell(models.Model):
    trip = models.ForeignKey("Trip",
        verbose_name="Deslocamento"
    )
    date = models.DateField("Data")
    partner = models.ForeignKey("Company",
                             verbose_name="Parceiro"
                             )
    quantity = models.FloatField(
        verbose_name="Quantidade",
    )
    sell_unity = models.ForeignKey("Unity",
                                       verbose_name="Unidade"
                                       )
    class Meta:
        verbose_name = "Venda"

    def __str__(self):
        return "Venda de %f (%s) para %s em %s" % (self.quantity, self.collect_unity.abreviation, self.date)