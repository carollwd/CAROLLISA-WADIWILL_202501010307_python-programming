# Week 5 Tutorial Documentation

## 1. Problem Analysis

### 1.1 Problem Statement
A cafe needs an automated Python program to calculate customer bills and print receipts based on fixed item prices instead of manual calculations.

### 1.2 Inputs
- Customer name - String
- Quantity of Coffee ordered - Integer
- Quantity of Tea ordered - Integer
- Quantity of Sandwich ordered - Integer

### 1.3 Outputs
- Itemized receipt displaying:
  - Customer Name
  - Quantities of Coffee, Tea, and Sandwich ordered
  - Total bill amount formatted in RM

### 1.4 Process Flow
1. Prompt user to enter customer name and item quantities.
2. Pass quantities to the calculation function (`calculate_total`).
3. Compute total cost
4. Return total amount.
5. Pass name, quantities, and total amount to the receipt printing function (`print_receipt`).
6. Display formatted receipt output to the user.

### 1.5 Constraints
* Item quantities must be non-negative integers
* Prices are fixed constants (Coffee = RM 8.50, Tea = RM 6.00, Sandwich = RM 12.00).



## 2. Problem Decomposition

1. **Input Handling (`main.py`)**: Collect customer details and quantities.
2. **Business Logic (`utils.py`)**: Calculate total price based on unit rates.
3. **Display Logic (`utils.py`)**: Format and output receipt.
4. **Execution (`main.py`)**: Integrate functions and control flow.

---

## 3. Pseudocode

```text
START
    Define prices: COFFEE_PRICE = 8.50, TEA_PRICE = 6.00, SANDWICH_PRICE = 12.00

    FUNCTION calculate_total(coffee_qty, tea_qty, sandwich_qty):
        total = (coffee_qty * COFFEE_PRICE) + (tea_qty * TEA_PRICE) + (sandwich_qty * SANDWICH_PRICE)
        RETURN total
    END FUNCTION

    FUNCTION print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total):
        PRINT "\n====== RECEIPT ======"
        PRINT "Customer : " + customer_name
        PRINT "Coffee   : " + coffee_qty
        PRINT "Tea      : " + tea_qty
        PRINT "Sandwich : " + sandwich_qty
        PRINT "-----------------------"
        PRINT "Total = RM " + total formatted to 2 decimal places
    END FUNCTION

    INPUT customer_name
    INPUT coffee_qty
    INPUT tea_qty
    INPUT sandwich_qty

    total_amount = CALL calculate_total(coffee_qty, tea_qty, sandwich_qty)
    CALL print_receipt(customer_name, coffee_qty, tea_qty, sandwich_qty, total_amount)
END