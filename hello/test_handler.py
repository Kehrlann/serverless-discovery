import unittest
from hello import handler


class LambdaSimpleTest(unittest.TestCase):

    def test_has_200_response_code(self):
        response = handler.handle()
        self.assertEqual(200, response["statusCode"])

    def test_says_hello(self):
        no_name = handler.handle()
        anton = handler.handle(
            {
                "queryStringParameters":
                    {
                        "name": "Anton",
                        "garbage": 42
                    }
            }
        )

        self.assertEqual("Hello World", no_name["body"])
        self.assertEqual("Hello Anton", anton["body"])
