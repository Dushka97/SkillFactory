<<<<<<< Updated upstream
=======
<<<<<<< HEAD
# SkillFactory
SF homework
=======
>>>>>>> Stashed changes
# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/Dushka97/sf_data_science/tree/main/project_0/READMEmd#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/Dushka97/sf_data_science/tree/main/project_0/READMEmd#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/Dushka97/sf_data_science/tree/main/project_0/READMEmd#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/Dushka97/sf_data_science/tree/main/project_0/READMEmd#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/Dushka97/sf_data_science/tree/main/project_0/READMEmd#Результаты)

[6. Выводы при выполнении проекта](https://github.com/Dushka97/sf_data_science/tree/main/project_0/READMEmd#Выводы-при-выполнении-проекта)

### Описание проекта
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению]()

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток, а именно меньше 20

**Условия соревнования:**

- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под "угадать", подрузумевается "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем?**
- Учимся писать хороший код на Python
- Уимся работать с IDE
- Учимся работать с GitHub

### Краткая информация о данных
Компьютер получает на вход число и угадывает его за менее, чем 20 попыток

### Этапы работы над проектом
Пишем функцию - new_random_predict(), которая получает на вход загаданное целое число - number.

Внутри функции формирует минимальное и макисмальное занчение числа, которое может быть. 

Заводим счетчик попыток определить число - count.

Оределяем серднее между минимальным и максимальным.

Запускаем цикл while до тех пора пока number неравно preidict_number, за каждых ход добавляем 1 к счетчику.

В теле цикла формируем условия перебора:

- Если number больше predict_number, то минимальное число приравниваем к predict_number и определяем среднее между максимумом и новым минимумом;
    
- Если number меньше predict_number, то максимальное число приравниваем к predict_number и определяем среднее между новым максимумом и минимумом;

Завершаем цикл возвращением числа попыток.

Для оценки качества алгоритма написана функция score_game(), которая получает на вход функцию угадывания числа. Функция запускает алгоритм 1000 раз и считает среднее число попыток для угадывания числа от 1 до 100. 

### Результаты

В результате алгоритм в среднем угадывает число за 7 попыток.

### Выводы при выполнении проекта

При выполнении технического задания было определено, что наилучшим образом определить загаданное число от 1 до 100 при наличии цсловия больше или меньше является деление числового диапазона на 2 части.

<<<<<<< Updated upstream
:arrow_up: [к оглавлению]()
=======
:arrow_up: [к оглавлению]()
>>>>>>> 9925d63 (Initial commit)
>>>>>>> Stashed changes