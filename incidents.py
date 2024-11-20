from nicegui import ui
import json

def submit_form():
    if not date_input.value or not source_input.value or not organization_input.value or not incident_type_input.value:
        ui.notify("Пожалуйста, заполните все обязательные поля!", color='red')
        return
    
    if incident_type_input.value == 'Прочее':
        data = {
            "Дата сообщения": date_input.value,
            "Источник сообщения": source_input.value,
            "Название организации": organization_input.value,
            "Тип инцидента": incident_type_input.value,
            "Описание инцидента": incident_description_input.value,
            "Дополнительные данные": additional_info_input.value
        }
    else:
        data = {
            "Дата сообщения": date_input.value,
            "Источник сообщения": source_input.value,
            "Название организации": organization_input.value,
            "Тип инцидента": incident_type_input.value,
            "Дополнительные данные": additional_info_input.value
        }

    # Сохранение данных в файл с указанием кодировки
    try:
        with open('incidents.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')  # Записываем новую строку для каждого инцидента
        ui.notify("Данные отправлены!", color='green')
    except Exception as e:
        ui.notify(f"Ошибка при сохранении данных: {e}", color='red')
    
    # Очистка формы
    date_input.value = ''
    source_input.value = ''
    organization_input.value = ''
    incident_type_input.value = ''
    incident_description_input.value = ''
    additional_info_input.value = ''

def on_incident_type_change(value):
    # Управление видимостью текстового поля для описания инцидента
    if value.value == 'Прочее':
        incident_description_input.visible = True
        label.visible = True
    else:
        incident_description_input.visible = False
        incident_description_input.value = ''  # Очистить поле, если выбрана другая опция
        label.visible = False

# Интерфейс формы
with ui.card().tight().classes('px-6 py-4'):  
    ui.label('Форма заполнения данных по инциденту').classes('text-2xl font-bold mb-4')
    
    # Поле для ввода даты
    with ui.row().classes('mb-3 w-full'):
        ui.label('Дата сообщения').classes('font-semibold w-full')
        with ui.input('Укажите дату сообщения').classes('w-full').bind_value(globals(), 'date') as date_input:
            with ui.menu() as menu:
                ui.date().bind_value(date_input)
            with date_input.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')

    # Поля для ввода источника сообщения, названия организации и типа инцидента
    with ui.row().classes('mb-3 w-full'):
        ui.label('Источник сообщения').classes('font-semibold w-full')
        source_input = ui.input('Название канала, форума или чата').classes('w-full')

    with ui.row().classes('mb-3 w-full'):
        ui.label('Название организации').classes('font-semibold w-full')
        organization_input = ui.input('На которую направлена угроза').classes('w-full')

    with ui.row().classes('mb-3 w-full'):
        ui.label('Тип инцидента').classes('font-semibold w-full')
        incident_type_input = ui.select(
            options=['DDoS-атака', 'Утечка данных', 'Взлом', 'Фишинг', 'Прочее'],
            on_change=lambda e: on_incident_type_change(e)
        ).classes('w-full')

    # Поле для описания инцидента (по умолчанию скрыто)
    with ui.row().classes('mb-3 w-full'):
        label = ui.label('Описание инцидента (если выбрано "Прочее")').classes('font-semibold w-full')
        incident_description_input = ui.textarea('Опишите инцидент').classes('w-full')
        incident_description_input.visible = False  # Скрываем поле по умолчанию
        label.visible = False  # Скрываем подписку по умолчанию

    # Поле для ввода дополнительной информации
    with ui.row().classes('mb-3 w-full'):
        ui.label('Дополнительные данные').classes('font-semibold w-full')
        additional_info_input = ui.textarea('Атакуемые IP-адреса, методы атаки и др.').classes('w-full')
    
    # Кнопка отправки
    ui.button('Отправить', on_click=submit_form).classes('w-full bg-blue-600 text-white mt-4 hover:bg-blue-700')

ui.run()
