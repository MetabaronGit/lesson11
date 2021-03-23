# slovnik a ukládání do binárky

# %%writefile numbers.txt
# 235152
# 285535
# 432920
# 846088
# 978842
# 204820

# def nacteni_udaju(soubor: str) -> list:
#     with open(soubor, mode="r") as txt:
#         return txt.readlines()
#
#
# def ocisti_ciselne_udaje(neupravene: list) -> list:
#     return [naformatuj_data(radek.strip()) for radek in neupravene]
#
#
# def naformatuj_data(udaj: str) -> str:
#     return f"ID: {udaj}, TYPE: {type(udaj)}"
#
#
# def zkontroluj_typ_udaje(upravene: list) -> None:
#     overene_udaje = []
#     while upravene:
#         overeni_typu(overene_udaje, upravene)
#
#
# def overeni_typu(uloziste: list, detail: list) -> None:
#     try:
#         vyber_cislo = detail.pop().split()[1][:-1]
#         prevedena_hodnota = int(vyber_cislo)
#
#     except ValueError as ve:
#         print(f"NEKONVERTOVATELNE --> {vyber_cislo},  {ve.__class__.__name__}")
#
#     else:
#         print(f"{vyber_cislo} --> OK, pokracuji...")
#         uloziste.append(prevedena_hodnota)
#
#     finally:
#         print("-" * 40)


import pickle

slovnik = {}

while True:
  dvojice_slov = input("Zadej klic a hodnotu(oddel je carkou) nebo zadej q pro exit: ")
  if dvojice_slov != "q":
    klic, hodnota = dvojice_slov.split(",")
    slovnik[klic] = hodnota
  else:
    break

    with open("aj_cj.pickle", mode="wb") as b_file:
        pickle.dump(slovnik, b_file, protocol=pickle.HIGHEST_PROTOCOL)

        with open("aj_cj.pickle", mode="rb") as b_file:
            data = pickle.load(b_file)