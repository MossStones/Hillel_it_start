
seconds = int(input("Введіть кількість секунд (0 до 8640000): "))

days = seconds // 86400
seconds = seconds % 86400
hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60

seconds = seconds % 60

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

print(f"{days} {hours_str}:{minutes_str}:{seconds_str}")
