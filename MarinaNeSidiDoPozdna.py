from RectangularScene import RectangularScene

if __name__ == '__main__':
    scene = RectangularScene(10, 10, 3, 0.01, 0.5, 5)
    scene.run()
    final_positions = scene.get_particles()
    print()
