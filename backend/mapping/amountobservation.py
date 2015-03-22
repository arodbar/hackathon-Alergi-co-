'''
Created on 6 Mar 2015

@author: alioth
'''
from string import Template
import conf.settings
import time

JSONLD_TEMPLATE = '''{
   "@context" : {
        "qu" : "http://purl.oclc.org/NET/ssnx/qu/qu#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "qu:name": {
            "@type" : "xsd:string"
        }
    },
    "@id": "''' + conf.settings.AMOUNTOBSERVATIONURL + '''",
    "@type" : "qu:ScaleValueDefinition",
    "qu:name" : "${value}"
}'''

def getURL(tree, fecha, value):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(conf.settings.AMOUNTOBSERVATIONURL).substitute({
                                                                        "property" : tree, 
                                                                        "fecha" : time.strftime("%d-%m-%Y", d), 
                                                                        "value" : value
                                                                    })

def getJSONLD(tree, fecha, value):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(JSONLD_TEMPLATE).substitute({
                                                    "property" : tree, 
                                                    "fecha" : time.strftime("%d-%m-%Y", d), 
                                                    "value" : value
                                                })
    