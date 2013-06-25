from django.http import HttpResponse
from django.template import *
from django.template.loader import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import *
from dataBrowser.models.linked_data_part.models import *
from SPARQLWrapper import SPARQLWrapper, JSON

from django.utils.html import *
# lxml
from lxml import etree

def itIsSPARQL(clientRequest, contentType, response):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <"+str(response)+"> rdfs:label ?label }")
    sparql.setReturnFormat(JSON)
    results = sparql.query()
    results.print_results()

