import unittest

class AppTesting(unittest.TestCase):
#@unittest.SkipTest
#@unittest.skip("This is not ready so I am Skipping")
#@unittest.skipIf(1==1."One is Equal 1")
 def test_search(self):
  print("This is Search Test")


 def test_advancesearch(self):
  print("This is AdvanceSearch Test")


 def test_prepaidrechargr(self):
  print("This is PrepaidRecharge Test")


 def test_postpaidrechargr(self):
  print("This is PostpaidRecharge Test")

 def test_loginfacebook(self):
  print("This is facebook Test")


 def test_logintwitter(self):
  print("This is twitter Test")

if __name__ == "__main__":
        unittest.main()