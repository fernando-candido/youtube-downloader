import pytube
import colorama 
import time

colorama.init()
print('\033[0;31;107m#### Bem vindo! ###')
print('\033[0;31;107mDigite a URL do video que quer baixar: ')
link = input('')
youtube = pytube.YouTube(link)
print('\033[0;31;107m** '+'Baixando...')
baixar = youtube.streams.get_highest_resolution()
baixar.download(output_path='C:/Users/Public/Desktop')
if(baixar.download):
    print('\033[0;31;107m** '+ youtube.title + ' **  baixado com sucesso!! ')
    print('\033[0;31;107m** '+'O vídeo está na sua área de trabalho.')
    print('\033[0;31;107m** '+'Obrigado!')
    time.sleep(5)

# https://www.youtube.com/watch?v=aUQ2M9bYe58