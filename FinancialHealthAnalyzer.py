import unittest
from io import StringIO

#FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
#This class does not need to be edited
class FinancialTransaction: # This is the parent class , all classes below inherit from this class
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)

class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    #Adds together all transactions labeled "Income" by utilizng a list method from staticmethod
    def total_revenue(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Income")

    #Adds together all transactions labeled "Expense" by utilizng a list method from staticmethod
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")
    
    #Taking our total revenue, we subtract the expenses (after converting the expenses into dollars) from our income to determine profit
    def profit(self):  
        profitvalue = self.total_revenue() - self.total_expenses()/20
        return profitvalue
    
    #Function designated in determining the profit margin by dividing the profit by the total revenue
    def profit_margin(self):
        profitmargin = self.profit()/self.total_revenue()
        return profitmargin 
    
    #Function designated in determining the average amount of money from transactions that came though
    def average_transaction_amount(self):
        amountoftransactions =  len(self.transactions)
        return (self.profit()/amountoftransactions)
         
        
    #Determines financial health and returns the corresponding string by utilizing an if statment 
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        elif -1000 >= profit < 0:
            return "Warning"
        else:
            return "Critical"

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 1000),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 1500)
        ]
        self.transactions = transactions_data

    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases. No need to change variables all the time since analyzer is not a public variable or class specific variable, just funciton only variable
    #test Function designated in determining the total amount of income by comparing to calculated value 
    def test_total_revenue(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_revenue(), 2500)

    # test Function designated in determining the total amount of expenses accumalted after converting it into dollars using the 1$ to R20 exchange rate which is then compared to calcualted value 
    def test_total_expenses(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_expenses()/20, 40)

    # test Function designated in determining the total profit after deducting  total expenses from total revenue which is then compared to a calculated value
    def test_profit(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit(), 2460)

    # test Function designated in determining the profit margin by dividing the profit by the total revenue which is then compared to a calculated value  
    def test_profit_margin(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit_margin(), 0.984)

    # test Function designated in determining the average amount of money from transactions that came though which is then compared to a calculated value   
    def test_average_transaction_amount(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.average_transaction_amount(), 615)
    
    # test Function designated in determining the financial status of the company which is then compared to another calculated status
    def test_financial_health(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.financial_health(), "Healthy")

#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)
    print("Profit: ", analyzer.profit(), "$")
    print("Profit margin: ", analyzer.profit_margin())
    print("Average transaction amount: ", analyzer.average_transaction_amount(), "$")
    print("Financial health: ",analyzer.financial_health() )
    unittest.main()
    