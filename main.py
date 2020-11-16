"""
var: 1:10.15
1 adress
30 bits

"""
import random
import utils
import keyboard

i = -1
R1 = f'{random.getrandbits(30):030b}'
R2 = f'{random.getrandbits(30):030b}'
R3 = f'{random.getrandbits(30):030b}'
AC = R1  # accumulator
PS = '+'  # status register
CC = 1  # commands.csv count
TC = 1  # tacts count


def programm():
    global R1, R2, R3, AC, PS, CC, TC, i
    if keyboard.is_pressed('shift'):
        i += 1
    try:
        command = utils.command_identification(i // 2)
        IR = ','.join(command)  # commmand
    except TypeError:
        print('programm ended')
        exit()
    if i > 0:   #realisation of tacts count and commands count
        TC += 1
        if TC % 2 == 1:
            CC += 1
            TC = 1

    if command[0] == 'mov' and TC ==2:
        command[2] = int(command[2])
        if int(command[2]) < 0:
            PS = '-'
            command[2] = -command[2]
        else:
            PS = '+'
        x = lambda i: '{:030b}'.format(i)
        if command[1]== 'R1':
            R1 = x(command[2])
        elif command[1] == 'R2':
            R2 = x(command[2])
        else:
            R3 = x(command[2])
        AC = x(command[2])
    if command[0] == 'per' and TC ==2:
        if command[1]== 'R1':
            R1 = utils.per(R1, command[2])
        elif command[1]== 'R2':
            R2 = utils.per(R2, command[2])
        else:
            R3 = utils.per(R3, command[2])


    print(f'IR: {IR}')
    print(f'R1: {R1}')
    print(f'R2: {R2}')
    print(f'R3: {R3}')
    print(f'AC: {AC}')
    print(f'PS: {PS}')
    print(f'CC: {CC}')
    print(f'TC: {TC} \n')


if __name__ == '__main__':
    keyboard.add_hotkey('shift', lambda: programm())
    keyboard.wait('esc')
