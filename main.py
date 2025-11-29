from blessed import Terminal
from view_handler import ViewHandler
from Database.import_games import import_games

if __name__ == "__main__":
    import_success = import_games()
    
    if not import_success:
        exit(1)
    
    term = Terminal()
    app = ViewHandler(term)
    app.run()