"""Игра угадай число.
Угадываем число меньше, чем за 20 попыток
"""
from statistics import mean
import numpy as np
def new_random_predict(number:int=1)->int:
    """Угадываем число меньше, чем за 20 попыток

    Args:
        number (int, optional): Загаданное число . Defaults to 1.

    Returns:
        int: Число попыток
    """
    minimal=1
    maximal=100
    predict_number=maximal/2
    count=1
    while number!= predict_number:
        count+=1
        if number > predict_number:
            minimal=predict_number
            predict_number=round((minimal+maximal)/2)
        elif number < predict_number:
            maximal=predict_number
            predict_number=round((minimal+maximal)/2)
    return count

def score_game(new_random_predict)->int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls=[]
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=1000)
    
    for number in random_array:
        count_ls.append(new_random_predict(number))
    
    score=int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__=='__main__':
# RUN
    score_game(new_random_predict)