import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class InvertedPendulum:
    def __init__(self, length=1.0, mass=1.0, damping=0.0, gravity=9.8):
        self.length = length
        self.mass = mass
        self.damping = damping
        self.gravity = gravity
        self.angle = np.pi/2
        self.angular_velocity = 0.0

    def step(self, force, time_step):
        # Update the pendulum state using numerical integration
        torque = force * self.length
        angular_acceleration = (
            -self.gravity / self.length *3* np.sin(self.angle) - self.damping * self.angular_velocity
        ) + torque / (self.mass * self.length ** 2)

        self.angular_velocity += angular_acceleration * time_step
        self.angle += self.angular_velocity * time_step

    def get_position(self):
        # Return the (x, y) position of the pendulum bob
        x = self.length * np.sin(self.angle)
        y = -self.length * np.cos(self.angle)
        return x, y

def pd_controller(pendulum):
    # Proportional-Derivative (PD) controller
    # You may need to tune the parameters based on your specific system
    kp = 20.0  # Proportional gain
    kd = 2.0   # Derivative gain

    # Control law
    desired_angle = 0.0
    error = desired_angle - pendulum.angle
    control_force = kp * error - kd * pendulum.angular_velocity
    control_force = 0

    return control_force

def update(frame, pendulum, ax):
    time_step = 0.05
    control_force = pd_controller(pendulum)
    pendulum.step(control_force, time_step)

    x, y = pendulum.get_position()
    line.set_data([0, x], [0, y])
    return line,

# Create an inverted pendulum
pendulum = InvertedPendulum()

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-pendulum.length - 1, pendulum.length + 1)
ax.set_ylim(-pendulum.length - 1, pendulum.length + 1)
line, = ax.plot([], [], 'o-', lw=2)

# Create the animation
animation = FuncAnimation(fig, update, frames=range(300), fargs=(pendulum, ax),
                          interval=50, blit=True)

plt.show()
