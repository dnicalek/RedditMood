class CryptoData:

    @staticmethod
    def get_crypto_list():
        return [
            "Binance Coin", "Bitcoin", "Cardano", "Chainlink", "Solana",
            "Dogecoin", "Ethereum", "Litecoin", "Polkadot", "XRP"
        ]

    @staticmethod
    def get_crypto_symbol(crypto_name):
        crypto_symbols = {
            "Binance Coin": "BNB",
            "Bitcoin": "BTC",
            "Cardano": "ADA",
            "Chainlink": "LINK",
            "Solana": "SOL",
            "Dogecoin": "DOGE",
            "Ethereum": "ETH",
            "Litecoin": "LTC",
            "Polkadot": "DOT",
            "XRP": "XRP"
        }
        return crypto_symbols.get(crypto_name, crypto_name)

    @staticmethod
    def get_photo_url(crypto_name):
        photo_urls = {
            "Binance Coin": "https://cryptologos.cc/logos/binance-usd-busd-logo.png",
            "Bitcoin": "https://cryptologos.cc/logos/bitcoin-btc-logo.png",
            "Cardano": "https://cryptologos.cc/logos/cardano-ada-logo.png",
            "Chainlink": "https://cryptologos.cc/logos/chainlink-link-logo.png",
            "Solana": "https://cryptologos.cc/logos/solana-sol-logo.png?v=029",
            "Dogecoin": "https://cryptologos.cc/logos/dogecoin-doge-logo.png",
            "Ethereum": "https://cryptologos.cc/logos/ethereum-eth-logo.png",
            "Litecoin": "https://cryptologos.cc/logos/litecoin-ltc-logo.png",
            "Polkadot": "https://cryptologos.cc/logos/polkadot-new-dot-logo.png",
            "XRP": "https://finvesting.net/wp-content/uploads/2022/03/xrp-icon-freelogovectors.net_-400x400.png"
        }
        return photo_urls.get(crypto_name, "Brak dostępnego URL zdjęcia")