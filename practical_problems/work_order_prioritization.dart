/*
Scenario 3: Work order prioritization
Field teams get a list of work orders to visit.

[
  { "id": "wo-1", "priority": "HIGH", "status": "open", "createdAt": "2026-02-17T18:00:00Z" },
  { "id": "wo-2", "priority": "LOW",  "status": "open", "createdAt": "2026-02-17T19:00:00Z" },
  { "id": "wo-3", "priority": "MEDIUM", "status": "in_progress", "createdAt": "2026-02-17T17:30:00Z" }
]

Task:
Model a WorkOrder type.
Implement a function:

List<WorkOrder> sortForTechnician(List<WorkOrder> orders);

Rules:
status open > in_progress > closed.
Within same status, priority: HIGH > MEDIUM > LOW.
If same status and priority, older createdAt first.
Make your sort logic easy to change.
*/

enum Priority {
  low,
  medium,
  high;

  static const priorityOrdering = {low: 2, medium: 1, high: 0};

  int compare(Priority other) {
    final thisPriorityOrder = priorityOrdering[this];
    final otherPriorityOrder = priorityOrdering[other];
    if (thisPriorityOrder == null) {
      throw StateError('Priority: $this not in ordering map');
    } else if (otherPriorityOrder == null) {
      throw StateError('Priority: $other not in ordering map');
    }
    return thisPriorityOrder.compareTo(otherPriorityOrder);
  }
}

enum Status {
  open,
  in_progress,
  closed;

  static const statusOrdering = {open: 0, in_progress: 1, closed: 2};

  int compare(Status other) {
    final thisStatusOrder = statusOrdering[this];
    final otherStatusOrder = statusOrdering[other];
    if (thisStatusOrder == null) {
      throw StateError('Status: $this not in ordering map');
    } else if (otherStatusOrder == null) {
      throw StateError('Status: $other not in ordering map');
    }
    return thisStatusOrder.compareTo(otherStatusOrder);
  }
}

class WorkOrder {
  final String id;
  Priority priority;
  Status status;
  final DateTime createdAt;

  WorkOrder({required this.id, required this.priority, required this.status, required this.createdAt});
}

List<WorkOrder> sortForTechnician(List<WorkOrder> orders) {
  /*
    So we can use Dart's sort method.
    We can define our own compare() callback to ensure it has the correct primary and secondary ordering.
    When we are sorting, we want to return -1 if a comes before b, 0 if their ordering does not matter, and 1 if a goes after b.

    We could give our enums contrived values to make our sorting pretty concise.
    Our method would look like this:

    return orders..sort((WorkOrder a, WorkOrder b) {
      if (a.status.value == b.status.value) {
        return a.priority.value.compareTo(b.priority.value);
      }
      return a.status.value.compareTo(b.status.value);
    });

    With enums:

    enum Priority {
      low(2),
      medium(1),
      high(0);

      final int value;
      const Priority(this.value);
    }

    enum Status {
      open(0),
      in_progress(1),
      closed(2);

      final int value;
      const Status(this.value);
    }

    Alternative, but this is brittle and not very maintainable

    return orders..sort((WorkOrder a, WorkOrder b) {
      if (a.status == b.status) {
        if (a.priority == b.priority) {
          return 0;
        } else if (a.priority == Priority.high) {
          return -1;
        } else if (b.priority == Priority.high) {
          return 1;
        } else if (a.priority == Priority.medium) {
          return -1;
        } else if (b.priority == Priority.medium) {
          return 1;
        }
      } else if (a.status == Status.open) {
        return -1;
      } else if (b.status == Status.open) {
        return 1;
      } else if (a.status == Status.in_progress) {
        return -1;
      } else if (b.status == Status.in_progress) {
        return 1;
      }
      return 0;
    });
  */
  return orders..sort((WorkOrder a, WorkOrder b) {
    if (a.status == b.status) {
      return a.priority.compare(b.priority);
    }
    return a.status.compare(b.status);
  });
}

void main() {
  // Test 1: Status ordering (open > in_progress > closed)
  final statusTest = [
    WorkOrder(
      id: 'wo-1',
      priority: Priority.low,
      status: Status.closed,
      createdAt: DateTime.parse('2026-02-17T18:00:00Z'),
    ),
    WorkOrder(
      id: 'wo-2',
      priority: Priority.low,
      status: Status.open,
      createdAt: DateTime.parse('2026-02-17T19:00:00Z'),
    ),
    WorkOrder(
      id: 'wo-3',
      priority: Priority.low,
      status: Status.in_progress,
      createdAt: DateTime.parse('2026-02-17T17:30:00Z'),
    ),
  ];
  final sortedStatus = sortForTechnician(statusTest);
  assert(sortedStatus[0].status == Status.open);
  assert(sortedStatus[1].status == Status.in_progress);
  assert(sortedStatus[2].status == Status.closed);
  print('Test 1 passed: Status ordering');

  // Test 2: Priority ordering within same status (HIGH > MEDIUM > LOW)
  final priorityTest = [
    WorkOrder(
      id: 'wo-1',
      priority: Priority.low,
      status: Status.open,
      createdAt: DateTime.parse('2026-02-17T18:00:00Z'),
    ),
    WorkOrder(
      id: 'wo-2',
      priority: Priority.high,
      status: Status.open,
      createdAt: DateTime.parse('2026-02-17T19:00:00Z'),
    ),
    WorkOrder(
      id: 'wo-3',
      priority: Priority.medium,
      status: Status.open,
      createdAt: DateTime.parse('2026-02-17T17:30:00Z'),
    ),
  ];
  final sortedPriority = sortForTechnician(priorityTest);
  assert(sortedPriority[0].priority == Priority.high);
  assert(sortedPriority[1].priority == Priority.medium);
  assert(sortedPriority[2].priority == Priority.low);
  print('Test 2 passed: Priority ordering');

  print('All tests passed!');
}
