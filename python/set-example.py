"""input = ['not', 'hashable']
hash(input)"""
# Create a set containing sports
sports = {'soccer', 'basketball', 'tennis', 'swimming', 'cycling'}

# Create a set containing sports played as a team
team_sports = {'soccer', 'basketball', 'volleyball', 'hockey'}

# Combine all unique elements from sports and
# team_sports into one set
all_sports = sports.union(team_sports)

print("Union of sets:", all_sports)

# Combine all shared elements from sports and
# team_sports into one set
common_sports = sports.intersection(team_sports)
print("Intersection of sets:", common_sports)

# Difference of sets
non_team_sports = sports.difference(team_sports)
print("Difference of sets:", non_team_sports)