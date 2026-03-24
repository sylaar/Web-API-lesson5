from typing import Optional


def predict_salary(
        salary_from: int = None,
        salary_to: int = None
        ) -> Optional[int]:
    '''Вычисляет ожидаемую зарплату'''
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2.0)
    elif salary_from:
        return int(salary_from * 1.2)
    elif salary_to:
        return int(salary_to * 0.8)
    else:
        return
    

def predict_rub_salary_hh(vacancy: dict) -> Optional[int]:
    '''Вычисляет ожидаемую зарплату из вакансии HH'''
    salary = vacancy.get('salary')
    if not salary or salary.get('currency') != 'RUR':
        return
    
    salary_from = salary.get('from')
    salary_to = salary.get('to')
    return predict_salary(salary_from, salary_to)


def predict_rub_salary_sj(vacancy: dict) -> Optional[int]:
    '''Вычисляет ожидаемую зарплату из вакансии SuperJob'''
    salary_from = vacancy.get('payment_from')
    salary_to = vacancy.get('payment_to')
    if (not salary_from) and (not salary_to):
        return
    return predict_salary(salary_from, salary_to)


