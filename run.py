from app import App
from web.wsgi import flak_app

def run_in_terminal():
    app = App()
    app.run()

def run_on_web():
    if __name__ == "__main__" :
        flak_app.run(debug=True)
        
def run():
    print()
    print("1 : Terminal")
    print("2 : Web")
    print()
    to_run = input("Ou voulez vous lancer le programe ? ")
    if to_run == "1":
        run_in_terminal()
    elif to_run == "2":
        run_on_web()
    else :
        print("Option Non valid")
        

run()
