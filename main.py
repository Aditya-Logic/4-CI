
import matplotlib.pyplot as plt

# ---------------- BAR PLOT ----------------

fig, ax = plt.subplots()

fruits = ["apples", "blueberry", "cherry", "orange"]
count = [40, 65, 24, 77]

bar_labels = ["red", "blue", "_red", "orange"]
bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

ax.bar(
    fruits,
    count,
    label=bar_labels,
    color=bar_colors
)

ax.set_ylabel("Fruit supply")
ax.set_title("Fruit supply by kind and color")
ax.legend(title="Fruit color")

plt.savefig("bars.png", bbox_inches="tight")
plt.close()


# ---------------- LINE PLOT ----------------

cat = ["bored", "happy", "happy", "bored", "happy"]
dog = ["happy", "bored", "bored", "happy", "bored"]

activities = [
    "combing",
    "drinking",
    "feeding",
    "napping",
    "playing"
]

fig, ax = plt.subplots()

ax.plot(activities, dog, label="dog")
ax.plot(activities, cat, label="cat")

ax.legend()

plt.savefig("lines.png", bbox_inches="tight")
plt.close()
