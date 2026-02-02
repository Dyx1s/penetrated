# penetrated
Payloads, scripts, tears and hopes

## blindSql.py

Скрипт для **Blind SQL Injection** — извлечения имени базы данных посимвольно методом бинарного поиска.

### Как работает

1. **is_true(payload)** — отправляет POST-запрос с payload в поле `title`, проверяет наличие маркеров в ответе (`found.` / `not found.`) и возвращает, истинно ли условие.

2. **extract_char(pos)** — бинарным поиском по ASCII (32–126) определяет символ на позиции `pos` в `database()`, подставляя условие `ASCII(SUBSTRING(database(),pos,1)) > mid` в payload.

3. **extract_database_name(length)** — собирает имя БД посимвольно, вызывая `extract_char` для каждой позиции.

### Использование

1. Замените `TARGET_URL_HERE` в скрипте на целевой URL.
2. Убедитесь, что маркеры `TRUE_MARKER` и `FALSE_MARKER` соответствуют ответам целевого приложения.
3. Установите `DB_LENGTH` — длину имени БД (если известна).
4. Запустите: `python blindSql.py`

### Требования

- Python 3
- `requests`
