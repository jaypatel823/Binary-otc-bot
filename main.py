import os
from fastapi import FastAPI
from iqoptionapi.stable_api import IQ_Option
import time

app = FastAPI()

# IQ Option लॉगिन (Environment Variables से)
email = os.getenv("IQOPTION_EMAIL")
password = os.getenv("IQOPTION_PASSWORD")
Iq = IQ_Option(email, password)
Iq.connect()

markets = ["EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC"]
timeframe = 60

def get_signals():
    signals = []
    for market in markets:
        candles = Iq.get_candles(market, timeframe, 10, time.time())
        last_price = candles[-1]['close']
        signals.append({"market": market, "price": last_price})
    return signals

@app.get("/signals")
def fetch_signals():
    return {"signals": get_signals()}
