"""Agregación y figuras a partir de observaciones reales."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def summary(frame):
    table = frame.pivot_table(index="input_size", columns="algorithm", values="elapsed_ns", aggfunc="median").sort_index()
    for name in ("Kadane", "Fuerza bruta"):
        ratio = table[name] / table[name].shift(1)
        table[f"Razón {name}"] = ratio.where(table.index.to_series() == 2 * table.index.to_series().shift(1))
    return table


def chart(frame, logarithmic=False):
    table = summary(frame)
    with plt.rc_context({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False}):
        fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
        for name, color in (("Kadane", "#059669"), ("Fuerza bruta", "#536878")):
            ax.plot(table.index, table[name] / 1e6, "o-", label=name, color=color, linewidth=2)
        if logarithmic:
            ax.set_xscale("log", base=2)
            ax.set_yscale("log")
        ax.set(xlabel="Tamaño de entrada n", ylabel="Mediana (ms)", title="Crecimiento observado" + (" · log-log" if logarithmic else ""))
        ax.grid(alpha=.2)
        ax.legend()
        return fig


def save_charts(frame, directory):
    for log, name in ((False, "normal"), (True, "loglog")):
        fig = chart(frame, log)
        fig.savefig(directory / f"timing_{name}.png", dpi=180)
        plt.close(fig)
    summary(frame).to_csv(directory / "summary.csv")
