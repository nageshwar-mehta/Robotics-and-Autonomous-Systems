import numpy as np
import matplotlib.pyplot as plt

# Time parameters
dt = 0.1  # Time step
ts = 50  # Total simulation time
t = np.arange(0, ts + dt, dt)  # Time array

# Initial conditions
x0 = 0
y0 = 0
psi0 = 0

# Initial state vector
eta0 = np.array([x0, y0, psi0]).flatten()

# Matrix to store the position and orientation of the body at each time step
eta = np.zeros((3, len(t) + 1))
eta[:, 0] = eta0

# Velocity-related matrices
zeta = np.zeros((3, len(t)))  # Body-frame velocities
eta_dot = np.zeros((3, len(t)))  # World-frame velocities

# Simulation loop
for i in range(len(t)):
    psi = eta[2, i]  # Current orientation (psi)

    # Jacobian matrix for coordinate transformation
    j_psi = np.array([
        [np.cos(psi), -np.sin(psi), 0],
        [np.sin(psi),  np.cos(psi), 0],
        [0, 0, 1]
    ])

    # Desired trajectory and its derivative
    eta_d = np.array([
        2 - 2 * np.cos(0.1 * t[i]),
        2 * np.sin(0.1 * t[i]),
        0.1 * t[i]
    ]).reshape(3, 1)
    eta_dot[:, i] = np.array([
        2 * 0.1 * np.sin(0.1 * t[i]),
        2 * 0.1 * np.cos(0.1 * t[i]),
        0.1
    ])

    # Compute body-frame velocities
    zeta[:, i] = np.linalg.inv(j_psi) @ eta_dot[:, i]

    # Update the state vector for the next time step
    eta[:, i + 1] = eta[:, i] + dt * eta_dot[:, i]

# Remove the extra column in eta
eta = eta[:, :-1]

# Plotting results
plt.figure()
plt.plot(t, eta[0, :], 'r-')
plt.xlabel("Time (sec)")
plt.ylabel("Position in X-axis")
plt.title("X vs Time")
plt.grid()
plt.show()

plt.figure()
plt.plot(t, eta[1, :], 'g-')
plt.xlabel("Time (sec)")
plt.ylabel("Position in Y-axis")
plt.title("Y vs Time")
plt.grid()
plt.show()

plt.figure()
plt.plot(t, eta[2, :], 'b-')
plt.xlabel("Time (sec)")
plt.ylabel("Orientation (psi)")
plt.title("Psi vs Time")
plt.grid()
plt.show()

plt.figure()
plt.plot(t, eta[0, :], label='X-position')
plt.plot(t, eta[1, :], label='Y-position')
plt.plot(t, eta[2, :], label='Psi-rotation')
plt.xlabel("Time (sec)")
plt.ylabel("Positions")
plt.legend()
plt.title("Positions vs Time")
plt.grid()
plt.show()

plt.figure()
plt.plot(eta[0, :], eta[1, :])
plt.xlabel("Position in X-axis")
plt.ylabel("Position in Y-axis")
plt.title("Trajectory in 2D Plane")
plt.grid()
plt.show()
