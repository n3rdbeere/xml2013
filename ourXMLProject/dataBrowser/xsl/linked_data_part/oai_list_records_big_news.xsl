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

        <xsl:element name="div">
            <xsl:attribute name="class">lof-main-item</xsl:attribute>
    
            <xsl:element name="img">
                <xsl:attribute name="src">/databrowser/site_media/databrowser/oai_xml_part/lofslidernews/images/pdf_back_image.jpg</xsl:attribute>
                <xsl:attribute name="title">
                    <xsl:value-of select="./binding[@name='label']/literal" />
                </xsl:attribute>
                <xsl:attribute name="height">300</xsl:attribute>
                <xsl:attribute name="width">900</xsl:attribute>
            </xsl:element>

            <xsl:element name="div">
                <xsl:attribute name="class">lof-main-item-desc</xsl:attribute>
                <xsl:element name="div">
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            headline
                        </xsl:attribute>
                        Person:
                    </xsl:element>
                    <br/>
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            bodytext
                        </xsl:attribute>
                        <xsl:value-of select="./binding[@name='label']/literal" />
                    </xsl:element>
                </xsl:element>
                <xsl:element name="div">
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            headline
                        </xsl:attribute>
                        Geburtsort:
                    </xsl:element>
                    <br/>
                    <xsl:element name="a">
                        <xsl:attribute name="target">_blank</xsl:attribute>
                        <xsl:attribute name="title">
                            <xsl:value-of select="./binding[@name='label']/literal" />
                        </xsl:attribute>
                        <xsl:attribute name="href">
                            <xsl:value-of select="./binding[@name='birthPlace']/uri" />
                        </xsl:attribute>
                        <xsl:value-of select="./binding[@name='label']/literal" />
                    </xsl:element>
                </xsl:element>
                <xsl:element name="span">
                        <xsl:attribute name="class">
                            headline
                        </xsl:attribute>
                        Language:
                    </xsl:element>
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            bodytext
                        </xsl:attribute>
                        <xsl:value-of select="./binding[@name='label']/literal/@xml:lang" />
                    </xsl:element>
                </xsl:element>
                <xsl:element name="div">
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            headline
                        </xsl:attribute>
                        Geburtsort-Info:
                    </xsl:element>
                    <br/>
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            bodytext
                        </xsl:attribute>
                        <xsl:choose>
                            <xsl:when test="./binding[@name='bpcomment']/literal=''">
                                No description available.
                            </xsl:when>
                            <xsl:otherwise>
                                <xsl:value-of select="substring(./binding[@name='bpcomment']/literal, 0, 500)" />
                                [...]
                            </xsl:otherwise>   
                        </xsl:choose>
                    </xsl:element>
                </xsl:element>
            </xsl:element>
    </xsl:template>


</xsl:stylesheet>
