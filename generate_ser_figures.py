from pathlib import Path

import matplotlib.pyplot as plt


SNR = [25, 27, 29, 31, 33, 35]

SER_16X16 = {
    "MMSE": [2.80e-1, 2.10e-1, 1.55e-1, 1.15e-1, 8.0e-2, 5.5e-2],
    "EP": [8.0e-2, 3.0e-2, 1.4e-2, 5.8e-3, 2.5e-3, 1.2e-3],
    "OAMP": [2.0e-1, 1.4e-1, 9.0e-2, 5.5e-2, 3.5e-2, 2.2e-2],
    "GEPNet": [8.0e-2, 3.0e-2, 1.05e-2, 3.6e-3, 1.35e-3, 5.5e-4],
    "GCEPNet": [8.5e-2, 2.7e-2, 7.2e-3, 2.2e-3, 7.0e-4, 2.5e-4],
    "DEPNet": [7.8e-2, 2.4e-2, 5.3e-3, 1.25e-3, 3.0e-4, 8.5e-5],
}

SER_32X32 = {
    "MMSE": [2.6e-1, 2.2e-1, 1.8e-1, 1.35e-1, 1.0e-1, 7.0e-2],
    "EP": [8.5e-2, 3.4e-2, 1.25e-2, 5.0e-3, 2.0e-3, 8.0e-4],
    "OAMP": [1.9e-1, 1.4e-1, 9.0e-2, 5.5e-2, 3.2e-2, 1.8e-2],
    "GEPNet": [8.2e-2, 2.4e-2, 5.5e-3, 1.2e-3, 3.6e-4, 1.1e-4],
    "GCEPNet": [8.6e-2, 2.2e-2, 4.5e-3, 9.5e-4, 2.2e-4, 5.5e-5],
    "DEPNet": [8.0e-2, 1.8e-2, 3.0e-3, 5.5e-4, 1.1e-4, 2.0e-5],
}

STYLES = {
    "MMSE": {"color": "#8a8a8a", "linestyle": "--", "marker": "^"},
    "EP": {"color": "#666666", "linestyle": "--", "marker": "*"},
    "OAMP": {"color": "#f28e2b", "linestyle": "--", "marker": "p"},
    "GEPNet": {"color": "#59a14f", "linestyle": "--", "marker": "o"},
    "GCEPNet": {"color": "#b23a48", "linestyle": "--", "marker": "s"},
    "DEPNet": {"color": "#4f83cc", "linestyle": "-", "marker": "D"},
}


def plot_ser(data, output_path, y_min):
    fig, ax = plt.subplots(figsize=(6.0, 4.35), dpi=300)

    for label, values in data.items():
        style = STYLES[label]
        ax.semilogy(
            SNR,
            values,
            label=label,
            color=style["color"],
            linestyle=style["linestyle"],
            linewidth=1.6,
            marker=style["marker"],
            markersize=6.0,
            markerfacecolor="white",
            markeredgewidth=1.25,
        )

    ax.set_xlim(25, 35)
    ax.set_xticks(SNR)
    ax.set_ylim(y_min, 5.0e-1)
    ax.set_xlabel("SNR (dB)")
    ax.set_ylabel("SER")
    ax.grid(True, which="major", linestyle="-", linewidth=0.45, alpha=0.35)
    ax.grid(True, which="minor", linestyle=":", linewidth=0.35, alpha=0.25)
    ax.legend(loc="lower left", framealpha=0.95, fontsize=8)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def main():
    output_dir = Path("figs")
    output_dir.mkdir(exist_ok=True)
    plot_ser(SER_16X16, output_dir / "ser_comparison_16x16_64QAM.png", 5.0e-5)
    plot_ser(SER_32X32, output_dir / "ser_comparison_32x32_64QAM.png", 1.0e-5)


if __name__ == "__main__":
    main()
