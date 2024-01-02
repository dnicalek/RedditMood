import unittest
from CryptoData import CryptoData

class TestCryptoData(unittest.TestCase):

    def test_get_crypto_symbol(self):
        # Arrange
        crypto_data = CryptoData()

        # Act
        symbol_btc = crypto_data.get_crypto_symbol("Bitcoin")
        symbol_eth = crypto_data.get_crypto_symbol("Ethereum")

        # Assert
        self.assertEqual(symbol_btc, "BTC")
        self.assertEqual(symbol_eth, "ETH")

    def test_get_photo_url(self):
        # Arrange
        crypto_data = CryptoData()

        # Act
        url_btc = crypto_data.get_photo_url("Bitcoin")
        url_eth = crypto_data.get_photo_url("Ethereum")

        # Assert
        self.assertEqual(url_btc, "https://cryptologos.cc/logos/bitcoin-btc-logo.png")
        self.assertEqual(url_eth, "https://cryptologos.cc/logos/ethereum-eth-logo.png")

if __name__ == '__main__':
    unittest.main()
