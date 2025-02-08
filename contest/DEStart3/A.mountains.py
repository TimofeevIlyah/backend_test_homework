import array


def valid_mountain_array(heights: array.array) -> bool:
    ln = len(heights)
    if ln < 3:
        return False

    is_peak = False
    prior_height = heights[0]

    for i in range(1, ln):
        current_height = heights[i]

        if current_height > prior_height:
            if is_peak:
                return False
        elif current_height < prior_height:
            if not is_peak:
                if i == 1:
                    return False
                is_peak = True
        else:
            return False

        prior_height = current_height

    return is_peak


def main():
    with open('input.txt', 'r') as f:
        heights = array.array('i', list(map(int, f.readline().split())))
    print(valid_mountain_array(heights))


if __name__ == '__main__':
    main()
