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
    uri = clientRequest.request.POST['uri']
    uri = uri.replace("http://","")
    uri2 = uri.partition("/")
    print >>sys.stderr, uri2[0]  
    sparql = SPARQLWrapper("http://"+uri2[0]+"/sparql")
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label ?comment ?sameAs
    WHERE {
	 <"""+clientRequest.request.POST['uri']+"""> rdfs:label ?label.
	<"""+clientRequest.request.POST['uri']+""">  rdfs:comment ?comment.
 	<"""+clientRequest.request.POST['uri']+""">  owl:sameAs ?sameAs}""")
    sparql.setReturnFormat(XML)
    response = sparql.query()
    return response.convert().toxml()
#render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext' : "XML:STANDARD" + contentType}
    #results.print_results()

