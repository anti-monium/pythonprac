from . import server

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        print('Server turned off')
