'''
Created on 13 Mar 2015

@author: alioth
'''

from string import Template
import conf.settings
import time

SENSOROUTPUTJSONLD_TEMPLATE = '''{
                                "@context" : {
                                    "ssn"  : "http://purl.oclc.org/NET/ssnx/ssn#",
                                    "ssn:hasValue" : {
                                        "@type" : "@id"
                                    }
                                },
                                "@id" : "''' + conf.settings.SENSOROUTPUTURL + '''",
                                "@type" : "ssn:SensorOutput",
                                "ssn:hasValue" : "''' + conf.settings.AMOUNTOBSERVATIONURL +'''"                 
                            }'''

def getURL(tree, fecha):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(conf.settings.SENSOROUTPUTURL).substitute({
                                                                "property" : tree,
                                                                "fecha" : time.strftime("%d-%m-%Y", d)
                                                            })


def getJSONLD(tree, fecha, valueamount):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(SENSOROUTPUTJSONLD_TEMPLATE).substitute({
                                                                "property" : tree,
                                                                "fecha" : time.strftime("%d-%m-%Y", d),
                                                                "value" : valueamount
                                                             })

if __name__ == '__main__':
    pass