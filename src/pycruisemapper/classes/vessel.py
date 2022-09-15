from datetime import datetime, timedelta
from typing import Optional, List, Tuple


class Cruise:
    name: Optional[str]
    url: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    itinerary: Optional[List[Optional[Tuple[str, str]]]]

    @property
    def days(self) -> Optional[int]:
        if self.end_date and self.start_date:
            return (self.end_date - self.start_date).days

class Flag:
    code: str
    name: str

class ShipLine:
    title: str
    id: int
    url: Optional[str]

class Vessel:
    id: Optional[int]
    name: Optional[str]
    url: Optional[str]
    url_deckplans: Optional[str]
    url_staterooms: Optional[str]
    image: Optional[str]
    flag: Flag
    line: Optional[ShipLine]
    spec_length: Optional[int] # stored in meters
    spec_passengers: Optional[int]
    year_built: Optional[int]
    last_report: Optional[str]
    imo: int
    mmsi: int
    latitude: float
    longitude: float
    cog: int # Course over Ground
    sog: int # Speed over Ground
    heading: int
    timestamp: datetime
    icon: int
    hover: str
    cruise: Optional[Cruise]
    path: Optional[List[Optional[Tuple[float, float]]]]
    ports: Optional[List[Optional[Tuple[datetime, float, float]]]]
    destination: str
    eta: Optional[datetime]
    current_temperature: Optional[float] # Celsius
    minimum_temperature: Optional[float] # Celsius
    maximum_temperature: Optional[float] # Celsius
    wind_degrees: Optional[float]
    wind_speed: Optional[float] # m/s
    wind_gust: Optional[float] # m/s
    utc_offset: Optional[timedelta]