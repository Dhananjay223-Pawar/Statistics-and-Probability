import matplotlib.pyplot as plt

screen_time = [42, 45, 39, 47, 44, 46, 43, 55]

plt.boxplot(
    screen_time,
    patch_artist=True,
    flierprops=dict(
        marker='o',
        markerfacecolor='red',
        markersize=8
    )
)

plt.xlabel("8-Week Period")
plt.ylabel("Screen Time (Hours)")
plt.title("Weekly Screen Time – Past 8 Weeks")

plt.show()
