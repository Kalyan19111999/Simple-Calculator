import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [
    [sg.In(size = (20,15), enable_events = True, key = "Op_Space")],
    [sg.HSeparator()],
    [sg.Button('1', size = (3,2), key = '1', enable_events = True), sg.Button('2', size = (3,2), key = '2', enable_events = True), sg.Button('3', size = (3,2), key = '3', enable_events = True)],
    [sg.HSeparator()],
    [sg.Button('4', size = (3,2), key = '4', enable_events = True), sg.Button('5', size = (3,2), key = '5', enable_events = True), sg.Button('6', size = (3,2), key = '6', enable_events = True)],
    [sg.HSeparator()],
    [sg.Button('7', size = (3,2), key = '7', enable_events = True), sg.Button('8', size = (3,2), key = '8', enable_events = True), sg.Button('9', size = (3,2), key = '9', enable_events = True)],
    [sg.HSeparator()],
    [sg.Button('0', size = (3,2), key = '0', enable_events = True), sg.Button('+', size = (3,2), key = '+', enable_events = True), sg.Button('-', size = (3,2), key = '-', enable_events = True)],
    [sg.HSeparator()],
    [sg.Button('*', size = (3,2), key = '*', enable_events = True), sg.Button('/', size = (3,2), key = '/', enable_events = True), sg.Button('=', size = (3,2), key = '=', enable_events = True)],
    [sg.HSeparator()],
    [sg.Button("Backspace", size = (9,1), key = "backspace"), sg.Button("Clear", size = (4,1), key = "clear")]
]

window = sg.Window("Calculator", layout, size = (160,350))

Number_1 = ''
Number_2 = ''
Operation = ''
Digits = ['1','2','3','4','5','6','7','8','9','0']
Operators = ['+','-','*','/']
while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event in Digits:
        
        if Operation == '':
            Number_1 += event
            window["Op_Space"].update(Number_1)
            
        else:
            Number_2 += event
            window["Op_Space"].update(Number_1 + Operation + Number_2)

    elif event in Operators:
        Operation = event
        window["Op_Space"].update(Number_1 + Operation)

    elif event == '=':
        if Number_1 == '' or Number_2 == '':
            pass
        else:
            window["Op_Space"]('')
            if Operation == '+':
                window["Op_Space"].update(int(Number_1) + int(Number_2))
            elif Operation == '-':
                window["Op_Space"].update(int(Number_1) - int(Number_2))
            elif Operation == '*':
                window["Op_Space"].update(int(Number_1) * int(Number_2))
            elif Operation == '/':
                window["Op_Space"].update(int(Number_1) / int(Number_2))
            Number_1 = ''
            Number_2 = ''
            Operation = ''

    elif event == "backspace":
        if Operation == '':    
            Number_1 = Number_1[:-1]
            window["Op_Space"].update(Number_1)
        elif Number_2 == '':
            Operation = ''
            window["Op_Space"].update(Number_1 + Operation)
        else:
            Number_2 = Number_2[:-1]
            window["Op_Space"].update(Number_1 + Operation + Number_2)

    elif event == "clear":
        window["Op_Space"]('')
        Number_1 = ''
        Number_2 = ''
        Operation = ''
    
    else:
        pass
    
    window.refresh()

window.close()