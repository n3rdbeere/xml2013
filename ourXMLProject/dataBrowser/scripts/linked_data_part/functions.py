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
from SPARQLWrapper import SPARQLWrapper, XML, RDF
from dataBrowser.scripts.basic.functions import *
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
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    SELECT DISTINCT ?label ?comment ?primaryTopic ?birthPlace ?bpcomment ?bplable
    WHERE {
	<"""+clientRequest.request.POST['uri']+"""> rdfs:label ?label.
	<"""+clientRequest.request.POST['uri']+"""> rdfs:comment ?comment.
	<"""+clientRequest.request.POST['uri']+"""> foaf:isPrimaryTopicOf ?primaryTopic.
        <"""+clientRequest.request.POST['uri']+"""> dbpedia-owl:birthPlace ?birthPlace.	
	OPTIONAL{?birthPlace rdfs:label ?bplable}.
        OPTIONAL{?birthPlace rdfs:comment ?bpcomment}.
}""")
    sparql.setReturnFormat(XML)
    response = sparql.query()
    #print >> sys.stderr,"query finished"
    dom = response.convert()
    sparql.setReturnFormat(RDF)
    results = sparql.query().convert()
    print sys.stderr,save_xmlrdf_to_virtuoso(results.serialize())
    xmlString = dom.toprettyxml()
    #print >> sys.stderr,xmlString
    xmlDoc = etree.XML(xmlString)
    bigNews = ""
    smallNews = ""
    bigNewsXSL = etree.parse(open("dataBrowser/xsl/linked_data_part/oai_list_records_big_news.xsl"))
    smallNewsXSL = etree.parse(open("dataBrowser/xsl/linked_data_part/oai_list_records_small_news.xsl"))
    bigNewsTransform = etree.XSLT(bigNewsXSL)
    smallNewsTransform = etree.XSLT(smallNewsXSL)
    bigNews = bigNewsTransform(xmlDoc)
#    print >>sys.stderr,bigNews
    smallNews = smallNewsTransform(xmlDoc)                    
    return render(clientRequest.request, 'databrowser/linked_data_part/list_records.html', {'bigNews' : bigNews, 'smallNews': smallNews})

