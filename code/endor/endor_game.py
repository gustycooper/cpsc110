from endorsmints import Endor
from calduum import init_params, out_lines, out_ints
from random import seed

def main():
    # Add login window here
    # If invalid login, quit the program

    # Valid logins continue here
    seed(25)
    init_params()
    global out_lines, out_ints
    endor = Endor("Gusty's Endor Game", out_lines, out_ints)
    endor.eventLoop()

main()
