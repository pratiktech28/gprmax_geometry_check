import matplotlib.pyplot as plt
import re
import sys

def plot_geometry(file_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    found_geometry = False

    with open(file_path, 'r') as f:
        for line in f:
            # Box check: #box: x1 y1 z1 x2 y2 z2 material
            if line.startswith('#box:'):
                parts = line.split(': ')[1].split()
                x1, y1, x2, y2 = float(parts[0]), float(parts[1]), float(parts[3]), float(parts[4])
                rect = plt.Rectangle((x1, y1), x2-x1, y2-y1, edgecolor='r', fill=False, label='Box')
                ax.add_patch(rect)
                found_geometry = True

            # Cylinder check: #cylinder: x y z_start z_end radius material
            elif line.startswith('#cylinder:'):
                parts = line.split(': ')[1].split()
                x, y, r = float(parts[0]), float(parts[1]), float(parts[4])
                circle = plt.Circle((x, y), r, color='b', fill=False, label='Cylinder')
                ax.add_patch(circle)
                found_geometry = True

    if not found_geometry:
        print("❌ No geometry found to plot!")
        sys.exit(1)

    ax.set_aspect('equal')
    plt.title("gprMax Geometry Preview (X-Y Plane)")
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.grid(True)
    plt.savefig('.github/workflows/geometry_preview.png')
    print("✅ Geometry plot saved as geometry_preview.png")

if __name__ == "__main__":
    plot_geometry('user_model.in')