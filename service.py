from requests import Session
from data import GoogleMapEndPoints


class GoogleMapAPI:
    def __init__(self):
        self.__end_points = GoogleMapEndPoints
        self.session = Session()

    def create_location(self, body):
        url = self.__end_points.url_of_create_location
        print(f"POST URL: {url}")
        with self.session as session:
            return session.post(url, body)

    def get_location(self, place_id):
        url = self.__end_points.url_of_get_location + f"&place_id={place_id}"
        print(f"GET URL: {url}")
        with self.session as session:
            return session.get(url)

    def get_multiple_locations(self, list_of_place_id):
        with self.session as session:
            for id in list_of_place_id:
                url = self.__end_points.url_of_get_location \
                      + f"&place_id={id}"
                print(f"GET URL: {url}")
                yield session.get(url)

    def create_multiple_locations(self, body, count_iterations):
        url = self.__end_points.url_of_create_location
        with self.session as session:
            for i in range(count_iterations):
                print(f"POST URL: {url}")
                yield session.post(url, body)

    def delete_location(self, body):
        url = self.__end_points.url_of_delete_location
        print(f"DELETE URL: {url}")
        with self.session as session:
            return session.delete(url, json=body)

    def delete_multiple_location(self, list_of_body):
        url = self.__end_points.url_of_delete_location
        print(f"DELETE URL: {url}")
        with self.session as session:
            for body in range(list_of_body):
                yield session.delete(url, json=body)