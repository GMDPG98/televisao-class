class Televisao:
    def __init__(self, canal, volume, mute):
        self.canal = canal
        self.volume = volume
        self.mute = mute

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1

    def muda_volume_para_baixo(self):
        self.volume -= 1

    def muda_volume_para_cima(self):
        self.volume += 1

    def liga_mute(self):
        self.mute = True

    def desliga_mute(self):
        self.mute = False


if __name__ == '__main__':
    tv = Televisao(5, 10, False)
    print('Canal inicial:', tv.canal)
    print('Volume:', tv.volume)
    print('Mudo:', tv.mute)

    tv.mute = False
    tv.canal = 5
    tv.volume = 10

    print('Volume inicial:', tv.volume)
    print('Canal inicial:', tv.canal)
    print('Está mudo?:', tv.mute)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal -', tv.canal)
    tv.muda_volume_para_cima()
    print('Volume +', tv.volume)
    tv.muda_volume_para_cima()
    print('Volume +', tv.volume)
    tv.muda_volume_para_baixo()
    print('Volume -', tv.volume)
    tv.liga_mute()
    print('Mudo Ligado', tv.mute)
    tv.desliga_mute()
    print('Mudo Desligado', tv.mute)
