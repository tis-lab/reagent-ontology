#!/usr/bin/python

# Author: Carlo Torniai
# Creation Date: 01/20/2012
# Last revision: 12/06/2012

# This programs builds an Ontofox input file starting from an ontology file


import xml.etree.ElementTree as ET
import sys



classSubclassDict={}
classLableDict={}
classList=[]
classSubClassList=[]
classLabeList=[]
#Added for properties

propSubPropertyDict={}
propLableDict={}
propList=[]
propSubPropList=[]
propLabeList=[]


OWLns="{http://www.w3.org/2002/07/owl#}"
RDFSns="{http://www.w3.org/2000/01/rdf-schema#}"
RDFns="{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
GOlocalns="{http://purl.obolibrary.org/obo/ero/dev/go-imports.owl}"

OntoIRI=""

def writefile(inlist,fname):
    """ Write a list (inlist) to a file (fname)
    """
    fh=open(fname, "w")
    fh.write(inlist)
    fh.close()

def createOFOutputFile(OntoIRI, sourceOntoPrefix, classList, classSubClassList, classLabeList):
    #Header strings for the Ontofox input file
    OFoutputfileURITag="[URI of the OWL(RDF/XML) output file]\n"
    OFSourceoOntologyTag = "[Source ontology]\n"
    OFLowLevelSourceTag="[Low level source term URIs]\n"
    OFTopLevelSourceURITag="[Top level source term URIs and target direct superclass URIs]\n"
    OFSourceTermsRetrievalTag="[Source term retrieval setting]\n"
    OFBranchExtractionTag="[Branch extractions from source term URIs and target direct superclass URIs]\n"
    OFSOurceAnootationsTag="[Source annotation URIs]\n"
    outString = '';
    #Adding Output Ontology URI
    outString+=OFoutputfileURITag+NewOntoIRI+"\n\n"
    #Adding the Source Ontology
    outString+=OFSourceoOntologyTag+sourceOntoPrefix+"\n\n"
    #Adding the Low Level Source Tag
    outString+=OFLowLevelSourceTag
    #Adding just list of classes
    for w in range(0,len(classList)):
        outString+=classList[w]+ " #" + classLabeList[w]+"\n"

    # Adding the Properties and Subproperties
    for x in range(0,len(propList)):
        outString+=propList[x]+ " #" + propLabeList[x]+"\n"
    outString+="\n"+OFTopLevelSourceURITag
    for z in range(0,len(classList)):
        outString+=classList[z]+ " #" + classLabeList[z]+"\n"
        outString+="subClassOf "+ classSubClassList[z]+"\n"
    for y in range(0,len(propList)):
        outString+=propList[y]+ " #" + propLabeList[y]+"\n"
        # Execute the following line JUST if the subproperty field isn't empty
        if propSubPropList[y]!='':
            outString+="subPropertyOf "+ propSubPropList[y]+"\n"

    #Add the Source Term retrieval
    outString+="\n"+OFSourceTermsRetrievalTag+"includeAllIntermediates\n\n"
    #Add Branch Extraction
    outString+=OFBranchExtractionTag+"\n"
    #Add Annotation Properties
    outString+=OFSOurceAnootationsTag
    outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
    outString+='http://www.w3.org/2000/01/rdf-schema#comment\n'
    outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
    outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
    outString+='http://www.geneontology.org/formats/oboInOwl#hasDefinition\n'
    outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000115\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000115  #definition\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000119  #definition source\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000117  # definition editor\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000118  # alternative term\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000111  # editor preferred term\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000112  # example\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000116  # editor note\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000114  # has curation status\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000589  # OBO Foundry unique label\n'
    outString+='http://purl.obolibrary.org/obo/IAO_0000232  # curator note\n'
    outString+='http://purl.obolibrary.org/obo/IAO_xref       # IAO_xRef\n'


    return outString

if (len(sys.argv) < 3):
    print "Usage: ./ontofoxInputfile.py import-file output-file source-ontology-prefix"
    exit(0)
#Parsing arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
sourceOntoPrefix = sys.argv[3]

# Open the input OWL file for parsing
try:
    tree= ET.parse(input_file)
except IOError:
    print ("Cannot open the files!")

# Get the ontology IRI
OWLOntologyElem= tree.find(OWLns+'Ontology')
OntoIRI= OWLOntologyElem.attrib[RDFns+'about']

# Change the IRI in order to load both ontologies with OWL API for comparison later
NewOntoIRI=OntoIRI.replace(".owl", "-ontofox.owl")


print "Parsing file: " + input_file + "...."
#Get all he classes, subclass and labels and build the dictionaries
for elem in tree.getiterator(OWLns+"Class"):
    ClassURI=''
    SubClassURI=''
    ClassLabel=''
    add = True
    # Get the Class URI


    if len(elem.attrib)>0:
        ClassURI= elem.attrib[RDFns+'about']
        # Get the children element
        elemchildren = elem.getchildren()
        for y in elemchildren:
             if y.tag==RDFSns+'subClassOf':
                if len(y.attrib)>0:
                    #Get the Subclass URI
                    SubClassURI = y.attrib[RDFns+'resource']
                if y.tag==RDFSns+'label':
                    #Get Class label
                    ClassLabel= y.text

    # Add the Class URI Subclass URI and Label info to the list
    # If they contain the source ontology prefix
    if  (sourceOntoPrefix in ClassURI and add):
        classList.append(ClassURI)
        classSubClassList.append(SubClassURI)
        classLabeList.append(ClassLabel)

# Adding a parsing part the generated Properties List
for elemprop in tree.getiterator(OWLns+"ObjectProperty"):
    PropertyURI=''
    SubPropertyURI=''
    PropertyLabel=''
    propAdd=True
    if len(elemprop.attrib)>0:
        PropertyURI= elemprop.attrib[RDFns+'about']

        # Get the children element
        propelemchildren = elemprop.getchildren()
        for z in propelemchildren:
             # Here I need to skip all the equivalent classes
             if z.tag==RDFSns+'subPropertyOf':
                if len(z.attrib)>0:
                    #Get the SUbProperty URI
                    SubPropertyURI = z.attrib[RDFns+'resource']
                if z.tag==RDFSns+'label':
                    PropertyLabel= z.text

        # Add the Property URI Subclass URI and Label info to the list
        # If they contain the source ontology prefix
    if  (sourceOntoPrefix in PropertyURI and propAdd):
        propList.append(PropertyURI)
        propSubPropList.append(SubPropertyURI)
        propLabeList.append(PropertyLabel)


#Generates and saves the ontofoxinputfile in outputfile

print ("Writing Ontofox input " + output_file)
writefile(createOFOutputFile(OntoIRI, sourceOntoPrefix, classList, classSubClassList, classLabeList), output_file)
print("Done!")


