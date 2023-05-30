import unittest
from moodclient import client
from unittest.mock import MagicMock

class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = MagicMock()
        cls.gamer = client.Cli_Dungeon
        cls.gamer.__init__ = lambda args: None
        cls.gamer.request = lambda command: setattr(cls.server, 'command', command)
        cls.game = cls.gamer()
        
    def setUp(self):
        pass
        
    def test_0(self):
        self.game.do_down('')
        self.assertEqual(self.server.command, 'move 0 1')
        
    def test_1(self):
        self.game.do_attack('sheep')
        self.assertEqual(self.server.command, 'attack sheep sword')
    
    def test_2(self):
        self.server.command = ''
        self.game.do_attack('igor')
        self.assertEqual(self.server.command, '')
