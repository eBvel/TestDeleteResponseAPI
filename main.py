from tests import TestGoogleMapAPI


def main():
    tests = TestGoogleMapAPI()
    # Тестируем создание локации.
    tests.test_create_location(200)
    # Тестируем получение локации.
    tests.test_find_location(200)
    # Тестируем удаление локации.
    tests.test_delete_location(200)
    # Тестируем создание нескольких (5) локаций.
    tests.test_create_multiple_locations()
    # Тестируем запись созданных локаций в файл.
    tests.test_record_place_id_list()
    # Тестируем запись существующих (неудаленных) локаций в файл.
    tests.test_record_existing_locations([2, 4])


if __name__ == "__main__":
    main()