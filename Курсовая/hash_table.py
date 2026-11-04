"""
Модуль реализации структуры данных: Хеш-таблица с открытой адресацией (1-й этап: костяк структуры).

Реализованы 3 стратегии разрешения коллизий (пробирования):
1. Линейное пробирование (linear)
2. Квадратичное пробирование (quadratic)
3. Двойное хеширование (double)

Также поддерживается ленивое удаление (маркер DELETED / Tombstone)
и вычисление коэффициента заполнения таблицы (load factor).
"""


class Slot:
    """Ячейка хеш-таблицы."""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.is_deleted = False  # Флаг "ленивого" удаления (Tombstone)

    def is_empty(self):
        """Свободна ли ячейка (никогда не была занята)."""
        return self.key is None and not self.is_deleted

    def is_occupied(self):
        """Занята ли ячейка актуальным элементом."""
        return self.key is not None and not self.is_deleted

    def __repr__(self):
        if self.is_deleted:
            return "<DELETED>"
        if self.is_empty():
            return "<EMPTY>"
        return f"{self.key}: {self.value}"


class HashTable:
    """
    Хеш-таблица с открытой адресацией.

    Параметры:
        capacity (int): Размер таблицы (рекомендуется простое число).
        strategy (str): Стратегия пробирования: 'linear', 'quadratic' или 'double'.
    """

    def __init__(self, capacity=11, strategy="linear"):
        if capacity < 3:
            raise ValueError("Размер таблицы должен быть не менее 3.")

        valid_strategies = ("linear", "quadratic", "double")
        if strategy not in valid_strategies:
            raise ValueError(f"Неизвестная стратегия: '{strategy}'. Допустимы: {valid_strategies}")

        self.capacity = capacity
        self.strategy = strategy
        self.slots = [Slot() for _ in range(self.capacity)]
        self.size = 0  # Количество активных элементов в таблице

    def _hash1(self, key):
        """Первичная хеш-функция."""
        return abs(hash(key)) % self.capacity

    def _hash2(self, key):
        """
        Вторичная хеш-функция для двойного хеширования.
        Возвращает шаг смещения от 1 до capacity - 1.
        Шаг не равен 0 и взаимно прост с capacity (при простом capacity).
        """
        return 1 + (abs(hash(key) // self.capacity) % (self.capacity - 1))

    def _get_probe_index(self, key, i):
        """
        Вычисляет индекс ячейки на i-м шаге пробирования (i = 0, 1, 2, ...).
        """
        h1 = self._hash1(key)

        if self.strategy == "linear":
            # Формула: h(k, i) = (h1 + i) mod m
            return (h1 + i) % self.capacity

        elif self.strategy == "quadratic":
            # Формула: h(k, i) = (h1 + i + i^2) mod m
            return (h1 + i + i * i) % self.capacity

        elif self.strategy == "double":
            # Формула: h(k, i) = (h1 + i * h2) mod m
            h2 = self._hash2(key)
            return (h1 + i * h2) % self.capacity

    def insert(self, key, value=None):
        """
        Вставка пары (ключ, значение) в таблицу.
        Если значение не указано, сохраняется сам ключ.
        Возвращает: (успех: bool, число выполненных проб: int).
        """
        if value is None:
            value = key

        first_deleted_idx = None
        probes = 0

        for i in range(self.capacity):
            probes += 1
            idx = self._get_probe_index(key, i)
            slot = self.slots[idx]

            # 1. Если ячейка занята
            if slot.is_occupied():
                if slot.key == key:
                    # Ключ уже существует — обновляем его значение
                    slot.value = value
                    return True, probes
                # Иначе коллизия — идём на следующий шаг пробирования

            # 2. Если ячейка помечена как удаленная
            elif slot.is_deleted:
                if first_deleted_idx is None:
                    first_deleted_idx = idx
                # Сканируем дальше: вдруг этот ключ уже лежит дальше по цепочке коллизий

            # 3. Если ячейка пуста (EMPTY)
            elif slot.is_empty():
                # Если ранее встречался удаленный слот — используем его
                target_idx = first_deleted_idx if first_deleted_idx is not None else idx
                self.slots[target_idx].key = key
                self.slots[target_idx].value = value
                self.slots[target_idx].is_deleted = False
                self.size += 1
                return True, probes

        # Если обошли всю таблицу, но нашли свободный удаленный слот
        if first_deleted_idx is not None:
            self.slots[first_deleted_idx].key = key
            self.slots[first_deleted_idx].value = value
            self.slots[first_deleted_idx].is_deleted = False
            self.size += 1
            return True, probes

        # Таблица полностью заполнена
        return False, probes

    def search(self, key):
        """
        Поиск значения по ключу.
        Возвращает: (найденное значение или None, число выполненных проб: int).
        """
        probes = 0
        for i in range(self.capacity):
            probes += 1
            idx = self._get_probe_index(key, i)
            slot = self.slots[idx]

            # Если наткнулись на пустую ячейку — ключа гарантированно нет в таблице
            if slot.is_empty():
                return None, probes

            # Если ячейка занята и ключ совпал
            if slot.is_occupied() and slot.key == key:
                return slot.value, probes

            # Если ячейка помечена DELETED — продолжаем поиск дальше

        return None, probes

    def delete(self, key):
        """
        Удаление ключа из таблицы (ленивое удаление: ставит маркер DELETED).
        Возвращает: (успех: bool, число выполненных проб: int).
        """
        probes = 0
        for i in range(self.capacity):
            probes += 1
            idx = self._get_probe_index(key, i)
            slot = self.slots[idx]

            # Пустая ячейка означает, что удалять нечего
            if slot.is_empty():
                return False, probes

            # Нашли нужный ключ
            if slot.is_occupied() and slot.key == key:
                slot.key = None
                slot.value = None
                slot.is_deleted = True  # Ставим маркер Tombstone
                self.size -= 1
                return True, probes

        return False, probes

    def load_factor(self):
        """
        Коэффициент заполнения таблицы: alpha = n / m.
        Где n — число активных элементов, m — емкость таблицы.
        """
        if self.capacity > 0:
            return self.size / self.capacity
        return 0.0

    def print_table(self):
        """Наглядный вывод содержимого таблицы в консоль."""
        print("-" * 55)
        print(f"Хеш-таблица: стратегия='{self.strategy}', емкость={self.capacity}, элементов={self.size}")
        print(f"Коэффициент заполнения (load factor): alpha = {self.load_factor():.2f}")
        print("-" * 55)

        for i, slot in enumerate(self.slots):
            if slot.is_occupied():
                status = f"ЗАНЯТА   -> ключ: '{slot.key}', значение: '{slot.value}'"
            elif slot.is_deleted:
                status = "DELETED  -> (удаленный элемент, Tombstone)"
            else:
                status = "ПУСТО"

            print(f"[{i:2d}] {status}")

        print("-" * 55 + "\n")
