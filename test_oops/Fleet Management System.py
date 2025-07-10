from abc import ABC, abstractmethod

# === Abstract Base Class ===
class Vehicle(ABC):
    def __init__(self, brand, fuel_capacity, fuel_efficiency):
        self._brand = brand
        self._fuel_capacity = fuel_capacity
        self._fuel_efficiency = fuel_efficiency  # km per liter
        self._fuel_level = 0
        self._km_run = 0

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def refuel(self, liters):
        if self._fuel_level + liters > self._fuel_capacity:
            print(f"{self._brand}: Cannot refuel beyond fuel capacity.")
        else:
            self._fuel_level += liters
            print(f"{self._brand}: Refueled {liters}L. Current fuel: {self._fuel_level}L")

    def run_trip(self, distance):
        fuel_needed = distance / self._fuel_efficiency
        if self._fuel_level >= fuel_needed:
            self._fuel_level -= fuel_needed
            self._km_run += distance
            print(f"{self._brand}: Trip of {distance} km completed.")
        else:
            print(f"{self._brand}: Not enough fuel for the trip.")

    def get_km_run(self):
        return self._km_run

    def get_fuel_level(self):
        return self._fuel_level

    def get_brand(self):
        return self._brand

    @abstractmethod
    def __str__(self):
        pass

    def needs_service(self):
        return self._km_run > 10000


# === Child Classes (Inheritance) ===
class Car(Vehicle):
    def start(self):
        print(f"{self._brand} Car is starting...")

    def stop(self):
        print(f"{self._brand} Car is stopping...")

    def __str__(self):
        return f"Car - Brand: {self._brand}, Fuel: {self._fuel_level}L, KM Run: {self._km_run}"


class Bike(Vehicle):
    def start(self):
        print(f"{self._brand} Bike is starting...")

    def stop(self):
        print(f"{self._brand} Bike is stopping...")

    def __str__(self):
        return f"Bike - Brand: {self._brand}, Fuel: {self._fuel_level}L, KM Run: {self._km_run}"


class Truck(Vehicle):
    def start(self):
        print(f"{self._brand} Truck is starting...")

    def stop(self):
        print(f"{self._brand} Truck is stopping...")

    def __str__(self):
        return f"Truck - Brand: {self._brand}, Fuel: {self._fuel_level}L, KM Run: {self._km_run}"


# === Fleet Manager ===
class FleetManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_summary(self):
        print("\n=== Fleet Summary ===")
        for v in self.vehicles:
            print(v)
            print(f"{v.get_brand()} is a {v.__class__.__name__}")
            print("Needs Service" if v.needs_service() else "Does Not Need Service")
            print()


# === Demo ===
def main():
    car = Car("Toyota", fuel_capacity=50, fuel_efficiency=15)   # 15 km/l
    bike = Bike("Yamaha", fuel_capacity=12, fuel_efficiency=40) # 40 km/l
    truck = Truck("Volvo", fuel_capacity=100, fuel_efficiency=5)# 5 km/l

    fleet = FleetManager()

    # Car actions
    car.start()
    car.refuel(30)
    car.run_trip(200)
    car.stop()

    # Simulate car crossing 10,000 km
    car._km_run = 10200

    # Bike actions
    bike.start()
    bike.refuel(30)  # Over capacity
    print(bike)
    bike.stop()

    # Truck actions
    truck.start()
    truck.refuel(30)
    truck.run_trip(200)  # Needs 40L, has 30L (Should still run for simplicity)
    truck._fuel_level -= 10  # Simulating overuse
    truck.stop()

    # Add all to fleet
    fleet.add_vehicle(car)
    fleet.add_vehicle(bike)
    fleet.add_vehicle(truck)

    fleet.show_summary()


if __name__ == "__main__":
    main()
