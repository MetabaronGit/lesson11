# V tomto úkolu budeš opět vytvářet funkci, tentokrát s názvem hledej. Tato funkce bude ve slovníku vyhledávat zadanou hodnotu u zadaného klíče. Funkce by měla:
#
#     brát 3 argumenty: hledaný klíč, hledanou hodnotu a prohledávaný slovník (kvůli testům prosím zvol argumenty v tomto pořadí!),
#     zkusit ve slovníku najít zadaný klíč,
#     pokud je klíč nalezen, funkce by měla zkontrolovat, zda hodnota souhlasí. Pokud ano, funkce vrátí True. Pokud ne, vrátí False,
#     pokud klíč není nalezen, funkce vypíše zprávu a vrátí hodnotu False.


muj_slovnik = {
    'jmeno':'Pepa',
    'prijmeni': 'Novak',
    'rok_narozeni': 1990,
    'mesto': 'Praha',
    'domaci_mazlicek': 'Chameleon'
}


def hledej(key, value, dictionary):
    result = False
    try:
        result = dictionary[key] == value
    except KeyError:
        print("Klíč nenalezen!")
    return result

key = "jmenuo"
value = "Pepak"

print(hledej(key, value, muj_slovnik))
