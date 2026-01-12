from dataclasses import dataclass, field


@dataclass
class GoogleMapEndPoints:
    base_url = "https://rahulshettyacademy.com"
    key_param: str = "?key=qaclick123"
    url_of_create_location : str = \
        f"{base_url}/maps/api/place/add/json{key_param}"
    url_of_edit_location : str = \
        f"{base_url}/maps/api/place/update/json{key_param}"
    url_of_get_location : str = \
        f"{base_url}/maps/api/place/get/json{key_param}"
    url_of_delete_location : str = \
        f"{base_url}/maps/api/place/delete/json{key_param}"


@dataclass
class GoogleMapBody:
    lat : float = -38.383494
    lng: float = 33.427362
    location: str = field(
                    init=False,
                    default=f'{{"lat": {lat}, "lng": {lng}}}'
                    )
    accuracy : int = 50
    name : str = "Frontline house"
    phone_number : str = "(+91) 983 893 3937"
    address : str = "29, side layout, cohen 09"
    new_address : str = "100 Lenina street, RU"
    types: str = f'["shoe park", "shop"]'
    website : str = "http://google.com"
    language : str = "French-IN"
    key: str = "qaclick123"

    def __repr__(self):
        return (f'{{\n"location": {self.location},\n'
                f'"accuracy": {self.accuracy},\n'
                f'"name": "{self.name}",\n'
                f'"phone_number": "{self.phone_number}",\n'
                f'"address": "{self.address}",\n'
                f'"types": {self.types},\n'
                f'"website": "{self.website}",\n'
                f'"language": "{self.language}"\n}}')

    def get_body_for_put_request(self, place_id):
        return (f'{{\n"place_id": "{place_id}",\n'
                f'"address": "{self.new_address}",\n'
                f'"key": "{self.key}"\n}}')