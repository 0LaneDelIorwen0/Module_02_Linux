"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""


import os

def get_summary_rss(ps_output_file_path: str) -> str:
    summary: int = 0
    with open(ps_output_file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines()[1:]:
            summary += int(line.split()[5])
    return rss_hum(summary)

def rss_hum(value: int) -> str:
    if value < 1024:
        return f'Потребляемая память: {value} Кб'
    elif 1023 < value < 1048576:
        return f'Потребляемая память: {value//1024} Мб'
    elif 1048575 < 1073741824:
        return f'Потребляемая память: {value//1048576} Гб'


if __name__ == '__main__':
    os.system('ps aux --sort=%mem > output_file.txt')
    path: str = 'output_file.txt'
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)

