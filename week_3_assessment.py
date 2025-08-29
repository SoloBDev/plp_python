def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage (0-100)
    
    Returns:
    float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
def main():
    print("🛍️  Discount Calculator")
    print("=" * 30)
    
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Input validation
        if original_price < 0:
            print("❌ Error: Price cannot be negative!")
            return
        if discount_percent < 0 or discount_percent > 100:
            print("❌ Error: Discount percentage must be between 0 and 100!")
            return
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display results
        print("\n" + "=" * 30)
        print("💳 CALCULATION RESULTS")
        print("=" * 30)
        print(f"Original price: ${original_price:.2f}")
        print(f"Discount percentage: {discount_percent}%")
        
        if discount_percent >= 20:
            discount_amount = original_price - final_price
            print(f"Discount applied: ${discount_amount:.2f}")
            print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
            print(f"💰 You saved: ${discount_amount:.2f}!")
        else:
            print("ℹ️  No discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("❌ Error: Please enter valid numbers!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
