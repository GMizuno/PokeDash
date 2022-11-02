from abc import abstractmethod
import httpx


class Requester:
    def __init__(self, url: str):
        self.url = url
        self.params = {'limit': '100000', 'offset': 0}

    def get_data(self, url: str) -> list:
        p1 = httpx.get(url).json()
        print(url)
        return self.get_info(p1)

    @abstractmethod
    def get_info(self, result: dict) -> list:
        pass

    @property
    def extract(self) -> list:
        urls = httpx.get(self.url, params=self.params).json().get('results')
        data = []
        for url in urls:
            data += self.get_data(url.get('url'))
        return data
