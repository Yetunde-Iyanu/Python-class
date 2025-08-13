#Creating a function called calculate_discount
def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def calculate_discount():
    price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percentage)
    
    if discount_percentage >= 20:
        print(f"The final price after discount is: {final_price:.2f}")
    else:
        print(f"No discount applied, the final price is: {price:.2f}")

calculate_discount()

      
    