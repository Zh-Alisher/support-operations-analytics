from pathlib import Path

import pandas as pd


# Путь к CSV строим относительно расположения этого файла,
# чтобы скрипт можно было запускать из корня проекта.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "support_tickets.csv"
REPORTS_DIR = PROJECT_DIR / "reports"


def load_data() -> pd.DataFrame:
    """Загрузить обращения из CSV и подготовить временные поля."""
    df = pd.read_csv(DATA_PATH)

    # TODO: преобразовать created_at, first_response_at и resolved_at в datetime.
    # Подсказка: pd.to_datetime(...)

    return df


def main() -> None:
    REPORTS_DIR.mkdir(exist_ok=True)

    df = load_data()

    print("Первые пять строк:")
    print(df.head())

    print("\nРазмер датасета:")
    print(df.shape)

    print("\nТипы данных:")
    print(df.dtypes)


if __name__ == "__main__":
    main()
