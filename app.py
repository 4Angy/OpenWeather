import curses
from var import Unidades, get_weather, get_weather_forecast, mostrar_historial

def iniciar_menu(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    menu_items = [
        ("Elegir ciudad", get_weather),
        ("Cambiar de unidad", Unidades),
        ("Ver historial", mostrar_historial),
        ("Clima de los próximos 5 días", get_weather_forecast),
        ("Salir de la aplicación", None)
    ]

    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, " * * * Menú Principal * * *", curses.A_BOLD)
        stdscr.addstr(1, 0, "---------------------------")

        for idx, (label, _) in enumerate(menu_items):
            x = 2
            y = idx + 2
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, label)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, label)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key == ord("\n"):
            if current_row == len(menu_items) - 1:
                break
            selected_function = menu_items[current_row][1]
            if selected_function:
                selected_function(stdscr)

curses.wrapper(iniciar_menu)
