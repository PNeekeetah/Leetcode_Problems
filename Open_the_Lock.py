"""
Beats 42% in terms of runtime 
Beats 12% in terms of memory

First time submission succesful 
Took me about 20 minutes to come
up with this
"""


def turn_wheel(combo: str, wheel: int, forward: bool):
    number = int(combo[wheel])
    number = (number + (forward * 1) - ((not forward) * 1)) % 10
    new_combo = combo[0:wheel] + str(number) + combo[wheel+1:]
    return new_combo


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen_set = set()
        queue = list()
        if "0000" not in deadends:
            queue = [("0000", 0)]
            seen_set.add("0000")
        index = 0
        while index < len(queue):
            current, moves = queue[index]
            combos = list()

            if current == target:
                return moves

            for i in range(4):
                # Turn forwards
                combo = turn_wheel(current, i, True)
                if combo not in deadends and combo not in seen_set:
                    combos.append((combo, moves + 1))
                    seen_set.add(combo)

                # Turn backwards
                combo = turn_wheel(current, i, False)
                if combo not in deadends and combo not in seen_set:
                    combos.append((combo, moves + 1))
                    seen_set.add(combo)

            queue.extend(combos)

            index += 1
        return -1
