import requests

def  listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()


    for pais in paises:
        # print(f"Nombre Comun: {pais["name"]["common"]}")
        # print(f"Nombre Oficial: {pais["name"]["official"]}")
        # print(f"Nombre Oficial: {pais["official"]}")
        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital  es: {pais['capital'][0]}")
        # print(pais)

    url = "https://restcountries.com/v3.1/independent?status=true&fields=translations,capital"
    listar_nombre_paises(url)


def obtener_informacion_pais(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pais = data[0]
        nombre_oficial = pais["name"]["official"]
        capital = pais["capital"][0]
        moneda = pais["currencies"].get("primary")
        codigo_telefonico = "+" + str(pais["callingCodes"][0])
        return nombre_oficial, capital, moneda, codigo_telefonico
    else:
        return None






