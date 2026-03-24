from environs import env
from requests.exceptions import HTTPError

from calculate_statistics import calculate_statistics
from hh_api import get_all_hh_vacancies
from predict_salary import predict_rub_salary_hh
from predict_salary import predict_rub_salary_sj
from print_stats_to_terminal import print_stats_to_terminal
from superjob_api import get_all_sj_vacancies
import settings


def main():
    env.read_env()
    superjob_secret_key = env('SUPERJOB_SECRET_KEY')

    hh_statistics = {}
    sj_statistics = {}

    for language in settings.LANGUAGES:
        try:
            hh_vacancies, hh_vacancies_found = get_all_hh_vacancies(
                text=f'Программист {language}',
            )
        except HTTPError as err:
            print(err)
        try:
            sj_vacancies, sj_vacancies_found = get_all_sj_vacancies(
                secret_key=superjob_secret_key,
                keyword=f'Программист {language}',
            )
        except HTTPError as err:
            print(err)
        hh_statistics[language] = calculate_statistics(hh_vacancies,
                                                       hh_vacancies_found,
                                                       predict_rub_salary_hh)
        sj_statistics[language] = calculate_statistics(sj_vacancies,
                                                       sj_vacancies_found,
                                                       predict_rub_salary_sj)
        
    print_stats_to_terminal(
        hh_statistics,
        title='HeadHunter Moscow'
    )
    print_stats_to_terminal(
        sj_statistics,
        title='SuperJob Moscow'
    )

if __name__ == '__main__':
    main()
