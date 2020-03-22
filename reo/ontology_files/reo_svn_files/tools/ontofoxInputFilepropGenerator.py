#!/usr/bin/python

# Author: Carlo Torniai
# Creation Date: 11/20/2011
# Last revision: 12/15/2011
# Example of usage:
# This programs builds an Ontofox input file starting from an ontology file
# Just parsing the XML file here for class and subclass URI. Nothing fancy :-)
# Example of usage:
# ./ontofoxInputFileGenerator.py ../../../ontology/imports/go-imports.owl GO-ontofox-input.txt GO
# TO DO :
# Optional: switch to seth or rdflib for parsing OWL - no documentation now

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
    #Depending on source ontologies
    if (sourceOntoPrefix=='CARO' ):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='CHEBI'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='CL'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='DOID'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='GO'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='MPATH'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='PATO'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='SO'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='PR'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    elif (sourceOntoPrefix=='UBERON'):
        outString+=OFSOurceAnootationsTag
        outString+='http://www.w3.org/2000/01/rdf-schema#label\n'
        outString+='http://purl.obolibrary.org/obo/IAO_0000115\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasExactSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'
        outString+='http://www.geneontology.org/formats/oboInOwl#hasSynonym\n'
        outString+='mapTo http://purl.obolibrary.org/obo/IAO_0000118\n'

    else:
        outString+=OFSOurceAnootationsTag+"includeAllAnnotationProperties\n"
    return outString

if (len(sys.argv) < 3):
    print "Usage: ontofoxInputfile.py input_file output_file source_ontology"
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
    # Here need to make sure we are dealing with class declaration and not another construct
    # by making sure that Class element has attributes.
    if len(elem.attrib)>0:

        # Here handling the case of GO for which we want to start with just a subset and get the intermediates
        # Looking just for classes with the following annotation  <subset rdf:datatype="http://www.w3.org/2001/XMLSchema#string">subset</subset>
        # ALl set as subclass of Processual entity

        ClassURI= elem.attrib[RDFns+'about']
            #print "Class URI = "+ClassURI
            # Get the children element
        elemchildren = elem.getchildren()
        for y in elemchildren:
             # Here I need to skip all the equivalent classes
             if y.tag==RDFSns+'subClassOf':
                # Just get the actual subclass statements: check if they have at least an attribute
                if len(y.attrib)>0:
                    #Get the Subclass URI
                    SubClassURI = y.attrib[RDFns+'resource']
                if y.tag==RDFSns+'label':
                    #Get Class labe
                    #print "Label"+y.text
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
        #print "Property URI = "+PropertyURI
        # Get the children element
        propelemchildren = elemprop.getchildren()
        for z in propelemchildren:
             # Here I need to skip all the equivalent classes
             if z.tag==RDFSns+'subPropertyOf':
                # Just get the actual subclass statements: check if they have at least an attribute
                if len(z.attrib)>0:
                    #Get the Subclass URI
                    SubPropertyURI = z.attrib[RDFns+'resource']
                    #print "Property Subproperty= "+SubPropertyURI
                if z.tag==RDFSns+'label':
                    #Get Class label
                    #print "Property Label"+z.text
                    PropertyLabel= z.text
        # Add the Property URI Subclass URI and Label info to the list
        # If they contain the source ontology prefix
    if  (sourceOntoPrefix in PropertyURI and propAdd):
        propList.append(PropertyURI)
        propSubPropList.append(SubPropertyURI)
        propLabeList.append(PropertyLabel)
        
#Output check for sanity control/ Debug
#for w in range(0,len(propList)):
#   print "Property= " + propList[w] + "  SubPropertyOf= " + propSubPropList[w] + "  Label= " +propLabeList[w]

#Generates and saves the ontofoxinputfile in outputfile

print ("Writing Ontofox input " + output_file)
writefile(createOFOutputFile(OntoIRI, sourceOntoPrefix, classList, classSubClassList, classLabeList), output_file)
print("Done!")


