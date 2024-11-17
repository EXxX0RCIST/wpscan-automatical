from urllib.parse import urlparse
from googlesearch import search # простейший поиск в google
import time

class DorkParser:

    def __init__(self) -> None:
        self.urls = set()
        self.TIME_SLEEP = 120 # pause search google 
        self.RESULT_SEARCH = 50 # search google dork (max 99)

    def set_time_sleep(self, time_slep):
        self.TIME_SLEEP = time_slep
        print(f"Time sleep={time_slep}")

    def set_result_search(self, result):
        if result > 99:
            print(f"You can't set results search > 99")
            return
        self.RESULT_SEARCH = result
        print(f"Result search google dork={result}")

    def pars_dork(self, dork):
        try:
            for result in search(dork, num_results=self.RESULT_SEARCH):
                result = self.trim_url(result)
                self.urls.add(result)
        except Exception as e:
            print(f'An error occurred while searching for google dork\n"{dork}": {e}')

    def trim_url(self, url):
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return base_url

    def main_pars(self):
        print("Start performing a search")
        with open('dorks.txt', 'r', encoding='utf-8') as dorks:
            for d in dorks:
                d = d.rstrip('\n')
                print(f"Search by dork {d}")
                start_time = time.time()
                self.pars_dork(d)
                finish_time = time.time()
                work_time = finish_time - start_time
                if self.TIME_SLEEP > work_time:
                    time.sleep(self.TIME_SLEEP - work_time)                
            with open('targets.txt', 'a') as targets:
                for target in self.urls:
                    targets.write(f'{target}\n')
