"""
This file is responsible for retrieving parking data and translating it into a commonly defined language
"""
import copy
import requests

DOMAIN = "https://parkingapi.martinusnel.com/parkingservice"


class ParkingAPIWrapper:
    def __init__(self, unified_layout):
        """
        initialise the wrapper
        :param unified_layout: the layout in which to return a message - the intention of this parameter is to fit with
            a unified language
        """
        self.unified_layout = unified_layout

    def get_data(self):
        response = requests.get(DOMAIN)
        response_text = response.json()

        return_struct = copy.copy(self.unified_layout)
        return_struct['payload'] = response_text

        return return_struct


if __name__ == "__main__":
    test_layout = {
        "payload": ""
    }
    wrapper = ParkingAPIWrapper(test_layout)
    print(wrapper.get_data())
