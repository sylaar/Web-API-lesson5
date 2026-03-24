def calculate_statistics(vacancies: list[dict],
                         vacancies_found: int,
                         salary_func):
    '''Вычисляет статистику по списку вакансий'''
    total_salary = 0
    processed = 0

    for vacancy in vacancies:
        salary = salary_func(vacancy)
        if salary:
            total_salary += salary
            processed += 1
    try:        
        average_salary = int(total_salary / processed)
    except ZeroDivisionError:
        average_salary = 0
    
    return {
        'vacancies_found': vacancies_found,
        'vacancies_processed': processed,
        'average_salary': average_salary,
    }