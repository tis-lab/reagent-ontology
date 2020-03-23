## The Reagent Ontology (Archive)
This repository was set up to hold files related to the Reagent Ontology (ReO), which has been inactive since its [SVN repository hosted at Google Code](https://code.google.com/archive/p/reagent-ontology/) was shut down many years ago. While the ontology as a whole has some pervasive issues (e.g. baroque axiomatization, scope creep, antiquated modeling, etc.), and hasn’t been developed at all in the past 8 years, there may be content that can inform or be ceded to other actively developed ontologiesm, such as the [Ontology of Biomedical Investigations (OBI)](http://obi-ontology.org/). 

An overview of the content and organization of the ReO Ontology can be found [here]( https://code.google.com/archive/p/reagent-ontology/wikis/Reagents.wiki). Informtion on a 'slim' version focused on antibody reagent representation, which is also archived in this repository, can be found [here](https://code.google.com/archive/p/reagent-ontology/wikis/Antibodies.wiki).

Contents of the directories in this repository are  described below. 

### ReO:
- `reo/`: ontology files and documents for the full reo ontology. 
    - `reo/ontology_files/`: the owl files for the ontology itself
        - `reo/ontology_files/reo_pre-merged_or_reasoned_files/`: a pre-merged version of reo (merges all imports into a single owl file), and a pre-reasoned merged version of reo (reasoner inferences come materialized). Note that the reasoned version may be slightly out of sync with the merged version.
        - `reo/ontology_files/reo_svn_files/`: source owl files used to build the pre-merged/reasoned versions (again, content of these may not be entirely in sync with that of merged/reasoned versions)
    - `reo/docs/`: a few documents about the ontology of potential interest for anyone looking to evaluate or use its content

### ReO Antibody Slim:
- `reo_ab_slim`: files from an effort to extract a subset of the full ontology relevant to antibody reagents.
    - `reo_ab_slim/ontology_files`:  pre-merged and pre-reasoned versions of this slim
    - `reo_ab_slim/docs`: various documents describing the modeling implemented in the ab-slim, and proposals for expanding this modeling for richer representations of the domain.




