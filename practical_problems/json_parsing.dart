/*
Scenario 1: Device status and filtering
You’re given JSON representing sensors on the grid:

json
[
  { "id": "dev-1", "region": "north", "status": "ok", "lastHeartbeat": "2026-02-17T21:00:00Z" },
  { "id": "dev-2", "region": "north", "status": "alert", "lastHeartbeat": "2026-02-17T20:30:00Z" },
  { "id": "dev-3", "region": "south", "status": "offline", "lastHeartbeat": "2026-02-17T19:00:00Z" }
]
Task:

Define a Device class in Dart with appropriate fields and a fromJson constructor.
Write a function List<Device> parseDevices(String jsonString).
Write a function List<Device> filterByStatus(List<Device> devices, String status) that returns devices with that status.
Write a function Map<String, int> countByRegion(List<Device> devices) that returns counts per region.

Problem Exploration:
The problem here is to create a Device data class with properties id, region, status, and lastHeartBeat.
Then we are to implement a few different functions.

Questions for the interviewer:
Are there any other classes we should consider or data structure that we should keep outside of the Device data class
to improve the performance of some of the defined functions? Or should we limit our code to the outlined classes and methods?

I am assuming that we should store lastHeartBeat as a DateTime object, is that right?
Should we store region and status as strings? Or should we create an Enum class for each? (It doesn't seem like a sealed class is necessary here yet)
*/

import "dart:convert";

class Device {
  final String id;
  final Region region;
  final Status status;
  final DateTime lastHeartbeat;

  const Device({required this.id, required this.region, required this.status, required this.lastHeartbeat});

  static Device? fromJson(Map<String, dynamic> json) {
    // Silently failing, in a production environment we could use a logger
    final id = json['id'];
    if (id == null || id is! String) return null;
    final rawRegion = json['region'];
    if (rawRegion == null || rawRegion is! String) return null;
    final region = Region.fromString(rawRegion);
    if (region == null) return null;
    final rawStatus = json['status'];
    if (rawStatus == null || rawStatus is! String) return null;
    final status = Status.fromString(rawStatus);
    if (status == null) return null;
    final rawLastHeartbeat = json['lastHeartbeat'];
    if (rawLastHeartbeat == null || rawLastHeartbeat is! String) return null;
    final lastHeartbeat = DateTime.tryParse(rawLastHeartbeat);
    if (lastHeartbeat == null) return null;
    return Device(id: id, region: region, status: status, lastHeartbeat: lastHeartbeat);
  }
}

//Returns a list of devices from a json encoded string
List<Device> parseDevices(String json) {
  final decodedJson = jsonDecode(json);
  if (decodedJson == null || decodedJson is! List<dynamic>) return <Device>[];
  return decodedJson
      .whereType<Map<String, dynamic>>()
      .map((jsonDevice) => Device.fromJson(jsonDevice))
      .nonNulls
      .toList();
}

//Returns only those devices that  have a given status
List<Device> filterByStatus(List<Device> devices, Status status) {
  return devices.where((device) => device.status == status).toList();
}

// Returns the count of all devices in a list that are located in a given region
Map<Region, int> countByRegion(List<Device> devices) {
  final regions = <Region, int>{};
  devices.forEach((device) => regions[device.region] = (regions[device.region] ?? 0) + 1);
  return regions;
}

// We could do something like this with enums
enum Status {
  ok('ok'),
  alert('alert'),
  offline('offline');

  const Status(this.name);

  final String name;

  static Status? fromString(String str) {
    final normalized = str.toLowerCase().trim();
    for (final status in Status.values) {
      if (status.name == normalized) {
        return status;
      }
    }
    return null;
  }
}

enum Region {
  north('north'),
  south('south'),
  east('east'),
  west('west');

  const Region(this.name);

  final String name;

  static Region? fromString(String str) {
    final normalized = str.toLowerCase().trim();
    for (final region in Region.values) {
      if (region.name == normalized) {
        return region;
      }
    }
    return null;
  }
}
