from data import GoogleMapBody
from files import FileManager
from service import GoogleMapAPI


FILE_PATH = "list_of_place_id.txt"


def compare_values(value_name, current_value, expected_value):
    print(f"\n{value_name}\n{current_value=}\n{expected_value=}")
    assert current_value == expected_value, f"Incorrect value {current_value}"
    print(f"PASSED: Value '{current_value}' is correct!")


def get_body_for_delete_location(place_id):
    return {"place_id" : place_id}


class TestGoogleMapAPI:
    def __init__(self):
        self.__api = GoogleMapAPI()
        self.__body = GoogleMapBody()

    def test_create_location(self, expected_status_code):
        print("\n-----START TEST: Create location-----")
        response = self.__api.create_location(str(self.__body))
        print(f"RESPONSE:\n{response.json()}")

        compare_values(
            "POST STATUS CODE",
            response.status_code,
            expected_status_code
        )
        compare_values("POST STATUS", response.json().get('status'), "OK")
        print("TEST PASSED!")

    def test_find_location(self, expected_status_code):
        print("\nSTART TEST: Find location")
        post_response = self.__api.create_location(str(self.__body))
        compare_values("POST STATUS CODE", post_response.status_code, 200)
        place_id = post_response.json().get('place_id')

        get_response = self.__api.get_location(place_id)
        print(f"RESPONSE:\n{get_response.json()}")
        compare_values(
            "GET STATUS CODE",
            get_response.status_code,
            expected_status_code
        )
        print("-----TEST PASSED!-----")

    def test_create_multiple_locations(self, count=5):
        print(f"\n-----START TEST: Create multiple({count}) locations-----")
        list_of_place_id = list()
        for response in self.__api.create_multiple_locations(
                str(self.__body),
                count
        ):
            list_of_place_id.append(response.json().get('place_id'))

        compare_values(
            "LENGTH OF PLACE_ID LIST",
            len(list_of_place_id),
            count
        )
        print("-----TEST PASSED!-----")

    def test_record_place_id_list(self, list_length=5):
        print("\n-----START TEST: Record place_id list-----")

        initial_list = []
        for response in self.__api.create_multiple_locations(
                str(self.__body),
                list_length
        ):
            initial_list.append(response.json().get('place_id'))

        FileManager.write_list(FILE_PATH, initial_list)
        recorded_list = FileManager.read_line_by_line(FILE_PATH)
        compare_values(
            "CHECK RECORDED PLACE_ID LIST",
            recorded_list,
            initial_list
        )
        print("-----TEST PASSED!-----")

    def test_delete_location(self, expected_status_code):
        print("\n-----START TEST: Delete location------")
        post_response = self.__api.create_location(str(self.__body))
        compare_values("POST STATUS CODE", post_response.status_code, 200)
        place_id = post_response.json().get('place_id')

        delete_response = self.__api.delete_location(
            get_body_for_delete_location(place_id)
        )
        compare_values(
            "DELETE STATUS CODE",
            delete_response.status_code,
            expected_status_code
        )
        compare_values(
            "DELETE STATUS",
            delete_response.json().get('status'),
            'OK'
        )

        get_response = self.__api.get_location(place_id)
        compare_values("GET STATUS CODE", get_response.status_code, 404)
        compare_values(
            "GET MSG",
            get_response.json().get('msg'),
            "Get operation failed, looks like place_id  doesn't exists"
        )
        print("-----TEST PASSED!-----")

    def test_record_existing_locations(self, deleted_locations_id):
        print("\n-----START TEST: Record exists locations-----")
        new_file_path = "place_id_of_existing_locations"

        place_id_list = FileManager.read_line_by_line(FILE_PATH)
        for id in deleted_locations_id:
            self.__api.delete_location(
                get_body_for_delete_location(place_id_list[id-1])
            )

        count = 0
        existing_locations = []
        for response in self.__api.get_multiple_locations(place_id_list):
            if response.status_code == 200:
                existing_locations.append(place_id_list[count])
            count += 1

        compare_values(
            "LENGTH OF EXISTING LOCATIONS LIST",
            len(existing_locations),
            len(place_id_list)-len(deleted_locations_id)
        )

        FileManager.write_list(new_file_path, existing_locations)
        recorded_list = FileManager.read_line_by_line(new_file_path)
        compare_values(
            "CHECK RECORDED EXISTING LOCATIONS LIST",
            recorded_list,
            existing_locations
        )
        print("-----TEST PASSED!-----")
