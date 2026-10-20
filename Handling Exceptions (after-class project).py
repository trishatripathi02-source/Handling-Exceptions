while True:
    try:
        total_bill = float(input("Enter total shopping bill: ₹"))
        discount = float(input("Enter discount amount: ₹"))
        people = int(input("Enter number of people: "))

        if total_bill < 0:
            raise ValueError("Bill cannot be negative.")

        if discount < 0:
            raise ValueError("Discount cannot be negative.")

        if discount > total_bill:
            raise ValueError("Discount cannot be greater than the bill.")

        if people <= 0:
            raise ValueError("Number of people must be greater than 0.")

    except ValueError as e:
        print("Input Error:", e)
        print("Please try again.\n")

    except TypeError:
        print("Type Error: Invalid data entered.")
        print("Please try again.\n")

    else:
        final_bill = total_bill - discount
        amount_per_person = final_bill / people

        print("\n----- BILL SUMMARY -----")
        print(f"Original Bill: ₹{total_bill:.2f}")
        print(f"Discount: ₹{discount:.2f}")
        print(f"Final Bill: ₹{final_bill:.2f}")
        print(f"People Sharing: {people}")
        print(f"Each Person Pays: ₹{amount_per_person:.2f}")
        break

    finally:
        print("Validation complete.\n")