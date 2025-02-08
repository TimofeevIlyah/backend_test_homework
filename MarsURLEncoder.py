from random import choice


class MarsURLEncoder:
    URL_PREFIX = 'https://ma.rs/'

    def __init__(self):
        self.storage = {}

    def encode(self, long_url) -> str:
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        while True:
            url_hash = ''
            for _ in range(6):
                url_hash += choice(long_url)
            if self.storage.get(url_hash) is None:
                self.storage[url_hash] = long_url
                return self.URL_PREFIX + url_hash

    def decode(self, short_url) -> str:
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        url_hash = short_url.replace(self.URL_PREFIX, '')
        return self.storage.get(url_hash)


mars_url_encoder = MarsURLEncoder()
k1 = mars_url_encoder.encode('https://skillbox.ru/media/code/slovari-v-python-'
                             'chto-nuzhno-znat-i-kak-polzovatsya/')
k2 = mars_url_encoder.encode('https://www.youtube.com/watch?v=UGH3aYuKNJU')
print(mars_url_encoder.decode(MarsURLEncoder.URL_PREFIX+k1))
print(mars_url_encoder.decode(MarsURLEncoder.URL_PREFIX+k2))
