import sys


def print_rocket(width, fuselage_segments, striped=False):
    print_nose_cone(width)
    print_fuselage(width, fuselage_segments, striped)
    print_tail_fin(width)


def print_nose_cone(width):
    # i stands for the number of stars
    STAR_ADDER = 2
    if width // 2:
        for i in range(1, width, STAR_ADDER):
            print(" " * ((width - i) // 2) + "*" * i)
    else:
        for i in range(2, width, STAR_ADDER):
            print(" " * ((width - i) // 2) + "*" * i)


def print_fuselage(width, segments, striped=False):
    segment_width = width
    for i in range(segments):  # i stands for the row
        if striped:  # define each row
            segment_normal = "X" * segment_width
            segment_striped = '_' * segment_width
            for j in range(segment_width // 2):
                print(segment_normal)
            for k in range(segment_width // 2 + 1):
                # because if the width is an odd number,
                # the striped is less than normal segments
                print(segment_striped)
        else:
            segment = "X" * segment_width
            for i in range(segment_width):  # print more rows
                print(segment)
    print("X" * width)


def print_tail_fin(width):
    for i in range(width // 2, width, 2):
        spaces = (width - i) // 2
        print(" " * spaces + "*" * i)
    for i in range(2):
        print('*' * width)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 make_a_rocket.py \
              <width> <fuselage_segments> [striped]")
        sys.exit(1)

    width = int(sys.argv[1])
    fuselage_segments = int(sys.argv[2])
    striped = len(sys.argv) > 3 and sys.argv[3] == "striped"

    print_rocket(width, fuselage_segments, striped)
