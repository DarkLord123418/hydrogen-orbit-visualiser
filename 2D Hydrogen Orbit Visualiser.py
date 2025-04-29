# run "pip install numpy matplotlib tk scipy" to install necessary libraries


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label, Button, Entry, StringVar, ttk, Frame
from scipy.special import genlaguerre, sph_harm
import math

# Constants
a0 = 0.53e-10  # Bohr radius

# Function to calculate the radial wavefunction
def radial_wavefunction(n, l, r):
    rho = 2 * r / (n * a0)
    prefactor = np.sqrt((2 / (n * a0))**3 * math.factorial(n - l - 1) / (2 * n * math.factorial(n + l)))
    laguerre = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    return prefactor * np.exp(-rho / 2) * rho**l * laguerre

# Function to calculate the spherical harmonic
def spherical_harmonic(l, m, theta, phi):
    return sph_harm(m, l, phi, theta)

# Function to calculate the probability density
def probability_density(n, l, m, r, theta, phi):
    R = radial_wavefunction(n, l, r)
    Y = spherical_harmonic(l, m, theta, phi)
    psi = R * Y
    return np.abs(psi)**2

# Function to map angular quantum number l to orbital name
def get_orbital_name(n, l):
    l_to_letter = {0: "s", 1: "p", 2: "d", 3: "f", 4: "g"}
    if l in l_to_letter:
        return f"{n}{l_to_letter[l]}"
    else:
        return f"{n}? (l={l})"  # For unsupported l values

# Function to plot the orbital or probability density
def plot_orbital():
    try:
        n = int(n_var.get())
        l = int(l_var.get())
        m = int(m_var.get())
        plot_mode = plot_mode_var.get()

        orbital_name = get_orbital_name(n, l)

        # Generate a 2D grid in the XY-plane
        x = np.linspace(-10 * a0, 10 * a0, 200)
        y = np.linspace(-10 * a0, 10 * a0, 200)
        x, y = np.meshgrid(x, y)

        # Convert to spherical coordinates
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(np.sqrt(x**2 + y**2), 0)  # Polar angle (fixed to XY-plane)
        phi = np.arctan2(y, x)  # Azimuthal angle

        # Compute the data to plot
        if plot_mode == "Orbital":
            data = radial_wavefunction(n, l, r)
        elif plot_mode == "Probability Density":
            data = probability_density(n, l, m, r, theta, phi)

        # Generate the plot
        fig, ax = plt.subplots(figsize=(6, 6))
        c = ax.contourf(x / a0, y / a0, data, 100, cmap="inferno")
        fig.colorbar(c, ax=ax, label="Wave Function")
        ax.set_title(f"{orbital_name} Orbital (n={n}, l={l}, m={m}, Mode={plot_mode})")
        ax.set_xlabel("X (in Bohr radii)")
        ax.set_ylabel("Y (in Bohr radii)")

        # Clear and embed the plot in the GUI
        for widget in plot_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    except Exception as e:
        error_label.config(text=f"Error: {e}")

# GUI setup
window = Tk()
window.title("Hydrogen Atom Orbital Visualizer (2D)")
window.geometry("900x700")

# Frames for layout
control_frame = Frame(window, width=200, height=600)
control_frame.pack(side="left", fill="y", padx=10, pady=10)

plot_frame = Frame(window, width=600, height=600, bg="white")
plot_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Controls
Label(control_frame, text="Quantum Numbers", font=("Arial", 14)).pack(pady=10)

Label(control_frame, text="Principal Quantum Number (n):").pack()
n_var = StringVar(value="1")
Entry(control_frame, textvariable=n_var).pack()

Label(control_frame, text="Angular Quantum Number (l):").pack()
l_var = StringVar(value="0")
Entry(control_frame, textvariable=l_var).pack()

Label(control_frame, text="Magnetic Quantum Number (m):").pack()
m_var = StringVar(value="0")
Entry(control_frame, textvariable=m_var).pack()

Label(control_frame, text="Plot Mode:").pack(pady=10)
plot_mode_var = StringVar(value="Orbital")
plot_mode_menu = ttk.Combobox(control_frame, textvariable=plot_mode_var, values=["Orbital", "Probability Density"])
plot_mode_menu.pack()

Button(control_frame, text="Plot", command=plot_orbital).pack(pady=20)

# Error label
error_label = Label(control_frame, text="", fg="red")
error_label.pack()

# Run the GUI
window.mainloop()
