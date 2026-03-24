from time import sleep

import requests

import settings


def get_hh_vacancies(
        text: str = None,
        area: int = settings.HH_MOSCOW_ID,
        page: int = 0,
):
    '''Возвращает первые 20 вакансий'''
    params = {
    'text': text,
    'area': settings.HH_MOSCOW_ID,
    'excluded_text': settings.EXCLUDED_TEXT,
}
    response = requests.get(settings.HH_API_URL, params=params)
    response.raise_for_status()
    return response.json()


def get_all_hh_vacancies(
        text: str = None,
        area: int = settings.HH_MOSCOW_ID,
        page: int = 0,
) -> tuple[list, int]:
    '''Возвращает все вакансии'''
    decoded_response = get_hh_vacancies(
        text=text,
        area=area,
        page=page
    )
    vacancies = decoded_response.get('items', [])
    vacancies_found = decoded_response.get('found', 0)
    pages = decoded_response.get('pages', 1)

    for page in range(1, pages):
        response_page = get_hh_vacancies(
            text,
            area,
            page,
        )
        vacancies.extend(response_page.get('items'))
        if page % 10 == 0:
            sleep(5)
    return vacancies, vacancies_found