with ui.expansion("Art"):
    c1 = ui.color_input(label="Color", value="#ff0000")
    c2 = ui.color_input(label="Color", value="#ff0000")
    ui.button("Set Color", on_click=lambda: print("Set Color"))


with ui.expansion("Circle"):
    cx = ui.number("circle x", value=8)
    cy = ui.number("circle y", value=8)
    rad = ui.number("circle rad", value=10)

    res = ui.number("Theta Resolution", value=20)
    th = np.linspace(0, 2*np.pi, res.value)


    

sp = ui.line_plot(n=1, update_every=1, close=False, figsize=(3, 2))

def scatter_plot(x, y):
    sp.push(x, [y])
    print('updated')



tta = ui.timer(1, sine_animate)

with ui.card():
    # circle plot
    circle=False
    if circle:
        x = [cx.value + rad.value * np.cos(theta) for theta in th]
        y = [cx.value + rad.value * np.sin(theta) for theta in th]

        a_x, a_y = [], []
        for i in range(len(x)):
            eq_x, eq_y = point_make(x[i], y[i])
            a_x.append(eq_x)
            a_y.append(eq_y)
        scatter_plot(a_x, a_y)

    elif True:
        pass
        
        