"""Varaston hallinnan päämoduuli."""
class Varasto:
    """Varasto luokka."""
    def __init__(self, tilavuus, alku_saldo = 0):
        """
        Alustaa varaston tilavuuden ja saldon.

        Args:
            tilavuus (float): Varaston tilavuus, joka ei voi olla negatiivinen.
            alku_saldo (float): Varaston alkusaldo, joka ei voi olla negatiivinen
            eikä ylittää tilavuutta.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """
        Laskee jäljellä olevan tilan varastossa.

        Returns:
            float: Jäljellä oleva tila.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Lisää varastoon tuotteita, jos mahdollista.

        Args:
            maara (float): Lisättävä määrä, joka ei voi olla negatiivinen.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Ottaa varastosta tuotteita, jos mahdollista.

        Args:
            maara (float): Otettava määrä, joka ei voi olla negatiivinen.

        Returns:
            float: Todellinen määrä, joka otettiin varastosta.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """
        Palauttaa varaston tilan merkkijonoesityksenä.

        Returns:
            str: Varaston saldo ja jäljellä oleva tila.
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
