from serial.tools import list_ports
from PyQt5.QtCore import QThread


def portlist():
    return sorted([port.device for port in list_ports.comports()])


def binary_converted(data):
    bin_conv = [] * len(data)
    for binx in data:
        bin_conv.append(bin(binx)[2:].__add__('0' * (8 - len(bin(binx[3])[2:]))))  # Добавить нули справа
    return bin_conv


def strToBin(data):
    # data_arr = [None] * len(data)
    #
    # for i in range(len(data)):
    #     data_arr[i] = data[i]

    data_arr = bytearray(data)

    data_out = [] * len(data)
    if len(data) > 6:
        data_out[0] = data_arr[0]
        data_out[1] = data_arr[1]
        data_out[2] = data_arr[2]
        data_out[3] = bin(data_arr[3])[2:].zfill(8)
        data_out[4] = bin(data_arr[4])[2:].zfill(8)
        data_out[5] = bin(data_arr[5])[2:].zfill(8)
        data_out[6] = data_arr[6]
        # data_out[6] = ord(ControlSum(str(data_arr)))
    return data_out


def listToString(s):
    # initialize an empty string
    str1 = ""
    result = str1.join(map(str, s))
    # return string
    return result


def ControlSum(bytebuff):
    x = 0
    for byte_str in bytebuff:
        x += ord(byte_str)
    # print(x)
    return chr(x)


def WriteCoM(bytebuff):
    writestr = bytebuff + [ControlSum(bytebuff)]
    return listToString(writestr).encode('raw_unicode_escape')


def SendMess(bytebuff, ser):
    data = WriteCoM(bytebuff)
    ser.write(data)


def ReadMess(ser):
    data = ser.readline(ser.inWaiting())
    return data


def thread_SendRead(bytebuff, ser):
    SendMess(bytebuff, ser)
    QThread.msleep(2)  # Задержка между отправкой и приемом
    rx_data = ReadMess(ser)
    return rx_data
