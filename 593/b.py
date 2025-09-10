n = int(input())
movies = []
for i in range(n):
    a, b = map(int, input().split())
    
    movies.append([a, b])

def max_non_overlapping_intervals(intervals):
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    
    # Initialize the end time of the last selected interval
    end = float('-inf')
    
    # Initialize the count of non-overlapping intervals
    count = 0
    
    # Iterate through the sorted intervals
    for interval in intervals:
        # If the start time of the current interval is greater than or equal to the end time of the last selected interval
        if interval[0] >= end:
            # Select this interval
            end = interval[1]
            # Increment the count
            count += 1
    
    return count
print(max_non_overlapping_intervals(movies))