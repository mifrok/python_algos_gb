"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""
import time

# logins = {  # 'login': [pass, activation_status]
#     'name1': ['123', True],
#     'name2': ['456', False],
#     'name3': ['789', True],
#     'name4': ['741', False],
#     'name5': ['852', True],
#     'name6': ['963', True]
# }
start = time.time()
logins = {
    'name' + str(x): ['123', x % 3 == 0] for x in range(9999999)
}  # каждый третий не активирован
stop = time.time()
print(stop - start)  # Генерация 10 миллионов записей за 10 секунд


##############################################################################
class User:
    def __init__(self):
        self.login = input('Введите логин: ')
        self.password = input('Введите пароль: ')
        self.authentication()

    def authentication(self):
        """O (N), самая сложная операция not in"""
        if self.login not in logins.keys():
            print('Вы не зарегистрированы в системе')
            return
        elif self.password != logins[self.login][0]:
            print('Неверный пароль')
            return
        elif not logins[self.login][1]:
            print('Ваша учетная запись не активирована, ссылка для активации '
                  'направлена на email')
            return
        else:
            print('Добро пожаловать!')


new_user = User()
##############################################################################
# Не придумал другой способ, отличающийся от описанного выше :(
