import numpy as np
import math
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Create a Sphere
def spheres(size, clr, dist=0):
    # Set up 100 points in a sphere
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    # Set up coordinates for points in the sphere
    x0 = size * np.outer(np.cos(theta), np.sin(phi)) + dist
    y0 = size * np.outer(np.sin(theta), np.sin(phi))
    z0 = size * np.outer(np.ones(np.size(theta)), np.cos(phi))

    # Set up trace for the sphere
    trace = go.Surface(x=x0, y=y0, z=z0, colorscale=[[0, clr], [1, clr]], showscale=False)
    trace.update(showlegend=False)

    return trace

# Create Orbits
def orbits(dist, offset=0, clr="white", wdth=2):
    # Initialize empty lists for each set of coordinates
    xcrd = []
    ycrd = []
    zcrd = []

    # Calculate the coordinates for each point in the orbit
    for i in range(0, 361):
        xcrd.append(dist * math.cos(math.radians(i)) + offset)
        ycrd.append(dist * math.sin(math.radians(i)))
        zcrd.append(0)

    trace = go.Scatter3d(x=xcrd, y=ycrd, z=zcrd, mode="lines", line=dict(color=clr, width=wdth))
    return trace

# Define Annotations
def annotations(xcrd, ycrd, txt, xancr='center'):
    strng = dict(showarrow=False, x=xcrd, y=ycrd, text=txt, xanchor=xancr, font=dict(color='white', size=12))
    return strng

# Visualize the Solar System
diameter_km = [200000, 4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370, 556, 24766, 1151, 1738]
diameter = [((i / 12756) * 2) for i in diameter_km]
distance_from_sun = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4, 7785.7, 1433.5, 2872.5, 4495.1]

# Create spheres for the Sun and Planets
trace0 = spheres(diameter[0], "#ffff00", distance_from_sun[0]) # Sun
trace1 = spheres(diameter[1], "#87877d", distance_from_sun[1]) # Mercury
trace2 = spheres(diameter[2], "#d23100", distance_from_sun[2]) # Venus
trace3 = spheres(diameter[3], "#325bff", distance_from_sun[3]) # Earth
trace4 = spheres(diameter[4], "#b20000", distance_from_sun[4]) # Mars
trace5 = spheres(diameter[5], "#ebebd2", distance_from_sun[5]) # Jupiter
trace6 = spheres(diameter[6], "#ebcd82", distance_from_sun[6]) # Saturn
trace7 = spheres(diameter[7], "#37ffda", distance_from_sun[7]) # Uranus
trace8 = spheres(diameter[8], "#2500ab", distance_from_sun[8]) # Neptune

# Set up orbit traces
trace11 = orbits(distance_from_sun[1]) # Mercury
trace12 = orbits(distance_from_sun[2]) # Venus
trace13 = orbits(distance_from_sun[3]) # Earth
trace14 = orbits(distance_from_sun[4]) # Mars
trace15 = orbits(distance_from_sun[5]) # Jupiter
trace16 = orbits(distance_from_sun[6]) # Saturn
trace17 = orbits(distance_from_sun[7]) # Uranus
trace18 = orbits(distance_from_sun[8]) # Neptune

# Use the same to draw a few rings for Saturn
trace21 = orbits(23, distance_from_sun[6], "#827962", 3)
trace22 = orbits(24, distance_from_sun[6], "#827962", 3)
trace23 = orbits(25, distance_from_sun[6], "#827962", 3)
trace24 = orbits(26, distance_from_sun[6], "#827962", 3)
trace25 = orbits(27, distance_from_sun[6], "#827962", 3)
trace26 = orbits(28, distance_from_sun[6], "#827962", 3)

layout = go.Layout(title = "Solar System", 
                   showlegend=False,
                   margin=dict(l=0, r=0, b=0, t=0),
                   paper_bgcolor = "black", 
                   scene = dict(xaxis=dict(title="Distance from the Sun", 
                                           titlefont=dict(color="black"),
                                           range=[-7000, 7000],
                                           backgroundcolor="black", 
                                           gridcolor="black", 
                                           color="black"),
                                yaxis=dict(title="Distance from the Sun",
                                           titlefont=dict(color="black"),
                                             range=[-7000, 7000],
                                                backgroundcolor="black",
                                                gridcolor="black",
                                                color="black"),
                                zaxis=dict(title="",
                                           range=[-7000, 7000],
                                           backgroundcolor="black",
                                           color="black",
                                           gridcolor="black"),
                                annotations = [annotations(distance_from_sun[0], 40, "Sun", xancr="left"),
                                               annotations(distance_from_sun[1], 5, "Mercury"),
                                               annotations(distance_from_sun[2], 9, "Venus"),
                                               annotations(distance_from_sun[3], 9, "Earth"),
                                               annotations(distance_from_sun[4], 7, "Mars"),
                                               annotations(distance_from_sun[5], 30, "Jupiter"),
                                               annotations(distance_from_sun[6], 28, "Saturn"),
                                               annotations(distance_from_sun[7], 20, "Uranus"),
                                               annotations(distance_from_sun[8], 20, "Neptune")]
                                )
                    )

fig = go.Figure(data=[trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8,
                      trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18,
                      trace21, trace22, trace23, trace24, trace25, trace26], layout=layout)

fig.show()