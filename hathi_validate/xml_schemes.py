import os
import pkgutil

MARC_XSD = r"""<?xml version="1.0"?>
<xsd:schema targetNamespace="http://www.loc.gov/MARC21/slim" xmlns="http://www.loc.gov/MARC21/slim" xmlns:xsd="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified" version="1.1" xml:lang="en">
  <xsd:annotation>
    <xsd:documentation>
			MARCXML: The MARC 21 XML Schema
			Prepared by Corey Keith
			
				May 21, 2002 - Version 1.0  - Initial Release

**********************************************
Changes.

August 4, 2003 - Version 1.1 - 
Removed import of xml namespace and the use of xml:space="preserve" attributes on the leader and controlfields. 
                    Whitespace preservation in these subfields is accomplished by the use of xsd:whiteSpace value="preserve"

May 21, 2009  - Version 1.2 - 
in subfieldcodeDataType  the pattern 
                          "[\da-z!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?{}_^`~\[\]\\]{1}"
	changed to:	
                         "[\dA-Za-z!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?{}_^`~\[\]\\]{1}"
    i.e "A-Z" added after "[\d" before "a-z"  to allow upper case.  This change is for consistency with the documentation.
	
************************************************************
			This schema supports XML markup of MARC21 records as specified in the MARC documentation (see www.loc.gov).  It allows tags with
			alphabetics and subfield codes that are symbols, neither of which are as yet used in  the MARC 21 communications formats, but are 
			allowed by MARC 21 for local data.  The schema accommodates all types of MARC 21 records: bibliographic, holdings, bibliographic 
			with embedded holdings, authority, classification, and community information.
		</xsd:documentation>
  </xsd:annotation>
  <xsd:element name="record" type="recordType" nillable="true" id="record.e">
    <xsd:annotation>
      <xsd:documentation>record is a top level container element for all of the field elements which compose the record</xsd:documentation>
    </xsd:annotation>
  </xsd:element>
  <xsd:element name="collection" type="collectionType" nillable="true" id="collection.e">
    <xsd:annotation>
      <xsd:documentation>collection is a top level container element for 0 or many records</xsd:documentation>
    </xsd:annotation>
  </xsd:element>
  <xsd:complexType name="collectionType" id="collection.ct">
    <xsd:sequence minOccurs="0" maxOccurs="unbounded">
      <xsd:element ref="record"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idDataType" use="optional"/>
  </xsd:complexType>
  <xsd:complexType name="recordType" id="record.ct">
    <xsd:sequence minOccurs="0">
      <xsd:element name="leader" type="leaderFieldType"/>
      <xsd:element name="controlfield" type="controlFieldType" minOccurs="0" maxOccurs="unbounded"/>
      <xsd:element name="datafield" type="dataFieldType" minOccurs="0" maxOccurs="unbounded"/>
    </xsd:sequence>
    <xsd:attribute name="type" type="recordTypeType" use="optional"/>
    <xsd:attribute name="id" type="idDataType" use="optional"/>
  </xsd:complexType>
  <xsd:simpleType name="recordTypeType" id="type.st">
    <xsd:restriction base="xsd:NMTOKEN">
      <xsd:enumeration value="Bibliographic"/>
      <xsd:enumeration value="Authority"/>
      <xsd:enumeration value="Holdings"/>
      <xsd:enumeration value="Classification"/>
      <xsd:enumeration value="Community"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:complexType name="leaderFieldType" id="leader.ct">
    <xsd:annotation>
      <xsd:documentation>MARC21 Leader, 24 bytes</xsd:documentation>
    </xsd:annotation>
    <xsd:simpleContent>
      <xsd:extension base="leaderDataType">
        <xsd:attribute name="id" type="idDataType" use="optional"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>
  <xsd:simpleType name="leaderDataType" id="leader.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
      <xsd:pattern value="[\d ]{5}[\dA-Za-z ]{1}[\dA-Za-z]{1}[\dA-Za-z ]{3}(2| )(2| )[\d ]{5}[\dA-Za-z ]{3}(4500|    )"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:complexType name="controlFieldType" id="controlfield.ct">
    <xsd:annotation>
      <xsd:documentation>MARC21 Fields 001-009</xsd:documentation>
    </xsd:annotation>
    <xsd:simpleContent>
      <xsd:extension base="controlDataType">
        <xsd:attribute name="id" type="idDataType" use="optional"/>
        <xsd:attribute name="tag" type="controltagDataType" use="required"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>
  <xsd:simpleType name="controlDataType" id="controlfield.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="controltagDataType" id="controltag.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
      <xsd:pattern value="00[1-9A-Za-z]{1}"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:complexType name="dataFieldType" id="datafield.ct">
    <xsd:annotation>
      <xsd:documentation>MARC21 Variable Data Fields 010-999</xsd:documentation>
    </xsd:annotation>
    <xsd:sequence maxOccurs="unbounded">
      <xsd:element name="subfield" type="subfieldatafieldType"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="idDataType" use="optional"/>
    <xsd:attribute name="tag" type="tagDataType" use="required"/>
    <xsd:attribute name="ind1" type="indicatorDataType" use="required"/>
    <xsd:attribute name="ind2" type="indicatorDataType" use="required"/>
  </xsd:complexType>
  <xsd:simpleType name="tagDataType" id="tag.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
      <xsd:pattern value="(0([1-9A-Z][0-9A-Z])|0([1-9a-z][0-9a-z]))|(([1-9A-Z][0-9A-Z]{2})|([1-9a-z][0-9a-z]{2}))"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="indicatorDataType" id="ind.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
      <xsd:pattern value="[\da-z ]{1}"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:complexType name="subfieldatafieldType" id="subfield.ct">
    <xsd:simpleContent>
      <xsd:extension base="subfieldDataType">
        <xsd:attribute name="id" type="idDataType" use="optional"/>
        <xsd:attribute name="code" type="subfieldcodeDataType" use="required"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>
  <xsd:simpleType name="subfieldDataType" id="subfield.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="subfieldcodeDataType" id="code.st">
    <xsd:restriction base="xsd:string">
      <xsd:whiteSpace value="preserve"/>
      <xsd:pattern value="[\dA-Za-z!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?{}_^`~\[\]\\]{1}"/>
      <!-- "A-Z" added after "\d" May 21, 2009 -->
    </xsd:restriction>
  </xsd:simpleType>
  <xsd:simpleType name="idDataType" id="id.st">
    <xsd:restriction base="xsd:ID"/>
  </xsd:simpleType>
</xsd:schema>
"""


def get_scheme(scheme_name):
    try:
        data = pkgutil.get_data("hathi_validate", "xsd/{}.xsd".format(scheme_name))
        return data
    except FileNotFoundError:
        raise ValueError("Unknown scheme {}".format(scheme_name))