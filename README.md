Created By 
Jahid Sarkar (jahidsarkar611@gmail.com) as a project under Prof. Dr. Manmohan Singh Shishodia as a mini project during Semester IV, in Quantum Mechanics & Applications (PH 312)



This project simulates the hydrogen atom's wavefunctions using the following quantum numbers:

Principal Quantum Number (n)

Angular Quantum Number (l)

Magnetic Quantum Number (m)

The simulation calculates the radial wavefunction and the spherical harmonics to visualize the orbital or the probability density. You can choose to display either the orbital shape or the probability density.

Key Functions
radial_wavefunction(n, l, r): Computes the radial wavefunction for the given quantum numbers and radial distance.

spherical_harmonic(l, m, theta, phi): Computes the spherical harmonic function based on the angular quantum numbers and angles.

probability_density(n, l, m, r, theta, phi): Calculates the probability density function for the hydrogen atom's wavefunction.

get_orbital_name(n, l): Returns the name of the orbital (e.g., 1s, 2p, etc.) based on the quantum numbers.

plot_orbital(): Plots the orbital or probability density based on user input and selected quantum numbers.

How to Use
Run the Python script 2D Hydrogen Orbit Visualiser.py.

The application window will open, and you can input your desired quantum numbers:

Principal Quantum Number (n): The energy level of the electron.

Angular Quantum Number (l): Determines the shape of the orbital.

Magnetic Quantum Number (m): Specifies the orientation of the orbital.

Choose the plot mode:

Orbital: Displays the orbital shape.

Probability Density: Displays the probability density of finding an electron at a given location.

Click "Plot" to visualize the selected orbital.

Example
This example shows the 1s orbital for the hydrogen atom:

Set n = 1, l = 0, m = 0.

Choose Orbital or Probability Density in the dropdown.

Click Plot.
