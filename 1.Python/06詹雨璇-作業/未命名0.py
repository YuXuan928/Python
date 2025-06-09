def generate_pattern(q, n=5):
    """
    q: int from 1 to 6 selecting the pattern:
      1: horizontal increment, upright, numbers
      2: horizontal increment, upright, letters
      3: vertical increment, upright, numbers
      4: vertical increment, upright, letters
      5: horizontal increment, inverted, numbers
      6: horizontal increment, inverted, letters
    n: height of the pattern (default 5)
    Returns: a string with the pattern lines
    """
    upright = q in {1, 2, 3, 4}
    horizontal = q in {1, 2, 5, 6}
    numeric = q in {1, 3, 5}

    base = ord('0') if numeric else ord('A')

    lines = []
    i_values = range(1, n+1) if upright else range(n, 0, -1)

    for i in i_values:
        indent_count = (n - i) if upright else (n - i)
        indent = '  ' * indent_count

        count = i if upright and horizontal else (
                i if upright and not horizontal else (
                (n - i + 1) if not upright and horizontal else (
                (n - i + 1))))

        row = []
        for j in range(1, count + 1):
            idx = i if not horizontal else j
            row.append(chr(base + idx))
        body = ' '.join(row)
        lines.append(f"{indent}{body}")
    return '\n'.join(lines)


def get_title(q):
    titles = {
        1: '1. 水平遞增, 正立, 數字',
        2: '2. 水平遞增, 正立, 英文字',
        3: '3. 垂直遞增, 正立, 數字',
        4: '4. 垂直遞增, 正立, 英文字',
        5: '5. 水平遞增, 倒立, 數字',
        6: '6. 水平遞增, 倒立, 英文字'
    }
    return titles.get(q, '')


def main():
    while True:
        try:
            x = int(input("請選擇： (1)第1題 (2)第2題 (3)第3題 (4)第4題 (5)第5題  (6)第6題 (0)結束 : "))
        except ValueError:
            print("請輸入 0-6 之間的數字")
            continue
        if x == 0:
            print("程式結束。")
            break
        if x not in range(1, 7):
            print("請輸入 0-6 之間的數字")
            continue

        title = get_title(x)
        pattern = generate_pattern(x)
        print(f"{title}\n{pattern}")

if __name__ == '__main__':
    main()