# -*- coding: utf-8 -*-
from scrapy.item import Item, Field

class Atracao(Item):
    cidade = Field()
    lugar = Field()
    dia = Field()
    hora = Field()
    artista = Field()
