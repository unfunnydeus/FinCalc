debt = float(input("Введите задолженность по кредиту: "))
interest_rate = float(input("Введите текущую процентную ставку: "))
term = int(input("Введите срок (в месяцах): "))

monthly_rate = interest_rate/(12*100)
monthly_rate_percent = monthly_rate * 100
monthly_payment = debt * (monthly_rate * (1+monthly_rate) ** term) / ((1 + monthly_rate) ** term - 1)
total_payment = monthly_payment * term
overpayment = total_payment - debt


print('=' * 50)
print(f"Месячная процентная ставка: {round(monthly_rate_percent, 2)} %")
print(f"Ежемесячный платеж: {round(monthly_payment, 2)} ₽")
print(f"Общая сумма выплат: {round(total_payment, 2)} ₽")
print(f"Переплата по процентам: {round(overpayment, 2)} ₽")
print('=' * 50)


