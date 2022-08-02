import math


class Wind:
  @classmethod
  def get_true_wind(cls, wind_angle, wind_speed, boat_velocity):
    new_wind_speed = None
    new_wind_angle = None

    r_wind_angle = math.radians(wind_angle)

    x = math.sin(r_wind_angle) * wind_speed
    y = math.cos(r_wind_angle) * wind_speed - boat_velocity

    new_wind_speed = math.sqrt(x**2 + y**2)
    new_wind_angle = math.degrees(math.atan2(x, y))

    print(f"True Wind Speed: {new_wind_speed}")
    print(f"True Wind Angle: {new_wind_angle}")


  @classmethod
  def get_apparent_wind(cls, wind_angle, wind_speed, boat_velocity):
    new_wind_speed = None
    new_wind_angle = None

    r_wind_angle = math.radians(wind_angle)

    x = math.sin(r_wind_angle) * wind_speed
    y = math.cos(r_wind_angle) * wind_speed + boat_velocity

    new_wind_speed = math.sqrt(x**2 + y**2)
    new_wind_angle = math.degrees(math.atan2(x, y))

    print(f"Apparent Wind Speed: {new_wind_speed}")
    print(f"Apparent Wind Angle: {new_wind_angle}")


def main():
  while True:
    mode = input("Apparent or True Wind given [A/t]: ")

    angle = input("Wind Angle: ")
    speed = input("Wind Speed: ")
    velocity = input("Velocity: ")

    try:
      angle = float(angle)
      speed = float(speed)
      velocity = float(velocity)
    except ValueError:
      print("An error ocurred... Try again!\n")
      continue

    print()
    if mode.lower().startswith("t"):
      Wind.get_apparent_wind(angle, speed, velocity)
    else:
      Wind.get_true_wind(angle, speed, velocity)
    print()


if __name__ == '__main__':
  main()