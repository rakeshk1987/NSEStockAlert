from nsetools import Nse
from pprint import pprint
import json

nse = Nse()

def NiftyIdex() :
    nifty50 = nse.get_index_quote("nifty 50")
    return nifty50

#Getting Index Positions
niftyNext50 = json.loads(json.dumps(nse.get_index_quote("NIFTY NEXT 50"))) #return NIFTY NEXT 50 details
niftyBank = json.loads(json.dumps(nse.get_index_quote("NIFTY BANK"))) #return NIFTY BANK details
niftyEnergy = json.loads(json.dumps(nse.get_index_quote("NIFTY ENERGY"))) #return NIFTY ENERGY details
niftyFmcg = json.loads(json.dumps(nse.get_index_quote("NIFTY FMCG"))) #return NIFTY FMCG details
niftyPharma = json.loads(json.dumps(nse.get_index_quote("NIFTY PHARMA"))) #return NIFTY PHARMA details
niftyIt = json.loads(json.dumps(nse.get_index_quote("NIFTY IT"))) #return NIFTY IT details
niftyMetal = json.loads(json.dumps(nse.get_index_quote("NIFTY METAL"))) #return NIFTY METAL details

#Getting Top Gainers of the Day

top_gainers = nse.get_top_gainers()

top_losers = nse.get_top_losers()
#print(top_losers)



