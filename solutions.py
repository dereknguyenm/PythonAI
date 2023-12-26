# 1) TWO SUM
# Solution 1
def twoNumberSum(array, targetSum):
    # Using Hashing with O(n) run time and O(n) space complexity
    values = {}
    for element in array:

        sumValue = targetSum - element  # 10-3

        if sumValue in values:
            return [element, sumValue]
        else:
            values[element] = True
    return []


# Solution 2
def twoNumberSum2(array, targetSum):
    # runtime of nlog(n)
    array.sort()
    left = 0
    right = len(array) - 1

    while left <= right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1
        else:  # array[left] + array[right] < targetSum
            left += 1
    return []


# 2) VALIDATE SUBSEQUENCE
# Solution 1
# runTime(n) with 1 space-time
def isValidSubsequence(array, sequence):
    indexOfSub = 0

    for element in array:
        if sequence[indexOfSub] == element:
            indexOfSub += 1

        if indexOfSub == len(sequence):
            return True

            # return indexOfSub == len(sequence)
    return False


# Solution 2
# Using while loop, potentially shorter than for loop method since it stops once it find it
# runTime(n) with 1 space-time
def isValidSubsequence2(array, sequence):
    seqIndex = 0
    arrayIndex = 0
    while arrayIndex < len(array) and seqIndex < len(sequence):

        if array[arrayIndex] == sequence[seqIndex]:
            seqIndex += 1

        arrayIndex += 1

    return seqIndex == len(sequence)


# 3) SORTED SQUARED ARRAY
# runtime O(n)
def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1
    squaredArray = []

    while left <= right:
        leftValue = abs(array[left]) ** 2
        rightValue = abs(array[right]) ** 2

        if leftValue == rightValue or rightValue > leftValue:
            squaredArray.insert(0, rightValue)
            right -= 1

        else:  # (leftValue>rightValue)
            squaredArray.insert(0, leftValue)
            left += 1

    return squaredArray


# 4) TOURNAMENT WINNER
# O(n) time and O(k) space
HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    bestTeam = ""
    scores = {bestTeam: 0}

    # loop through competitions array, enumerate keeps track of index
    for idx, competition in enumerate(competitions):
        result = results[idx]

        homeTeam, awayTeam = competition  # Sets hometeam and awayTeam

        if result == HOME_TEAM_WON:  # Determines team that won
            winningTeam = homeTeam
        else:
            winningTeam = awayTeam

        UpdateScores(winningTeam, scores, 3)  # Updates score of winning team
        if scores[bestTeam] < scores[winningTeam]:  # compares for the best team
            bestTeam = winningTeam

    return bestTeam


# Updates the winning team score or adds winning team into scores list
def UpdateScores(team, scores, points):
    if team in scores:
        scores[team] += points
    else:
        scores[team] = points


# 5) NON-CONSTRUCTABLE CHANGE
# O(nlogn) runtime and O(1) or O(n) space
def nonConstructibleChange(coins):
    coins.sort()

    possibleChange = 0

    for coin in coins:
        if coin > possibleChange + 1:
            return possibleChange + 1

        possibleChange += coin

    return possibleChange + 1


# 6) TRANSPOSE MATRIX
# O(w*h) runtime and O(w*h) space
def transposeMatrix(matrix):
    # row and column values are swapped
    transposedMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])

        transposedMatrix.append(newRow)

    return transposedMatrix

# 7) FIND THE CLOSEST VALUE IN BST (Binary Search Tree)


# 8) BRANCH SUMS (Binary Search Tree)
