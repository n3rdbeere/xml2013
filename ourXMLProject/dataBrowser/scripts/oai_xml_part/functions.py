from django.http import HttpResponse, HttpResponseRedirect
from django.template import *
from django.template.loader import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from urllib import *
from dataBrowser.models.oai_xml_part.models import *
from xml.dom.minidom import *
from django.utils.html import *
# lxml
from lxml import etree
from dataBrowser.scripts.basic.functions import *

# check, whether response xml is oai xml
def isOAI(root):

    #### scheme validation did not work, as there seem to be always mistakes in the oai-repos
    #response = urlopen("http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd")
    #responseBody = response.read()
    #xmlSchemaDoc = etree.fromstring(responseBody)
    #xmlSchema = etree.XMLSchema(xmlSchemaDoc)
 
    #xmlDoc = etree.fromstring(xmlResponseBody)
    #return xmlSchema.validate(xmlDoc))
    
    #### weaker but sufficient validation via elements of root
    if (root.nodeName == "OAI-PMH"):
        if ((root.childNodes[0].nodeName == "responseDate") and (root.childNodes[1].nodeName == "request")):
            return (True)
        else:
            return (False)
    else:
        return (False)
        

# process xml
def itIsXML(clientRequest, contentType, response, uri):

    responseBody = response.read()
    xml = parseString(responseBody)
    root = xml.documentElement
    # delete empty text nodes
    root = normalizeXML(root)
    
    # check, if it is an oai page   
    if (isOAI(root)) :
        requestElement = root.childNodes[1]
        verb = requestElement.attributes.get("verb").value
        xmlDoc = etree.XML(responseBody)

        # use OAI Template according to verb
        if (verb == "ListRecords"):
            metaDataPrefix = requestElement.attributes.get("metadataPrefix").value
            
            # use OAI Template according to metaDataPrefix          
            if (metaDataPrefix == "oai_dc") :
                # generate rdf xml
                rdfXSL = etree.parse(open("dataBrowser/xsl/oai_xml_part/oai_to_xmlrdf.xslt"))
                rdfTransform = etree.XSLT(rdfXSL)
                rdf = rdfTransform(xmlDoc)
                save_xmlrdf_to_virtuoso(rdf)

                bigNews = ""
                smallNews = ""
                bigNewsXSL = etree.parse(open("dataBrowser/xsl/oai_xml_part/oai_list_records_big_news.xsl"))
                smallNewsXSL = etree.parse(open("dataBrowser/xsl/oai_xml_part/oai_list_records_small_news.xsl"))
                bigNewsTransform = etree.XSLT(bigNewsXSL)
                smallNewsTransform = etree.XSLT(smallNewsXSL)
                bigNews = bigNewsTransform(xmlDoc)
                smallNews = smallNewsTransform(xmlDoc)                    
                return render(clientRequest.request, 'databrowser/oai_xml_part/list_records.html', {'bigNews' : bigNews, 'smallNews': smallNews})
            else :
                # http redirect
                return HttpResponseRedirect(uri)
        else :
            # http redirect
            return HttpResponseRedirect(uri)
    else:
        # http redirect
        return HttpResponseRedirect(uri)        
        # return render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext' : "XML:STANDARD" + contentType})
 
 
# delete empty text nodes of parameter node
def normalizeXML(root):
    for node in root.childNodes:
        if node.nodeType == Node.TEXT_NODE:
            node.data = node.data.strip()
    root.normalize()
    return root
