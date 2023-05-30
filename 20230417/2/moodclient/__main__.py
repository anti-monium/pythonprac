from . import client
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print('You must enter your nickname before starting the game')
            exit()
        nickname = sys.argv[1]
        cli = client.Cli_Dungeon(nickname, completekey='tab')
    except Exception:
        print('Your session was interrupted')
