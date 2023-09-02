# Create a set containing sports
sports = {'soccer', 'basketball', 'tennis', 'swimming', 'cycling'}

# Create a set containing sports played as a team
team_sports = {'soccer', 'basketball', 'volleyball', 'hockey'}

# Combine all unique elements from sports and
# team_sports into one set
all_sports = sports.union(team_sports)

# Union of sets: {'volleyball', 'hockey', 'soccer', 'cycling', 'tennis', 'swimming', 'basketball'}
print("Union of sets:", all_sports)

# Combine all shared elements from sports and
# team_sports into one set
shared_sports = sports.intersection(team_sports)

# Intersection of sets: {'soccer', 'basketball'}
print("Intersection of sets:", shared_sports)

# Create a set with elements that are unique 
# to the sports set when compared with team_sports
non_team_sports = sports.difference(team_sports)

# Difference of sets: {'cycling', 'swimming', 'tennis'}
print("Difference of sets:", non_team_sports)