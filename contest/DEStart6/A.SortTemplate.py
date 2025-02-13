def blocks_sort(block: list[int], template: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(0, len(template)):
        current_template = template[i]
        j = 0
        while True:
            if block[j] == current_template:
                result.append(current_template)
                block.pop(j)
            else:
                j += 1
            if j == len(block):
                break

    block.sort()
    result.extend(block)

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        block_amount = int(f.readline().strip())
        blocks = list(map(int, f.readline().split()))
        template_length = int(f.readline().strip())
        template = list(map(int, f.readline().split()))

        print(' '.join(str(x) for x in blocks_sort(blocks, template)))
