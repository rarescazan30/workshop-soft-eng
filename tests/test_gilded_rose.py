# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_brie(self):
        items = [Item("brie", 30, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("brie", items[0].name)

    def test_aged_brie_multiple_days(self):
        items = [Item("Aged Brie", 100, 40)]
        gilded_rose = GildedRose(items)
        for days in range(15):
            gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
    def test_sulphuras_multiple_days(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 100, 40)]
        gilded_rose = GildedRose(items)
        for days in range(15):
            gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(100, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
