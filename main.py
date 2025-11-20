from view_handler import ViewHandler
from Database.import_games import importGames

if __name__ == "__main__":
    importGames()
    app = ViewHandler()
    app.run()