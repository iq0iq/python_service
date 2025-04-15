# python_service
Система учета и анализа данных, поступающих с условного устройства. Полученные данные привязываются к временной метке и устройству, с которого пришли данные, и сохраняются в БД. Набор данных используется для дальнейшего анализа. 
<h3>Требования к системе</h3> 
<li>В системе реализован сбор статистики с устройства по его идентификатору
формат получаемой статистики - {“x”: float, “y”: float, “z”:float}</li>
<li>В системе реализован анализ собранной статистики с устройства за определенный период и за все время</li>
<li>Результатами анализа являются числовые характеристики величины:
минимальное значение,
максимальное значение,
количество,
сумма,
медиана</li>
<h3>Примеры запросов</h3>
curl -X POST "http://localhost:8000/data/" -H "Content-Type: application/json" -d '{"device_id": "device_1", "x": 1.0, "y": 2.0, "z": 3.0, "timestamp": "2024-11-11T12:00:00Z"}'<br>
curl -X GET "http://localhost:8000/data/device_1/analyze_period?start_date=2020-01-01T00:00:00&end_date=2025-11-21T23:59:59"<br>
curl -X GET "http://localhost:8000/data/device_1"<br>
curl -X GET "http://localhost:8000/data/analyze/device_1"
