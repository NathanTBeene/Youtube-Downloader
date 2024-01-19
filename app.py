import gui
from callbacks import check_dir

def main():
    #Check that directories exist. If not, create them.
    check_dir()
    
    #Draw the main GUI box
    gui.draw_window()



if __name__ == "__main__":
    main()