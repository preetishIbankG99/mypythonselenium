import unittest


def setUpModule():
    print("SetUpModule")

def tearDownModule():
        print("TearDownModule")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is LoginTest")

    @classmethod
    def tearDown(self):
     print("This is LogoutTest")

    @classmethod
    def setUpClass(cls):
       print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("This is Search Test")


    def test_advancesearch(self):
        print("This is AdvanceSearch Test")

    def test_prepaidrechargr(self):
        print("This is PrepaidRecharge Test")

    def test_postpaidrechargr(self):
        print("This is PostpaidRecharge Test")

        if __name__ == "__main__":
            unittest.main()