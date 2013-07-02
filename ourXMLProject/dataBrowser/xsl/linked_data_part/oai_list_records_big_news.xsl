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

        <xsl:element name="div">
            <xsl:attribute name="class">lof-main-item</xsl:attribute>
    
            <xsl:element name="img">
                <xsl:attribute name="src">/databrowser/site_media/databrowser/oai_xml_part/lofslidernews/images/pdf_back_image.jpg</xsl:attribute>
                <xsl:attribute name="title">
                    <xsl:value-of select="./sp:binding[@name='label']/sp:literal" />
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
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            bodytext
                        </xsl:attribute>
			<xsl:element name="a">
                        <xsl:attribute name="target">_blank</xsl:attribute>
                        <xsl:attribute name="title">
                            <xsl:value-of select="./sp:binding[@name='lable']/sp:literal" />
                        </xsl:attribute>
                        <xsl:attribute name="href">
                            <xsl:value-of select="./sp:binding[@name='primaryTopic']/sp:uri" />
                        </xsl:attribute>
                        <xsl:value-of select="./sp:binding[@name='label']/sp:literal" />
                    </xsl:element>
		     <br/>
                        <xsl:value-of select="./sp:binding[@name='comment']/sp:literal" />
		                    </xsl:element>
                </xsl:element>
                <xsl:element name="div">
                    <xsl:element name="span">
                        <xsl:attribute name="class">
                            headline
                        </xsl:attribute>
                        Birth place:
                    </xsl:element>
                    <xsl:element name="a">
                        <xsl:attribute name="target">_blank</xsl:attribute>
                        <xsl:attribute name="title">
                            <xsl:value-of select="./sp:binding[@name='bplable']/sp:literal" />
                        </xsl:attribute>
                        <xsl:attribute name="href">
                            <xsl:value-of select="./sp:binding[@name='birthPlace']/sp:uri" />
                        </xsl:attribute>
                        <xsl:value-of select="./sp:binding[@name='bplable']/sp:literal" />
                    </xsl:element>
		 <br/>
		<xsl:element name="span">
                        <xsl:attribute name="class">
                            bodytext
                        </xsl:attribute>
                        <xsl:value-of select="./sp:binding[@name='bpcomment']/sp:literal" />       
                    </xsl:element>
                </xsl:element>
		 <xsl:element name="div">
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
                        <xsl:value-of select="./sp:binding[@name='label']/sp:literal/@xml:lang" />
                    </xsl:element>
                  </xsl:element>
                </xsl:element>
            </xsl:element>
    </xsl:template>


</xsl:stylesheet>
