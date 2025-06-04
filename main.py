import random

raw_teams: str = input('Teams (separator:","): ')
teams: list[str] = [team.strip() for team in raw_teams.split(",")]

if len(teams) < 2:
    raise ValueError("At least 2 teams are needed")

seed: str = input("Seed: ")

raw_shuffle_amount: str = input("Times to Shuffle: ")

shuffle_exception: ValueError = ValueError("Shuffle Amount must be a valid int bigger then 0")

if raw_shuffle_amount.isnumeric():
    shuffle_amount: int = int(raw_shuffle_amount)
    if shuffle_amount < 1:
        raise shuffle_exception
else:
    raise shuffle_exception

random.seed(seed)

for i in range(shuffle_amount):
    random.shuffle(teams)
    print(f"Step: {i} > {', '.join(teams)}")

print()
print("Final Result:")
for i in range(0, len(teams), 2):
    print(f"{teams[i]} - {teams[i + 1] if len(teams) - 1 >= i + 1 else '*'}")
