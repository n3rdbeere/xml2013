#from dataBrowser.models.basic.models import *
from rdflib.store import Store
from rdflib.plugin import get as plugin
from rdflib import Graph, store
from rdflib import Namespace, Literal

from virtuoso import virtuoso
from virtuoso.virtuoso import Virtuoso

import logging
from rdflib.plugins.stores import sparqlstore
from rdflib.plugins import stores
import rdflib
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

# wrapper function in order to be able to read some necessary data from request
def getClientRequestData(viewFunction):
    def wrapper(request):
        clientRequest = ClientRequest(request)
        return viewFunction(clientRequest)
    return wrapper


def save_xmlrdf_to_virtuoso(xmlrdf=None,graphIRI=None):
    ''' Function to save data in XML/RDF format into the Virtuoso triplestore.
        If the data should be saved in a named graph, provide a String for the
        graph-name to graphIRI, otherwise data will be saved in the default graph
        
        Returns 0 on failure, 1 on success
    '''
    if(xmlrdf is None):
        #Nothing to add
        return 0
    
    triplestore = Virtuoso("localhost", "dba","dba", 8890, "/sparql")
    g =  rdflib.Graph()
    g.parse(data=xmlrdf, format="xml")

    graph = graphIRI

    for triple in g.triples((None, None, None)):
        triplestore.insert(graph,triple[0],triple[1],triple[2])

    return 1

def query_virtuoso(query = None, graph=None, output="ResultSet", printQuery = False):
    ''' Function to query for data from the Virtuoso triplestore.
        If only a specific graph should be searched, use the graph
        variable to specify the graph-name.
        If more then one graph should be used, it might be better to 
        directly name them in the query.
        
        Returns a result set which is to be used like in this example:
        
        resultset = query_virtuoso('SELECT DISTINCT * WHERE { ?s ?p "Juan" . }')
        for resultRow in resultset:
            print("%s has %s" % (resultRow["s"].value, resultRow["p"].value))
    '''
    if(query is None):
       return None # no query, no result 
    if(graph is not None):
        pos = query.lower().find('where')
        query   = query[0:pos] + " FROM <" + graph + "> " + query[pos:]
        
    triplestore = Virtuoso("localhost", "dba","dba", 8890, "/sparql")
    result = triplestore.endpoint.query(query = query, output = output)
    
    if (printQuery):
        print query
        
    return result
    

def delete_graph_virtuoso(graphIRI=None):
    ''' Method to delete the named graph graphIRI  from the Virtuoso triplestore.
        The default graph cannot be deleted with this function.
    '''
    triplestore = Virtuoso("localhost", "dba","dba", 8890, "/sparql")
    if graphIRI is None:
        #nothing to do, return
        return
    
    triplestore.isql.clean_graph(url)

def virtuosotest():
    """ Method for testing basic virtuoso connectivity 
    """
    triplestore = Virtuoso("localhost", "dba","dba", 8890, "/sparql")
    
    results = triplestore.endpoint.query("SELECT * WHERE {?s ?p ?o} LIMIT 5")
       
    graph = "http://my-graph"
    ns = Namespace("http://my-name-space.com/#")
    
    #Insert a triple into the triplestore
    # <http://my-name-space.com/#user123> <http://my-name-space.com/#user123> "Juan"
    triplestore.insert(graph, ns["user123"], ns["name"], Literal("Juan"))
    
    #Deleting the triple just inserted
    triplestore.delete(graph, ns["user123"], ns["name"], Literal("Juan"))
    
    #Clean the whole graph (cant use triplestore.clean as there's a typo in the wrapper..)
    triplestore.isql.clean_graph(graph)
    
if __name__ == '__main__':
    name_of_file = "dontupload2.xml"
    stringoffile = ""
    with open(name_of_file) as f:
        stringoffile = f.read()
        
    logging.basicConfig()
    print("Simple RDF storage test\nReading from %s..."% name_of_file)
    save_xmlrdf_to_virtuoso(stringoffile)
    resultset = query_virtuoso('SELECT * WHERE { ?s ?p "Juan" . }', printQuery=True)
    for resultRow in resultset:
        print("%s has %s" % (resultRow["s"].value, resultRow["p"].value))
