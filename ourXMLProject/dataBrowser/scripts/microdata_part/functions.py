from django.http import HttpResponse, HttpResponseRedirect
from django.template import *
from django.template.loader import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import *
from dataBrowser.models.microdata_part.models import *
from xml.dom.minidom import *
from django.utils.html import *
from dataBrowser.scripts.basic.functions import *
from lxml import etree

import rdflib
import microdata

def itIsMicrodata(clientRequest):
    uri = clientRequest.POST['uri']
    g = rdflib.Graph()
    g.parse(uri, format="microdata")
    return g.serialize()
	
