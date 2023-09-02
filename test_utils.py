import unittest
import pandas as pd
from utils import add_full_name, add_age_group, merge_data, calculate_total_spending_by_age


class TestDataProcessingFunctions(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        self.customers = pd.DataFrame({
            'customer_id': [18763, 48715, 4274, 12050, 41116, 43350, 3083, 26118, 19359, 14624, 36807, 35944, 25578,
                            33813, 33815, 33817],
            'first_name': ['Afqft', 'Beeah', 'Zhtvp', 'Nei', 'Yvjnw', 'Benajsdc', 'Uqwx', 'Ugafbwvu', 'Svhqio',
                           'Nzspqlqd', 'Xnwjoy', 'Pft', 'Bsnayyj', 'Djfjydg', 'Bniqohx', 'Utkla'],
            'last_name': ['Upuoxrm', 'Galgn', 'Xpdecbqj', 'Juvlebudxc', 'Zptvwycup', 'Kxjmehjf', 'Tiemkqwdeq',
                          'Eegpknit', 'Bjuchnimtu', 'Hwtvtj', 'Gtgfaltmdr', 'Akzj', 'Tiwfvyqjtg', 'Osuaecbaxs',
                          'Jzowmexaf', 'Yeqskeoxh'],
            'email': ['afqft.upuoxrm@example.com', 'beeah.galgn@web.com', 'zhtvp.xpdecbqj@example.com',
                      'nei.juvlebudxc@mail.com', 'yvjnw.zptvwycup@mail.com', 'benajsdc.kxjmehjf@web.com',
                      'uqwx.tiemkqwdeq@mail.com', 'ugafbwvu.eegpknit@web.com', 'svhqio.bjuchnimtu@mail.com',
                      'nzspqlqd.hwtvtj@web.com', 'xnwjoy.gtgfaltmdr@web.com', 'pft.akzj@example.com',
                      'bsnayyj.tiwfvyqjtg@web.com', 'djfjydg.osuaecbaxs@mail.com', 'bniqohx.jzowmexaf@mail.com',
                      'utkla.yeqskeoxh@web.com'],
            'age': [34, 37, 59, 60, 21, 60, 30, 54, 29, 52, 54, 47, 18, 50, 50, 28]
        })

        # Sample data for purchases
        self.purchases = pd.DataFrame({
            'customer_id': [18763, 48715, 4274, 12050, 41116, 43350, 3083, 26118, 19359, 14624, 36807, 35944, 25578,
                            33813],
            'product': ['Camera', 'Mouse', 'Camera', 'Desktop', 'Camera', 'Mobile', 'Laptop', 'Camera', 'Monitor',
                        'Laptop', 'Camera', 'Mobile', 'Tablet', 'Tablet'],
            'price': [843, 128, 1122, 631, 448, 519, 750, 1360, 1488, 644, 1267, 259, 1436, 170]
        })

    def test_add_full_name(self):
        # Test if 'full_name' column is added correctly
        customers_with_full_name = add_full_name(self.customers)
        self.assertTrue('full_name' in customers_with_full_name.columns)
        self.assertEqual(customers_with_full_name['full_name'][0], 'AfqftUpuoxrm')

    def test_add_age_group(self):
        # Test if 'age_group' column is added correctly
        customers_with_age_group = add_age_group(self.customers)
        self.assertTrue('age_group' in customers_with_age_group.columns)
        self.assertEqual(customers_with_age_group['age_group'][0], 'Middle-aged')
        self.assertEqual(customers_with_age_group['age_group'][1], 'Middle-aged')
        self.assertEqual(customers_with_age_group['age_group'][2], 'Senior')

    def test_merge_data(self):
        # Test if data is merged correctly
        merged_data = merge_data(self.customers, self.purchases)
        self.assertTrue('product' in merged_data.columns)
        self.assertTrue('price' in merged_data.columns)

    def test_calculate_total_spending_by_age(self):
        # Test if total spending by age group is calculated correctly
        customers_with_age_group = add_age_group(self.customers)
        merged_data = merge_data(customers_with_age_group, self.purchases)
        total_spending = calculate_total_spending_by_age(merged_data)
        print(total_spending)
        self.assertEqual(total_spending['age_group'][0], 'Middle-aged')
        self.assertEqual(total_spending['price'][0], 971)


if __name__ == '__main__':
    unittest.main()
