<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="a" name="test">
        <xsl:value-of select="./@name" />
    </xsl:template>

    <xsl:template match="//a">
        <xsl:call-template name="test" />
    </xsl:template>

</xsl:stylesheet>
