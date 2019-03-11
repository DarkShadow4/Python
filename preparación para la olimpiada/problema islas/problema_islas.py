# -*- coding: utf-8 -*-

def analize_isle(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year):
    isle = index[:]
    indice_isla = country.index(isle)
    indice = 0
    while len(isle) > 0:
        index = isle[indice]
        isle, sea_level, nislas, indice, index, country_at_the_end_of_the_year = analize_segment(isle, sea_level, nislas, indice, index, country_at_the_end_of_the_year)
    del(country[indice_isla])
    return country, sea_level, nislas, indice, index, country_at_the_end_of_the_year

def analize_segment(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year):
    if index[1] <= sea_level:
        if indice > 0:
            isla1 = country[:indice]
            nislas += 1
            country_at_the_end_of_the_year.append(country[:indice])
        # for segmento in country[:indice]:
        #     country_at_the_end_of_the_year.append(segmento)
        del(country[:indice+1])
        indice = 0
    else:
        if country.index(index) == len(country)-1:
            country_at_the_end_of_the_year.append(country[:])
            nislas += 1
            del(country[:])
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
            indice = 0
        else:
            country, sea_level, nislas, indice, index, country_at_the_end_of_the_year = analize_segment(country, sea_level, nislas, indice, index, country_at_the_end_of_the_year)

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

    try:
        sea_levels = raw_input().split(" ")
    except EOFError:
        end = True

    country = create_country(heights)
    for sea_level in sea_levels:
        country, nislas =analize_country(country, int(sea_level))
        print nislas,
    print ""
