# The Collatz conjecture is one of the most famous unsolved problems in mathematics.
# Consider the following operation on an arbitrary positive integer (n):
# If the number is even: /2
# If the number is odd:  3x+1.

from matplotlib import pyplot as plt
import time


def collatz_sequence(n):
    seq = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq


z = int(input("What number would you like to try? "))
plot = collatz_sequence(z)

plt.ion()
fig, ax = plt.subplots()
(line,) = ax.plot(plot)
ax.set_xlabel("Step")
ax.set_ylabel("Value")
ax.set_title("Collatz Sequence for the number " + str(z))
ax.set_facecolor("white")
ax.grid(False)

# Initialize annotation object
annotation = None

for step, value in enumerate(plot):
    line.set_xdata(range(len(plot[: step + 1])))
    line.set_ydata(plot[: step + 1])
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

    if annotation is not None:
        annotation.remove()  # Remove previous annotation

    # Update annotation with the current number
    annotation = ax.annotate(
        str(value),
        (step, value),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=12,
        color="blue",
    )

    time.sleep(0.3)

plt.ioff()
plt.show()
