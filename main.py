from controleDeMusica import (
    controleMusica,
    controleVolume
)

import serial


ser = serial.Serial(
    port="COM3",
    baudrate=9600,
    timeout=1
)


while True:

    acao = ser.readline().decode().strip()

    if not acao:
        continue

    if len(acao) > 3:

        controleMusica(acao)

    else:

        controleVolume(acao)
