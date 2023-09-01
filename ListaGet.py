from fastapi import FastAPI

app = FastAPI()


# Ejemplo de diccionario de motos  

motos = [

    {"codigo": 1, "marca": "Gottlieb", "modelo": "Daimler Reitwagen", "año": 1885},
    {"codigo": 2, "marca": "Flying Merkel", "modelo": "Model V", "año": 1911},
    {"codigo": 3, "marca": "Harley Davidson", "modelo": "Modelo 7D", "año": 1911},
    {"codigo": 4, "marca": "Peugeot", "modelo": "Paris Nice", "año": 1913},
    {"codigo": 5, "marca": "Indian", "modelo": "Valve Board", "año": 1915},
    {"codigo": 6, "marca": "Megola ", "modelo": "Sport", "año": 1920},
    {"codigo": 7, "marca": "Bmw", "modelo": "R32", "año": 1923},
    {"codigo": 8, "marca": "Bohmerland", "modelo": "Model 598", "año": 1925},
    {"codigo": 9, "marca": "Ariel Square Four", "modelo": "MK", "año": 1931},
    {"codigo": 10, "marca": "Indian", "modelo": "Sport Scout", "año": 1934},
    {"codigo": 11, "marca": "Triumph", "modelo": "Speed Twin", "año": 1938},
    {"codigo": 12, "marca": "Vespa", "modelo": "Gts", "año": 1946},
    {"codigo": 13, "marca": "Solex ", "modelo": "Velosolex", "año": 1946},
    {"codigo": 14, "marca": "Gilera", "modelo": "Saturno", "año": 1947},
    {"codigo": 15, "marca": "Indian", "modelo": "Chief", "año": 1948},
    {"codigo": 16, "marca": "BSA", "modelo": "Gold Star", "año": 1952},
    {"codigo": 17, "marca": "Montesa ", "modelo": "Brio 90", "año": 1953},
    {"codigo": 18, "marca": "Vespa", "modelo": "Gs", "año": 1955},
    {"codigo": 19, "marca": "Vespa", "modelo": "180SS", "año": 1911}, 
    {"codigo": 20, "marca": "Montesa", "modelo": "Cappra", "año": 1955},
    {"codigo": 21, "marca": "Montesca", "modelo": "Enduro", "año": 1944},
    {"codigo": 22, "marca": "Harley Davidson", "modelo": "Sportster XL", "año": 1957},
    {"codigo": 23, "marca": "Honda", "modelo": "Super club", "año": 1958},
    {"codigo": 24, "marca": "Triumph", "modelo": "Bonneville", "año": 1958},
    {"codigo": 25, "marca": "Harley Davidson", "modelo": "Duo Glide", "año": 1959},
    {"codigo": 26, "marca": "Bultaco", "modelo": "Tralla", "año": 1959},
    {"codigo": 27, "marca": "Honda", "modelo": "CB", "año": 1960},
    {"codigo": 28, "marca": "Montesa", "modelo": "Impala", "año": 1962},
    {"codigo": 29, "marca": "OSSA", "modelo": "GT", "año": 1962},
    {"codigo": 30, "marca": "Norton", "modelo": "Manx", "año": 1962},
    {"codigo": 31, "marca": "Bultaco", "modelo": "Sherpa T", "año": 1962},
    {"codigo": 32, "marca": "Bultaco", "modelo": "Metralla MK2", "año": 1966},
    {"codigo": 33, "marca": "Derbi", "modelo": "Antorcha 50", "año": 1965},
    {"codigo": 34, "marca": "Norton", "modelo": "Commando 750", "año": 1967},
    {"codigo": 35, "marca": "Buell", "modelo": " Mach III", "año": 1968},
    {"codigo": 36, "marca": "Vespa", "modelo": " Vespino", "año": 1968},
    {"codigo": 37, "marca": " Kawasaki", "modelo": " Mach III", "año": 1968},
    {"codigo": 38, "marca": "Montesa", "modelo": "Cota", "año": 1968},
    {"codigo": 39, "marca": "Honda", "modelo": "Four", "año": 1969},
    {"codigo": 40, "marca": "Suzuki", "modelo": "Gt", "año": 1968},
    {"codigo": 41, "marca": "Brixton", "modelo": "Z1", "año": 1972},
    {"codigo": 42, "marca": "Yamaha", "modelo": "RD", "año": 1972},
    {"codigo": 43, "marca": "Benelli", "modelo": "Sei", "año": 1973},
    {"codigo": 44, "marca": "Ducati", "modelo": "Road", "año": 1973},
    {"codigo": 45, "marca": "Sanglas", "modelo": "E", "año": 1973},
    {"codigo": 46, "marca": "Bultaco", "modelo": "Pursang MK8", "año": 1974}, 
    {"codigo": 47, "marca": "Ducati", "modelo": "SS 750", "año": 1974},
    {"codigo": 48, "marca": "Laverda", "modelo": "SF 750", "año": 1974},
    {"codigo": 49, "marca": "Honda", "modelo": "Gold Wing", "año": 1975},
    {"codigo": 50, "marca": "Bultaco", "modelo": "Frontera", "año": 1975},
    {"codigo": 51, "marca": "BMW", "modelo": "R 90", "año": 1976},
    {"codigo": 52, "marca": "OSSA", "modelo": "Yankee", "año": 1976},
    {"codigo": 53, "marca": "Guzzi", "modelo": "Le Mans", "año": 1977},
    {"codigo": 54, "marca": "Ariic", "modelo": "XT 500", "año": 1977},
    {"codigo": 55, "marca": "Honda", "modelo": "CBX", "año": 1978},
    {"codigo": 56, "marca": "Buell", "modelo": " Z 1300", "año": 1978},
    {"codigo": 57, "marca": "Yamaha", "modelo": "SR 500", "año": 1975},
    {"codigo": 58, "marca": "BMW", "modelo": "R 80", "año": 1980},
    {"codigo": 59, "marca": "Suzuki", "modelo": "Katana", "año": 1981},
    {"codigo": 60, "marca": "Suzuki", "modelo": "RG 250", "año": 1975},
    {"codigo": 61, "marca": "BMW", "modelo": "K 100", "año": 1984},
    {"codigo": 62, "marca": "Kawasaki", "modelo": "GPZ 900", "año": 1984},
    {"codigo": 63, "marca": "Yamaha", "modelo": "rd 500", "año": 1984},
    {"codigo": 64, "marca": "Arena", "modelo": "Max V", "año": 1985},
    {"codigo": 65, "marca": "Bicose", "modelo": "GSX", "año": 1985},
    {"codigo": 66, "marca": "Yamaha", "modelo": "FZ 750", "año": 1985},
    {"codigo": 67, "marca": "Ariic", "modelo": "VFR", "año": 1986},
    {"codigo": 68, "marca": "Arc", "modelo": "FZR", "año": 1984},
    {"codigo": 69, "marca": "Beta", "modelo": "Zero", "año": 1989},
    {"codigo": 70, "marca": "Yamaha", "modelo": "Super Tenere", "año": 1989},
    {"codigo": 71, "marca": "Bimota", "modelo": "Tesi", "año": 1990},
    {"codigo": 72, "marca": "Honda", "modelo": "Africa Twin", "año": 1990},
    {"codigo": 73, "marca": "Kawasaki", "modelo": "ZZ-R", "año": 1990},
    {"codigo": 74, "marca": "Caviga", "modelo": "DR Big", "año": 1990},
    {"codigo": 75, "marca": "Honda", "modelo": "CBR", "año": 1991},
    {"codigo": 76, "marca": " Honda", "modelo": "NR", "año": 1992},
    {"codigo": 77, "marca": "Ducati", "modelo": "Monster", "año": 1993},
    {"codigo": 78, "marca": "Sanglas", "modelo": "LS", "año": 1994},
    {"codigo": 79, "marca": "Triumph", "modelo": "Speed Triple", "año": 1994},
    {"codigo": 80, "marca": "KTM", "modelo": "Duke", "año": 1994},
    {"codigo": 81, "marca": "BMW", "modelo": "R 1200", "año": 1997},
    {"codigo": 82, "marca": "MV ", "modelo": "Agusta", "año": 1998},
    {"codigo": 83, "marca": "Suzuki", "modelo": "Burgman", "año": 1998},
    {"codigo": 84, "marca": "Caviga", "modelo": "R1J", "año": 1998},
    {"codigo": 85, "marca": "Suzuki", "modelo": "GSX 1300", "año": 1999},
    {"codigo": 86, "marca": "Yamaha", "modelo": "T max", "año": 2000},
    {"codigo": 87, "marca": "BMW", "modelo": "C1", "año": 2001},
    {"codigo": 88, "marca": "Harley Davidson", "modelo": "V Rod", "año": 2001},
    {"codigo": 89, "marca": "KTM", "modelo": "Adventure", "año": 2003},
    {"codigo": 90, "marca": "Honda", "modelo": "CBR RR", "año": 2004},
    {"codigo": 91, "marca": "Montesa", "modelo": "Cota RT", "año": 2005},
    {"codigo": 92, "marca": "Piaggio", "modelo": "MP3", "año": 2006},
    {"codigo": 93, "marca": "Triumph", "modelo": "Street Triple", "año": 2007},
    {"codigo": 94, "marca": "Zero", "modelo": "S", "año": 2009},
    {"codigo": 95, "marca": "BMW", "modelo": "C Evolution", "año": 2011},
    {"codigo": 96, "marca": "BMW", "modelo": "C 650", "año": 2012},
    {"codigo": 97, "marca": "Yamaha", "modelo": "MT 09", "año": 2013},
    {"codigo": 98, "marca": "Ducati", "modelo": "Scrambler", "año": 2015},
    {"codigo": 99, "marca": "Honda", "modelo": "X ADV", "año": 2017},
    {"codigo": 100, "marca": "Ducati", "modelo": "Superleggera", "año": 2017},
    {"codigo": 101, "marca": "BMW", "modelo": "HP4", "año": 2017},
    {"codigo": 102, "marca": "Yamaha", "modelo": "Nlken", "año": 2018},
    {"codigo": 103, "marca": "KYMCO", "modelo": "Lonex", "año": 2018},
    {"codigo": 104, "marca": "Harley Davidson", "modelo": "Livewire", "año": 2019},
    {"codigo": 105, "marca": "Daelim", "modelo": "Daystar", "año": 2015},
    {"codigo": 106, "marca": "Yamaha", "modelo": "Fazer N", "año": 2011},
    {"codigo": 107, "marca": "Hyosung", "modelo": "Karion", "año": 2012},
    {"codigo": 108, "marca": "Hyosung", "modelo": "GT Pro comet", "año": 2012},
    {"codigo": 109, "marca": "Hyosung", "modelo": "ST7", "año": 2012}, 
    {"codigo": 110, "marca": "KTM", "modelo": "SMC R", "año": 2001},
    {"codigo": 111, "marca": "KTM", "modelo": "Super Duke R", "año": 2017},
    {"codigo": 112, "marca": "Yamaha", "modelo": "SR400", "año": 2013},
    {"codigo": 113, "marca": "Kawasaki", "modelo": "ERN", "año": 2012},
    {"codigo": 114, "marca": "Colove", "modelo": "Inazumas 250", "año": 2013},
    {"codigo": 115, "marca": "Suzuki", "modelo": "Vanvan", "año": 2014},
    {"codigo": 116, "marca": "Suzuki", "modelo": "GSX R", "año": 2014},
    {"codigo": 117, "marca": "Colove", "modelo": "Intruder M", "año": 2002},
    {"codigo": 118, "marca": "KTM", "modelo": "RCB R", "año": 2003},
    {"codigo": 119, "marca": "BMW", "modelo": "GS R", "año": 2003},
    {"codigo": 120, "marca": "Derbi", "modelo": "S XR", "año": 2014},
    {"codigo": 121, "marca": "BMW", "modelo": "RR SL", "año": 2003},
    {"codigo": 122, "marca": "Suzuki", "modelo": "Bandit s", "año": 2014},
    {"codigo": 123, "marca": "Derbi", "modelo": "V strom ABS", "año": 2013},
    {"codigo": 124, "marca": "Suzuki", "modelo": "Hayabusa", "año": 2004},
    {"codigo": 125, "marca": "Kawasaki", "modelo": "Vulcan S", "año": 2004},
    {"codigo": 126, "marca": "BMW", "modelo": "GUM", "año": 2004},
    {"codigo": 127, "marca": "Triumph", "modelo": "Trophy", "año": 2005},
    {"codigo": 128, "marca": "Felo", "modelo": "ZSL", "año": 2005},
    {"codigo": 129, "marca": "Suzuki", "modelo": "Gladius T", "año": 2017},
    {"codigo": 130, "marca": "Kawasaki", "modelo": "Ninja", "año": 2014},
    {"codigo": 131, "marca": "Hanway", "modelo": "Versy L", "año": 2006},
    {"codigo": 132, "marca": "Ducati", "modelo": "Panigale", "año": 2013},
    {"codigo": 133, "marca": "Triumpg", "modelo": "Tiger XC", "año": 2012},
    {"codigo": 134, "marca": "Hanway", "modelo": "Gold Wing", "año": 2012},
    {"codigo": 135, "marca": "Honda", "modelo": "Fireblade", "año": 2007},
    {"codigo": 136, "marca": "Kawasaki", "modelo": "Z", "año": 2007},
    {"codigo": 137, "marca": "Felo", "modelo": "VFR", "año": 2007},
    {"codigo": 138, "marca": "Ducati", "modelo": "Urban Enduro", "año": 2007},
    {"codigo": 139, "marca": "KTM", "modelo": "Adventure K", "año": 2007},
    {"codigo": 140, "marca": "Triumph", "modelo": "Tiger Explorer XC", "año": 2012},
    {"codigo": 141, "marca": "Kawasaki", "modelo": "Versys", "año": 2011},
    {"codigo": 142, "marca": "Ducati", "modelo": "Monster 821", "año": 20012},
    {"codigo": 143, "marca": "Ducati", "modelo": "Multistrada", "año": 2008},
    {"codigo": 144, "marca": "CfMoto", "modelo": "Nike", "año": 2018},
    {"codigo": 145, "marca": "Benelli", "modelo": "BN R", "año": 2018},
    {"codigo": 146, "marca": "Royal Enfield", "modelo": "Himalaya", "año": 2018},
    {"codigo": 147, "marca": "Fantic Caballero", "modelo": "Flat Track", "año": 2018},
    {"codigo": 148, "marca": "Aprilia", "modelo": "Factory", "año": 2017},
    {"codigo": 149, "marca": "Husqvarna", "modelo": "Vitpilen", "año": 2018},
    {"codigo": 150, "marca": "Husqvarn", "modelo": "Svartpilen", "año": 2016},
    {"codigo": 151, "marca": "Goes ", "modelo": "GP", "año": 2018},
    {"codigo": 152, "marca": "Goes", "modelo": "TK", "año": 2017},
    {"codigo": 153, "marca": "MV Agusta", "modelo": "F3", "año": 2018},
    {"codigo": 154, "marca": "MV Agusta", "modelo": "Brutale", "año": 2019},
    {"codigo": 155, "marca": "CFMoto", "modelo": "Papio", "año": 2018},
    {"codigo": 156, "marca": "Moto Guzzi", "modelo": "Milano", "año": 2017},
    {"codigo": 157, "marca": "Mitt", "modelo": "Scrambler", "año": 2017},
    {"codigo": 158, "marca": "MH", "modelo": "WYN", "año": 2019},
    {"codigo": 159, "marca": "MH", "modelo": "Lord Martin", "año": 2019},
    {"codigo": 160, "marca": "MH", "modelo": "Bogga", "año": 2019},
    {"codigo": 161, "marca": "Malaguti", "modelo": "XTM", "año": 2019},
    {"codigo": 162, "marca": "Malaguti", "modelo": "Monte Pro", "año": 2020},
    {"codigo": 163, "marca": "Brixton", "modelo": "BX", "año": 2020},
    {"codigo": 164, "marca": "Brixton", "modelo": "Saxby", "año": 2020},
    {"codigo": 165, "marca": "Macbor", "modelo": "Fun", "año": 2021},
    {"codigo": 166, "marca": "Keeway", "modelo": "RKF", "año": 2021},
    {"codigo": 167, "marca": "Triumph", "modelo": "Street Triple R", "año": 2021},
    {"codigo": 168, "marca": "Voge", "modelo": "R500", "año": 2020},
    {"codigo": 169, "marca": "Keeway", "modelo": "Superlight", "año": 2020},
    {"codigo": 170, "marca": "Zero", "modelo": "SR", "año": 2020},
    {"codigo": 171, "marca": "Zontes", "modelo": "V", "año": 2021},
    {"codigo": 172, "marca": "MV", "modelo": "Dragster", "año": 2020},
    {"codigo": 173, "marca": "Voge", "modelo": "DS", "año": 2020},
    {"codigo": 174, "marca": "FB Mondial", "modelo": "HPS", "año": 2021},
    {"codigo": 175, "marca": "OX One", "modelo": "Tokyo", "año": 2021},
    {"codigo": 176, "marca": "Motron", "modelo": "Revolver", "año": 2021}, 
    {"codigo": 177, "marca": "Motron", "modelo": "Vizion", "año": 2022},
    {"codigo": 178, "marca": "Zontes", "modelo": "GX1", "año": 2022},
    {"codigo": 179, "marca": "Urbet", "modelo": "Gadiro", "año": 2023},
    {"codigo": 180, "marca": "Orcal", "modelo": "Astor", "año": 2022},
    {"codigo": 181, "marca": "Zontes", "modelo": "U1", "año": 2023},
    {"codigo": 182, "marca": "Urbet", "modelo": "Nura", "año": 2023},
    {"codigo": 183, "marca": "Bimoto", "modelo": "Tesi", "año": 2022},
    {"codigo": 184, "marca": "Super Soco", "modelo": "TS Street Hunter", "año": 2022},
    {"codigo": 185, "marca": "QJ SRK", "modelo": "S", "año": 2023},
    {"codigo": 186, "marca": "Mutt", "modelo": "Mushman", "año": 2023},
    {"codigo": 187, "marca": "QJ SRK", "modelo": "X", "año": 2023},
    {"codigo": 188, "marca": "RGNT", "modelo": "Scrambler", "año": 2022},
    {"codigo": 189, "marca": "RGNT", "modelo": "Clasicc", "año": 2023},
    {"codigo": 190, "marca": "OX One", "modelo": "Montecarlo", "año": 2021},
    {"codigo": 191, "marca": "Orcal", "modelo": "SK03", "año": 2021},
    {"codigo": 192, "marca": "Leonart", "modelo": "Rigger", "año": 2023},
    {"codigo": 193, "marca": "Macbor Rockster", "modelo": "Flat", "año": 2017},
    {"codigo": 194, "marca": "Triumph", "modelo": "Trident", "año": 2024},
    {"codigo": 195, "marca": "Rieju", "modelo": "Century", "año": 2024},
    {"codigo": 196, "marca": "Keeway", "modelo": "V3C", "año": 2023},
    {"codigo": 197, "marca": "Energica", "modelo": "Experia", "año": 2024},
    {"codigo": 198, "marca": "Triumph", "modelo": "Rocket 3", "año": 2017},
    {"codigo": 199, "marca": "Macbor Rockster", "modelo": "Mot", "año": 2024},
    {"codigo": 200, "marca": "Vmoto", "modelo": "Stash", "año": 2024},   
        ]

 
