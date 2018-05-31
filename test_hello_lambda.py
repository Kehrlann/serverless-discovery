import unittest
import hello_handler


class LambdaSimpleTest(unittest.TestCase):

    def test_has_200_response_code(self):
        response = hello_handler.handle()
        self.assertEqual(200, response["statusCode"])

    def test_says_hello(self):
        no_name = hello_handler.handle()
        anton = hello_handler.handle(
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
