FairyCraftJewellery
Для запуска проекта необходимо открыть папку проекта в среде разработки Visual Studio Code и выполнить следующие действия:
  Установить расширения python, django, pillow для корректной работы проекта
  Открыть теринал внутри VS Code
Для Windows:
  venv/bin/activate
  cd Jewellery
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
Для MacOS:
  source venv/bin/activate
  cd Jewellery
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
