"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime
app = Flask(__name__)

GREETINGS =(
    'Хорошего понедельника',
    'Хорошего вторника',
    'Хорошей среды',
    'Хорошего четверга',
    'Хорошей пятницы',
    'Хорошей субботы',
    'Хорошего воскресенья'
)


@app.route('/hello-world/<name>')
def hello_world(name: str) -> str:
    weekday: int = datetime.today().weekday()
    greeting: str = GREETINGS[weekday]
    return f'Привет, {name}. {greeting}!'


if __name__ == '__main__':
    app.run(debug=True)