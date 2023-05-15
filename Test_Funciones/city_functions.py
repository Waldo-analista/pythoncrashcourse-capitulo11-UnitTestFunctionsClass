def ciudad_pais(city_name,country_name,population=0):
    if population:
        cadena=city_name.title()+', '+country_name.title()+'- population '+str(population)
        return cadena
    else:
        cadena=city_name.title()+', '+country_name.title()
        return cadena
    


    