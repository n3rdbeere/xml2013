# general
import sys
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import *
from django.utils import *
from xml.dom.minidom import *

# models
from dataBrowser.models.basic.models import *
from dataBrowser.models.json_part.models import *
from dataBrowser.models.linked_data_part.models import *
from dataBrowser.models.microdata_part.models import *
from dataBrowser.models.oai_xml_part.models import *

# further functions
from dataBrowser.scripts.oai_xml_part.functions import *
from dataBrowser.scripts.linked_data_part.functions import *
from dataBrowser.scripts.basic.functions import *

# lxml
from lxml import etree



@getClientRequestData
def index(clientRequest):
    template = loader.get_template('databrowser/basic/address_form.html')
    context = Context({})
    return HttpResponse(template.render(context))

@csrf_exempt
@getClientRequestData
def openUri(clientRequest):
    # open URI
    uri = clientRequest.request.POST['uri']
    response = urlopen(uri)

    # get some response's meta information
    headers = response.info()
    contentType = headers["Content-Type"]
    print >> sys.stderr, contentType
    # choose template according to content type
    if (contentType == "text/xml;charset=UTF-8"):
        return itIsXML(clientRequest, contentType, response)
    elif(contentType == "text/html; charset=UTF-8"):
         #result = "default"
         return itIsSPARQL(clientRequest, contentType, response)
	 #return render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext': uri,'searchresult' : result})
	
