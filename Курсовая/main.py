"""
Демонстрационный скрипт работы хеш-таблицы с открытой адресацией (1-й этап).
Показывает базовые операции, возникновение коллизий, механизм Tombstone
и сравнение трех стратегий пробирования.
"""

import sys

# Обеспечиваем корректный вывод кириллицы в консоли Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from hash_table import HashTable


def demo_basic_operations():
    print("=" * 60)
    print(" 1. ДЕМОНСТРАЦИЯ БАЗОВЫХ ОПЕРАЦИЙ (Линейное пробирование)")
    print("=" * 60)

    # Создаем таблицу размера 7
    ht = HashTable(capacity=7, strategy="linear")

    print("\n>>> Вставка элементов: 'apple' -> 100, 'banana' -> 200, 'cherry' -> 300")
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("cherry", 300)
    ht.print_table()

    # Поиск
    print(">>> Поиск элементов:")
    val, probes = ht.search("banana")
    print(f"Поиск 'banana': найдено={val}, число проверок ячеек (проб)={probes}")

    val, probes = ht.search("orange")
    print(f"Поиск 'orange' (нет в таблице): найдено={val}, число проверок ячеек={probes}")

    # Удаление
    print("\n>>> Удаление элемента 'banana':")
    success, probes = ht.delete("banana")
    print(f"Удаление 'banana': успешно={success}, выполнено проб={probes}")
    ht.print_table()

    # Проверка, что после удаления 'cherry' по-прежнему доступен
    val, probes = ht.search("cherry")
    print(f">>> Повторный поиск 'cherry' после удаления 'banana':")
    print(f"Результат: найдено={val}, проверок ячеек={probes} (Tombstone пройден успешно!)")


def demo_collision_and_tombstone():
    print("\n" + "=" * 60)
    print(" 2. ДЕМОНСТРАЦИЯ РАЗРЕШЕНИЯ КОЛЛИЗИЙ И МЕХАНИЗМА TOMBSTONE")
    print("=" * 60)

    # Таблица емкостью 11
    ht = HashTable(capacity=11, strategy="linear")

    # Специально подбираем ключи, дающие одинаковый остаток от деления на 11
    # Например, числа 5, 16, 27 (так как 5 % 11 = 5, 16 % 11 = 5, 27 % 11 = 5)
    print("\n>>> Вставляем ключи с одинаковым первичным хешем: 5, 16, 27 (коллизия в ячейке 5)")
    for k in [5, 16, 27]:
        ok, p = ht.insert(k, f"Value_{k}")
        print(f"Вставка ключа {k:2d}: размещен за {p} проб(ы)")

    ht.print_table()

    print(">>> Удаляем промежуточный ключ 16 (становится <DELETED>):")
    ht.delete(16)
    ht.print_table()

    print(">>> Ищем ключ 27 (он был вставлен ПОСЛЕ 16):")
    val, p = ht.search(27)
    print(f"Результат: найдено='{val}', число проб={p}")
    print("Вывод: поиск не оборвался на удаленной ячейке, инвариант сохранен!")


def demo_strategies_comparison():
    print("\n" + "=" * 60)
    print(" 3. СРАВНЕНИЕ ТРЕХ СТРАТЕГИЙ ПРОБИРОВАНИЯ")
    print("=" * 60)

    keys = [10, 21, 32, 43, 54]  # Все дают коллизию при capacity = 11: 10 % 11 = 10, 21 % 11 = 10...

    for strat in ["linear", "quadratic", "double"]:
        ht = HashTable(capacity=11, strategy=strat)
        total_probes = 0
        print(f"\n--- Стратегия: {strat.upper()} ---")

        for k in keys:
            ok, p = ht.insert(k, f"Val_{k}")
            total_probes += p
            print(f"Ключ {k:2d} -> проб для вставки: {p}")

        ht.print_table()
        print(f"Суммарно проб на вставку 5 элементов: {total_probes}")


if __name__ == "__main__":
    demo_basic_operations()
    demo_collision_and_tombstone()
    demo_strategies_comparison()
