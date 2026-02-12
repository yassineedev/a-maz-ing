import curses


def main(stdscr):
    curses.curs_set(0)
    curses.clear()
    curses.addstr(5, 10, "@")


curses.wrapper(main)

