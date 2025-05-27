
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

g = 9.81
t_span = (0, 20)
t_eval = np.linspace(*t_span, 1000)

params_init = {
    'alpha': 2.0,
    'gamma': 1.2,
    'omega': 2.5,
    'L': 1.5,
    'theta0': 0.1,
    'v0': 0.0
}

modo_oscuro = False

def resolver_pendulo_caotico(alpha, gamma, omega, L, theta0, v0):
    beta = g / L
    def pendulo_caotico(t, y):
        theta, v = y
        return [v, -alpha * v - beta * np.sin(theta) + gamma * np.cos(omega * t)]
    sol = solve_ivp(pendulo_caotico, t_span, [theta0, v0], t_eval=t_eval)
    x = L * np.sin(sol.y[0])
    y = -L * np.cos(sol.y[0])
    return sol, x, y

sol, x, y = resolver_pendulo_caotico(**params_init)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
plt.subplots_adjust(left=0.1, bottom=0.4, right=0.9, top=0.9, wspace=0.4)

line, = ax1.plot([], [], 'o-', lw=2)
trace, = ax1.plot([], [], 'r-', alpha=0.3)
theta_line, = ax2.plot([], [], 'b-')

ax1.set_xlim(-2.5, 2.5)
ax1.set_ylim(-2.5, 2.5)
ax1.set_aspect('equal')
ax1.set_title('Péndulo caótico')

ax2.set_xlim(t_span)
ax2.set_ylim(-np.pi, np.pi)
ax2.set_title('θ(t)')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Ángulo (rad)')

slider_height = 0.03
start_y = 0.30
space = 0.05
slider_axes = {
    key: plt.axes([0.15, start_y - i * space, 0.65, slider_height])
    for i, key in enumerate(params_init)
}
sliders = {
    'alpha': Slider(slider_axes['alpha'], 'Amortiguamiento α', 0.0, 5.0, valinit=params_init['alpha']),
    'gamma': Slider(slider_axes['gamma'], 'Forzamiento γ', 0.0, 5.0, valinit=params_init['gamma']),
    'omega': Slider(slider_axes['omega'], 'Frecuencia ω', 0.1, 10.0, valinit=params_init['omega']),
    'L': Slider(slider_axes['L'], 'Longitud L (m)', 0.5, 3.0, valinit=params_init['L']),
    'theta0': Slider(slider_axes['theta0'], 'Ángulo inicial θ₀ (rad)', -np.pi, np.pi, valinit=params_init['theta0']),
    'v0': Slider(slider_axes['v0'], 'Velocidad inicial v₀ (rad/s)', -10.0, 10.0, valinit=params_init['v0'])
}

reset_ax = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(reset_ax, 'Reiniciar')

darkmode_ax = plt.axes([0.1, 0.025, 0.15, 0.04])
button_darkmode = Button(darkmode_ax, '🌙 Modo oscuro')

trail_x, trail_y = [], []
theta_data_t, theta_data = [], []

def aplicar_modo_oscuro(activo):
    fondo = '#121212' if activo else 'white'
    fig.patch.set_facecolor(fondo)
    fondo_ax = '#1e1e1e' if activo else 'white'
    color_txt = 'white' if activo else 'black'
    color_linea = 'cyan' if activo else 'blue'
    ax1.set_facecolor(fondo_ax)
    ax2.set_facecolor(fondo_ax)
    ax1.title.set_color(color_txt)
    ax2.title.set_color(color_txt)
    ax1.xaxis.label.set_color(color_txt)
    ax2.xaxis.label.set_color(color_txt)
    ax1.yaxis.label.set_color(color_txt)
    ax2.yaxis.label.set_color(color_txt)
    ax1.tick_params(colors=color_txt)
    ax2.tick_params(colors=color_txt)
    for spine in ax1.spines.values():
        spine.set_color(color_txt)
    for spine in ax2.spines.values():
        spine.set_color(color_txt)
    theta_line.set_color(color_linea)
    fig.canvas.draw_idle()

def inicio():
    line.set_data([], [])
    trace.set_data(trail_x, trail_y)
    theta_line.set_data(theta_data_t, theta_data)
    return line, trace, theta_line

def cambiar(frame):
    i = frame
    line.set_data([0, x[i]], [0, y[i]])
    trail_x.append(x[i])
    trail_y.append(y[i])
    trace.set_data(trail_x, trail_y)
    theta_data_t.append(sol.t[i])
    theta_data.append(sol.y[0][i])
    theta_line.set_data(theta_data_t, theta_data)
    return line, trace, theta_line

ani = FuncAnimation(fig, cambiar, frames=len(t_eval), init_func=inicio, interval=20, blit=True)

def actualizar(val):
    global sol, x, y
    valores = {key: sliders[key].val for key in sliders}
    sol, x, y = resolver_pendulo_caotico(**valores)
    inicio()

for slider in sliders.values():
    slider.on_changed(actualizar)

def reiniciar(event):
    for slider in sliders.values():
        slider.reset()
    trail_x.clear()
    trail_y.clear()
    theta_data_t.clear()
    theta_data.clear()

def alternar_modo_oscuro(event):
    global modo_oscuro
    modo_oscuro = not modo_oscuro
    aplicar_modo_oscuro(modo_oscuro)

button_reset.on_clicked(reiniciar)
button_darkmode.on_clicked(alternar_modo_oscuro)

aplicar_modo_oscuro(modo_oscuro)
plt.show()
