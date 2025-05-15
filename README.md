# Анализ цитат с сайта quotes.toscrape.com

**Автор:** 

## Структура проекта

project-folder/
├── README.md                  ← этот файл
├── requirements.txt           ← список зависимостей
├── notebooks/
│   └── analysis.ipynb         ← Jupyter Notebook с отчётом
├── scripts/
│   └── parse_reviews.py       ← скрипт для парсинга данных
├── data/
│   └── reviews.csv            ← CSV-файл с собранными данными


## Инструкция по запуску

1. **Клонировать репозиторий** или распаковать ZIP-файл:
   
   git clone https://github.com/ВАШ_АККАУНТ/ИМЯ_РЕПО.git
   cd ИМЯ_РЕПО
   

2. **Создать виртуальное окружение** и установить зависимости:
   
   python3 -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   

3. **Сбор данных**:
   
   python scripts/parse_reviews.py
   
   В результате в папке `data/` появится файл `reviews.csv`.

4. **Запуск отчёта**:
   
   jupyter notebook notebooks/analysis.ipynb
   
   Откройте файл `analysis.ipynb` и последовательно выполните все ячейки (Shift+Enter).

## Описание проекта

В этом проекте выполнен полный цикл анализа текстовых данных:
- Сбор данных: парсинг цитат с сайта `quotes.toscrape.com`.
- Очистка и подготовка: удаление пропусков и дубликатов, приведение к табличному виду.
- Анализ и визуализация: определение самых цитируемых авторов, популярных тем (тегов) и ключевых слов (облако слов, гистограммы, диаграммы).
- Формирование выводов: ключевые инсайты и рекомендации.

## Заметки

- Папка `.ipynb_checkpoints` создаётся автоматически Jupyter Notebook. Её можно удалить, если она не нужна.