import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D


# Time parameters
dt = 0.1  # Time step
ts = 100  # Total simulation time
t = np.arange(0, ts + dt, dt)  # Time array

# Mobile robot parameters
a = 0.05
d_y = 0.2

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

    # input
    omega1 = 3
    omega2 =2*np.sin(0.1*t[i])
    omega = np.array([omega1,omega2]).reshape(2,1)

    # wheel configuration
    W = np.array([
        [a/2,a/2],
        [0,0],
        [-a/(2*d_y),a/(2*d_y)]
    ])
    zeta[:,i] = (W@omega).flatten()

    eta_dot[:,i]= j_psi@zeta[:,i]
    eta[:,i+1]=eta[:,i]+dt*eta_dot[:,i]



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



# Animation setup

fig, axis = plt.subplots()
axis.set_xlim([min(eta[0,:])-1, max(eta[0,:])+1])
axis.set_ylim([min(eta[1,:])-1, max(eta[1,:])+1])
axis.grid(True, zorder=1)

# Set aspect ratio to be equal
axis.set_aspect('equal', adjustable='box')

l, w = 0.2, 0.1  # Car dimensions
animated_plot, = axis.plot([], [], 'b-', zorder=2,label = 'path')  # Trajectory line
animated_box = axis.add_patch(plt.Rectangle((0, 0), l, w, fill=True, color='green', zorder=3,label='Robot'))
axis.legend(loc='upper right')

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
animation.save('car4.gif')
plt.show()
