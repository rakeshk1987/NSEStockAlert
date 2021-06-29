from stockApiCall import *
import json
from datetime import date

niftyDumps = json.dumps(NiftyIdex())
niftyStatus = json.loads(niftyDumps)


#Main header section
def niftyOverview() :
    if (int(float(niftyStatus["change"]))) > 0 :
        return "Nifty has Gained <b>" + str(round(float(niftyStatus["change"]))) + "</b> points <b>("+ str(niftyStatus["pChange"]) +"% \U000025B2)</b> today (" + str(date.today()) + ")"

    elif (int(float(niftyStatus["change"]))) < 0 :
        return "Nifty has dropped <b>" + str(round(float(niftyStatus["change"]))) + "</b> points <b>("+ str(niftyStatus["pChange"]) +"% \U000025BC)</b> today (" + str(date.today()) + ")"

    else :
        return "No change in Nifty points today \U0001F504"

# Index Details section
title = "\nINDEX   | Value | Change | Change% \n"
underline   = "-----------------------------------\n"
niftyFifty  = "NIFTY" + "   | "+ str(round(float(niftyStatus["lastPrice"]))).ljust(5, ' ') + " | " + str(round(float(niftyStatus["change"]))).ljust(6, ' ') + " | " + str(niftyStatus["pChange"]) + "% \n"
niftyNext   = "NEXT50" + "  | "+ str(round(float(niftyNext50["lastPrice"]))).ljust(5, ' ') + " | " + str(round(float(niftyNext50["change"]))).ljust(6, ' ') + " | " + str(niftyNext50["pChange"]) + "% \n"
niftyBnk    = "BANK" + "    | "+ str(round(float(niftyBank["lastPrice"]))).ljust(5, ' ')   + " | " + str(round(float(niftyBank["change"]))).ljust(6, ' ')   + " | " + str(niftyBank["pChange"]) + "% \n"
niftyEnrgy  = "ENRGY" + "   | "+ str(round(float(niftyEnergy["lastPrice"]))).ljust(5, ' ') + " | " + str(round(float(niftyEnergy["change"]))).ljust(6, ' ') + " | " + str(niftyEnergy["pChange"]) + "% \n"
niftyRetail = "FMCG" + "    | "+ str(round(float(niftyFmcg["lastPrice"]))).ljust(5, ' ')   + " | " + str(round(float(niftyFmcg["change"]))).ljust(6, ' ')   + " | " + str(niftyFmcg["pChange"]) + "% \n"
niftyPh     = "PHRMA" + "   | "+ str(round(float(niftyPharma["lastPrice"]))).ljust(5, ' ') + " | " + str(round(float(niftyPharma["change"]))).ljust(6, ' ') + " | " + str(niftyPharma["pChange"]) + "% \n"
niftyTech   = "TECH" + "    | "+ str(round(float(niftyIt["lastPrice"]))).ljust(5, ' ')     + " | " + str(round(float(niftyIt["change"]))).ljust(6, ' ')     + " | " + str(niftyIt["pChange"]) + "% \n"
niftyMet    = "RETAIL" + "  | "+ str(round(float(niftyMetal["lastPrice"]))).ljust(5, ' ')  + " | " + str(round(float(niftyMetal["change"]))).ljust(6, ' ')  + " | " + str(niftyMetal["pChange"]) + "% \n"

def niftyIndexDetails():
    return "<pre><code>" + title + underline + niftyFifty + niftyNext+ niftyBnk + niftyEnrgy + niftyRetail + niftyPh + niftyTech + niftyMet + "</code></pre>"

#Get Top Gainers of the Day
gainerslist = json.loads(json.dumps(top_gainers))
gainMsg = "\n\U00002197 Top 10 Gainers of the day \n\n"
titleGainlose = "TICKER     | Price     | Change% \n"
ulgainLose   = "-----------------------------\n"

def topGainers():
    gainvalue = ""
    for items in gainerslist:
        stockName = items['symbol']
        if len(stockName) > 10:
            stockName = stockName[0:10]
        elif len(stockName) < 10:
            stockName = stockName.ljust(10, ' ')

        gainvalue += stockName + " | ₹" + str(items['ltp']).ljust(8, ' ') + " | " + str(items['netPrice']) + "% \n"
    return "<pre><code>" + gainMsg + titleGainlose + ulgainLose + gainvalue + "</code></pre>"

#Get Top Losers of the Day
loserslist = json.loads(json.dumps(top_losers))
loseMsg = "\n\U00002198 Top 10 Losers of the day  \n\n"

def topLosers():
    losevalue = ""
    for items in loserslist:
        stockName = items['symbol']
        if len(stockName) > 10:
            stockName = stockName[0:10]
        elif len(stockName) < 10:
            stockName = stockName.ljust(10, ' ')

        losevalue += stockName + " | ₹" + str(items['ltp']).ljust(8, ' ') + " | " + str(items['netPrice']) + "% \n"
    return "<pre><code>" + loseMsg + titleGainlose + ulgainLose + losevalue + "</code></pre>"

        

