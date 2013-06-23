from django.http import HttpResponse
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

def isOAI(root):

    #### scheme validation did not work, as there are always mistakes in the oai-repos
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
        

        
def itIsXML(clientRequest, contentType, response):

    responseBody = response.read()
    xml = parseString(responseBody)
    root = xml.documentElement
    # delete empty text nodes
    root = normalizeXML(root)
    
    # check, if it is an oai page   
    if (isOAI(root)) :
        requestElement = root.childNodes[1]
        verb = requestElement.attributes.get("verb").value
        
        text = etree.parse(open("dataBrowser/xsl/oai_xml_part/oai.xsl"))
        transform = etree.XSLT(text)
        doc = etree.XML('''\
            <root>
                <a title="AAA" name="Adam" >
                    Anfang A-Tag
                    <b name="Berta">
                        B-Tag
                    </b>
                        Mitte
                    <c name="Caesar">
                        C-Tag
                    </c>
                    Ende A-Tag
                </a>
            </root>            
        ''')
        result = transform(doc)
        return render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext': result})

        # use OAI Template according to verb
        if (verb == "Identify"):
            return render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext': "OAI"})
        elif (verb == "ListRecords") :
            metaDataPrefix = requestElement.attributes.get("metadataPrefix").value
            
            # use OAI Template according to metaDataPrefix          
            if (metaDataPrefix == "oai_dc") :
                elementListRecords = normalizeXML(root.getElementsByTagName("ListRecords")[0])
                bigNews = ""
                smallNews = ""
                
                for record in elementListRecords.childNodes:
                    title = ""
                    
                    if (len(record.getElementsByTagName("dc:title")) > 0):
                        title = record.getElementsByTagName("dc:title")[0].firstChild.nodeValue
                    
                    bigNews = bigNews + render_to_string('databrowser/oai_xml_part/bignews.html', {'title' : title})
                    smallNews = smallNews + render_to_string('databrowser/oai_xml_part/smallnews.html', {'title' : title})
                    
                #html_parser = html.parser.HTMLParser()
                print(bigNews.encode("UTF-8"))
                #bigNews = html_parser.unescape(bigNews)
                    
                return render(clientRequest.request, 'databrowser/oai_xml_part/list_records.html', {'bigNews' : bigNews.encode("UTF-8"), 'smallNews': smallNews})
            else :
                # use default OAI xslt 
                pass
        else :
            # use default OAI xslt 
            pass
    else:
        # use default xml template
        return render(clientRequest.request, 'databrowser/oai_xml_part/results.html', {'searchtext' : "XML:STANDARD" + contentType})
 
 
 
def normalizeXML(root):
    for node in root.childNodes:
        if node.nodeType == Node.TEXT_NODE:
            node.data = node.data.strip()
    root.normalize()
    return root
