import unittest
import prog
import socket
import multiprocessing
import time


class TestSqroots(unittest.TestCase):

    def test_0_sqroots(self):
        self.assertEqual(prog.sqroots('1 2 3'), '')
        
    def test_1_sqroots(self):
        self.assertEqual(prog.sqroots('1 6 9'), '-3.0')
        
    def test_2_sqroots(self):
        self.assertEqual(prog.sqroots('2 5 2'), '-0.5 -2.0')
        
    def test_exception_sqroots(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(prog.sqroots('0 2 3'), '')
            
            
class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.proc = multiprocessing.Process(target=prog.serve)
        cls.proc.start()
        time.sleep(1)
        
    def setUp(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', 1337))
        
    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        
    def tearDown(self):
        self.socket.close()
        
    def test_0(self):
        self.assertEqual(prog.sqrootnet('2 5 2', self.socket), '-0.5 -2.0')
