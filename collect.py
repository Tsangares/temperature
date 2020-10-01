import time,json
import adafruit_dht
from sensor import Controller
from iota import Iota, ProposedTransaction, Address, TryteString, Fragment, Transaction

class Collector:
    def __init__(self):
        self.api = Iota(adapter='https://nodes.thetangle.org:443')
        self.endpoint = Controller.endpoint

    def getData(self,txHash):
        hashes=api.find_transactions(addresses=[address,])['hashes']
    
    def read(self):
        address = Address(self.endpoint)
        txHashes = self.api.find_transactions(addresses=[address,])['hashes']
        txs = self.api.get_transaction_objects(txHashes)['transactions']
        decode = lambda a: json.loads(a.signature_message_fragment.decode())
        return sorted([decode(t) for t in txs], key=lambda a: a[0],reverse=True)
        
if __name__=='__main__':
    collector = Collector()
    txs = collector.read() 
    print(txs)
