cd ~/demo-python-qdb
source .venv/bin/activate

python /Users/andrewjuikov/Documents/DIASOFT/Presentation/21.04.26/diasoft.py


Что делать дальше
Запускай демо через тот вариант, который у тебя уже работает:
cd ~/demo-python-qdb
source .venv/bin/activate
python /Users/andrewjuikov/Documents/DIASOFT/Presentation/21.04.26/diasoft.py
А pyodbc пока можно оставить в стороне как запасной вариант.
Как это красиво подать в речи
Можно сказать так:
“Помимо подключения через клиентские инструменты, к системе могут подключаться и собственные приложения. В данном случае это простой пример на Python, который выполняет запросы к той же базе и получает результаты работы.”
Это уже звучит крепко и без лишней возни с драйверами.

1. Не трогать pyodbc и идти дальше с pymssql.
Для демо это лучший путь, если pymssql у тебя уже завёлся. Он проще, и у тебя уже меньше шансов словить macOS-сюрприз в кадре.


andrewjuikov@macm4 ~ % cd ~/demo-python-qdb                                                                                                                    
andrewjuikov@macm4 demo-python-qdb % source .venv/bin/activate
(.venv) andrewjuikov@macm4 demo-python-qdb % python /Users/andrewjuikov/Documents/DIASOFT/Presentation/21.04.26/diasoft.py
Подключаемся...
Подключение успешно!

=== Данные из Sales ===
(1, 'Ноутбук ASUS VivoBook', Decimal('90000.00000000'))
(2, 'Мышь беспроводная', Decimal('6000.00000000'))
(3, 'Монитор 24"', Decimal('18000.00000000'))
(4, 'Клавиатура механическая', Decimal('10500.00000000'))
(5, 'Ноутбук Lenovo IdeaPad', Decimal('52000.00000000'))
(6, 'Коврик для мыши', Decimal('5000.00000000'))

=== Отчет ===
(6, Decimal('181500.00000000'), Decimal('30250.00000000'), Decimal('90000.00000000'), Decimal('5000.00000000'))
('Ноутбук ASUS VivoBook', 2, Decimal('90000.00000000'), '49.59%')
('Ноутбук Lenovo IdeaPad', 1, Decimal('52000.00000000'), '28.65%')
('Монитор 24"', 1, Decimal('18000.00000000'), '9.92%')
('Клавиатура механическая', 3, Decimal('10500.00000000'), '5.79%')
('Мышь беспроводная', 5, Decimal('6000.00000000'), '3.31%')
('Коврик для мыши', 10, Decimal('5000.00000000'), '2.75%')
('2024-01', 3, Decimal('114000.00000000'))
('2024-02', 2, Decimal('62500.00000000'))
('2024-03', 1, Decimal('5000.00000000'))

Готово!
(.venv) andrewjuikov@macm4 demo-python-qdb % deactivate
andrewjuikov@macm4 demo-python-qdb % 
