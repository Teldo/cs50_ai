import csv
import sys

from util import Node, StackFrontier, QueueFrontier
from degrees import load_data, person_id_for_name, shortest_path, names, people, movies


# # Maps names to a set of corresponding person_ids
# names = {}

# # Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
# people = {}

# # Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
# movies = {}

def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    ## debug
    print("----------- debug ------------")
    try:
        print(source)
        print(people[source])
    except KeyError:
        print("KeyError")
    print("----------- debug ------------")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")
    

if __name__ == "__main__":
    main()