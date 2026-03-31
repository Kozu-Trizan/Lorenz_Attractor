import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation Constants
SIGMA = 10
RHO = 28
BETA = 8/3
DUR = 100

# time parameters
data_points, dT = np.linspace(0, DUR, 10000, retstep=True)

# initial parameters
states = np.array([
    [1, 2, 3], 
    [1.001, 2.001, 3.001],
    [1.002, 3.002, 3.002],
    [1.0001, 3.0001, 3.0001],
    [1.0003, 3.0003, 3.0003],
]) 

# Visualization
X = np.zeros((len(states), len(data_points)))
Y = np.zeros((len(states), len(data_points)))
Z = np.zeros((len(states), len(data_points)))

def RK4_Solver(func, dt, t0, vect_x):
    f1 = func(t0, vect_x)
    f2 = func(t0+dt/2, vect_x+dt*f1/2)
    f3 = func(t0+dt/2, vect_x+dt*f2/2)
    f4 = func(t0+dt, vect_x+dt*f3)
    return (vect_x + dt*(f1 + 2*f2 + 2*f3 + f4)/6)

def lorenz_attractor(t, p):
    '''
    p is a 3 Dimensional state vector. f -> f(x, y, z)
    '''
    dp_dt = [
        SIGMA*(p[1] - p[0]),
        p[0]*(RHO - p[2]) - p[1],
        p[0]*p[1] - BETA*p[2]
    ]
    return np.array(dp_dt)

state_count = 0
for state in states:
    i = 0
    curr_state = state
    for t in data_points:
        X[state_count][i], Y[state_count][i], Z[state_count][i] = curr_state
        curr_state = RK4_Solver(lorenz_attractor, dT, t, curr_state)
        i += 1
    state_count += 1

# Plotting
fig = plt.figure(figsize=(12, 5))
fig.set_facecolor('black')
# fig.tight_layout()

ax = fig.add_subplot(111, projection='3d')
#ax.set_facecolor('black')
ax.set_axis_off()
# ax.set_aspect('equal')
xlim = np.max(np.abs(X)) + 10
ylim = np.max(np.abs(Y)) + 10
zlim = np.max(np.abs(Z)) + 10
ax.set_xlim(-xlim, xlim)
ax.set_ylim(-ylim, ylim)
ax.set_zlim(-zlim, zlim)

plots = [ax.plot([], [], '-o', linewidth=1, markersize=0) for state in states]
plots[0][0].set_color("#e82929ff")

def update(frame):
    i = 0
    return_states = []
    for plot in plots:
        plot[0].set_data(X[i][:frame], Y[i][:frame])
        plot[0].set_3d_properties(Z[i][:frame])
        i += 1
        return_states.append(plot[0])
    
    return return_states

ani = animation.FuncAnimation(
    fig=fig,
    frames=len(X[0]),
    func=update,
    interval=dT*1000,
    repeat=False,
    blit=False,
)


plt.title(f'Lorenz Attractor', color='white')
plt.show()