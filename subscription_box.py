# Ask the user for their membership level
membership = input("Enter your membership level (Platinum, Gold, Silver, Bronze, Free Trial): ")

# Make the input easier to match by ignoring capitalization and extra spaces
membership = membership.strip().title()

# Check the membership level and print the cost
if membership == "Platinum":
    print("Monthly cost: $60")
elif membership == "Gold":
    print("Monthly cost: $50")
elif membership == "Silver":
    print("Monthly cost: $40")
elif membership == "Bronze":
    print("Monthly cost: $30")
elif membership == "Free Trial":
    print("Monthly cost: $0")
else:
    print("Invalid membership level entered.")
