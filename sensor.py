import time,json
from MockDHT import MockDHT
from iota import Iota, ProposedTransaction, Address, TryteString, Fragment, Transaction,adapter
from multiprocessing import Process
class Controller:
    endpoint = ('AMARCUS'*81)[:81]
    def __init__(self,delay=60):
        self.delay=delay
        self.dht = MockDHT()
        self.api = Iota(adapter='https://nodes.thetangle.org:443',local_pow=False)
        
    def getMeasurement(self):
        return [time.time(),self.dht.temperature,self.dht.humidity]
    
    def record(self):
        datum = self.getMeasurement()
        tx = ProposedTransaction(
            address = Address(self.endpoint),
            value = 0,
            message = TryteString.from_unicode(str(datum))
        )
        startTime = time.time()
        print(f"Sending new measurement: {datum}")
        try:
            bundle = self.api.send_transfer(transfers=[tx])['bundle']
        except adapter.BadApiResponse as e:
            print("Bad response from server. Failed to send.")
            return
        duration = time.time() - startTime
        reference = bundle.transactions[0].hash            
        print(f'Sent in {duration:.01f} secconds to {reference}')

    def monitor(self):
        delay = self.delay #secconds
        while(True):
            startTime = time.time()
            p = Process(target=self.record)
            p.start()
            p.join(timeout=20)
            if p.exitcode is None:
                p.terminate()
                print("Sending took longer than 20 secconds. Retrying.")
            duration = time.time() - startTime
            print(f"Waiting {int(delay-duration)} secconds.")
            time.sleep(int(delay-duration))
if __name__=="__main__":
    controller = Controller()
    print(controller.endpoint)
    controller.monitor()
