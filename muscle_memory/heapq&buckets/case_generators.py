#!/usr/bin/env python3
"""Deterministic, high-coverage cases for heap and bucket pattern drills."""

from __future__ import annotations

import bisect
import heapq
import random
from collections import Counter, defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    stdin: str
    expected: str
    size: int
    category: str


EXERCISES = {
    "h01": ("Top K Frequent Words", "h01_top_k_frequent_words.py"),
    "h02": ("K Pairs With Smallest Sums", "h02_k_pairs_with_smallest_sums.py"),
    "h03": ("Merge K Sorted Arrays", "h03_merge_k_sorted_arrays.py"),
    "h04": ("Kth Smallest in Sorted Matrix", "h04_kth_smallest_sorted_matrix.py"),
    "h05": ("Smallest Range Covering K Lists", "h05_smallest_range_k_lists.py"),
    "h06": ("IPO Maximized Capital", "h06_ipo_maximized_capital.py"),
    "h07": ("Meeting Rooms III", "h07_meeting_rooms_iii.py"),
    "h08": ("Sliding Window Median", "h08_sliding_window_median.py"),
    "h09": ("Reorganize String", "h09_reorganize_string.py"),
    "b01": ("Sort Characters by Frequency", "b01_sort_characters_by_frequency.py"),
    "b02": ("H-Index", "b02_h_index.py"),
    "b03": ("Maximum Gap", "b03_maximum_gap.py"),
    "b04": ("Contains Nearby Almost Duplicate", "b04_contains_nearby_almost_duplicate.py"),
    "b05": ("Relative Sort Array", "b05_relative_sort_array.py"),
    "b06": ("Car Pooling", "b06_car_pooling.py"),
}


def _ints(values) -> str:
    return " ".join(map(str, values))


