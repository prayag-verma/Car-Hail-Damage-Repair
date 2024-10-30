import math

def calculate_force(damage_area, material_strength=1000):  # material_strength in N/m^2
    # This is a simplified model. In a real-world scenario, you'd use more complex physics models.
    radius = math.sqrt(damage_area / math.pi)
    force = material_strength * damage_area * 0.01  # Scaling factor to get more reasonable numbers
    return force

def get_device_adjustment(force, max_force=10000):  # max_force in Newtons
    adjustment_percentage = min(force / max_force * 100, 100)
    return f"Device needs to adjust to {adjustment_percentage:.2f}% of its maximum capability"