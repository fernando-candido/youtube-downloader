import PySimpleGUI as sg
from pytube import YouTube

layout = [[sg.Text('Informe o link do vídeo: '), sg.InputText()], # primeira linha
            [sg.Text('Informe a pasta para silvar: '), sg.InputText(),
            sg.FolderBrowse()], # segunda linha
            [(sg.Button('Baixar'), sg.Button('Cancelar'))] # terceira linha
            ]

janela = sg.Window("VideoDonwloader", layout)

while True:
    event, values = janela.read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break 
    elif event == 'Baixar':
        video = YouTube (values[0])
        video.streams.get_highest_resolution ().download (output_path=values[1])
        sg.popup_ok("Download concluido com sucesso!")
        
janela.close()
