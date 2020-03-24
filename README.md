## The Reagent Ontology (Archive)

### Overview
This repository was set up to hold files related to the Reagent Ontology (ReO), which has been inactive since its SVN repository hosted at Google Code ([link](https://code.google.com/archive/p/reagent-ontology/)) was shut down many years ago. While the ontology as a whole has some pervasive issues (e.g. baroque axiomatization, scope creep, antiquated modeling, etc.), and hasn’t been developed at all in the past 8 years, there may be content that can inform or be ceded to other actively developed ontologiesm, such as the Ontology of Biomedical Investigations ([link](http://obi-ontology.org/)). 

An overview of the content, organization, and ontological principles of the Reagent Ontology can be found in the 2011 conference abstract [here](http://ceur-ws.org/Vol-833/paper32.pdf). Information on a 'slim' version focused on antibody reagent representation, which is also archived in this repository, can be found [here](https://code.google.com/archive/p/reagent-ontology/wikis/Antibodies.wiki).

The best file to explore if you want to poke around the ontology itself is the **pre-merged and reasoned** version [here](https://github.com/tis-lab/reagent-ontology/blob/master/reo/ontology_files/reo_pre-merged_or_reasoned_files/reo_reasoned_9-6-12.owl). The central hierarchy rooted at the 'reagent' class is built only upon running a reasoned over the ontology to collect all classes with a reagent role in one place - and the baroque axiomatization of classes in the ontology make reasoning in Protégé prohibitively slow (at least with the most common Protege reasoner plugins).



------------------------

### Directory Structure
The directory structure and content of this ReO archive repository is described below: 

- `reo/`: ontology files and documents for the full reo ontology. 
    - `reo/ontology_files/`: the owl files for the ontology itself
        - `reo/ontology_files/reo_pre-merged_or_reasoned_files/`: a pre-merged version of reo (merges all imports into a single owl file), and a pre-reasoned merged version of reo (reasoner inferences come materialized). Note that the reasoned version may be slightly out of sync with the merged version.
        - `reo/ontology_files/reo_svn_files/`: source owl files used to build the pre-merged/reasoned versions (again, content of these may not be entirely in sync with that of merged/reasoned versions)
    - `reo/docs/`: a few documents about the ontology of potential interest for anyone looking to evaluate or use its content

- `reo_ab_slim`: files from an effort to extract a subset of the full ontology relevant to antibody reagents.
    - `reo_ab_slim/ontology_files`:  pre-merged and pre-reasoned versions of this slim
    - `reo_ab_slim/docs`: various documents describing the modeling implemented in the ab-slim, and proposals for expanding this modeling for richer representations of the domain.


----------------------


## About ReO
The Reagent Ontology (ReO) adheres to OBO Foundry principles (obofoundry.org) to model the domain of biomedical research reagents, considered broadly to include materials applied “chemically” in scientific techniques to facilitate generation of data and research materials. ReO is a modular ontology that re-uses existing ontologies to facilitate cross-domain interoperability. It consists of reagents and their properties, linking diverse biological and experimental entities to which they are related. ReO supports community use cases by providing a flexible, extensible, and deeply integrated framework that can be adapted and extended with more specific modeling to meet application needs. More information about the content, organization, and ontological principles of the ReO Ontology can be found in the 2011 conference abstract [here](http://ceur-ws.org/Vol-833/paper32.pdf).

