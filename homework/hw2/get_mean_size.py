"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys
from typing import List

def get_mean_size(ls_output: str) -> float:
    lines: List = ls_output.strip().split('\n')[1:]
    if len(lines) != 0:
        summ: int = 0
        lines_cnt = 0
        for line in lines:
            if line[0] != 'd':
                print(line)
                lines_cnt += 1
                summ += int(line.split()[4])
        return 0.0

if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(mean_size)


