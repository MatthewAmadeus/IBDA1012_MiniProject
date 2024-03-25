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

print(score)
bubbleSort(score)
print(score)