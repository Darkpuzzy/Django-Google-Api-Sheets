# Django + Google Api Sheets

How used this:
    1. docker-compose build
    2. docker-compose up

URI Google Sheet : https://docs.google.com/spreadsheets/d/1M-qhu19fs8fUE8KjKTiGFxae4Ws69MgP9bsYyUHjxz4/edit#gid=0

Routing: 
    localhost/react/ - List Orders
    localhost/react/api/orders - OPEN api orders
    localhost/index/<int:pk> - get orders

Добавление в БД происходит в realtime, но страницу нужно будет обновлять :)