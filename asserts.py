from circle import Circle

tire = Circle(42)
# tire.area()

tire.correct_radius(-1.02)
print(tire.radius)


tire.area()