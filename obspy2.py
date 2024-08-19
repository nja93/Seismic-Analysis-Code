from obspy import UTCDateTime
starttime = UTCDateTime("2018-04-30T14:00:00") + 10 * 3600
from obspy.clients.fdsn import Client
client = Client("IRIS") 
endtime=starttime + 24 * 60 * 60
inv = client.get_stations(network="HV", station="*", channel="EHZ", level="channel", starttime=starttime, endtime=endtime)
inv = client.get_stations(network="HV", station="*", channel="EHZ", level="channel", starttime=starttime, endtime=endtime, minlatitude="19.25", maxlatitude="19.75", minlongitude="-155.22", maxlongitude="-154")
https://docs.obspy.org/packages/autogen/obspy.core.inventory.inventory.Inventory.get_coordinates.html
from obspy import read_inventory
inv.get_coordinates("HV.KLUD..EHZ")
stream = client.get_waveforms("HV", "KLUD", "", "EHZ", starttime, endtime)
stream.plot(type="dayplot", interval=60) 
from obspy.clients.iris import Client
iris = Client()
result = iris.distaz(lat1, lon1, lat2, lon2)
print(result)
