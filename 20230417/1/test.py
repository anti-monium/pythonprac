import unittest
from moodserver import server
from moodclient import client
import socket
import multiprocessing
import time
import cowsay

class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.proc = multiprocessing.Process(target=server.start)
        cls.proc.start()
        time.sleep(1)
        cls.gamer = client.Cli_Dungeon('TeStNaMe', completekey='tab')
        
    def setUp(self):
        pass
        
    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.gamer.do_exit('')
        
    def tearDown(self):
        pass
        
    def test_0(self):
        self.gamer.do_down('')
        ans = self.gamer.dungeon_socket.recv(4096).decode().strip()
        self.assertEqual(ans, 'Moved to (0, 1)')
        
    def test_1(self):
        self.gamer.do_addmon('sheep hello priv hp 15 coords 0 0')
        ans = self.gamer.dungeon_socket.recv(4096).decode().strip()
        self.assertEqual(ans, 'Added monster sheep to (0, 0) saying priv')
    
    def test_2(self):
        self.gamer.do_up('')
        ans = self.gamer.dungeon_socket.recv(4096).decode().strip()
        self.assertEqual(ans, 'Moved to (0, 0)' + '\n' + cowsay.cowsay('priv', cow='sheep'))
        
    def test_3(self):
        self.gamer.do_attack('sheep with sword')
        ans = self.gamer.dungeon_socket.recv(4096).decode().strip()
        self.assertEqual(ans, 'Attacked sheep, damage 10\nsheep now has 5 health points')
