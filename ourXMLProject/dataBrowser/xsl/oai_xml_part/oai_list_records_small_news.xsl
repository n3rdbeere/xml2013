<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:oai="http://www.openarchives.org/OAI/2.0/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:oai_dc="http://www.openarchives.org/OAI/2.0/oai_dc/"
    exclude-result-prefixes="oai dc oai_dc"
>
    <xsl:output method="html" />

    <xsl:template match="text()|@*" />
    <xsl:template match="/processing-instruction()" />

    <!-- Record Template -->
    <xsl:template match="/oai:OAI-PMH/oai:ListRecords/oai:record">

        <xsl:element name="li">
            <xsl:element name="div">
                <xsl:element name="img">
                    <xsl:attribute name="src">/databrowser/site_media/databrowser/oai_xml_part/lofslidernews/images/lofthumbs/pdf_small.jpg</xsl:attribute>
                    <xsl:attribute name="title"><xsl:value-of select="./oai:metadata/oai_dc:dc/dc:title" /></xsl:attribute>
                </xsl:element>
                <xsl:element name="h3">
                    <!--<xsl:value-of select="./oai:metadata/oai_dc:dc/dc:title" />-->
                </xsl:element>
                <xsl:element name="span">
                    <xsl:value-of select="./oai:metadata/oai_dc:dc/dc:creator" /><br />
                    <xsl:value-of select="./oai:metadata/oai_dc:dc/dc:title" />
                </xsl:element>
            </xsl:element>
        </xsl:element>

    </xsl:template>

</xsl:stylesheet>
