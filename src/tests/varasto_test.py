"""Yksikkötestit Varasto-luokalle."""
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Testaa Varasto-luokan eri toiminnallisuudet."""
    def setUp(self):
        """Asettaa varastoon."""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa tyhjan varaston."""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """testaa uuden varaston tilavuutta."""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa saldon lisaysta"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa vapaata tilaa"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa palauttamista"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa ottamista"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_negatiivinen_maara_ei_muuta_saldoa(self):
        """Testaa, että negatiivinen määrä ei muuta saldoa."""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yli_kapasiteetin(self):
        """Testaa, että lisaa_varastoon() ei ylitä varaston kapasiteettia."""
        self.varasto.lisaa_varastoon(15)  # Yritetään lisätä liikaa
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Saldoa ei voi olla yli 10

    def test_ottaminen_liikaa(self):
        """Testaa, että ota_varastosta() palauttaa koko saldon, jos pyydetään enemmän kuin saldo."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)  # Yritetään ottaa liikaa
        self.assertAlmostEqual(saatu_maara, 5)  # Palautetaan koko saldo
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_negatiivinen_maara_palauttaa_nollan(self):
        """Testaa, että negatiivinen määrä palauttaa nollan."""
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(saatu_maara, 0)  # Palautetaan 0
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_str_metodi(self):
        """Testaa, että __str__() metodi palauttaa oikean merkkijonon."""
        self.varasto.lisaa_varastoon(5)
        expected_str = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(self.varasto), expected_str)

    def test_konstruktori_negatiivinen_tilavuus(self):
        """Testaa, että negatiivinen tilavuus nollaa kapasiteetin."""
        varasto = Varasto(-5)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_negatiivinen_alku_saldo(self):
        """Testaa, että negatiivinen alku-saldo nollaa saldon."""
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_alku_saldo_yli_tilavuuden(self):
        """Testaa, että alku-saldo ylittää kapasiteetin, asetetaan saldo tilavuuteen."""
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)
