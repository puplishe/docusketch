## Запуск
1. Клонировать репозиторий и прописать docker-compose build, потом docker-compose up -d
2. Запрос в powershell на создание Invoke-RestMethod -Uri "http://localhost:8080/api/create" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"key": "example_key", "value": "example_value"}'
3. На изменение Invoke-RestMethod -Uri "http://localhost:8080/api/change/example_key" -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"value": "updated_value"}'
4. Просмотреть все записи: http://localhost:8080/api/getall