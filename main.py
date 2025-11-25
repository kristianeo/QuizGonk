from tkinter import Tk

from view_handler import ViewHandler
from Database.import_games import import_games

if __name__ == "__main__":
    root = Tk()
    import_games()
    app = ViewHandler(root)
    app.run()
    root.mainloop()