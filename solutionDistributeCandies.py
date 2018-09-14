# Mary have to share her candies with her brother. Given an integer array 
# with even length, where different numbers in this array represent different 
# kinds of candies. Each number means one candy of the corresponding kind. 
# You need to distribute these candies equally in number to brother and sister. 
# Additionally, Mary wants to get a major variety of candies, so you need to
# apply a prioritization on the candies distribution.
# Return the array with the kinds of candies the sister could gain.
def solutionDistributeCandies(T):
    T.sort(reverse=True)
    candiesVar = {}
    #1: Count candies variety
    for item in T:
        if item not in candiesVar.keys():
            candiesVar[item] = 1
        else:
            candiesVar[item] += 1
    #2: Share candies
    candiesShare = { "Mary": [], "Brother": [] }
    for candie in T:
        if candiesVar[candie] == 1:
            candiesShare["Mary"].append(candie)
        else:
            if len(candiesShare["Brother"]) < len(candiesShare["Mary"]):
                candiesShare["Brother"].append(candie)
            else:
                candiesShare["Mary"].append(candie)
    #3: Count Mary's candies variety
    candiesVar = {}
    for item in candiesShare["Mary"]:
        if item not in candiesVar.keys():
            candiesVar[item] = 1
        else:
            candiesVar[item] += 1
    return candiesShare["Mary"]

print(solutionDistributeCandies([3, 4, 7, 7, 6, 6]))
print(solutionDistributeCandies([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]))