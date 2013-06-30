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

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def itIsSPARQL(clientRequest, contentType, response):
    print >>sys.stderr,clientRequest.request.POST['uri']
    uri = clientRequest.request.POST['uri']
    uri = uri.replace("http://","")
    uri2 = uri.partition("/")
    print >>sys.stderr, uri2[0]  
    sparql = SPARQLWrapper("http://"+uri2[0]+"/sparql")
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    SELECT ?label ?comment ?sameAs ?primaryTopic ?birthPlace
    WHERE {
	<"""+clientRequest.request.POST['uri']+"""> rdfs:label ?label.
 	<"""+clientRequest.request.POST['uri']+"""> owl:sameAs ?sameAs.
	<"""+clientRequest.request.POST['uri']+"""> rdfs:comment ?comment.
	<"""+clientRequest.request.POST['uri']+"""> foaf:isPrimaryTopicOf ?primaryTopic.	
	<"""+clientRequest.request.POST['uri']+"""> dbpedia-owl:birthPlace ?birthPlace.
}""")
    sparql.setReturnFormat(XML)
    response = sparql.query()
    dom = response.convert()
    bindingElements = dom.getElementsByTagName("binding")
    birthPlaceURL =""
    for elem in bindingElements:
#	if elem.hasAttribute("name")
	if elem.getAttribute("name") == "birthPlace":
	       	birthPlaceURL = elem.getElementsByTagName("uri")[0].childNodes[0].data
		break
    sparql = SPARQLWrapper("http://"+uri2[0]+"/sparql")
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label ?comment ?sameAs ?primaryTopic ?birthPlace
    WHERE {
	<"""+birthPlaceURL+"""> rdfs:comment ?comment.
    }""")
    sparql.setReturnFormat(XML)
    response2 = sparql.query()
    xmlString = dom.toprettyxml()
  #  test = etree.XML(xmlString)
   
    return dom.toprettyxml()

#render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext' : "XML:STANDARD" + contentType}
    #results.print_results()
#PREFIX foaf: <http://xmlns.com/foaf/0.1/>
#    PREFIX  owl: <http://www.w3.org/2002/07/owl> 

