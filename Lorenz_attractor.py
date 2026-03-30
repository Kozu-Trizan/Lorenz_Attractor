'''
This is a simulation of Lorenz Attractor (A chaotic system) using the euler Method
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patheffects as path_effects

# Simulation Constants
SIGMA = 10
RHO = 28
BETA = 8/3

# time parameters
data_points, dt = np.linspace(0, 10, 1000, retstep=True)

# initial parameters
states = [
    [1, 2, 3], 
    [1.001, 2.001, 3.001],
    [1.002, 3.002, 3.002,]
] 

# Visualization
X = []
Y = []
Z = []

def get_state(x_ini, y_ini, z_ini):
    x_coord = []
    y_coord = []
    z_coord = []
    for t in data_points:
        x_coord.append(x_ini)
        y_coord.append(y_ini)
        z_coord.append(z_ini)

        x_new = x_ini + (SIGMA*(y_ini - x_ini))*dt
        y_new = y_ini + (x_ini*(RHO - z_ini) - y_ini)*dt
        z_new = z_ini + (x_ini*y_ini - BETA*z_ini)*dt

        x_ini = x_new
        y_ini = y_new
        z_ini = z_new

    X.append(x_coord)
    Y.append(y_coord)
    Z.append(z_coord)


for state in states:
    get_state(state[0], state[1], state [2])

X = np.array(X, dtype=float)
Y = np.array(Y, dtype=float)
Z = np.array(Z, dtype=float)

# Plotting
fig = plt.figure()
fig.set_facecolor('black')
plt.tight_layout()

ax = fig.add_subplot(projection='3d')
ax.set_facecolor('black')
ax.set_axis_off()
ax.set_aspect('equal')
xlim = np.max(np.abs(X))
ylim = np.max(np.abs(Y))
zlim = np.max(np.abs(Z))
ax.set_xlim(-xlim, xlim)
ax.set_ylim(-ylim, ylim)
ax.set_zlim(-zlim, zlim)


state1, = ax.plot([], [], [], '-o', linewidth=1, markersize=0, label="State One", color="#e82929ff")
state1.set_path_effects([path_effects.Stroke(linewidth=1, foreground="#292d2da0"),
                        path_effects.Normal(),
                    ])
state2, = ax.plot([], [], [], '-o', linewidth=1, markersize=0, label="State Two", color="#bac931ff")
state2.set_path_effects([path_effects.Stroke(linewidth=1, foreground='#292d2da0'),
                        path_effects.Normal(),
                    ])
state3, = ax.plot([], [], [], '-o', linewidth=1, markersize=0, label="State Three", color="#3159ebff")
state3.set_path_effects([path_effects.Stroke(linewidth=1, foreground='#292d2da0'),
                        path_effects.Normal(),
                    ])

def update(frame):
    state1.set_data(X[0][:frame], Y[0][:frame])
    state1.set_3d_properties(Z[0][:frame])
    state2.set_data(X[1][:frame], Y[1][:frame])
    state2.set_3d_properties(Z[1][:frame])
    state3.set_data(X[2][:frame], Y[2][:frame])
    state3.set_3d_properties(Z[2][:frame])

    return state1, state2, state3

ani = animation.FuncAnimation(
    fig=fig,
    frames=len(X[0]),
    func=update,
    interval=dt*1000,
    repeat=False,
    blit=False,
)
ani.save("lorentz_attractor.mp4", fps=60)
plt.title("Lorenz Attractor", color='white')
plt.show()