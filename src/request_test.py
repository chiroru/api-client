# -*- coding: utf-8 -*-

from unittest import TestCase
from request import Request

class RequestTestCase(TestCase):
    
    def setUp(self):
        TestCase.setUp(self)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_sum(self):
        r = Request('/test/1', 1)
        r.countUp(5)
        r.countUp(9)
        
        self.assertEqual(15, r.getSum())
        
    def test_average(self):
        r = Request('/test/1', 1)
        r.countUp(5)
        r.countUp(9)
        
        self.assertEqual(5, r.getAverage())