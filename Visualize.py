from mpl_toolkits.mplot3d import Axes3D
import matplotlib as plt

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot satellite position
ax.scatter(*satellite_position, color="blue", s=100, label="Satellite")

# Plot debris positions
ax.scatter(debris_data['X_Position'], debris_data['Y_Position'], debris_data['Z_Position'], color="red", s=50, label="Debris")

# Labels and legend
ax.set_xlabel("X Position (km)")
ax.set_ylabel("Y Position (km)")
ax.set_zlabel("Z Position (km)")
ax.set_title("Satellite and Space Debris Positions")
ax.legend()
plt.show()
