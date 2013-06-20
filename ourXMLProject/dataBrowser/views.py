# general
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import *
from django.utils import *

# models
from dataBrowser.models.basic.models import *
from dataBrowser.models.json_part.models import *
from dataBrowser.models.linked_data_part.models import *
from dataBrowser.models.microdata_part.models import *
from dataBrowser.models.oai_xml_part.models import *

# further functions
from dataBrowser.scripts.oai_xml_part.functions import *
from dataBrowser.scripts.basic.functions import *





@getClientRequestData
def index(clientRequest):
    template = loader.get_template('databrowser/basic/address_form.html')
    context = Context({})
    return HttpResponse(template.render(context))



@csrf_exempt
@getClientRequestData
def open(clientRequest):
    # open URI
    uri = clientRequest.request.POST['uri']
    response = urlopen(uri)
    
    # get some response's meta information
    contentType = headers["Content-Type"]
    
    # get response body
    responseBody = response.read()
    
    # choose template according to content type
    if (contentType == "text/xml;charset=UTF-8"):
        return itIsXML(clientRequest, contentType, responseBody)
    else:
        return render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext': "Default"})



