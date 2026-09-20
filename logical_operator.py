"""
logical operator or, and
"""

age = 11
can_vote = True

elegible_to_vote_self = age < 10 and can_vote
elegible_to_vote_self_ = age <= 10 or can_vote

print(elegible_to_vote_self)
print(elegible_to_vote_self_)