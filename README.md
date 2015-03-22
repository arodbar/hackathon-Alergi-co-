# hackathon-Alergi-co-
Basicamente lo que se pretendía es simular un endpoint sparql que se consultara desde fuera.

Tiene precargado las páginas de la dbpedia correspondientes a los árboles que se miden en el colegio de farmaceuticos.

El xml que se consulta desde la web del ayuntamiento de zaragoza, se mapea para generar un Json-ld que se almacena en un grafo (el creado con la libreria rdflib de python). Se utilizan ontologías varias que se pueden consultar en el código.

Se intenta usar la SSN Ontology, para simular lo que se tiene en calidad del aire. No esta totalmente bien estructurada, pero se intenta dar un ejemplo del uso de utilizar información semántica.
