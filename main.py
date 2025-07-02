from GUI_folder import gui_main
from data_base_folder import data_base_connect


if __name__ == "__main__":
    gui_main.run_gui()
    data_base_connect.star_connecet_db()