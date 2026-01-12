import requests
from data import GoogleMapEndPoints


class GoogleMapAPI:
    def __init__(self):
        self.__end_points = GoogleMapEndPoints()

    def create_location(self, body):
        url = self.__end_points.url_of_create_location
        print(f"POST URL: {url}")
        return requests.post(url, body)

    def get_location(self, place_id):
        url = self.__end_points.url_of_get_location + f"&place_id={place_id}"
        print(f"GET URL: {url}")
        return requests.get(url)

    def get_multiple_locations(self, list_of_place_id):
        for id in list_of_place_id:
            url = self.__end_points.url_of_get_location + f"&place_id={id}"
            print(f"GET URL: {url}")
            yield requests.get(url)

    def create_multiple_locations(self, body, count_iterations):
        url = self.__end_points.url_of_create_location
        for i in range(count_iterations):
            print(f"POST URL: {url}")
            yield requests.post(url, body)

    def delete_location(self, body):
        url = self.__end_points.url_of_delete_location
        print(f"DELETE URL: {url}")
        return requests.delete(url, json=body)

    def delete_multiple_location(self, list_of_body):
        url = self.__end_points.url_of_delete_location
        print(f"DELETE URL: {url}")
        for body in range(list_of_body):
            yield requests.delete(url, json=body)