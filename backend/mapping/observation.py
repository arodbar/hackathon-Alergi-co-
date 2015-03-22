'''
Created on 21 Mar 2015

@author: alioth
'''
from string import Template
import conf.settings
import time

PLANTS = {
          "morera":"http://es.dbpedia.org/resource/Morus_alba", 
          "quercus":"http://es.dbpedia.org/resource/Quercus", 
          "olivo":"http://es.dbpedia.org/resource/Olea_europaea", 
          "platano":"http://es.dbpedia.org/resource/Platanus_%C3%97_hispanica", 
          "cenizo":"http://es.dbpedia.org/resource/Chenopodium", 
          "plantago":"http://es.dbpedia.org/resource/Plantago", 
          "amarantaceas":"http://es.dbpedia.org/resource/Amaranthaceae", 
          "chopo":"http://es.dbpedia.org/resource/Populus", 
          "cupresaceas":"http://es.dbpedia.org/resource/Cupressaceae", 
          "pino":"http://es.dbpedia.org/resource/Pinus", 
          "graminea":"http://es.dbpedia.org/resource/Poaceae", 
          "cielo":"http://es.dbpedia.org/resource/Ailanthus_altissima", 
          "urticacea":"http://es.dbpedia.org/resource/Urticaceae"
        }

OBSERVATIONSONLD_TEMPLATE = '''{
                                "@context" : {
                                    "ssn"  : "http://purl.oclc.org/NET/ssnx/ssn#",
                                    "ssn:observationResultTime" : {
                                        "@type" : "@id"
                                    },
                                    "ssn:observedProperty" : {
                                        "@type" : "@id"
                                    },
                                    "ssn:featureOfInterest" : {
                                        "@type" : "@id"
                                    },
                                    "ssn:observationResult" : {
                                        "@type" : "@id"
                                    }
                                },
                                "@id" : "''' + conf.settings.OBSERVATIONOFPROPERTYURL + '''",
                                "@type" : "ssn:Observation",
                                "ssn:observedProperty": "${urlplant}",
                                "ssn:featureOfInterest" : "http://dbpedia.org/resource/Pollination",
                                "ssn:observationResultTime" : "''' + conf.settings.INSTANTTIMEURL + '''",
                                "ssn:observationResult" : "''' + conf.settings.SENSOROUTPUTURL + '''"                
                            }'''

def getURL(fecha, tree):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(conf.settings.OBSERVATIONOFPROPERTYURL).substitute({
                                                            "property" : tree,
                                                            "fecha" : time.strftime("%d-%m-%Y", d)
                                                          })
                            
def getJSONLD(fecha, tree):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(OBSERVATIONSONLD_TEMPLATE).substitute({
                                                           "property" : tree,
                                                           "urlplant" : PLANTS[tree],
                                                           "fecha" : time.strftime("%d-%m-%Y", d)
                                                        })