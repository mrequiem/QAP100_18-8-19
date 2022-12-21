tickets = int(input("Сколько билетов вы хотите приобрести? "))
print("")
price = 0
for i in range(tickets):
    i += 1
    age = int(input(f"Возраст посетителя по билету {i} "))
    if age < 18:
        print("Цена билета: БЕСПЛАТНО!")
    elif 18 <= age < 25:
        price = price + 990
        print("Цена билета: 990 руб.")
    else:
        price = price + 1390
        print("Цена билета: 1390 руб.")
if tickets <= 3:
    print("\nИтого к оплате:", price)
else:
    print("\nИтого к оплате с учетом скидки:", price - price * 0.1)