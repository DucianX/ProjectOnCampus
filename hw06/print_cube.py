def horizontal_edge(n):
    x = int(n / 2)
    print(' ' * (1 + x) + '+' + '-'* 2 * n + '+')
   

def hori_edge_1to2(n):
    x = int(n / 2)
    y = int(n)
    for i in range(x):
        print(' ' * x + '/'+ ' ' * 2 * y + '/' + i * ' ' + '|')
        x -= 1


def second_hori_edge(n):
    y = int(n)
    x = int(n / 2)
    print('+' + '-' * (2 * y) + '+' + ' ' * x + '|')


def upperhalf_vertical_edge(n):
    x = int(n / 2)
    z = int(n * 2)
    q = int ((n - 2) / 2)
    for i in range(q):
        print('|' + ' ' * z + '|' + x * ' ' + '|')
    
    print('|' + ' ' * z + '|' + x * ' ' + '+')


def lower_half(n):
    x = int(n / 2 - 1)
    y = int(n)
    z = int(2 * n)
    while(x + 1):
        print('|' + ' ' * z + '|' + x * ' ' + '/' )
        x -= 1 


def lowest_horizontal_edge(n):
    print('+' + '-'* 2 * n + '+')


def main():
    size = int(input("Input cube size (multiple of 2): "))
    while size % 2 != 0:  # Ensure the size is a multiple of 2
        size = int(input("Please ensure you enter a multiple of 2: "))
    # draw_cube(size)
    horizontal_edge(size)
    hori_edge_1to2(size)
    second_hori_edge(size)
    upperhalf_vertical_edge(size)
    lower_half(size)
    lowest_horizontal_edge(size)


if __name__ == "__main__":
    main()
