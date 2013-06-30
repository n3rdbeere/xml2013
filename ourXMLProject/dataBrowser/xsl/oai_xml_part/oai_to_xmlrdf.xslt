<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:oai="http://www.openarchives.org/OAI/2.0/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
    exclude-result-prefixes=""
>
	<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="text()|@*" />
    <xsl:template match="/processing-instruction()" />
	
	<!--
		Entry Template
	-->
	<xsl:template match="/">	
		<rdf:RDF 
			xmlns="http://www.openarchives.org/OAI/2.0/"			
			xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
			xmlns:dc="http://purl.org/dc/elements/1.1/"
			xmlns:oai="http://www.openarchives.org/OAI/2.0/"
			xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
			xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
			<xsl:apply-templates/>
		</rdf:RDF>
	</xsl:template>
	
	<!--
		Main OAI Template with general information and list of records
	-->
	<xsl:template match="oai:OAI-PMH">
		<xsl:element name="rdf:Description">
			<xsl:attribute name="rdf:about">
				<xsl:value-of select="oai:request"/>?verb=<xsl:value-of select="oai:request/@verb"/>&amp;metadataPrefix=<xsl:value-of select="oai:request/@metadataPrefix"/>
			</xsl:attribute>
			
			<!-- other fancy stuff possible-->
			<xsl:element name="oai:responseDate">
				<xsl:value-of select="oai:responseDate"/>
			</xsl:element>
			<xsl:element name="oai:verb">
				<xsl:value-of select="oai:request/@verb"/>
			</xsl:element>
			<xsl:element name="oai:metadataPrefix">
				<xsl:value-of select="oai:request/@metadataPrefix"/>
			</xsl:element>
			
			<!-- Records of this resource -->
			<xsl:for-each select="oai:ListRecords/oai:record">
				<xsl:element name="oai:record">
					<xsl:attribute name="rdf:resource">
						<xsl:value-of select="oai:header/oai:identifier"/>
					</xsl:attribute>
				</xsl:element>
			</xsl:for-each>
		</xsl:element>
		
		<xsl:apply-templates select="oai:ListRecords" />
	</xsl:template>
	
	<!--
		OAI record template
	-->
	<xsl:template match="oai:record" >
		<xsl:element name="rdf:Description">
			<xsl:attribute name="rdf:about">
				<xsl:value-of select="oai:header/oai:identifier"/>
			</xsl:attribute>
			<xsl:for-each select="oai:metadata/oai_dc:dc/*">
				<xsl:copy>
					<xsl:value-of select="."/>
				</xsl:copy>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	
</xsl:stylesheet>
