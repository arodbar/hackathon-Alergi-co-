'''
Created on 13 Mar 2015

@author: alioth
'''

from string import Template
import conf.settings
import time

INSTANTJSONLD_TEMPLATE = '''{
                                "@context" : {
                                    "time"  : "http://www.w3.org/2006/time#",
                                    "xsd"   : "http://www.w3.org/2001/XMLSchema#",
                                    "time:inDateTime" : {
                                        "@type" : "@id"
                                    },
                                    "time:inXSDDataTime" : {
                                        "@type" : "xsd:dateTime"
                                    }
                                },
                                "@id" : "''' + conf.settings.INSTANTTIMEURL + '''",
                                "@type" : "time:Instant",
                                "time:inXSDDataTime" :  "${year}-${month}-${day}T00:00+0100",
                                "time:inDateTime" : "''' + conf.settings.INSTANTTIMEDESCRIPTIONURL + '''"                   
                            }'''
                   
INSTANTDESCRIPTIONJSONLD_TEMPLATE = '''{
                                            "@context" : {
                                                "time"  : "http://www.w3.org/2006/time#",
                                                "xsd"   : "http://www.w3.org/2001/XMLSchema#",
                                                "time:unitType" : {
                                                    "@type" : "@id"
                                                },
                                                "time:month" : {
                                                    "@type" : "xsd:gMonth"
                                                },
                                                "time:day" : {
                                                    "@type" : "xsd:gDay"
                                                },
                                                "time:year" : {
                                                    "@type" : "xsd:gYear"
                                                }
                                            },
                                            "@id" : "''' + conf.settings.INSTANTTIMEDESCRIPTIONURL + '''",
                                            "@type" : "time:DateTimeDescription",
                                            "time:unitType" : "time:unitDay",
                                            "time:month" : "${month}",
                                            "time:day" : "${day}",
                                            "time:year" : "${year}"                 
                                        }'''

def getURLInstantTime(fecha):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(conf.settings.INSTANTTIMEURL).substitute({
                                                            "fecha" : time.strftime("%d-%m-%Y", d)
                                                          })

def getURLInstantTimeDescription(fecha):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(conf.settings.INSTANTTIMEDESCRIPTIONURL).substitute({"fecha" : time.strftime("%d-%m-%Y", d)})

def getInstantTimeJSONLD(fecha):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(INSTANTJSONLD_TEMPLATE).substitute({"fecha" : time.strftime("%d-%m-%Y", d),
                                                        "year" : d.tm_year,
                                                        "month" : d.tm_mon,
                                                        "day" : d.tm_mday
                                                        })

def getInstantTimeDescriptionJSONLD(fecha):
    d = time.strptime(fecha, '%d/%m/%Y')
    return Template(INSTANTDESCRIPTIONJSONLD_TEMPLATE).substitute({"fecha" : time.strftime("%d-%m-%Y", d),
                                                                   "year" : d.tm_year,
                                                                   "month" : d.tm_mon,
                                                                   "day" : d.tm_mday
                                                                })

if __name__ == '__main__':
    pass