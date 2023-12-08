"""
Plot some x coordinates against y coordinates over a clipped region.

Args:
    x_coords: The x coords to plot.
    y_coords: The y coords to plot.
    title: The title of the plot.
    x_min: The minimum x cut off.
    x_max: The maximum x cut off.
    width: The width of the plot.
    height: The height of the plot.
    fontsize: The fontsize of the plot.
    dot_size: The size of the dots in the plot.
"""
def plot_bifurcation_diagram(
    x_coords, 
    y_coords, 
    title="",
    x_min=None, 
    x_max=None, 
    width=50, 
    height=30,
    fontsize=24,
    dot_size=0.05,
    gridline_count=30,
    x_label="R",
    y_label="x_eq"
):
    # Create the plot
    fig, axes = plt.subplots(figsize=(width, height))

    # Clip the plot if we have a min or max provided
    if x_min or x_max:
        axes.set_xlim(x_min, x_max)

    # Plot the coordinates
    axes.scatter(x_coords, y_coords, marker='o', linestyle='-', color='b', s=dot_size)

    # Set the title and labels of the plot
    axes.set_title(f'{title} (from x={x_min} to x={x_max})', fontsize=fontsize)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    
    # Specify the positions of our vertical gridlines by disabling the default x axis gridlines
    # and then manually adding in our own.
    axes.grid(axis='y', linestyle='--')
    gridlines = np.linspace(*axes.get_xlim(), gridline_count)
    axes.set_xticks(gridlines)
    for gridline in gridlines:
        axes.axvline(x=gridline, color='black', linestyle='-', linewidth=.3)