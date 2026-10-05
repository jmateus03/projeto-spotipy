def controleMusica(controle):

    if controle == "passar musica":
        sp.next_track()

    elif controle == "voltar musica":
        sp.previous_track()

    elif controle == "pular 10s":
        controlarTempo(10)

    elif controle == "voltar 10s":
        controlarTempo(-10)

    elif controle == "play":
        reproduzirMusica()

    else:
        print("Nada aconteceu")


def controleVolume(volume):

    try:
        volume = int(volume)

        if 0 <= volume <= 100:
            sp.volume(volume)
        else:
            print("O volume deve estar entre 0 e 100")

    except ValueError:
        print("Volume inválido")


def controlarTempo(tempo):

    musica = sp.current_playback()

    if musica is None:
        print("Nenhuma música está tocando")
        return

    tempo_atual = musica["progress_ms"]

    novo_tempo = tempo_atual + (tempo * 1000)

    novo_tempo = max(0, novo_tempo)

    sp.seek_track(novo_tempo)


def reproduzirMusica():

    musica = sp.current_playback()

    if musica is None:
        print("Nenhuma música está tocando")
        return

    if musica["is_playing"]:
        sp.pause_playback()
    else:
        sp.start_playback()