from parsing_dork import DorkParser
from start_wpscan import wpscan
import argparse

banner = '''
 __          __      _____                         
 \ \        / /     |  __ \                        
  \ \  /\  / / __   | |__) |_ _ _ __ ___  ___ _ __ 
   \ \/  \/ / '_ \  |  ___/ _` | '__/ __|/ _ \ '__|
    \  /\  /| |_) | | |  | (_| | |  \__ \  __/ |   
     \/  \/ | .__/  |_|   \__,_|_|  |___/\___|_|   
            | |                                    
            |_|                                   
'''

def main():
    scan = wpscan()
    search = DorkParser()

    parser = argparse.ArgumentParser(description="EXxX0RCIST E6AJI BCEM PTbI U }I{0nbI")

    # Добавляем аргументы
    parser.add_argument('-p', '--parsing', type=str, help='only parsing and collecting entry points')
    parser.add_argument('-s', '--scan', type=str, help='only scan targets')
    parser.add_argument('-d', '--dorkresult', type=int, help='number of search results for dorks')
    parser.add_argument('-t', '--timesleep', type=int, help='time between google queries')
    parser.add_argument('-T', '--triger', type=str, help='set triger for wpscan out')

    # Парсим аргументы
    args = parser.parse_args()

    print(banner)

    # Обработка аргументов
    if args.parsing:
        if args.timesleep is not None:
            search.set_time_sleep(args.timesleep)
        if args.dorkresult is not None:
            search.set_result_search(args.dorkresult)
        search.main_pars()

    elif args.scan:
        if args.triger is not None:
            scan.set_triger(args.triger)
        scan.main_scan()
    else:
        if args.timesleep is not None:
            search.set_time_sleep(args.timesleep)
        if args.dorkresult is not None:
            search.set_result_search(args.dorkresult)
        if args.triger is not None:
            scan.set_triger(args.triger)
        search.main_pars()
        scan.main_scan()

if __name__ == '__main__':
    main()