import subprocess

class wpscan:
    def __init__(self) -> None:
        self.targets = open('targets.txt', 'r')
        self.TRIGER = ""
        self.scanout = open('wpscan_out', 'a')

    def start_scan(self, target):
        
        param = ['wpscan', '--url', f'{target}', '--enumerate', 'p']

        process = subprocess.Popen(param, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()

        output = stdout.decode()
        error_output = stderr.decode()

        if process.returncode == 0:
            if self.TRIGER in output:
                with open('sqli.txt', 'a') as sql_save:
                    sql_save.write(f"{param}\n")
                print(f"Scan {param[2]} activate triger {self.TRIGER}")
            else:
                print(f"Site {param[2].strip('"')} not have critical vulnerability((")            
        else:
            print(f"ERROR: \n{error_output}")
            return
        self.scanout.write(f'SCAN SITE: {target}\n{output}\n\n\n')
        print(output)

    def set_triger(self, tr):
        self.TRIGER = tr
        print(f'Triger="{tr}"')

    def main_scan(self):
        for target in self.targets:
            target = target.strip()
            print(f"Scaning {target}")
            self.start_scan(target)