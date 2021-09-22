import requests
import unittest


class VerifyCall(unittest.TestCase):

    def test_call_endpoint(self):
        expected_result = {"Hello": "World"}
        actual_result = requests.get('http://127.0.0.1:8000/call')
        assert actual_result.json() == expected_result


class VerifyCallNegative(unittest.TestCase):

    def test_call_endpoint(self):
        expected_result = {"detail": "Method Not Allowed"}
        actual_result = requests.put('http://127.0.0.1:8000/call')
        assert actual_result.json() == expected_result


class VerifyCallMe(unittest.TestCase):

    def test_call_me_endpoint(self):
        test_data = {"my_number": "+380000000002"}
        expected_result = {'Patient Last Name': None, 'Patient First Name': None, 'Patient DOB': None,
                           'Patient Phone': '+380000000002', 'Patient Alt Phone': None}
        actual_result = requests.post('http://127.0.0.1:8000/call_me', json=test_data)
        assert actual_result.json() == expected_result


class VerifyCallMeNegative(unittest.TestCase):

    def test_call_me_endpoint(self):
        test_data = {"your_number": "+380000000002"}
        expected_result = {
            "detail": [
                {
                    "loc": [
                        "body",
                        "my_number"
                    ],
                    "msg": "field required",
                    "type": "value_error.missing"
                }
            ]
        }
        actual_result = requests.post('http://127.0.0.1:8000/call_me', json=test_data)
        assert actual_result.json() == expected_result


class VerifyCallMeNotString(unittest.TestCase):

    def test_call_me_endpoint(self):
        test_data = {"my_number": []}
        expected_result = {
            "detail": [
                {
                    "loc": [
                        "body",
                        "my_number"
                    ],
                    "msg": "str type expected",
                    "type": "type_error.str"
                }
            ]
        }
        actual_result = requests.post('http://127.0.0.1:8000/call_me', json=test_data)
        assert actual_result.json() == expected_result


if __name__ == "__main__":
    unittest.main()
