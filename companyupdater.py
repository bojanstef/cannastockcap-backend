from spreadsheet import get_companies
import threading
import time

class CompanyUpdater(object):
    def __init__(self, interval=1):
        self.interval = interval
        self.companies = {}
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.companies = get_companies()
            time.sleep(self.interval)
