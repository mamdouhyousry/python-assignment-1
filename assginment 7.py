import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [22, 24, 19, 23, 25, 28, 26]  # <-- You need this

plt.plot(days, temps, marker='o', color='b', linestyle='--')

plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variation Over a Week")

plt.show()
