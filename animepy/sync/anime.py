import requests

class Anime():
    def __init__(self):
        self._session = requests.Session()
        self._base = "https://kitsu.io/api/edge"
        self._kitsu_headers = {
            "Accept" : "application/vnd.api+json",
            "Content-Type" : "application/vnd.api+json"
        }


    def search(self, search_term : str):
        search_term = search_term.replace(" ", r"%20")
        url = self._base +  "/anime?filter[text]={}".format(search_term)
        response = self._session.get(url, headers = self._kitsu_headers).json()
        return response

    def advanced_search(self, filter_data : dict):
        filter_type = filter_data.get("filter_type")
        if filter_type is None:
            raise ValueError("Params Dict does not contain filter_type key!")
        values = filter_data.get("values")
        if values is None:
            raise ValueError("Params Dict does not contain values key!")

        url = self._base + "anime?filter[{}]={}".format(filter_type, values)
        response = self._session.get(url, headers = self._kitsu_headers).json()
        return response












