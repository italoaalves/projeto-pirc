import socket
import json
from os import system, name

from views.voter.count import count
from views.voter.vote import vote

HOST = '127.0.0.1'
PORT = 40000
TAM_MSG = 1024

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)


options = [quit, vote, count]


if __name__ == "__main__":
    while True:
        system('cls' if name == 'nt' else 'clear')
        print("Digital ballot box")
        print('''
            (1) Vote
            (2) Count Votes

            (0) Exit program
            ''')

        opt = int(input('> '))

        system('cls' if name == 'nt' else 'clear')

        request = options[opt]()

        sock.send(str.encode(json.dumps(request)))

        while True:
            response = sock.recv(TAM_MSG)

            if response:
                break

        response = json.loads(response.decode())

        if "status" in response:
            print(response)
        else:
            for candidate, votes in response.items():
                print(f'Candidato: {candidate}: {votes} votos')
            input("ENTER para continuar")

    sock.close()
