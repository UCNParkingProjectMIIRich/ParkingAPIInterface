from ParkingApi.retrievedata import ParkingAPIWrapper

def test_output_format():
    """
    check that a payload has been given
    """
    test_layout = {
        "payload": ""
    }
    wrapper = ParkingAPIWrapper(test_layout)

    data = wrapper.get_data()
    assert data['payload'] != ""
