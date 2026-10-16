from sklearn import tree

# step 1: prepare our training clues
# features: [is_raining, temperature, is_windy]
# 0 = no, 1 = yes
clues = [
    [0, 28, 0],  # sunny, 28 C, calm wind -> great day!
    [1, 24, 1],  # raining, 24 C, very windy -> stay inside!
    [0, 42, 0],  # sunny, but 42 C heatwave -> too hot!
    [0, 25, 1],  # nice, 25 C, breezy -> still fine to play!
    [1, 29, 0],  # raining, 29 C, calm -> wet pitch, stay inside!
    [0, 31, 0],  # warm, 31 C, calm -> good for an evening match!
]

# step 2: the correct answers for each day
# 1 = go play outside, 0 = stay inside
answers = [1, 0, 0, 1, 0, 1]

# step 3: create the smart tree
my_tree = tree.DecisionTreeClassifier()

# step 4: teach the tree using our clues and answers
my_tree.fit(clues, answers)

# step 5: test a brand new day!
# let's test: no rain, 30 C, calm breeze
today = [[0, 30, 0]]
verdict = my_tree.predict(today)

if verdict[0] == 1:
    print("grab your bat and ball, it is time to play cricket!")
else:
    print("better stay home, sip some hot chai, and play a board game!")
