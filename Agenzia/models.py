# classe Immobile


class Immobile:
    # costruttore
    def __init__(self, codice, indirizzo, cap, citta, superficie):
        self.__codice = codice
        self.__indirizzo = indirizzo
        self.__cap = cap
        self.__citta = citta
        self.__superficie = superficie

    @property
    def codice(self):
        return self.__codice

    @codice.setter
    def codice(self, new_codice):
        self.__codice = new_codice

    @property
    def indirizzo(self):
        return self.__indirizzo

    @indirizzo.setter
    def indirizzo(self, new_indirizzo):
        self.__indirizzo = new_indirizzo

    @property
    def cap(self):
        return self.__cap

    @cap.setter
    def cap(self, new__cap):
        self.__cap = new__cap

    @property
    def citta(self):
        return self.__citta

    @citta.setter
    def citta(self, new_citta):
        self.__citta = new_citta

    @property
    def superficie(self):
        return self.__superficie

    @superficie.setter
    def superficie(self, new_superficie):
        self.__superficie = new_superficie

    # public method
    # restituisce tutti i dati dell'immobile
    def scheda_immobile(self):
        return f"Immbobile: \n{self._write()}"

    # public method
    # cerca una chiave nelle proprieta dell'immobile
    def contains(self, key: str):
        if key in str(self.codice):
            return True
        elif key in str(self.indirizzo):
            return True
        elif key in str(self.cap):
            return True
        elif key in str(self.citta):
            return True
        elif key in str(self.superficie):
            return True
        else:
            return False

    # protected method
    # formatta i dati dell'immobile
    def _write(self):
        return f"Codice: {self.codice}\nIndirizzo: {self.indirizzo}\nCAP: {self.cap}\nCittà: {self.citta}\nSuperficie: {self.superficie}"

# classe Box : Immobile


class Box(Immobile):
    # costruttore
    def __init__(self, codice, indirizzo, cap, citta, superficie, posti_auto):
        super().__init__(codice, indirizzo, cap, citta, superficie)
        self.__posti_auto = posti_auto

    @property
    def posti_auto(self):
        return self.__posti_auto

    @posti_auto.setter
    def posti_auto(self, new_posti_auto):
        self.__posti_auto = new_posti_auto

    def scheda_immobile(self):
        return f"Box: \n{self._write()}"

    def contains(self, key: str):
        if super().contains(key):
            return True
        elif key in str(self.posti_auto):
            return True
        else:
            return False

    def _write(self):
        return f"{super()._write()}\n{self.posti_auto}"


# classe Appartamento : Immobile


class Appartamento(Immobile):
    # costruttore
    def __init__(self, codice, indirizzo, cap, citta, superficie, numero_vani, numero_bagni):
        super().__init__(codice, indirizzo, cap, citta, superficie)
        self.__numero_vani = numero_vani
        self.__numero_bagni = numero_bagni

    @property
    def numero_vani(self):
        return self.__numero_vani

    @numero_vani.setter
    def numero_vani(self, new_numero_vani):
        self.__numero_vani = new_numero_vani

    @property
    def numero_bagni(self):
        return self.__numero_bagni

    @numero_bagni.setter
    def numero_bagni(self, new_numero_bagni):
        self.__numero_bagni = new_numero_bagni

    def scheda_immobile(self):
        return f"Appartamento: \n{self._write()}"

    def contains(self, key: str):
        if super().contains(key):
            return True
        elif key in str(self.numero_vani):
            return True
        elif key in str(self.numero_bagni):
            return True
        else:
            return False

    def _write(self):
        return f"{super()._write()}\nNumero vani: {self.numero_vani}\nNumero Bagni: {self.numero_bagni}"

# classe Villa : Appartamento


class Villa(Appartamento):
    def __init__(self, codice, indirizzo, cap, citta, superficie, numero_vani, numero_bagni, superficie_giardino):
        super().__init__(codice, indirizzo, cap, citta,
                         superficie, numero_vani, numero_bagni)
        self.__superfice_giardino = superficie_giardino

    @property
    def superficie_giardino(self):
        return self.__superfice_giardino

    @superficie_giardino.setter
    def superficie_giardino(self, new_sup_giardino):
        self.__superfice_giardino = new_sup_giardino

    def scheda_immobile(self):
        return f"Villa: \n{self._write()}"

    def contains(self, key: str):
        if super().contains(key):
            return True
        elif key in str(self.numero_bagni):
            return True
        else:
            return False

    def _write(self):
        return f"{super()._write()}\nSuperficie giardino: {self.superficie_giardino}"
