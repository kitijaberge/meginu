import PySimpleGUI as sg


#jaizveido menu mainigo

menu_def=[['File ',['iziet']], ['Edit', ['Cut', 'Copy', 'Paste']]]
layout = [
    [sg.Menu(menu_def)],
    [sg.T("")],
    [sg.T("       "), sg.Button('Sveiki!', size=(8,4)),sg.Button('nekas', size=(8,4))],
    [sg.T("")],
    [sg.T("        "), sg.Checkbox('Drukāt',default=False,key='-IN-')],
    [sg.T("        "), sg.Radio('Ir atļauja', 'Radio1', default=False,key='-IN2-')],
    [sg.T("        "), sg.Radio('Nav atļauja', 'Radio1', default=False,key='-IN2-')],
    [sg.Multiline(size=(60,10), key='--vieta--')],
    [sg.Button('Iziet')]
]

window = sg.Window('nosaukums', layout, size=(500,500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Iziet":
        break
    elif event=='Sveiki!':
        if values["-IN-"] == True and values['-IN2-']==True:
            window['--vieta--'].update(f"Labrīt no rīta - cik jauks ir rīts!")

window.close()