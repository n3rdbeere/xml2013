<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:sp="http://www.w3.org/2005/sparql-results#" 
>
    <xsl:output method="html" />

    <xsl:template match="text()|@*" />
    <xsl:template match="/processing-instruction()" />

    <!-- Record Template -->
    <xsl:template match="/sp:sparql/sp:results/sp:result">

        <xsl:element name="li">
            <xsl:element name="div">
                <xsl:element name="img">
                    <xsl:attribute name="src">/databrowser/site_media/databrowser/linked_data_part/lofslidernews/images/lofthumbs/pdf_small.jpg</xsl:attribute>
                    <xsl:attribute name="title"><xsl:value-of select="./sp:binding[@name='label']/sp:literal" /></xsl:attribute>
                </xsl:element>
                <xsl:element name="h3">
                    <!--<xsl:value-of select="./oai:metadata/oai_dc:dc/dc:title" />-->
                </xsl:element>
                <xsl:element name="span">
                    <xsl:attribute name="class">smallNewsHeadline</xsl:attribute>
		    Person:
                </xsl:element>
                <xsl:element name="span">
                    <xsl:attribute name="class">smallNews</xsl:attribute>
                    <xsl:value-of select="./sp:binding[@name='label']/sp:literal" />
                </xsl:element><br/><br/>
		<xsl:element name="span">
                    <xsl:attribute name="class">smallNewsHeadline</xsl:attribute>
                    Language:
                </xsl:element>
                <xsl:element name="span">
                    <xsl:attribute name="class">smallNews</xsl:attribute>
                    <xsl:value-of select="./sp:binding[@name='label']/sp:literal/@xml:lang" />
                </xsl:element>
            </xsl:element>
        </xsl:element>

    </xsl:template>

</xsl:stylesheet>
