import unittest
#   The unittest system splits testing up away from the code that is being tested.
# For display purposes, we will be testing the 'basic.py' module, which needs importing
import basic

#   unittest works alot like JUnit in Java. One must create a class that extends 
# unittest.TestCase. Then one writes functions within this class, which can be called 
# anything though must start with 'test'. Within these functions one writes 
# self.assertEqual functions to perform the actual testing.
# - assertEqual(first, second, msg = None)
# Test functions are all run. The assertEqual commands within these test are performed
# until one fails, ending that testing function.

# Setup And Teardown
# These are useful for setting up variables and states before testing begins.
#   setUp(self)  tearDown(self)
# these functions are run before and after each testing function is run

class AdderTest(unittest.TestCase):

    def setUp(self):
        self.importantString = "this is an important string"
        print ("setUp executed!")

    def tearDown(self):
        self.importantString = None
        print ("tearDown executed!")

    def testCalculation(self):
        print ("running test testCalculation")
        self.assertEqual(basic.adder(0,0), 0)
        self.assertEqual(basic.adder(1,0), 1)
        self.assertEqual(basic.adder(5,0), 58, "Hello") # this test will fail, thus execution will return here and produce a error on the console
        self.assertEqual(basic.adder(10,1), 11)
        self.assertEqual(basic.adder(20,20), 430)

    def testCalculation2(self):
        print ("running test testCalculation2")
        self.assertEqual(basic.adder(0,0), 0)
        self.assertEqual(basic.adder(1,0), 1)
        self.assertEqual(basic.adder(5,0), 5)
        self.assertEqual(basic.adder(10,1), 11)
        self.assertEqual(basic.adder(20,20), 430) # this test will fail, thus execution will return here and produce a error on the console

    def testCalculation3(self):
        print ("running test testCalculation3")
        # this test runs smooth, thus you won't hear much about it
        self.assertEqual(basic.adder(0,0), 0)
        self.assertEqual(basic.adder(1,0), 1)
        self.assertEqual(basic.adder(5,0), 5)
        self.assertEqual(basic.adder(10,1), 11)
        self.assertEqual(basic.adder(20,20), 40) 

"""
 ---- Assertions available within this class include ----

assertTrue(expr, msg=None)	                                            	                            	                            
    Checks if the expression "expr" is True.
assertFalse(expr, msg=None)	                                            	                            
    Checks if expression "expr" is False.

assertEqual(first, second, msg=None)	                                
    The test fails if the two objects are not equal as determined by the '==' operator.
assertGreater(a, b, msg=None)	                                        	                            
    Checks, if a > b is True.
assertGreaterEqual(a, b, msg=None)	                                    	                            
    Checks if a ≥ b
assertLess(a, b, msg=None)	                                            	                            
    Checks if a < b
assertLessEqual(a, b, msg=None)	                                        	                            
    Checks if a ≤ b

assertAlmostEqual(first, second, places=None, msg=None, delta=None)	    
    The test fails if the two objects are unequal as determined by their difference rounded to the given 
    number of decimal places (default 7) and comparing to zero, or by comparing that the between the two 
    objects is more than the given delta. Note that decimal places (from zero) are usually not the same 
    as significant digits (measured from the most significant digit). If the two objects compare equal 
    then they will automatically compare almost equal.

assertCountEqual(first, second, msg=None)	                            
    An unordered sequence comparison asserting that the same elements, regardless of order. If the same 
    element occurs more than once, it verifies that the elements occur the same number of times.  
        self.assertEqual(Counter(list(first)), Counter(list(second)))  
    Example:  
        [0, 1, 1] and [1, 0, 1] compare equal, because the number of ones and zeroes are the same. 
        [0, 0, 1] and [0, 1] compare unequal, because zero appears twice in the first list and only once in the second list. 

assertIn(member, container, msg=None)	                                	                            
    Checks if a in b

assertIsInstance(obj, cls, msg=None)	                                	                            
    Checks if isinstance(obj, cls).

assertIs(expr1, expr2, msg=None)	                                    	                            
    Checks if "a is b"
assertIsNot(expr1, expr2, msg=None)	                                    	                            
    Checks if "a is not b"

assertIsNone(obj, msg=None)	                                            	                            
    Checks if "obj is None"
assertIsNotNone(obj, msg=None)	                                        	                            
    Checks if obj is not equal to None

assertListEqual(list1, list2, msg=None)	                                	                            
    Lists are checked for equality.
assertTupleEqual(tuple1, tuple2, msg=None)	                            	                            
    Analogous to assertListEqual
assertDictEqual(d1, d2, msg=None)	                                    	                            
    Both arguments are taken as dictionaries and they are checked if they are equal.
assertMultiLineEqual(first, second, msg=None)	                        	                            
    Assert that two multi-line strings are equal.q
assertNotRegexpMatches(text, unexpected_regexp, msg=None)	            	                            
    Fails, if the text Text "text" of the regular expression unexpected_regexp matches.
"""

#   One must run the function unittest.testmod() using the same method of testing the 
# __name__ global as with basic testing.
if __name__ == "__main__": 
    unittest.main()