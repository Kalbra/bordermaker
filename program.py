def border_text(text="hello world", down_left_cornor="+", down_right_cornor="+", up_left_cornor="+", up_right_cornor="+", up_area="-", down_area="-", left_area="|", right_area="|"):

    length_raw = len(text)

    length1 = length_raw
    length2 = length_raw

    print(up_left_cornor, end="")
    while length1 > 0:
        print(up_area, end="")
        length1 = length1 - 1
    print(up_right_cornor)
    print(left_area+text+right_area)

    print(down_left_cornor, end="")
    while length2 > 0:
        print(down_area, end="")
        length2 = length2 - 1
    print(down_right_cornor)
