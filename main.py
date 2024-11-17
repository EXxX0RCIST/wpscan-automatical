from parsing_dork import DorkParser
from start_wpscan import wpscan
import argparse


b = '''
    ▗▖ ▗▖▗▄▄▖     ▗▄▄▖  ▗▄▖ ▗▄▄▖  ▗▄▄▖▗▄▄▄▖▗▄▄▖ 
    ▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌
    ▐▌ ▐▌▐▛▀▘     ▐▛▀▘ ▐▛▀▜▌▐▛▀▚▖ ▝▀▚▖▐▛▀▀▘▐▛▀▚▖
    ▐▙█▟▌▐▌       ▐▌   ▐▌ ▐▌▐▌ ▐▌▗▄▄▞▘▐▙▄▄▖▐▌ ▐▌
        
                                t.me/EXxX0RCIST
    '''
    
def main():
    parser = argparse.ArgumentParser(description=b)

    search = DorkParser()
    scan = wpscan()

    # Добавляем аргументы
    parser.add_argument('-p', '--parsing', type=str, help='only parsing and collecting entry points')
    parser.add_argument('-d', '--dorkresult', type=int, help='number of search results for dorks')
    parser.add_argument('-t', '--timesleep', type=int, help='time between google queries')
    parser.add_argument('-s', '--wpscan', type=str, help='only scan wpscan of targets')
    parser.add_argument('-T', '--triger', type=str, help='set triger to output wpscan')
    parser.add_argument('-o', '--saveout', type=str, help='set save output wpscan')

    # Парсим аргументы
    args = parser.parse_args()

    if args.parsing:
        if args.dorkresult is not None:
            search.set_result_search(args.parsing)
        if args.timesleep is not None:
            search.set_time_sleep(args.timesleep)
        search.main_pars()
    elif args.wpscan:
        if args.triger is not None:
            scan.set_triger(args.triger)
        if args.saveout is not None:
            scan.set_save_output()
        scan.main_scan()
    else:
        if args.dorkresult is not None:
            search.set_result_search(args.parsing)
        if args.timesleep is not None:
            search.set_time_sleep(args.timesleep)
        if args.triger is not None:
            scan.set_triger(args.triger)
        search.main_pars()
        scan.main_scan()

if __name__ == '__main__':
    main()
