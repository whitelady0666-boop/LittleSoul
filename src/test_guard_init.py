from belief_engine import BeliefEngine
from response_guard import ResponseGuard



belief=BeliefEngine()


print("================")
print("原始belief")
print(belief.beliefs)



guard=ResponseGuard(
    belief
)


print("================")
print("Guard内部belief")

print(
    guard.belief.beliefs
)