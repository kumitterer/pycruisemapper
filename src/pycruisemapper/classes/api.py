from .http import HTTPRequest
from .vessel import Vessel, Cruise, ShipLine, Flag
from ..const import SHIPS_URL, SHIP_URL

from urllib.parse import urlencode
from datetime import datetime
from typing import List, Dict

import json


class CruiseMapper:
    def request_vessels(self, **kwargs) -> List[Dict]:
        payload = {
            "minLat": kwargs.get("min_lat", -90),
            "maxLat": kwargs.get("max_lat", 90),
            "minLon": kwargs.get("min_lon", -180),
            "maxLon": kwargs.get("max_lon", 180),
            "filter": ",".join(kwargs.get("filter", [str(i) for i in range(100)])),
            "zoom": "",
            "imo": kwargs.get("imo", ""),
            "mmsi": kwargs.get("mmsi", ""),
            "t": int(kwargs.get("timestamp", datetime.now().timestamp()))
        }

        request = HTTPRequest(f"{SHIPS_URL}?{urlencode(payload)}")

        return json.loads(request.open().read())

    def request_vessel(self, **kwargs) -> Dict:
        payload = {
            "imo": kwargs.get("imo", ""),
            "mmsi": kwargs.get("mmsi", ""),
            "zoom": ""
        }

        request = HTTPRequest(f"{SHIP_URL}?{urlencode(payload)}")

        return json.loads(request.open().read())

    def get_vessels(self, **kwargs) -> List[Vessel]:
        pass

    def get_vessel(self, **kwargs) -> Vessel:
        pass

    def fill_vessel(self, vessel: Vessel):
        pass