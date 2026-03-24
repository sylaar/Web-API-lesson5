import requests

import settings


def get_sj_vacancies(
        secret_key: str,
        keyword: str,
        town: int = settings.SUPERJOB_MOSCOW_ID,
        catalogues: int = settings.CATALOGUE_PROGRAMMING,
        page: int = 0,
) -> dict[str]:
    '''Возвращает первую страницу с вакансиями SupeJob'''
    headers = {
        "X-Api-App-Id": secret_key,
    }
    params = {
        "town": town,
        "keyword": keyword,
        "catalogues": catalogues,
        "page": page,
    }

    response = requests.get(
        url=settings.SUPERJOB_API_URL,
        headers=headers,
        params=params,
    )
    response.raise_for_status()
    return response.json()


def get_all_sj_vacancies(
        secret_key: str,
        keyword: str = None,
        town: int = settings.SUPERJOB_MOSCOW_ID,
        catalogues: int = settings.CATALOGUE_PROGRAMMING,
) -> tuple[list, int]:
    '''Возвращает dct страницs с вакансиями SupeJob'''
    page = 0
    decoded_response = get_sj_vacancies(
        secret_key=secret_key,
        keyword=keyword,
        town=town,
        catalogues=catalogues,
        page=page,
    )
    vacancies = decoded_response.get('objects', [])
    vacancies_found = decoded_response.get('total', 0)

    while decoded_response.get('more'):
        page += 1
        response_page = get_sj_vacancies(
            secret_key=secret_key,
            keyword=keyword,
            town=town,
            catalogues=catalogues,
            page=page,
        )
        vacancies.extend(response_page.get('objects'))

    return vacancies, vacancies_found