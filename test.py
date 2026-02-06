import curses

def main(stdscr):
    curses.curs_set(0)  # يخفي المؤشر
    stdscr.nodelay(True)  # باش ما يقاطعش البرنامج في انتظار الزر
    stdscr.clear()
    
    x, y = 0, 0
    key = ''

    while key != ord('q'):  # q باش نخرج
        stdscr.clear()
        stdscr.addstr(y, x, 'X')  # الحرف اللي غادي يتحرك
        stdscr.refresh()

        try:
            key = stdscr.getch()  # تقرأ الضغط على الزر
        except:
            key = None

        if key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1

curses.wrapper(main)