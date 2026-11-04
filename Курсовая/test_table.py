"""
Модульные тесты для хеш-таблицы с открытой адресацией (1-й этап).
Запуск: python -m unittest test_table.py
"""

import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def test_01_insert_and_search(self):
        """Проверка базовой вставки и поиска элементов."""
        ht = HashTable(capacity=7, strategy="linear")
        ht.insert("a", 10)
        ht.insert("b", 20)
        ht.insert("c", 30)

        self.assertEqual(ht.size, 3)
        val, _ = ht.search("a")
        self.assertEqual(val, 10)
        val, _ = ht.search("b")
        self.assertEqual(val, 20)
        val, _ = ht.search("c")
        self.assertEqual(val, 30)

    def test_02_collision_resolution_all_strategies(self):
        """Проверка разрешения коллизий для всех трех стратегий."""
        for strat in ["linear", "quadratic", "double"]:
            with self.subTest(strategy=strat):
                ht = HashTable(capacity=11, strategy=strat)
                # Ключи, дающие коллизии при остатке от деления
                keys = [5, 16, 27, 38]
                for k in keys:
                    ok, _ = ht.insert(k, f"val_{k}")
                    self.assertTrue(ok)

                # Все ключи должны успешно находиться
                for k in keys:
                    val, _ = ht.search(k)
                    self.assertEqual(val, f"val_{k}")

    def test_03_tombstone_deletion(self):
        """
        Проверка маркера DELETED (Tombstone):
        удаление промежуточного элемента не должно ломать поиск элементов,
        вставленных после него.
        """
        ht = HashTable(capacity=11, strategy="linear")
        # Вставляем коллидирующие элементы
        ht.insert(1, "первый")
        ht.insert(12, "второй")  # 12 % 11 = 1
        ht.insert(23, "третий")  # 23 % 11 = 1

        # Удаляем второй элемент
        ok, _ = ht.delete(12)
        self.assertTrue(ok)

        # Проверяем, что 12 больше не находится
        val, _ = ht.search(12)
        self.assertIsNone(val)

        # Элементы 1 и 23 по-прежнему должны находиться!
        val1, _ = ht.search(1)
        self.assertEqual(val1, "первый")
        val3, _ = ht.search(23)
        self.assertEqual(val3, "третий")

        # Новая вставка может использовать удаленный слот
        ok, _ = ht.insert(99, "новый")
        self.assertTrue(ok)
        val_new, _ = ht.search(99)
        self.assertEqual(val_new, "новый")

    def test_04_update_existing_key(self):
        """Проверка обновления значения существующего ключа."""
        ht = HashTable(capacity=11, strategy="linear")
        ht.insert("test", 100)
        self.assertEqual(ht.size, 1)

        # Перезаписываем
        ht.insert("test", 500)
        val, _ = ht.search("test")
        self.assertEqual(val, 500)
        self.assertEqual(ht.size, 1)  # Размер не должен расти

    def test_05_unsuccessful_search(self):
        """Проверка поиска несуществующего ключа."""
        ht = HashTable(capacity=7, strategy="double")
        ht.insert("key1", 1)
        ht.insert("key2", 2)

        val, _ = ht.search("non_existent")
        self.assertIsNone(val)

    def test_06_load_factor(self):
        """Проверка расчета коэффициента заполнения (load factor)."""
        ht = HashTable(capacity=10, strategy="linear")
        self.assertAlmostEqual(ht.load_factor(), 0.0)

        # Вставляем 5 элементов -> alpha = 0.5
        for i in range(5):
            ht.insert(f"k{i}", i)
        self.assertAlmostEqual(ht.load_factor(), 0.5)

        # Удаляем 1 элемент -> alpha = 0.4
        ht.delete("k0")
        self.assertAlmostEqual(ht.load_factor(), 0.4)


if __name__ == "__main__":
    unittest.main()
