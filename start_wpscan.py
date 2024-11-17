import subprocess

class wpscan:
    def __init__(self) -> None:
        self.targets = open('targets.txt', 'r')
        self.TRIGER = set()
        self.SAVE_OUTPUT = False
        self.scanout = open('wpscan_out', 'a')

    def start_scan(self, target):
        
        param = ['wpscan', '--url', f'{target}', '--enumerate', 'p', 
                 '--ignore-main-redirect', '--rua']

        process = subprocess.Popen(param, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()

        output = stdout.decode()
        error_output = stderr.decode()

        if process.returncode == 0:
            if self.TRIGER in output:
                self.scanout.write(f'SCAN SITE: {target}\nDETECTED TRIGER\n{output}\n\n')
                print(f"Scan {param[2]} activate triger {self.TRIGER}")
            else:
                print(f"Site {param[2]} not have critical vulnerability((")
                if self.SAVE_OUTPUT:
                    self.scanout.write(f'SCAN SITE: {target}\n{output}\n\n')

        else:
            print(f"ERROR: \n{error_output}")
            return
        print(output)

    def set_triger(self, tr):
        self.TRIGER = tr.split(', ')
        print(f'Triger=', end='')
        for x in self.TRIGER:
            print(x)
    
    def set_save_output(self):
        self.SAVE_OUTPUT = True
        print("Save output=True")

    def main_scan(self):
        for target in self.targets:
            target = target.strip()
            print(f"Scaning {target}")
            self.start_scan(target)
