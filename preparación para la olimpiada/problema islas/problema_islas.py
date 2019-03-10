# -*- coding: utf-8 -*-
import sys

def analize_isle(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year):
    print "Isla"
    isle = index[:]
    indice_isla = country.index(isle)
    indice = 0
    print "isle:", isle, "with length:", len(isle)
    while len(isle) > 0:
        index = isle[indice]
        isle, sea_level, nislas, indice, index, country_at_the_end_of_the_year = analize_segment(isle, sea_level, nislas, indice, index, country_at_the_end_of_the_year)
    del(country[indice_isla])
    return country, sea_level, nislas, indice, index, country_at_the_end_of_the_year

def analize_segment(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year):
    print "Segmento"
    print "Indice", country.index(index)
    print "Index:", index
    print "nivel segmento:", index[1]
    print "Nivel mar:", sea_level
    print "Nivel mar es superior a nivel segmento?", index[1] <= sea_level
    print "Pais restante:", country, "longitud:", len(country), "primer item del pais:", country[0], "con indice:", country.index(country[0])
    if index[1] <= sea_level:
        print index[0], "se hunde"
        if indice > 0:
            isla1 = country[:indice]
            nislas += 1
            country_at_the_end_of_the_year.append(country[:indice])
            print "country_at_the_end_of_the_year:", country_at_the_end_of_the_year
            print "nueva isla:", isla1
        # for segmento in country[:indice]:
        #     country_at_the_end_of_the_year.append(segmento)
        del(country[:indice+1])
        indice = 0
    else:
        print index[0], u"Esta por encima del nivel del mar"
        if country.index(index) == len(country)-1:
            country_at_the_end_of_the_year.append(country[:])
            nislas += 1
            del(country[:])
            print "country:", country
        indice += 1
    return country, sea_level, nislas, indice, index, country_at_the_end_of_the_year

def analize_country(country, sea_level):
    nislas = 0
    indice = 0
    country_at_the_end_of_the_year = []
    while len(country) > 0:
        index = country[indice]
        if type(index) is list:
            country, sea_level, nislas, indice, index, country_at_the_end_of_the_year = analize_isle(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year)
        else:
            country, sea_level, nislas, indice, index, country_at_the_end_of_the_year = analize_segment(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year)
        print "numero de islas", nislas
        print "---------------------"

    return country_at_the_end_of_the_year, nislas

def create_country(heights):
    country = []
    for segment in range(len(heights)):
        country.append(("Segment"+str(segment+1), int(heights[segment])))
    return country

end = False
while end == False:
    try:
        ys = raw_input().split(" ")
    except EOFError:
        end = True
    try:
        heights = raw_input().split(" ")
    except EOFError:
        end = True
    print heights
    try:
        sea_levels = raw_input().split(" ")
    except EOFError:
        end = True
    country = create_country(heights)
    print country
    for sea_level in sea_levels:
        print "########################",
        print "FASE", sea_levels.index(sea_level)+1,
        print "########################"
        print sea_level
        country, nislas =analize_country(country, sea_level)
        print "country now:", country
        print nislas,
