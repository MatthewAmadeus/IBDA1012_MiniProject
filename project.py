import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('Mini Project\student-scores.csv')

# Sort the DataFrame based on the 'full_name' and 'industry' columns
df_sorted = df.sort_values(['first_name', 'last_name'])

# Print the sorted DataFrame
df.drop(['email'], axis=1, inplace=True)
# print(df['geography_score'])
# english score
score = df.values[:,-2]
# name of person
name = df.values[:,1]
# b = df['english_score']
print("this is df:",score)
print("this is df:",name)




# print(df_sorted.values[:,-2])

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot  = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    # Traverse through all array elements
    for i in range(n-1):

        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        swapped = False
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def checklist(arr, sorted):
    checklist = []
    found_in_checklist = None

    for s in sorted:
        for index in range(len(arr)):
            found_in_checklist = False

            if arr[index] == s:
                for checklist_index in checklist: 
                    if index == checklist_index:
                        found_in_checklist = True
                        break
            
                if found_in_checklist == False:
                    checklist.append(index)
                    # print(name[index])
                    break

    return checklist

print('score',score)

print(bubbleSort(score))
quickSort_sorted_score = quickSort(score)
# bubbleSort_sorted_score = bubbleSort(score)
print(f'quickSort_sorted_score:{quickSort_sorted_score}')
# print(f'bubbleSort_sorted_score:{bubbleSort_sorted_score}')

sorted_score_index = checklist(score, quickSort_sorted_score)

# print
for i in sorted_score_index:
    print("name:", name[i],"\tscore:", score[i])


