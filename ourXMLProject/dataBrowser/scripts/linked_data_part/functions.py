#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from django.http import HttpResponse
from django.template import *
from django.template.loader import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import *
from dataBrowser.models.linked_data_part.models import *
from SPARQLWrapper import SPARQLWrapper, XML

from django.utils.html import *
# lxml
from lxml import etree

def itIsSPARQL(clientRequest, contentType, response):
    print >>sys.stderr,clientRequest.request.POST['uri']
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <"""+clientRequest.request.POST['uri']+"""> rdfs:label ?label }""")
    sparql.setReturnFormat(XML)
    response = sparql.query()
    return response.convert().toxml()
#render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext' : "XML:STANDARD" + contentType}
    #results.print_results()

