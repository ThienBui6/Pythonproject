import numpy as np

# Define the collision threshold (1 km distance)
collision_threshold = 1.0  
num_simulations = 10_000  
collision_count = 0  

# Run Monte Carlo Simulation
for _ in range(num_simulations):
    # Add random noise to debris positions (simulating orbit drift)
    debris_sim = debris_data[['X_Position', 'Y_Position', 'Z_Position']] + np.random.normal(0, 0.5, size=(10, 3))
    
    # Calculate distance to satellite for each debris piece
    distances = np.linalg.norm(satellite_position - debris_sim.values, axis=1)
    
    # Count if any debris comes within the collision threshold
    collision_count += np.sum(distances < collision_threshold)

# Calculate probability of collision
collision_probability = (collision_count / num_simulations) * 100
print(f"Collision Probability: {collision_probability:.2f}%")
