# classe Agenzia
from Agenzia.models import *


class Agenzia:
    def __init__(self, nome, sede):
        self.__nome = nome
        self.__sede = sede
        self.__immobili = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_nome):
        self.__nome = new_nome

    @property
    def sede(self):
        return self.__sede

    @sede.setter
    def sede(self, new_sede):
        self.__sede = new_sede

    # aggiunge immobile nell agenzia
    def add_immobile(self, immobile):
        if immobile is not None:
            self.__immobili.append(immobile)
            return True
        else:
            return False

    # cerca immobili nell'agenzia con una chiave
    def search_immobili(self, key: str):
        immobili_trovati = []
        for immobile in self.__immobili:
            if immobile.contains(key):
                immobili_trovati.append(immobile)

        return immobili_trovati

    def immobili(self):
        scheda_immobili = ""
        for immobile in self.__immobili:
            scheda_immobili += f"{immobile.scheda_immobile()}\n\n"
        return scheda_immobili
