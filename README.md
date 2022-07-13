# staff_test
Необходимо ввести свои данные Postgresqsl (user, name, host, port, password) в config.py для подключение к локальному базе данных

Далее инсталируем зависимости (в виртуальном окружении)
>pip install -r requirements.txt

Затем запускаем скрипт сидера для заполнения базы данных записями
>python manage.py runscript db_seeder
