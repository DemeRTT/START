## Инструкция по запуску проекта:
1. Установить фреймворк **NiceGUI**
   ```bash
   python -m pip install nicegui
   ```
2. Склонировать файлы с репозитория
   ```bash
   git clone https://github.com/DemeRTT/incidents-and-hackers.git
   ```
3. Формы запускать с помощью следующих команд
    * Для инцидентов ИБ
    ```bash
    python incidents.py
    ```
    * Для хакерских группировок
    ```bash
    python hackers.py
    ```
4. Для завершения проекта достаточно нажать сочетание клавиш **`ctrl+c`**
> P.S. после нажатия кнопки **"Отправить"** внутри любой из форм заполненные данные поступят соответственно в файлы `incidents.json` и `hackers.json`
> 
> P.S.S. Для проверки проект запускался на ОC Windows 10 в PowerShell с версией Python 3.12.3
