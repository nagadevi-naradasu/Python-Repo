def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return round(amount, 2)

P, R, T = map(float, input().split())
total_amount = calculate_compound_interest(P, R, T)
print(f"{total_amount:.2f}")
