import csv
import keyboard


def command_identification(arg):
    with open('commands.csv') as File:
        data = csv.reader(File)
        line = 0
        for row in data:
            if line == arg:
                return row
            line +=1


def per(oper, bits):
    bits = int(bits)
    a = bits//100
    b = bits%100
    oper = list(oper)
    oper[a-1], oper[b-1] = oper[b-1], oper[a-1]
    return ''.join(oper)
