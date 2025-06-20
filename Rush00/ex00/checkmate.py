def checkmate(board: str): #ฟังชั่นหลัก
    board = board.strip().split('\n')
    size = len(board)

    for row in board: #หาพิกัดในบอร์ดหาไม่เจอจะขึ้นerror
        if len(row) != size:
            print("Error")
            return

    king_pos = None #หาพิกัดของK
    for i in range(size): #row แถวนอน i
        for j in range(len(board[i])): #collum แถวตั้ง j
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos: #ไม่มีคิงให้ขึ้นerror
        print("Error")
        return

    def in_bounds(x, y): #ฟังชั่นพิกัดในบอร์ด
        return 0 <= x < size and 0 <= y < len(board[x])

    def is_pawn_attacking(): #การหาพิกัดพอนที่โจมตีคิง
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and board[nx][ny] == 'P':
                return True
        return False

    def is_bishop_attacking(): #หาพิกัดที่บิช็อบจะสามารถโจมตีคิง
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece == 'B' or piece == 'Q':
                    return True
                else:
                    break
        return False

    def is_rook_attacking(): #หาพิกัดที่รุกจะโจมตีคิง
        x, y = king_pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece == 'R' or piece == 'Q':
                    return True
                else:
                    break
        return False

    if is_pawn_attacking() or is_bishop_attacking() or is_rook_attacking():
        print("Success")
    else:
        print("Fail")