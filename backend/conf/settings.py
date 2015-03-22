'''
Created on 19 Feb 2015

@author: alioth
'''

URLBASE = "http://alergicos.es/"

INSTANTTIMEURL = URLBASE + "instantTime/${fecha}"

# Depends on WEATHER STATION URL
OBSERVATIONOFPROPERTYURL = URLBASE + "/observation_of_pollination_of_${property}_at_${fecha}"

# Depends on OBSERVATION OF PROPERTY URL
SENSOROUTPUTURL = OBSERVATIONOFPROPERTYURL + "/result"

# Depends on RESULT OBSERVATION URL
AMOUNTOBSERVATIONURL = SENSOROUTPUTURL + "/value/${value}"

# Depends on INSTANT TIME URL
INSTANTTIMEDESCRIPTIONURL = INSTANTTIMEURL + "/description"


if __name__ == '__main__':
    pass