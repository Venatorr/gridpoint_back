Gridpoint test task, Backend.
Приложение, состоит из трех частей: фронт, бэкенд, агент. 

Агент проверяет наличие новых файлов .test в заданной директории, 
отправляет их на сервер, на сервере данные перекладываются в БД и предоставляются фронту.
Фронт позволяет зарегестироваться, авторизоваться и просматривать файлы и данные из файлов.

Все три части выложены в DockerHub и запускаются с помощью Docker-compose.
Как запустить у себя:
1) Установить Docker
2) Скачать docker-compose.yaml из этого репозитория
3) Выполнить docker-compose up из директории с docker-compose.yaml
4) Открыть у себя в браузере http://localhost:8080/

- это репозиторий бэкенда приложения
- фронт: https://github.com/Venatorr/gridpoint_front
- агент: https://github.com/Venatorr/gridpoint_agent
