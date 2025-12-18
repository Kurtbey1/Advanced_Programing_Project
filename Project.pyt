# =================================================================
# Q3) Simple Simulated Self-Driving Car (Python OOP)
# =================================================================


LANE_CENTER = 0.0 # Lane center is defined as lateral position 0.0
SIMULATION_STEPS = 20
FORWARD_SPEED = 1.0 # Constant forward movement per step
STEERING_SENSITIVITY = 0.5 

class Car:

    def __init__(self, initial_position: float = 4.0, speed: float = FORWARD_SPEED):
        self.position = initial_position
        self.speed = speed
        self.steering_angle = 0.0
        self.distance_forward = 0.0 

    def update_position(self):

        self.position += self.steering_angle
        

        self.distance_forward += self.speed

    def steer(self, angle: float):
        self.steering_angle = angle

    def __str__(self):
        return (f"Pos: {self.position:.2f} | "
                f"Steering: {self.steering_angle:+.2f} | "
                f"Forward: {self.distance_forward:.0f}")


class LaneSensor:

    def get_lane_offset(self, car_position: float) -> float:

        return car_position - LANE_CENTER


class Controller:

    def __init__(self, sensitivity: float = STEERING_SENSITIVITY):
        self.sensitivity = sensitivity

    def decide_steering_angle(self, offset: float) -> float:
        return -offset * self.sensitivity


# --- Main Program Simulation ---
def run_simulation():
    
    car = Car(initial_position=4.0) 
    sensor = LaneSensor()
    controller = Controller()

    print("\n" + "=" * 70)
    print("Q3: Simple Self-Driving Car Simulation (OOP)")
    print("-" * 70)
    print(f"Initial Lateral Position: {car.position:.1f} (Car starts off-center, Lane Center is {LANE_CENTER:.1f})")
    print(f"Simulation Steps: {SIMULATION_STEPS}")
    print("-" * 70)
    print(f"STEP | OFFSET | STEERING ANGLE | CAR POSITION (Lateral)")
    print("-" * 70)

    for step in range(1, SIMULATION_STEPS + 1):
        offset = sensor.get_lane_offset(car.position)
        
        new_steering_angle = controller.decide_steering_angle(offset)
        
        car.steer(new_steering_angle)
        car.update_position()
        
        print(f"{step:4} | {offset:+.4f} | {new_steering_angle:+.4f} | {car.position:+.4f}")

    print("-" * 70)
    print(f"Simulation End: Car final position is {car.position:+.4f}. Correction successful.")
    print("=" * 70)


if __name__ == "__main__":
    run_simulation()