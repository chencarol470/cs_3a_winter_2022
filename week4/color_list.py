# 2-tuples in a larger list of various colors:
# manual list of pairs:  (name = string, rgb values = 3-tuple)
RGB_COLORS = [
   ("white", (1., 1., 1.)),
   ("silver", (.75, .75, .75)),
   ("gray", (.5, .5, .5)),
   ("black", (0., 0., 0.)),
   ("red", (1., 0., 0.)),
   ("maroon", (.5, 0., 0.)),
   ("yellow", (1., 1., 0.)),
   ("olive", (.5, .5, 0.)),
   ("lime", (.75, 1., 0.)),
   ("green", (0., .5, 0.)),
   ("aqua", (0., 1., 0.)),
   ("teal", (1., .5, .5)),
   ("sky blue", (0.529, 0.808, 0.922)),
   ("blue", (0., 0., 1.)),
   ("navy", (0., 0., 0.5)),
   ("fuchsia", (1., 0., 1.)),
   ("purple", (.5, 0., .5)),
   ("pink", (1., 0.753, 0.796)),
   ("hot pink", (1., 0.412, 0.706)),
   ("lime green", (0.196, 0.804, 0.196)),
   ("pale green", (0.596, 0.984, 0.596)),
   ("blue violet", (0.541, 0.169, 0.886)),
   ("turquoise", (0.251, 0.878, 0.816)),
   ("sea green", (0.180, 0.545, 0.341)),
   ("slate blue", (0.415, 0.353, 0.205)),
   ("aquamarine", (0.498, 1., 0.831)),
   ("peach puff", (1., 0.855, 0.725)),
   ("khaki", (0.941, 0.901, 0.549)),
   ("tan", (0.824, 0.706, 0.549))
   ]




"""
The program will ask the user to supply three numbers from 0 to 1 to represent a custom color of their choosing:

enter red, green and blue values of your color, separated by a spaces. 
legal values run from 0.0 (min) to 1.0 (max): .9 .25 .73
Here they chose red = .9, green = .25 and blue = .73. The program then compares this choice to the 3-tuples of rgb values in our list and locate the closest match. It then tells the user the name and valued of the closest color in our "off the shelf" colors to their creation:

The pre-packaged color that most closely matches your custom design is 
'hot pink', whose rgb values are red = 1.0, green = 0.412, blue = 0.706
The way it measures this "closeness" of two colors is by taking the sum of the squares of the differences of the three components, i.e.

distance between (r1, g1, b1) and (r2, g2, bg)

is defined to be the number

(r2 - r1)2 + (g2 - g1)2 + (b2 - b1)2.

This will be a number from 0.0 (identical colors) to 3.0 (very distinct colors). The smaller the number the closer they are.

We'll do lots of error checking to make sure that the user supplies three values, all numeric and all between 0 and 1. Only then will it try to find the best match.

Here's the entire program.
"""

# manual list of pairs:  (name = string, rgb values = 3-tuple)
RGB_COLORS = [
    ("white", (1., 1., 1.)),
    ("silver", (.75, .75, .75)),
    ("gray", (.5, .5, .5)),
    ("black", (0., 0., 0.)),
    ("red", (1., 0., 0.)),
    ("maroon", (.5, 0., 0.)),
    ("yellow", (1., 1., 0.)),
    ("olive", (1., 0., 0.)),
    ("lime", (0., 1., 0.)),
    ("green", (0., .5, 0.)),
    ("aqua", (0., 1., 0.)),
    ("teal", (1., .5, .5)),
    ("sky blue", (0.529, 0.808, 0.922)),
    ("blue", (0., 0., 1.)),
    ("navy", (0., 0., 0.5)),
    ("fuchsia", (1., 0., 1.)),
    ("purple", (.5, 0., .5)),
    ("pink", (1., 0.753, 0.796)),
    ("hot pink", (1., 0.412, 0.706)),
    ("lime green", (0.196, 0.804, 0.196)),
    ("pale green", (0.596, 0.984, 0.596)),
    ("blue violet", (0.541, 0.169, 0.886)),
    ("turquoise", (0.251, 0.878, 0.816)),
    ("sea green", (0.180, 0.545, 0.341)),
    ("slate blue", (0.415, 0.353, 0.205)),
    ("aquamarine", (0.498, 1., 0.831)),
    ("peach puff", (1., 0.855, 0.725)),
    ("khaki", (0.941, 0.901, 0.549)),
    ("tan", (0.824, 0.706, 0.549))
]


def get_rgb_value():
    """ ask use for three values between 0.0 and 1.0 and return as a 3-tuple
        keep in loop until obey """
    accepted = False
    while not accepted:
        user_color = input("\nenter red, green and blue values of your color, "
                           "separated by a spaces. "
                           "\nlegal values run from 0.0 (min) to 1.0 (max): ")
        try:
            rgb_list = user_color.split()
            r, g, b = rgb_list
            r, g, b = float(r), float(g), float(b)
            if not (0 <= r <= 1 and 0 <= g <= 1 and 0 <= b <= 1):
                print(" *ERROR*  Values must be between 0.0 and "
                      "1.0 (inclusive).")
                continue
            accepted = True
        except ValueError:
            print(" *ERROR*  Please enter 3 numbers separated by spaces.")

    return (r, g, b)


def color_dist(rgb_1, rgb_2):
    """ accept two color tuples and return the distance between them """
    if (type(rgb_1) != tuple
            or
            type(rgb_2) != tuple
            or
            len(rgb_1) != 3
            or
            len(rgb_2) != 3
    ):
        return None

    dist = 0
    for k in range(3):
        dist += (rgb_2[k] - rgb_1[k]) ** 2
        print(dist)

    return dist


def find_closest_match(rgb_val, color_list):
    """ show the color name closest to rgb_val"""

    # establish initial "best" values
    best_color_so_far = None
    # whatever the definition of dist() is, the following is larger:
    smallest_dist_so_far = 1 + color_dist((0, 0, 0), (1, 1, 1))
    print(smallest_dist_so_far)

    for color in color_list:
        current_distance = color_dist(rgb_val, color[1])
        if current_distance < smallest_dist_so_far:
            smallest_dist_so_far = current_distance
            best_color_so_far = color

    return best_color_so_far


def main():
    print("\nThese are our packaged colors --------------\n")
    for k in range(len(RGB_COLORS)):
        print("tuple #{:3}: {:13} = {}".
              format(k, RGB_COLORS[k][0], str(RGB_COLORS[k][1])))

    print("\nNow, you can provide the RGB values of your own custom color.\n")
    user_rgb_tuple = get_rgb_value()
    winner = find_closest_match(user_rgb_tuple, RGB_COLORS)

    print(f"\nThe pre-packaged color that most closely matches your custom "
          f"design is \n{winner[0]}, whose rgb values are "
          f"red = {winner[1][0]}, green = {winner[1][1]}, "
          f"blue = {winner[1][2]}\n")


if __name__ == "__main__":
    main()