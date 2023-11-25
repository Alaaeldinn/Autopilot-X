import carla
import time

# Connect to the Carla server
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)  # seconds

# Retrieve the Carla world
world = client.get_world()

# Get the blueprint library
blueprint_library = world.get_blueprint_library()

# Select a vehicle blueprint (e.g., "vehicle.tesla.model3")
vehicle_blueprint = blueprint_library.filter('vehicle.tesla.model3')[0]

# Set the spawn location
spawn_location = carla.Transform(carla.Location(x=10, y=10, z=2), carla.Rotation())

# Spawn the vehicle
vehicle = world.spawn_actor(vehicle_blueprint, spawn_location)

# Let the vehicle exist for a few seconds
time.sleep(5)

# Destroy the vehicle
vehicle.destroy()
