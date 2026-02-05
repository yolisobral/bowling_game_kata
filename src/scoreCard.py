class ScoreCard:
    VALUES = {'-': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9, 'X': 10} 

    def __init__(self, rolls: str):
        self.rolls = rolls                            
        self.roll_values = self._expand_rolls()       

    def _expand_rolls(self):
        values = []
        prev = 0

        for r in self.rolls:
            if r == 'X':
                values.append(10)
                prev = 10
            elif r == '/':
                spare_val = 10 - prev
                values.append(spare_val)
                prev = spare_val
            else:
                v = self.VALUES[r]
                values.append(v)
                prev = v

        return values

    def score(self):
        total = 0
        roll_index = 0

        for frame in range(10):
            # Strike
            if self.rolls[roll_index] == 'X':
                total += 10 + self.roll_values[roll_index+1] + self.roll_values[roll_index+2]
                roll_index += 1
                continue

            # Spare
            if self.rolls[roll_index+1] == '/':
                total += 10 + self.roll_values[roll_index+2]
                roll_index += 2
                continue

            # Open frame
            total += self.roll_values[roll_index] + self.roll_values[roll_index+1]
            roll_index += 2

        return total

  