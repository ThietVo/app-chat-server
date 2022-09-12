import unittest
from unittest import result
import requests


class TestMessageAPI(unittest.TestCase):
    URL = 'http://localhost:5001/messages/'

    result = [
        {
            "created_at": "Fri, 09 Sep 2022 01:07:38 GMT",
            "id": 1,
            "message": "message 1",
            "type": "http",
            "updated_at": "Fri, 09 Sep 2022 01:07:38 GMT",
            "userId": 1,
            "username": "user1"
        },
        {
            "created_at": "Fri, 09 Sep 2022 01:07:38 GMT",
            "id": 2,
            "message": "message 2",
            "type": "http",
            "updated_at": "Fri, 09 Sep 2022 01:07:38 GMT",
            "userId": 2,
            "username": "user2"
        },
        {
            "created_at": "Fri, 09 Sep 2022 01:07:38 GMT",
            "id": 3,
            "message": "message 1",
            "type": "http",
            "updated_at": "Fri, 09 Sep 2022 01:07:38 GMT",
            "userId": 3,
            "username": "user3"
        }
    ]

    mess = {
        'message': ' message test 1',
        'type': 'socket',
        'userId': 2,
    }

    def test_get_messages(self):
        res = requests.get(self.URL + 'http')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 3)
        self.assertListEqual(res.json(), self.result)
        print('Test 1 complete')

    def test_post_messages(self):
        res = requests.post(self.URL, json=self.mess)
        self.assertEqual(res.status_code, 200)
        print("Test 2 compeleted")

# if __name__ == '__main__':
#     unittest.main()
