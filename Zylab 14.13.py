#Joel Sibi
#1617077

# Global variable
num_calls = 0


def partition(user_ids, i, k):
    #  Pick middle element as pivot
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]

    #  Initialize variables
    done = False
    l = i
    h = k
    while not done:
        #  Increment l while numbers[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h]
        while pivot < user_ids[h]:
            h = h - 1
        """  If there are zero or one items remaining,
              all numbers are partitioned. Return h """
        if l >= h:
            done = True
        else:
            """  Swap numbers[l] and numbers[h],
                  update l and h """
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
    return h


def quicksort(user_ids, i, k):
    global num_calls
    num_calls +=1
    j = 0
    """  Base case: If there are 1 or zero entries to sort,
          partition is already sorted  """
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """
    j = partition(user_ids, i, k)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)