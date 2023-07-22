
from streamlit.connections import ExperimentalBaseConnection
from pynytimes import NYTAPI
import pandas as pd
import json
import datetime
from shhh import ny_key

nyt = NYTAPI(ny_key, parse_dates=True)
top_stories = nyt.top_stories()

class NYTDBConnection(ExperimentalBaseConnection):

    def _connect(self, **kwargs):
        return nyt
    
    def query(self, query):
        cnxn = self._connect()
        res = None
        if query == "TOP_Stories":
            res = cnxn.top_stories()
        return res
    
nyc = NYTDBConnection("NY_CNXN")
ts = nyc.query("TOP_Stories")

def json_encoder(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

def resp_to_df(data):
    jd = json.dumps(ts, default=json_encoder)
    df = pd.read_json(jd)
    return df
