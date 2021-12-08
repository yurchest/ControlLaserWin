from PyQt5.QtGui import QPixmap


def setLeds(self):
    # -------------------------------------------------------------------#
    #                       Байт состояния ВПЛП-М                        #
    # -------------------------------------------------------------------#

    if self.dataBin[3][0] == '0':  # Местное управление
        self.w_root.label_44.setPixmap(QPixmap(self.ICON_GREEN_LED))
        self.w_root.label_45.setPixmap(QPixmap(self.ICON_RED_LED))

    elif self.dataBin[3][0] == '1':  # Центральное управление
        self.w_root.label_45.setPixmap(QPixmap(self.ICON_GREEN_LED))
        self.w_root.label_44.setPixmap(QPixmap(self.ICON_RED_LED))

    if self.dataBin[3][1] == '0':  # Внутрення синхронизация
        self.w_root.label_37.setText('Внутр')
        self.w_root.label.setText(" ")
    elif self.dataBin[3][1] == '1':  # Внешняя синхронизация
        self.w_root.label_37.setText('Внешн')
        if self.dataBin[3][6] == '0':  # Внешние синхроимпульсы в норме
            self.w_root.label.setStyleSheet('color: rgb(111, 189, 100)')
            self.w_root.label.setText("Внешние синхроимпульсы в норме")
        elif self.dataBin[3][6] == '1':  # Ошибка поступления внешних синхроимпульсов
            self.w_root.label.setText("Ошибка поступления внешних синхроимпульсов")
            self.w_root.label.setStyleSheet('color: rgb(255, 0, 0)')

    if self.dataBin[3][2:4] == '00':  # Ожидание готовности
        self.w_root.label_55.setText('Ожидание готовности')
        self.w_root.label_55.setStyleSheet('background-color: rgb(211, 255, 183,100); border-radius: 20')
    elif self.dataBin[3][2:4] == '01':  # Готов
        self.w_root.label_55.setText('Готов')
        self.w_root.label_55.setStyleSheet('background-color: rgb(255, 255, 0,100); border-radius: 20')
    elif self.dataBin[3][2:4] == '10':  # Работа
        self.w_root.label_55.setText('Работа')
        self.w_root.label_55.setStyleSheet('background-color: rgb(0, 255, 0,100); border-radius: 20')
    else:
        self.w_root.label_55.setText('? Неизвестно ?')
        self.w_root.label_55.setStyleSheet('background-color: rgb(255, 0, 0,100); border-radius: 20')

    if self.dataBin[3][4] == '0':  # В системе присутсвуют ошибки
        self.w_root.label_54.setText('Да')
        self.w_root.label_54.setStyleSheet('border-radius: 14;background-color: rgb(255, 0, 0,120);')
    elif self.dataBin[3][4] == '1':  # Ошибок нет
        self.w_root.label_54.setText('Нет')
        self.w_root.label_54.setStyleSheet('border-radius: 14;background-color: rgb(25, 255, 0, 100);')

    if self.dataBin[3][5] == '0':  # Система охлаждения не готова
        self.w_root.label_41.setPixmap(QPixmap(self.ICON_RED_LED))
    elif self.dataBin[3][5] == '1':  # Система охлаждения готова
        self.w_root.label_41.setPixmap(QPixmap(self.ICON_GREEN_LED))

    if self.dataBin[3][7] == '1':  # Выходная энергия выходит за границы допустимого диапазона (не ошибка)
        pass

    if self.requestModules:
        # -------------------------------------------------------------------#
        #                   Старший байт состояния модулей                   #
        # -------------------------------------------------------------------#
        if self.dataBin[4][0] == '0':  # Модуль задающего генератора не готов
            self.w_root.label_47.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[4][0] == '1':  # Модуль задающего генератора готов
            self.w_root.label_47.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[4][1] == '1':  # Ошибка модуля задающего генератора
            self.w_root.label_46.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[4][2] == '0':  # Модуль задающего генератора не работет
            self.w_root.label_48.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[4][2] == '1':  # Модуль задающего генератора работает
            self.w_root.label_48.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[4][3] == '0':  # Модуль регенеративного усилителя не готов
            self.w_root.label_26.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[4][3] == '1':  # Модуль регенеративного усилителя готов
            self.w_root.label_26.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[4][4] == '1':  # Ошибка модуля регенеративного усилителя
            self.w_root.label_25.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[4][5] == '0':  # Модуль регенеративного усилителя не работает или 1064 не в норме
            self.w_root.label_58.setText('Не в норме')
            self.w_root.label_58.setStyleSheet('border-radius: 14;background-color: rgb(255, 0, 0,120);')
            self.isEn1064 = False
        elif self.dataBin[4][5] == '1':  # Модуль регенеративного усилителя работает 1064 в норме
            self.w_root.label_58.setText('В норме')
            self.w_root.label_58.setStyleSheet('border-radius: 14;background-color: rgb(25, 255, 0, 100);')
            self.isEn1064 = True

        if self.dataBin[4][6] == '0':  # Модуль регенеративного усилителя не работает или 532  не в норме
            self.w_root.label_59.setText('Не в норме')
            self.w_root.label_59.setStyleSheet('border-radius: 14;background-color: rgb(255, 0, 0,120);')
            self.isEn532 = False
        elif self.dataBin[4][7] == '1':  # Модуль регенеративного усилителя работает 532 в норме
            self.w_root.label_59.setText('В норме')
            self.w_root.label_59.setStyleSheet('border-radius: 14;background-color: rgb(25, 255, 0, 100);')
            self.isEn532 = True

        if self.isEn532 and self.isEn1064:
            self.w_root.label_27.setPixmap(QPixmap(self.ICON_GREEN_LED))
        else:
            self.w_root.label_27.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[4][7] == '0':  # Пустой бит (Всегда 0)
            pass
        elif self.dataBin[4][7] == '1':
            pass

        # -------------------------------------------------------------------#
        #                   Младший байт состояния модулей                   #
        # -------------------------------------------------------------------#

        if self.dataBin[5][0] == '0':  # Модуль накачки 1 не готов
            self.w_root.label_8.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][0] == '1':  # Модуль накачки 1 готов
            self.w_root.label_8.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][1] == '1':  # Ошибка модуля накачки 1
            self.w_root.label_10.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[5][2] == '0':  # Модуль накачки 1 не работает
            self.w_root.label_9.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][2] == '1':  # Модуль накачки 1 работает
            self.w_root.label_9.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][3] == '0':  # Модуль накачки 2 не готов
            self.w_root.label_12.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][3] == '1':  # Модуль накачки 2 готов
            self.w_root.label_12.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][4] == '1':  # Ошибка модуля накачки 2
            self.w_root.label_11.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[5][5] == '0':  # Модуль накачки 2 не работает
            self.w_root.label_13.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][5] == '1':  # Модуль накачки 2 работает
            self.w_root.label_13.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][6] == '0':  # Перключатель синхронизации в положении ВНУТР
            self.w_root.label_34.setText('ВНУТР')
        elif self.dataBin[5][6] == '1':  # Перключатель синхронизации в положении ВНЕШН
            self.w_root.label_34.setText('ВНЕШН')

        if self.dataBin[5][7] == '0':  # Переключатель МУ/ЦУ находится в положении МУ
            self.w_root.label_36.setText('МУ')
        elif self.dataBin[5][7] == '1':  # Переключатель МУ/ЦУ находится в положении ЦУ
            self.w_root.label_36.setText('ЦУ')

    elif not self.requestModules:

        # -------------------------------------------------------------------#
        #                   Старший байт состояния устройств                 #
        # -------------------------------------------------------------------#

        if self.dataBin[4][0] == '0':  # Термоконтроллер АЭ не готов
            self.w_root.label_71.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[4][0] == '1':  # Термоконтроллер АЭ готов
            self.w_root.label_71.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[4][1] == '1':  # Ошибка термоконтроллера АЭ
            self.w_root.label_72.setPixmap(QPixmap(self.ICON_RED_LED))

        # Добавил Егоров Петр

        if self.dataBin[4][2] == '0':  # Термоконтроллер ГВГ не готов
            self.w_root.label_73.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[4][2] == '1':  # Термоконтроллер ГВГ готов
            self.w_root.label_73.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[4][3] == '1':  # Ошибка термоконтроллера ГВГ
            self.w_root.label_74.setPixmap(QPixmap(self.ICON_RED_LED))

        # -------------------------------------------------------------------#
        #                   Младший байт состояния устройств                 #
        # -------------------------------------------------------------------#

        if self.dataBin[5][0] == '0':  # Термоконтроллер LD1 не готов
            self.w_root.label_60.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][0] == '1':  # Термоконтроллер LD1 готов
            self.w_root.label_60.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][1] == '1':  # Ошибка Термоконтроллера LD1
            self.w_root.label_61.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[5][2] == '0':  # Выходная мощность LD1 не в норме
            self.w_root.label_62.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][2] == '1':  # Выходная мощность LD1 в норме
            self.w_root.label_62.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][3] == '1':  # Ошибка драйвера тока LD1
            self.w_root.label_66.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[5][4] == '0':  # Термоконтроллер LD2 не готов
            self.w_root.label_80.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][4] == '1':  # Термоконтроллер LD2 готов
            self.w_root.label_80.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][5] == '1':  # Ошибка Термоконтроллера LD2
            self.w_root.label_81.setPixmap(QPixmap(self.ICON_RED_LED))

        if self.dataBin[5][6] == '0':  # Выходная мощность LD2 не в норме
            self.w_root.label_82.setPixmap(QPixmap(self.ICON_RED_LED))
        elif self.dataBin[5][6] == '1':  # Выходная мощность LD2 в норме
            self.w_root.label_82.setPixmap(QPixmap(self.ICON_GREEN_LED))

        if self.dataBin[5][7] == '1':  # Ошибка драйвера тока LD2
            self.w_root.label_84.setPixmap(QPixmap(self.ICON_RED_LED))
