import math


def list_maker(f):
	lines = list()
	dictionary = dict()
	while True:
		line = f.readline()
		if not line:
			break
		lines.append(line.strip())
		for line in lines:
			line = line.split(":")
			dictionary[line[0]] = line[1].split(",")
	return dictionary


def stop_dimension(drone_stops, stops):
	drone_stops_list = list()
	for stop in drone_stops:
		drone_stops_list.append(stops[stop])
	return drone_stops_list


def dimensions(coordinates):
	d = 0
	for i in range(len(coordinates)):
		for j in range(i + 1, len(coordinates)):
			x1, y1 = coordinates[i]
			x2, y2 = coordinates[j]
			d += math.sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)
			break
	return d


def max_dictionary(dictionary):
	max_value = max(dictionary.values())
	max_key = None

	for key, value in dictionary.items():
		if value == max_value:
			max_key = key
			break

	return [max_key, max_value]


def main():
	with open("drones.txt", "r") as f:
		drones = list_maker(f)

	with open("stops.txt", "r") as f:
		stops = list_maker(f)

	drones_distance = dict()
	for drone in drones:
		drone_stops = stop_dimension(drones[drone], stops)
		drones_distance[drone] = dimensions(drone_stops)

	total_distance = 0
	for drone in drones_distance:
		if total_distance < drones_distance[drone]:
			total_distance = drones_distance[drone]

	total_stops = max_dictionary(drones_distance)[0]
	total_distance = max_dictionary(drones_distance)[1]

	print(f" highest battery capacity for {max_dictionary(drones_distance)[0]}")
	print(f"total distance = {total_distance}")
	print("number of stops = ", len(drones[total_stops]))


if __name__ == "__main__":
	main()
