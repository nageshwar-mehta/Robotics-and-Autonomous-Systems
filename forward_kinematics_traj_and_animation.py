import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D
from matplotlib.animation import FFMpegWriter

# Constants
dt = 0.1  # Time step
ts = 10   # Total time
t = np.arange(0, ts + dt, dt)  # Time array

# Initial conditions
x0, y0, psi0 = 0, 0, 0  # Initial position and orientation
eta0 = np.array([x0, y0, psi0])  # Initial state vector

# State matrices
eta = np.zeros((3, len(t)))  # Stores position/orientation over time
zeta = np.zeros((3, len(t)))  # Velocity vector
d_eta = np.zeros((3, len(t)))  # Derivative of state vector

# Set initial state
eta[:, 0] = eta0

# Main simulation loop
for i in range(len(t) - 1):
    psi = eta[2, i]  # Current orientation

    # Define velocities
    u, v, r = 1, 0.5, -0.2  # Linear velocities in x, y and angular velocity
    zeta[:, i] = [u, v, r]

    # Jacobian matrix
    j_psi = np.array([
        [np.cos(psi), -np.sin(psi), 0],
        [np.sin(psi),  np.cos(psi), 0],
        [0, 0, 1]
    ])

    # Compute derivative of state vector
    d_eta[:, i] = j_psi @ zeta[:, i]

    # Update state vector
    eta[:, i + 1] = eta[:, i] + dt * d_eta[:, i]

# Plot results
def plot_results(t, eta):
    plt.figure()
    plt.plot(t, eta[0, :], 'r-', label='X-position')
    plt.xlabel("Time (s)")
    plt.ylabel("X Position")
    plt.title("X vs Time")
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(t, eta[1, :], 'g-', label='Y-position')
    plt.xlabel("Time (s)")
    plt.ylabel("Y Position")
    plt.title("Y vs Time")
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(t, eta[2, :], 'b-', label='Psi (orientation)')
    plt.xlabel("Time (s)")
    plt.ylabel("Psi (Orientation)")
    plt.title("Psi vs Time")
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(eta[0, :], eta[1, :], label='Trajectory')
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.title("2D Trajectory")
    plt.grid()
    plt.show()

plot_results(t, eta)

# Animation setup
fig, axis = plt.subplots()
axis.set_xlim([0, 12])
axis.set_ylim([-10, 2])
axis.grid(True, zorder=1)

# Set aspect ratio to be equal
axis.set_aspect('equal', adjustable='box')

l, w = 2, 1  # Car dimensions
animated_plot, = axis.plot([], [], 'b-', zorder=2)  # Trajectory line
animated_box = axis.add_patch(plt.Rectangle((0, 0), l, w, fill=True, color='green', zorder=3))

# Animation update function
def update_data(frame):
    animated_plot.set_data(eta[0, :frame], eta[1, :frame])
    animated_box.set_xy([eta[0, frame] - l / 2, eta[1, frame] - w / 2])
    animated_box.set_edgecolor('black')
    animated_box.set_linewidth(0.5)

    # Rotate the rectangle
    transform = Affine2D().rotate_deg_around(
        eta[0, frame], eta[1, frame], np.rad2deg(eta[2, frame])
    ) + axis.transData
    animated_box.set_transform(transform)

    return animated_plot, animated_box,

# Create animation
animation = FuncAnimation(
    fig=fig,  # Figure for the animation
    func=update_data,  # Function to update each frame
    frames=len(t),  # Total number of frames (based on time array)
    interval=dt * 1000,  # Interval between frames in milliseconds
    repeat=False  # Do not repeat the animation after it finishes
)

# Save animation
animation.save('car2.gif')
plt.show()
