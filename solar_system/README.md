# :ringed_planet:Solar System - Plotly Scatter3D & Surface

A combination of Plotly Scatter3D and Plotly Surface plots is used to create an entire **Solar System** inside a graph. 

## Abstract
### Throughout the code:
1. We start by creating a few lists that contain the distance from the Sun and the diameter of celestial objects. Note that we had to reduce the size of the Sun by making it much smaller otherwise it would have made it too big for our graph.
2. While we have maintained the scale to ensure that the sizes of the planets are correct relative to each other, the Sun is not. In addition, the distance of the planets is to scale, for example, Jupyter is 7 times farther from the Sun than Venus.
3. However, we did not maintain the scale between the planets and the distance to the Sun because we expressed the diameter in kilometres while the distance was expressed in millions of kilometres.
4. Then we just use the functions defined previously to create traces for each sphere and orbit, including a few rings around Saturn.

## Reference
https://thecleverprogrammer.com/2020/10/07/visualize-a-solar-system-with-python/
