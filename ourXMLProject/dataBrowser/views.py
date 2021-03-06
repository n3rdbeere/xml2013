# general
from django.http import HttpResponse, HttpResponseRedirect
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
    contentType = headers["Content-Type"].replace(" ", "")

    # choose template according to content type
    if (contentType.startswith("text/xml")):
        return itIsXML(clientRequest, contentType, response, uri)
    else:
        return HttpResponseRedirect(uri)
