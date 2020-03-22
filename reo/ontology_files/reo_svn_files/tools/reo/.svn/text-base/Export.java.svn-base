package reo;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLAnnotation;
import org.semanticweb.owlapi.model.OWLAnnotationAssertionAxiom;
import org.semanticweb.owlapi.model.OWLAxiom;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.OWLOntologyCreationException;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.model.OWLOntologyStorageException;

public class Export {

	/**
	 * @param args
	 * @throws OWLOntologyCreationException
	 * @throws FileNotFoundException
	 * @throws OWLOntologyStorageException
	 * @throws InterruptedException
	 */
	public static void main(String[] args) throws OWLOntologyCreationException,
			OWLOntologyStorageException, FileNotFoundException,
			InterruptedException {
		// TODO Auto-generated method stub

		OWLOntologyManager man = OWLManager.createOWLOntologyManager();
		man.setSilentMissingImportsHandling(true);
		OWLOntology reo = man.loadOntologyFromOntologyDocument(new File(
				"../src/ontology/reo.owl"));
		OWLOntology reoanot = man.createOntology(IRI
				.create("htt://purl.obolibrary.org/obo/reo-annot.owl"));

		for (OWLAxiom a : reo.getAxioms()) {

			if (a instanceof OWLAnnotationAssertionAxiom) {
				OWLAnnotationAssertionAxiom aa = (OWLAnnotationAssertionAxiom) a;

				String u = aa.getAnnotation().getProperty().getIRI().toString();
				if (u.endsWith("0208") || u.endsWith("0513")) {
					man.addAxiom(reoanot, aa);
					man.removeAxiom(reo, aa);
					;
				}

			}
		}

		man.saveOntology(reo, new FileOutputStream(new File(
				"../src/ontology/reo-clean.owl")));
		man.saveOntology(reoanot, new FileOutputStream(new File(
				"../src/ontology/reo-annot.owl")));

	}

}
