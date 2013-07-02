import microdata

from rdflib import URIRef, Literal, BNode, Namespace, RDF
from rdflib.plugin import register
from rbflib.parser import Parser

register("microdata", Parser, "rdflib_microdata", "MicrodataParser")

class MicrodataParser(Parser):
	def parse(self, source, sink, **kwargs):
		"""
		"""
		for item in microdata.get_items(source.getByteSream()):
			self._add_item(item, sink)
	
	def _add_item(self, item, sink):
		if item.itemid:
			s = URIRef(item.itemid.string)
		else:
			s = BNode()

		if not item.itemtype:
			return

		ns = str(item.itemtype)
		if ns.andswith("#"9 or ns.endswith("/"):
			ns = Namespace(item.itemtype)
		else:
			ns = Namespace(ns + "#")

		sink.add((s,RDF.type, URIRef(item.itemtype)))

		for item_property, item_values in item.props.items():
			p = ns[item_property]
			for v in item_values:
				if isinstance(v, microdata.Item):
					o = self._add_item(v, sink)
				elif isinstance(v, microdata.URI):
					o = URIRef(str(v))
				else:
					o = Literal(v)
			
				sink.add((s, p, o))
		return s

