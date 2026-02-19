/*
Scenario 4: Simple GIS bounding and filtering
You have assets with coordinates:

class Asset {
  final String id;
  final double lat;
  final double lon;
  final String status;
  Asset({required this.id, required this.lat, required this.lon, required this.status});
}

Implement:
  List<Asset> filterInBoundingBox(
    List<Asset> assets,
    double minLat,
    double maxLat,
    double minLon,
    double maxLon,
  );

  List<Asset> filterByStatus(List<Asset> assets, String status);

Combine them so a user can see “all alerting devices in this visible map area”.
*/

class Asset {
  final String id;
  final double lat;
  final double lon;
  final String status;
  Asset({required this.id, required this.lat, required this.lon, required this.status});
}

List<Asset> filterInBoundingBox(List<Asset> assets, double minLat, double maxLat, double minLon, double maxLon) {
  return assets
      .where((asset) => asset.lat <= maxLat && asset.lat >= minLat && asset.lon <= maxLon && asset.lon >= minLon)
      .toList();
}

List<Asset> filterByStatus(List<Asset> assets, String status) {
  return assets.where((asset) => asset.status == status).toList();
}

List<Asset> filterByAlertingDevicesInVisibleMap(
  List<Asset> assets,
  double minLat,
  double maxLat,
  double minLon,
  double maxLon,
) {
  return filterInBoundingBox(filterByStatus(assets, 'alerting'), minLat, maxLat, minLon, maxLon);
}

void main() {
  final assets = [
    Asset(id: 'asset-1', lat: 40.7128, lon: -74.0060, status: 'alerting'),
    Asset(id: 'asset-2', lat: 40.7580, lon: -73.9855, status: 'ok'),
    Asset(id: 'asset-3', lat: 40.7489, lon: -73.9680, status: 'alerting'),
    Asset(id: 'asset-4', lat: 34.0522, lon: -118.2437, status: 'alerting'),
    Asset(id: 'asset-5', lat: 40.7614, lon: -73.9776, status: 'alerting'),
  ];

  // Test 1: Filter by status
  final alertingAssets = filterByStatus(assets, 'alerting');
  assert(alertingAssets.length == 4);
  assert(alertingAssets.every((asset) => asset.status == 'alerting'));
  print('Test 1 passed: Filter by status');

  // Test 2: Filter by bounding box
  final nyBoundingBox = filterInBoundingBox(assets, 40.7000, 40.7700, -74.0100, -73.9500);
  assert(nyBoundingBox.length == 4);
  assert(nyBoundingBox.every((asset) => asset.id != 'asset-4'));
  print('Test 2 passed: Filter by bounding box');

  // Test 3: Filter by bounding box with no results
  final emptyBox = filterInBoundingBox(assets, 30.0, 32.0, -100.0, -99.0);
  assert(emptyBox.isEmpty);
  print('Test 3 passed: Empty bounding box');

  // Test 4: Combined filter (alerting devices in visible map)
  final alertingInNY = filterByAlertingDevicesInVisibleMap(assets, 40.7000, 40.7700, -74.0100, -73.9500);
  assert(alertingInNY.length == 3);
  assert(alertingInNY.every((asset) => asset.status == 'alerting'));
  assert(alertingInNY.every((asset) => asset.lat >= 40.7000 && asset.lat <= 40.7700));
  print('Test 4 passed: Combined filter');

  print('All tests passed!');
}
