'''
Created on 21 Mar 2015

@author: Alioth Rodríguez Barrios

Hackathon Zaragoza 2015

Backend whose main goal is to map the xml about pollination of the trees in Zaragoza on rdf format.
This could run like a SPARQL endpoint where it stores the different pages of the trees from dbpedia.es and the
information about the data in realtime about pollination.

'''

from flask import Flask
from flask.json import jsonify
app = Flask(__name__)

import urllib.request
import mapping.time
import mapping.sensoroutput
import mapping.observation
import mapping.amountobservation
from xml.etree import ElementTree as ET
from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import json
from functools import wraps
from flask import request, current_app, Response

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs).data.decode('ascii')) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function

g = Graph()

def importrdfs(g):
    for key in mapping.observation.PLANTS:
        g.parse(mapping.observation.PLANTS[key])
        
def init():
    importrdfs(g)

@app.route("/", methods=['GET'])
@support_jsonp
def getplants():

    querybasic = """
                    PREFIX ssn: <http://purl.oclc.org/NET/ssnx/ssn#>
                    PREFIX qu: <http://purl.oclc.org/NET/ssnx/qu/qu#>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT ?name ?value WHERE {
                        ?a a ssn:Observation;
                            ssn:observedProperty ?url.
                        ?a ssn:observationResult ?result.
                        ?result a ssn:SensorOutput.
                        ?result ssn:hasValue ?amount.
                        ?amount a qu:ScaleValueDefinition.
                        ?amount qu:name ?value.
                        ?url rdfs:label ?name.
                    }
                """
    
    requestURL = 'http://www.zaragoza.es/datos/movil/include/polen.xml'
    
    requestweb = urllib.request.Request(requestURL)
    response = urllib.request.urlopen(requestweb)
    
    root = ET.fromstring(response.read().decode('utf-8'))
    
    fecha = root.attrib["fecha"]
    
    g.parse(data=mapping.time.getInstantTimeDescriptionJSONLD(fecha), format='json-ld')
    g.parse(data=mapping.time.getInstantTimeJSONLD(fecha), format='json-ld')
    for plant in root.findall('planta'):
        tree = plant.find('nombre').text
        value = plant.find('valor').text
        g.parse(data=mapping.observation.getJSONLD(fecha, tree), format='json-ld')
        g.parse(data=mapping.sensoroutput.getJSONLD(tree, fecha, value), format='json-ld')
        g.parse(data=mapping.amountobservation.getJSONLD(tree, fecha, value), format='json-ld')
    
    qres = g.query(querybasic)
    
    mydata = qres.serialize(format='json').decode('ascii')
    
    return Response(mydata,  mimetype='application/json')

if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0', debug=True)
    getplants()