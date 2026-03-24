from terminaltables import AsciiTable


def print_stats_to_terminal(stats: dict, title: str):
    '''Пеачатает статистику по вакансиям в терминал в виде таблицы'''
    table_headers = [
        ('Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'),
    ]

    for language, data in stats.items():
        table_headers.append([
            language,
            str(data.get('vacancies_found')),
            str(data.get('vacancies_processed')),
            str(data.get('average_salary')),
        ])
    table = AsciiTable(table_headers, title)
    print(table.table)