# Ruta para obtener la lista de motos

@app.get("/obtener-motos")

async def obtener_motos():
 
    return motos

 

# Ruta para obtener una motos por su codigo

@app.get("/obtener-moto/{moto_codigo}")
 
async def obtener_moto(moto_codigo: int):

    for moto in motos:

        if moto["codigo"] == moto_codigo:

            return moto
 
    return {"mensaje": "Motos no encontrado"}
 
 

# Ruta para obtener motos por marca

@app.get("/obtener-motos-por-marca/{marca}")

async def obtener_motos_por_marca(marca: str):

    motos_por_marca = [motos for motos in motos if motos["marca"].lower() == marca.lower()]

    if motos_por_marca:

        return motos_por_marca

    return {"mensaje": "No se encontraron motos para la marca especificada"}


# Ruta para obtener motos por modelo
@app.get("/obtener-motos-por-modelo/{modelo}")

async def obtener_motos_por_modelo(modelo: str):

    motos_por_modelo = [motos for motos in motos if motos["modelo"].lower() == modelo.lower()]

    if motos_por_modelo:

        return motos_por_modelo

    return {"mensaje": "No se encontraron motos para la marca especificada"}


#obtner por año o fecha 
@app.get("/obtener-por-fecha/{fecha}")

async def obtener_año(fecha: int):

    for moto in motos:

        if moto["año"] == fecha:

            return moto

    return {"mensaje": "Moto no encontrada"}



#obtner toda la lista de marcas que hay en el item
@app.get("/obtener-marcas")
async def obtener_marcas():
    lista = []
    for i in motos:
        lista.append(i["marca"])
    return lista

#obtener toda la lista de modelos que hay 
@app.get("/obtener-modelos")
async def obtener_modelos():
    lista = []
    for i in motos:
        lista.append(i["modelo"])
    return lista 

#obtner todos los años que hay en la lista de elementos
@app.get("/obtener-fecha")
async def obtener_fecha():
    lista = []
    for i in motos:
        lista.append(i["año"])
    return lista


#obtener los primeros diez elementos del array "motos"
@app.get("/primeros10")
async def obtener_10elementos():
    lista = []
    contador = 1
    for moto in motos:
        if contador <= 10: 
            lista.append(moto)
            contador += 1
    return lista


#obtener los ultimos diez elementos del array "motos"
@app.get("/intermedios10")
async def obtener_intermedios10():
    lista = []
    contador = 1
    for moto in motos:
        if contador >= 180 and contador <= 190:
            lista.append(moto)
        contador += 1        
    return lista   
# uvicorn ListaGet:app --reload levantar servidor api 




