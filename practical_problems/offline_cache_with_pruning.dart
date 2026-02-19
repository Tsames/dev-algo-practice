/*
Scenario 2: Offline cache with pruning
You’re building an offline‑capable app that caches device telemetry locally.

Task:
Implement a simple in‑memory cache:

Requirements:
put inserts/updates an entry and sets timestamps.
get returns value (or null) and updates lastAccessed.

prune:
Removes entries older than ttl (based on createdAt).
If still over maxEntries, removes least‑recently‑used entries.

Things they might probe:
Choosing Map<String, CacheEntry<T>> vs list.
Time complexity tradeoffs vs simplicity.

How you’d move this to local storage (SQLite / Hive) in a real app.
*/

class CacheEntry<T> {
  final T value;
  final DateTime createdAt;
  DateTime lastAccessed;

  CacheEntry({required this.value, required this.createdAt, required this.lastAccessed});
}

class TelemetryCache<T> {
  final Map<String, CacheEntry<T>> cache = {};

  TelemetryCache({required this.maxEntries, required this.ttl});

  final int maxEntries;
  final Duration ttl;

  // O(1) Time for Map, O(n) Time for List
  void put(String key, T value) {
    final now = DateTime.now();
    cache.update(key, (entry) {
      entry.lastAccessed = now;
      return entry;
    }, ifAbsent: () => CacheEntry(value: value, createdAt: now, lastAccessed: now));
  }

  // O(1) Time for Map, O(n) Time for List
  T? get(String key) {
    return (cache[key]?..lastAccessed = DateTime.now())?.value;
  }

  // O(n log n) Time for Map, O(n log n) Time for List
  // We would have to iterate through the iterable twice and sort either way
  void prune() {
    cache.removeWhere((key, entry) => entry.lastAccessed.difference(entry.createdAt) >= ttl);
    if (cache.length > maxEntries) {
      final sortedCache = cache.entries.toList()..sort((a, b) => b.value.lastAccessed.compareTo(a.value.lastAccessed));
      while (sortedCache.length > maxEntries) {
        cache.remove(sortedCache.removeLast().key);
      }
    }
  }
}
