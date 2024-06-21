import unittest
from unittest.mock import MagicMock, patch

from src.utils import get_transactions, read_transactions_from_csv, read_transactions_from_excel


class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open")
    def test_get_transactions_valid_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"transaction_id": 1, "amount": 100}]'
        transactions = get_transactions("test_file.json")
        self.assertEqual(transactions, [{"transaction_id": 1, "amount": 100}])

    @patch("builtins.open")
    def test_get_transactions_empty_file(self, mock_open: MagicMock) -> None:
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        transactions = get_transactions("test_file.json")
        self.assertEqual(transactions, [])

    def test_get_transactions_file_not_found(self) -> None:
        transactions = get_transactions("nonexistent_file.json")
        self.assertEqual(transactions, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_transactions_file_not_found_with_patch(self, mock_open):
        transactions = get_transactions("test_file.json")
        self.assertEqual(transactions, [])

    def test_read_transactions_from_csv(self):
        df = read_transactions_from_csv("data/transactions_csv.csv")
        self.assertFalse(df.empty)  # Проверяем, что DataFrame не пустой

    def test_read_transactions_from_excel(self):
        df = read_transactions_from_excel("data/transactions_excel.xlsx")
        self.assertFalse(df.empty)  # Проверяем, что DataFrame не пустой
