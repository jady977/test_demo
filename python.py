def get_num_rooms(areas):
    """Returns the number of rooms above and below the average area."""
    avg = sum(areas) / len(areas)
    above = sum(1 for area in areas if area > avg)
    below = sum(1 for area in areas if area < avg)
    return above, below

def read_rooms(file_path):
    """Reads room data from the given file and calculates area and perimeter."""
    rooms = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0]
                    length = float(parts[1])
                    width = float(parts[2])
                    area = length * width
                    perimeter = 2 * (length + width)
                    rooms.append({
                        'name': name,
                        'area': area,
                        'perimeter': perimeter
                    })
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return rooms

def display_table(rooms):
    """Displays the room statistics in a formatted table."""
    print("\n" + "-"*35)
    print("        |House Rooms Stats|")
    print("-"*35 + "\n")
    print(f"{'Room Num':<10}{'Room':<18}{'Area (m^2)':<15}{'Perimeter (m)':<15}")
    print(f"{'-'*10} {'-'*17} {'-'*14} {'-'*14}")

    max_area = max(room['area'] for room in rooms)
    min_area = min(room['area'] for room in rooms)
    total_area = 0

    for i, room in enumerate(rooms, start=1):
        marker = ''
        if room['area'] == max_area:
            marker = "<=== Max Area"
        elif room['area'] == min_area:
            marker = "<=== Min Area"
        print(f"{i:<10}{room['name']:<18}{room['area']:<15.0f}{room['perimeter']:<15.0f}{marker}")
        total_area += room['area']

    print("-" * 50)
    print(f"Total area: {total_area:.0f} m^2")
    return [room['area'] for room in rooms]

def main():
    file_path = "house.txt"  # Must be in the same folder
    rooms = read_rooms(file_path)

    if not rooms:
        return

    areas = display_table(rooms)
    above, below = get_num_rooms(areas)

    print(f"\nThe number of rooms above the avg: {above}")
    print(f"The number of rooms below the avg: {below}")

if __name__ == "__main__":
    main()
