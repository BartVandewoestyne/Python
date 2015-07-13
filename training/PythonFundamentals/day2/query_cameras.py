import argparse

# TODO: finish this

# Opmerkingen:
#   - Beter alles in lijsten opbouwedn, en dan tuple retourneren.
#   - Laatste 9 kan je er af slicen

def parse(data):
    # Skip first 2 lines.
    data.next()
    data.next()
    result = []
    for line in data:
        result.append(tuple(line.split(',')))
    result = result[:-9]  # Remove last 9 lines.
    filtered_result = list(filter(lambda cinfo: cinfo[2] == "E40", result))
    return tuple(filtered_result)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--cameras", dest="camera_file", type=str, required=True,
                        help="A properly formatted file containing locations of cameras")
    parser.add_argument("--cameras-in-city", type=str, dest="city",
                        help="Queries input files for all cameras in a city")
    parser.add_argument("--cameras-on-road", type=str, dest="road",
                        help="Queries input files for all cameras on a certain road")
    args = parser.parse_args()
    f = open(args.cameras)
    camera_info = parse(f)
    print("Found {0:d} cameras".format(len(camera_info)))
    for camera in camera_info:
        print(camera)
