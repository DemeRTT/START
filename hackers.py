from nicegui import ui
import json

def submit_form():
    if not grouping_name_input.value or not attacked_orgs_input.value or not attack_method_input.value or not danger_level_input.value:
        ui.notify("Пожалуйста, заполните все обязательные поля!", color='red')
        return

    if attack_method_input.value == 'Другое':
        data = {
            "Название группировки": grouping_name_input.value,
            "Названия атакуемых организаций": attacked_orgs_input.value,
            "Метод атаки": other_attack_method_input.value,
            "Уровень опасности": danger_level_input.value,
            "Дата атаки": attack_date_input.value,
            "Дополнительные данные": additional_info_input.value
        }
    else: 
        data = {
            "Название группировки": grouping_name_input.value,
            "Названия атакуемых организаций": attacked_orgs_input.value,
            "Метод атаки": attack_method_input.value,
            "Уровень опасности": danger_level_input.value,
            "Дата атаки": attack_date_input.value,
            "Дополнительные данные": additional_info_input.value
        }

    try:
        with open('hackers.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')  # Добавляем новую строку после каждой записи
        ui.notify("Данные отправлены!", color='green')
    except Exception as e:
        ui.notify(f"Ошибка при сохранении данных: {e}", color='red')

    # Очистка формы
    grouping_name_input.value = ''
    attacked_orgs_input.value = ''
    attack_method_input.value = ''
    danger_level_input.value = ''
    other_attack_method_input.value = ''
    attack_date_input.value = ''
    additional_info_input.value = ''

def on_incident_type_change(value):
    # Управление видимостью текстового поля для описания инцидента
    if value.value == 'Другое':
        other_attack_method_input.visible = True
        label.visible = True
    else:
        other_attack_method_input.visible = False
        other_attack_method_input.value = ''  # Очистить поле, если выбрана другая опция
        label.visible = False

# Интерфейс формы
with ui.card().tight().classes('px-6 py-4'):
    ui.label('Форма заполнения данных о хакерской группировке').classes('text-2xl font-bold mb-4')

    # Поле для ввода названия группировки
    with ui.row().classes('mb-3 w-full'):
        ui.label('Название группировки').classes('font-semibold w-full')
        grouping_name_input = ui.input('Введите название группировки').classes('w-full')

    # Поле для ввода атакуемых организаций
    with ui.row().classes('mb-3 w-full'):
        ui.label('Названия атакуемых организаций').classes('font-semibold w-full')
        attacked_orgs_input = ui.textarea('Введите названия организаций через запятую').classes('w-full')

    # Поле для выбора метода атаки
    with ui.row().classes('mb-3 w-full'):
        ui.label('Метод атаки').classes('font-semibold w-full')
        attack_method_input = ui.select(
            options=['Фишинг', 'SQL-инъекция', 'Уязвимости ПО', 'DDoS-атака', 'Другое'],
            on_change=lambda e: on_incident_type_change(e)
        ).classes('w-full')

    # Поле для ввода другого метода атаки (появляется только при выборе "Другое")
    with ui.row().classes('mb-3 w-full'):
        label = ui.label('Другой метод атаки').classes('font-semibold w-full')
        other_attack_method_input = ui.textarea('Введите свой вариант метода атаки').classes('w-full')
        other_attack_method_input.visible = False  # Скрываем поле по умолчанию
        label.visible = False  # Скрываем подписку по умолчанию

    # Поле для выбора уровня опасности
    with ui.row().classes('mb-3 w-full'):
        ui.label('Уровень опасности').classes('font-semibold w-full')
        danger_level_input = ui.select(
            options=['Низкий', 'Средний', 'Высокий', 'Очень высокий']
        ).classes('w-full')

    # Поле для выбора даты атаки
    with ui.row().classes('mb-3 w-full'):
        ui.label('Дата атаки').classes('font-semibold w-full')
        with ui.input('Укажите дату атаки').classes('w-full').bind_value(globals(), 'date') as attack_date_input:
            with ui.menu() as menu:
                ui.date().bind_value(attack_date_input)
            with attack_date_input.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')


    # Поле для ввода дополнительной информации
    with ui.row().classes('mb-3 w-full'):
        ui.label('Дополнительные данные').classes('font-semibold w-full')
        additional_info_input = ui.textarea('Атакуемые IP-адреса, описание атак и др.').classes('w-full')

    # Кнопка отправки
    ui.button('Отправить', on_click=submit_form).classes('w-full bg-blue-600 text-white mt-4 hover:bg-blue-700')

ui.run()
