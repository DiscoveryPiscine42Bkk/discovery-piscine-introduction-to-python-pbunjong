from checkmate import checkmate

def main():
    board = """\
....
....
.K..
..p."""
    checkmate(board)

    board = """\
....
....
.K..
..P."""
    checkmate(board)

if __name__ == "__main__":
    main()