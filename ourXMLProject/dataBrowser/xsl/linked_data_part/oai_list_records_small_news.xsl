<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:rdfs ="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:owl = "http://www.w3.org/2002/07/owl#"
    xmlns:foaf = "http://xmlns.com/foaf/0.1/"
    xmlns:dbpedia-owl = "http://dbpedia.org/ontology/"

    exclude-result-prefixes="rdfs owl foaf dbpedia-owl"
>
    <xsl:output method="html" />

    <xsl:template match="text()|@*" />
    <xsl:template match="/processing-instruction()" />

    <!-- Record Template -->
    <xsl:template match="/sparql/results/result">

        <xsl:element name="li">
            <xsl:element name="div">
                <xsl:element name="img">
                    <xsl:attribute name="src">/databrowser/site_media/databrowser/oai_xml_part/lofslidernews/images/lofthumbs/pdf_small.jpg</xsl:attribute>
                    <xsl:attribute name="title"><xsl:value-of select="./binding[@name='label']/literal" /></xsl:attribute>
                </xsl:element>
                <xsl:element name="h3">
                    <!--<xsl:value-of select="./oai:metadata/oai_dc:dc/dc:title" />-->
                </xsl:element>
                <xsl:element name="span">
                    <xsl:attribute name="class">smallNewsHeadline</xsl:attribute>
                    A:
                </xsl:element>
                <xsl:element name="span">
                    <xsl:attribute name="class">smallNews</xsl:attribute>
                    <xsl:value-of select="substring(./binding[@name='label']/literal, 0, 50)" />[...]
                </xsl:element><br /><br />
<xsl:element name="span">
                    <xsl:attribute name="class">smallNewsHeadline</xsl:attribute>
                    T:
                </xsl:element>
                <xsl:element name="span">
                    <xsl:attribute name="class">smallNews</xsl:attribute>
                    <xsl:value-of select="substring(./binding[@name='label']/literal, 0, 50)" />[...]
                </xsl:element>
            </xsl:element>
        </xsl:element>

    </xsl:template>

</xsl:stylesheet>
