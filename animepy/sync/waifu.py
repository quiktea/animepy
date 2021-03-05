import requests

class WaifuSFW():
    def __init__(self):
        self._session = requests.Session()
        self._base = "https://waifu.pics/api/sfw/"
        self._many_base = "https://waifu.pics/api/many/sfw/"


    def get_image(self, category : str) -> dict:
        url = self._base + category
        response = self._session.get(url).json()
        return response

    def get_many_images(self, category : str) -> dict:
        url = self._many_base + category
        response = self._session.get(url).json()
        return response




class WaifuNSFW():
    def __init__(self):
        self._session = requests.Session()
        self._base = "https://waifu.pics/api/nsfw/"
        self._many_base = "https://waifu.pics/api/many/nsfw/"


    def get_image(self, category : str) -> dict:
        url = self._base + category
        response = self._session.get(url).json()
        return response

    def get_many_images(self, category : str) -> dict:
        url = self._many_base + category
        response = self._session.get(url).json()
        return response




