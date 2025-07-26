# Bitunix Token Parser / Парсер токенов Bitunix

Скрипт для получения информации о токенах и их контрактах с биржи Bitunix через API.

## Функциональность / Functionality

- Получение списка всех токенов с биржи Bitunix
- Извлечение информации о сетях и контрактах
- Фильтрация и форматирование данных о токенах
- Вывод информации в формате: chain (сеть), name (имя токена), contractAddress (адрес контракта)

## Требования / Requirements

- Python 3.7+
- requests==2.31.0

## Установка / Installation

1. Клонируйте репозиторий / Clone the repository
```bash
git clone https://github.com/godspeedstreet/search_coins
```

2. Установите зависимости / Install dependencies
```bash
pip install -r requirements.txt
```

## Использование / Usage

Просто запустите скрипт:
```bash
python bitunix.py
```

Скрипт выведет список всех токенов в формате:
```
(chain, name, contractAddress)
```
Где:
- chain - название блокчейн-сети (eth, bsc, и т.д.)
- name - название токена
- contractAddress - адрес смарт-контракта токена (если есть)

## Структура кода / Code Structure

- `fetch_data()` - получение данных с API Bitunix
- `extract_tokens()` - обработка и форматирование полученных данных
- Использование регулярных выражений для валидации адресов контрактов

## API Endpoint

```
https://openapi.bitunix.com/api/spot/v1/common/coin/coin_network/list
```

## Обработка ошибок / Error Handling

- Обработка ошибок сетевых запросов
- Проверка корректности адресов контрактов
- Безопасная обработка отсутствующих данных

