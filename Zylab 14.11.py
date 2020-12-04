#Joel Sibi
#1617077


def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_smallest]:
                index_smallest = j

        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
        for num in numbers:
            print(str(num), end=' ')
        print()


if __name__ == "__main__":
    parts = input().split()
    numbers = []
    for i in range(len(parts)):
        numbers.append(int(parts[i]))
    selection_sort_descend_trace(numbers)