import tkinter as tk 
import unittest 

class TestCalculator(unittest.TestCase): 
    def setUp(self): 
        self.root = tk.Tk()  
        self.clacualtor = Calculator(self.root) 

    def test_addition(self):      
        self.clacualtor.button_clicked('2') 
        self.clacualtor.button_clicked('+') 
        self.clacualtor.button_clicked('2') 
        self.calculator.button_equal() 
        self.assertEqual(self.calculator.text_val.get(), '4') 

    def test_substraction(self):      
        self.clacualtor.button_clicked('2') 
        self.clacualtor.button_clicked('-') 
        self.clacualtor.button_clicked('1') 
        self.calculator.button_equal() 
        self.assertEqual(self.calculator.text_val.get(), '1') 

    def test_clear_char(self): 
        self.clacualtor.button_clicked('2') 
        self.calculator.button_clicked('C') 
        self.assertEqual(self.calculator.text_val.get(), '') 

    def test_clear_all_char(self):
        self.clacualtor.button_clicked('2') 
        self.calculator.button_clicked('AC') 
        self.assertEqual(self.calculator.text_val.get(), '') 
 
    def tearDown(self): 
        self.clacualtor.master.destroy() 

if __name__ == '__main__': 
    unittest.main() 