def _median(values: list[int]) -> str:
    middle = len(values) // 2
    if len(values) % 2:
        return str(values[middle])
    total = values[middle - 1] + values[middle]
    return str(total // 2) if total % 2 == 0 else f"{total / 2:.1f}"


def _build_h01() -> list[Case]:
    rng = random.Random(1001)
    cases = []
    for index in range(99):
        if index == 0:
            words, k, category = ["i", "love", "leetcode", "i", "love", "coding"], 2, "classic boundary"
        elif index == 1:
            words, k, category = ["a", "b", "c"] * 80, 2, "lexicographic tie"
        elif index == 2:
            words, k, category = ["only"], 1, "single word"
        else:
            vocabulary_size = 40 + rng.randrange(180)
            vocabulary = [f"word{value:03d}" for value in range(vocabulary_size)]
            frequencies = [rng.randint(1, 50) for _ in vocabulary]
            if index % 2 == 0:
                tied = rng.randint(10, 35)
                for position in range(min(15, vocabulary_size)):
                    frequencies[position] = tied
            words = [word for word, frequency in zip(vocabulary, frequencies) for _ in range(frequency)]
            while len(words) < 700:
                words.extend(words[: min(len(words), 700 - len(words))])
            rng.shuffle(words)
            k = (1, vocabulary_size, vocabulary_size // 2, rng.randint(1, vocabulary_size))[index % 4]
            category = "frequency and lexicographic ties"
        counts = Counter(words)
        answer = sorted(counts, key=lambda word: (-counts[word], word))[:k]
        stdin = f"{len(words)}\n" + "\n".join(words) + f"\n{k}\n"
        cases.append(Case(stdin, "\n".join(answer) + "\n", len(words), category))
    return cases


def _build_h02() -> list[Case]:
    rng = random.Random(1002)
    cases = []
    for index in range(99):
        if index == 0:
            left, right, k, category = [1, 7, 11], [2, 4, 6], 3, "classic example"
        elif index == 1:
            left, right, k, category = [1, 1, 2], [1, 2, 2], 6, "duplicate pairs and ties"
        elif index == 2:
            left, right, k, category = [-1], [1], 1, "single pair"
        else:
            left_size = 50 + rng.randrange(80)
            right_size = 50 + rng.randrange(80)
            spread = 30 if index % 3 == 0 else 10**6
            left = sorted(rng.randint(-spread, spread) for _ in range(left_size))
            right = sorted(rng.randint(-spread, spread) for _ in range(right_size))
            pair_count = left_size * right_size
            k = (1, min(pair_count, 600), min(pair_count, 200), rng.randint(1, min(pair_count, 500)))[index % 4]
            category = "negative values, duplicates, and sum ties"
        pairs = sorted(((a + b, a, b) for a in left for b in right))[:k]
        expected = "".join(f"{a} {b}\n" for _, a, b in pairs)
        stdin = f"{len(left)} {len(right)} {k}\n{_ints(left)}\n{_ints(right)}\n"
        cases.append(Case(stdin, expected, len(left) + len(right), category))
    return cases


def _build_h03() -> list[Case]:
    rng = random.Random(1003)
    cases = []
    for index in range(99):
        if index == 0:
            arrays, category = [[]], "empty array"
        elif index == 1:
            arrays, category = [[1], [], [-1, 2]], "singletons and empty members"
        elif index == 2:
            arrays, category = [[1] * 100, [1] * 100, [1] * 100], "all equal"
        else:
            array_count = 8 + rng.randrange(25)
            arrays = []
            for array_index in range(array_count):
                length = 0 if (index + array_index) % 17 == 0 else 25 + rng.randrange(100)
                spread = 30 if index % 3 == 0 else 10**6
                arrays.append(sorted(rng.randint(-spread, spread) for _ in range(length)))
            category = "overlapping ranges and empty members"
        merged = sorted(value for array in arrays for value in array)
        stdin = f"{len(arrays)}\n" + "".join(f"{len(array)}\n{_ints(array)}\n" for array in arrays)
        cases.append(Case(stdin, _ints(merged) + "\n", len(merged), category))
    return cases


def _build_h04() -> list[Case]:
    rng = random.Random(1004)
    cases = []
    for index in range(99):
        if index == 0:
            matrix, k, category = [[1]], 1, "single cell"
        elif index == 1:
            matrix, k, category = [[1, 1], [1, 1]], 3, "all equal"
        elif index == 2:
            matrix, k, category = [[-5, -4, -1], [-3, 0, 2]], 4, "rectangular negatives"
        else:
            rows = 15 + rng.randrange(30)
            cols = 15 + rng.randrange(30)
            if index % 3 == 0:
                matrix = [[row + col for col in range(cols)] for row in range(rows)]
            else:
                row_offsets = sorted(rng.randint(-10**6, 10**6) for _ in range(rows))
                col_offsets = sorted(rng.randint(-10**6, 10**6) for _ in range(cols))
                matrix = [[row_offsets[row] + col_offsets[col] for col in range(cols)] for row in range(rows)]
            k = (1, rows * cols, rows * cols // 2, rng.randint(1, rows * cols))[index % 4]
            category = "rectangular matrix with duplicate and extreme values"
        flattened = sorted(value for row in matrix for value in row)
        stdin = f"{len(matrix)} {len(matrix[0])} {k}\n" + "".join(_ints(row) + "\n" for row in matrix)
        cases.append(Case(stdin, f"{flattened[k - 1]}\n", len(flattened), category))
    return cases


def _smallest_range(lists: list[list[int]]) -> tuple[int, int]:
    heap = []
    current_right = -(10**30)
    for list_index, values in enumerate(lists):
        heap.append((values[0], list_index, 0))
        current_right = max(current_right, values[0])
    heapq.heapify(heap)
    best_left, best_right = heap[0][0], current_right
    while True:
        current_left, list_index, value_index = heapq.heappop(heap)
        if current_right - current_left < best_right - best_left or (
            current_right - current_left == best_right - best_left and current_left < best_left
        ):
            best_left, best_right = current_left, current_right
        next_index = value_index + 1
        if next_index == len(lists[list_index]):
            return best_left, best_right
        next_value = lists[list_index][next_index]
        current_right = max(current_right, next_value)
        heapq.heappush(heap, (next_value, list_index, next_index))


def _build_h05() -> list[Case]:
    rng = random.Random(1005)
    cases = []
    for index in range(99):
        if index == 0:
            lists, category = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], "classic example"
        elif index == 1:
            lists, category = [[1], [1], [1]], "single shared point"
        elif index == 2:
            lists, category = [[-10, -5], [0], [5, 10]], "separated lists"
        else:
            list_count = 5 + rng.randrange(15)
            lists = []
            for _ in range(list_count):
                length = 25 + rng.randrange(90)
                spread = 50 if index % 3 == 0 else 10**6
                lists.append(sorted(rng.randint(-spread, spread) for _ in range(length)))
            category = "overlapping lists, duplicates, and extreme values"
        left, right = _smallest_range(lists)
        stdin = f"{len(lists)}\n" + "".join(f"{len(values)}\n{_ints(values)}\n" for values in lists)
        cases.append(Case(stdin, f"{left} {right}\n", sum(map(len, lists)), category))
    return cases


def _ipo(profits: list[int], required: list[int], k: int, capital: int) -> int:
    projects = sorted(zip(required, profits))
    available = []
    project_index = 0
    for _ in range(k):
        while project_index < len(projects) and projects[project_index][0] <= capital:
            heapq.heappush(available, -projects[project_index][1])
            project_index += 1
        if not available:
            break
        capital -= heapq.heappop(available)
    return capital


def _build_h06() -> list[Case]:
    rng = random.Random(1006)
    cases = []
    for index in range(99):
        if index == 0:
            profits, required, k, capital, category = [1, 2, 3], [0, 1, 1], 2, 0, "classic example"
        elif index == 1:
            profits, required, k, capital, category = [5], [10], 1, 0, "no affordable project"
        elif index == 2:
            profits, required, k, capital, category = [0] * 120, [0] * 120, 120, 0, "zero profits"
        else:
            size = 300 + rng.randrange(1200)
            profits = [rng.randint(0, 10**5) for _ in range(size)]
            required = [rng.randint(0, 10**7) for _ in range(size)]
            capital = (0, 10**7, rng.randint(0, 10**6))[index % 3]
            k = (1, size, min(size, 100), rng.randint(1, size))[index % 4]
            category = "affordability frontier and competing profits"
        answer = _ipo(profits, required, k, capital)
        stdin = f"{len(profits)} {k} {capital}\n{_ints(profits)}\n{_ints(required)}\n"
        cases.append(Case(stdin, f"{answer}\n", len(profits), category))
    return cases


def _meeting_room(room_count: int, meetings: list[tuple[int, int]]) -> int:
    free = list(range(room_count))
    heapq.heapify(free)
    busy = []
    usage = [0] * room_count
    for start, end in sorted(meetings):
        while busy and busy[0][0] <= start:
            _, room = heapq.heappop(busy)
            heapq.heappush(free, room)
        duration = end - start
        if free:
            room = heapq.heappop(free)
            finish = end
        else:
            available_at, room = heapq.heappop(busy)
            finish = available_at + duration
        usage[room] += 1
        heapq.heappush(busy, (finish, room))
    return max(range(room_count), key=lambda room: (usage[room], -room))


def _build_h07() -> list[Case]:
    rng = random.Random(1007)
    cases = []
    for index in range(99):
        if index == 0:
            rooms, meetings, category = 2, [(0, 10), (1, 5), (2, 7), (3, 4)], "classic delay"
        elif index == 1:
            rooms, meetings, category = 1, [(0, 1), (1, 2)], "one room"
        elif index == 2:
            rooms, meetings, category = 100, [(0, 1)], "many idle rooms"
        else:
            rooms = 2 + rng.randrange(40)
            meeting_count = 250 + rng.randrange(1200)
            starts = sorted(rng.sample(range(meeting_count * 10), meeting_count))
            meetings = [(start, start + rng.randint(1, 500)) for start in starts]
            if index % 3 == 0:
                meetings = [(start, start + 10**6) for start in starts]
            category = "contention, release ties, and long delays"
        answer = _meeting_room(rooms, meetings)
        stdin = f"{rooms} {len(meetings)}\n" + "".join(f"{start} {end}\n" for start, end in meetings)
        cases.append(Case(stdin, f"{answer}\n", len(meetings), category))
    return cases


def _build_h08() -> list[Case]:
    rng = random.Random(1008)
    cases = []
    for index in range(99):
        if index == 0:
            nums, k, category = [1, 3, -1, -3, 5, 3, 6, 7], 3, "classic example"
        elif index == 1:
            nums, k, category = [1], 1, "single window"
        elif index == 2:
            nums, k, category = [5] * 200, 100, "all equal and even window"
        else:
            size = 500 + rng.randrange(1800)
            mode = index % 4
            if mode == 0:
                nums = [rng.randint(-20, 20) for _ in range(size)]
            elif mode == 1:
                nums = list(range(size))
            elif mode == 2:
                nums = list(range(size, 0, -1))
            else:
                nums = [rng.randint(-10**9, 10**9) for _ in range(size)]
            k = (1, size, max(1, size // 2), rng.randint(1, size))[index % 4]
            category = "duplicates, extremes, and odd/even windows"
        ordered = sorted(nums[:k])
        medians = [_median(ordered)]
        for right in range(k, len(nums)):
            outgoing = nums[right - k]
            ordered.pop(bisect.bisect_left(ordered, outgoing))
            bisect.insort(ordered, nums[right])
            medians.append(_median(ordered))
        stdin = f"{len(nums)} {k}\n{_ints(nums)}\n"
        cases.append(Case(stdin, " ".join(medians) + "\n", len(nums), category))
    return cases


def _reorganize(text: str) -> str:
    counts = Counter(text)
    heap = [(-frequency, character) for character, frequency in counts.items()]
    heapq.heapify(heap)
    previous_frequency = 0
    previous_character = ""
    output = []
    while heap:
        frequency, character = heapq.heappop(heap)
        output.append(character)
        frequency += 1
        if previous_frequency < 0:
            heapq.heappush(heap, (previous_frequency, previous_character))
        previous_frequency, previous_character = frequency, character
    result = "".join(output)
    return result if len(result) == len(text) else "IMPOSSIBLE"


def _build_h09() -> list[Case]:
    rng = random.Random(1009)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cases = []
    for index in range(99):
        if index == 0:
            text, category = "aab", "small possible"
        elif index == 1:
            text, category = "aaab", "small impossible"
        elif index == 2:
            text, category = "a", "single character"
        else:
            size = 500 + rng.randrange(2500)
            if index % 4 == 0:
                dominant = size // 2 + 2
                text = "a" * dominant + "b" * (size - dominant)
            elif index % 4 == 1:
                dominant = (size + 1) // 2
                text = "a" * dominant + "".join(rng.choice(alphabet[1:]) for _ in range(size - dominant))
            else:
                active = alphabet[: 2 + rng.randrange(24)]
                text = "".join(rng.choice(active) for _ in range(size))
            characters = list(text)
            rng.shuffle(characters)
            text = "".join(characters)
            category = "possible/impossible threshold and frequency ties"
        cases.append(Case(text + "\n", _reorganize(text) + "\n", len(text), category))
    return cases


def _build_b01() -> list[Case]:
    rng = random.Random(2001)
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    cases = []
    for index in range(99):
        if index == 0:
            text, category = "tree", "small frequency tie"
        elif index == 1:
            text, category = "a" * 200, "single distinct character"
        elif index == 2:
            text, category = alphabet * 4, "wide equal-frequency alphabet"
        else:
            size = 600 + rng.randrange(2600)
            active = alphabet[: 5 + rng.randrange(len(alphabet) - 4)]
            weights = [1] * len(active) if index % 3 == 0 else [rng.randint(1, 30) for _ in active]
            text = "".join(rng.choices(active, weights=weights, k=size))
            category = "wide alphabet and frequency ties"
        counts = Counter(text)
        expected = "".join(character * counts[character] for character in sorted(counts, key=lambda char: (-counts[char], char)))
        cases.append(Case(text + "\n", expected + "\n", len(text), category))
    return cases


def _h_index(citations: list[int]) -> int:
    ordered = sorted(citations, reverse=True)
    return max((index for index, value in enumerate(ordered, start=1) if value >= index), default=0)


def _build_b02() -> list[Case]:
    rng = random.Random(2002)
    cases = []
    for index in range(99):
        if index == 0:
            citations, category = [3, 0, 6, 1, 5], "classic example"
        elif index == 1:
            citations, category = [0], "zero"
        elif index == 2:
            citations, category = [500] * 500, "all highly cited"
        else:
            size = 500 + rng.randrange(2200)
            mode = index % 5
            if mode == 0:
                citations = [rng.randint(0, 5) for _ in range(size)]
            elif mode == 1:
                citations = [rng.randint(0, size * 3) for _ in range(size)]
            elif mode == 2:
                citations = sorted(rng.randint(0, size) for _ in range(size))
            elif mode == 3:
                citations = sorted((rng.randint(0, size) for _ in range(size)), reverse=True)
            else:
                citations = [0] * (size // 2) + [size + index] * (size - size // 2)
            category = "zero, capped, sorted, and extreme citations"
        cases.append(Case(f"{len(citations)}\n{_ints(citations)}\n", f"{_h_index(citations)}\n", len(citations), category))
    return cases


def _build_b03() -> list[Case]:
    rng = random.Random(2003)
    cases = []
    for index in range(99):
        if index == 0:
            nums, category = [3, 6, 9, 1], "classic example"
        elif index == 1:
            nums, category = [1], "single value"
        elif index == 2:
            nums, category = [0] * 300, "all equal"
        else:
            size = 500 + rng.randrange(1700)
            mode = index % 5
            if mode == 0:
                nums = [rng.randint(0, 100) for _ in range(size)]
            elif mode == 1:
                nums = rng.sample(range(0, size * 30), size)
            elif mode == 2:
                nums = sorted(rng.randint(0, 10**9) for _ in range(size))
            elif mode == 3:
                nums = sorted((rng.randint(0, 10**9) for _ in range(size)), reverse=True)
            else:
                nums = [rng.choice((0, 1, 10**9 - 1, 10**9)) for _ in range(size)]
            category = "duplicates, sparse ranges, extremes, and order"
        ordered = sorted(nums)
        answer = max((right - left for left, right in zip(ordered, ordered[1:])), default=0)
        cases.append(Case(f"{len(nums)}\n{_ints(nums)}\n", f"{answer}\n", len(nums), category))
    return cases


def _nearby_almost_duplicate(nums: list[int], index_diff: int, value_diff: int) -> bool:
    for right, value in enumerate(nums):
        left_bound = max(0, right - index_diff)
        if any(abs(value - nums[left]) <= value_diff for left in range(left_bound, right)):
            return True
    return False


def _build_b04() -> list[Case]:
    rng = random.Random(2004)
    cases = []
    for index in range(99):
        if index == 0:
            nums, index_diff, value_diff, category = [1, 2, 3, 1], 3, 0, "exact nearby duplicate"
        elif index == 1:
            nums, index_diff, value_diff, category = [1, 5, 9, 1, 5, 9], 2, 3, "classic false case"
        elif index == 2:
            nums, index_diff, value_diff, category = [1], 0, 0, "no pair window"
        else:
            size = 500 + rng.randrange(1400)
            mode = index % 4
            nums = [rng.randint(-10**9, 10**9) for _ in range(size)]
            index_diff = (0, 1, 50, rng.randint(2, 100))[index % 4]
            value_diff = (0, 1, 10**9, rng.randint(2, 10**6))[index % 4]
            if mode == 0 and index_diff > 0:
                position = rng.randrange(size - index_diff)
                nums[position + index_diff] = nums[position]
            category = "sliding index window, bucket boundaries, and extremes"
        answer = _nearby_almost_duplicate(nums, index_diff, value_diff)
        stdin = f"{len(nums)} {index_diff} {value_diff}\n{_ints(nums)}\n"
        cases.append(Case(stdin, f"{1 if answer else 0}\n", len(nums), category))
    return cases


def _build_b05() -> list[Case]:
    rng = random.Random(2005)
    cases = []
    for index in range(99):
        if index == 0:
            arr1, arr2, category = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6], "classic example"
        elif index == 1:
            arr1, arr2, category = [1], [1], "single value"
        elif index == 2:
            arr1, arr2, category = [5] * 300, [5], "all equal"
        else:
            size = 600 + rng.randrange(1800)
            value_pool = list(range(-100, 201))
            arr1 = [rng.choice(value_pool) for _ in range(size)]
            present = list(set(arr1))
            rng.shuffle(present)
            arr2 = present[: rng.randint(1, len(present))]
            category = "partial priority order, duplicates, and negative values"
        priority = {value: position for position, value in enumerate(arr2)}
        answer = sorted(arr1, key=lambda value: (0, priority[value]) if value in priority else (1, value))
        stdin = f"{len(arr1)} {len(arr2)}\n{_ints(arr1)}\n{_ints(arr2)}\n"
        cases.append(Case(stdin, _ints(answer) + "\n", len(arr1), category))
    return cases


def _car_pooling(capacity: int, trips: list[tuple[int, int, int]]) -> bool:
    changes = defaultdict(int)
    for passengers, start, end in trips:
        changes[start] += passengers
        changes[end] -= passengers
    current = 0
    for location in sorted(changes):
        current += changes[location]
        if current > capacity:
            return False
    return True


def _build_b06() -> list[Case]:
    rng = random.Random(2006)
    cases = []
    for index in range(99):
        if index == 0:
            capacity, trips, category = 4, [(2, 1, 5), (3, 3, 7)], "classic overload"
        elif index == 1:
            capacity, trips, category = 5, [(2, 1, 5), (3, 5, 7)], "drop-off before pickup"
        elif index == 2:
            capacity, trips, category = 1, [(1, 0, 1)], "single trip"
        else:
            trip_count = 250 + rng.randrange(1300)
            max_location = 1000 + rng.randrange(9000)
            trips = []
            for _ in range(trip_count):
                start = rng.randrange(max_location)
                end = rng.randrange(start + 1, max_location + 1)
                trips.append((rng.randint(1, 20), start, end))
            peak_upper_bound = sum(passengers for passengers, _, _ in trips)
            capacity = (1, peak_upper_bound, rng.randint(20, max(20, peak_upper_bound)))[index % 3]
            category = "simultaneous pickup/drop-off and dense overlapping trips"
        answer = _car_pooling(capacity, trips)
        stdin = f"{capacity} {len(trips)}\n" + "".join(f"{passengers} {start} {end}\n" for passengers, start, end in trips)
        cases.append(Case(stdin, f"{1 if answer else 0}\n", len(trips), category))
    return cases


BUILDERS = {
    "h01": _build_h01,
    "h02": _build_h02,
    "h03": _build_h03,
    "h04": _build_h04,
    "h05": _build_h05,
    "h06": _build_h06,
    "h07": _build_h07,
    "h08": _build_h08,
    "h09": _build_h09,
    "b01": _build_b01,
    "b02": _build_b02,
    "b03": _build_b03,
    "b04": _build_b04,
    "b05": _build_b05,
    "b06": _build_b06,
}


def build_cases(exercise_id: str) -> list[Case]:
    cases = BUILDERS[exercise_id]()
    if len(cases) != 99:
        raise ValueError(f"{exercise_id} generated {len(cases)} cases instead of 99")
    if len({case.stdin for case in cases}) != len(cases):
        raise ValueError(f"{exercise_id} generated duplicate stdin payloads")
    return cases
