import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CartPendulumSystem:
    def __init__(self, cart_mass=1.0, pendulum_mass=0.1, pendulum_length=1.0, damping=0.1, gravity=9.8):
        self.cart_mass = cart_mass
        self.pendulum_mass = pendulum_mass
        self.pendulum_length = pendulum_length
        self.damping = damping
        self.gravity = gravity

        # Initial state [cart position, cart velocity, pendulum angle, pendulum angular velocity]
        self.state = np.array([0.0, 0.0, np.pi/2, 0.0])

    def dynamics(self, state, force):
        x, x_dot, theta, theta_dot = state

        # Equations of motion for the cart-pendulum system
        cart_acceleration = (force - self.pendulum_mass * self.pendulum_length * theta_dot**2 * np.sin(theta) + self.damping * x_dot) / (self.cart_mass + self.pendulum_mass)
        pendulum_acceleration = ((self.cart_mass + self.pendulum_mass) * self.gravity * np.sin(theta) - self.damping * theta_dot - force * np.cos(theta)) / (self.pendulum_length * (self.cart_mass + self.pendulum_mass * (np.sin(theta))**2))

        # Time derivatives of state variables
        x_dot_dot = cart_acceleration
        theta_dot_dot = pendulum_acceleration

        return np.array([x_dot, x_dot_dot, theta_dot, theta_dot_dot])

    def step(self, force, time_step):
        # Runge-Kutta numerical integration
        k1 = time_step * self.dynamics(self.state, force)
        k2 = time_step * self.dynamics(self.state + 0.5 * k1, force)
        k3 = time_step * self.dynamics(self.state + 0.5 * k2, force)
        k4 = time_step * self.dynamics(self.state + k3, force)

        self.state += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    def get_cart_position(self):
        return self.state[0]

    def get_pendulum_position(self):
        return self.pendulum_length * np.sin(self.state[2])

def pd_controller(system):
    # Proportional-Derivative (PD) controller
    # You may need to tune the parameters based on your specific system
    kp = 20.0  # Proportional gain
    kd = 2.0   # Derivative gain

    # Control law
    desired_position = np.pi
    error = desired_position - system.get_cart_position()
    control_force = kp * error - kd * system.state[1]

    return control_force

def update(frame, system, ax):
    time_step = 0.05
    control_force = pd_controller(system)
    system.step(control_force, time_step)

    x_cart = system.get_cart_position()
    x_pendulum = x_cart + system.get_pendulum_position()

    cart.set_data([x_cart - 0.2, x_cart + 0.2], [0, 0])
    pendulum.set_data([x_cart, x_pendulum], [0, system.pendulum_length * np.cos(system.state[2])])

    return cart, pendulum

# Create a cart-pendulum system
system = CartPendulumSystem()

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
cart, = ax.plot([], [], 'ko-', lw=4)
pendulum, = ax.plot([], [], 'ro-', lw=2)

# Create the animation
animation = FuncAnimation(fig, update, frames=range(300), fargs=(system, ax),
                          interval=50, blit=True)

plt.show()
