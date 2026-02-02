class ScoreCard:
   
    VALUES = {'-': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9, 'X': 10, '/': 10}

    def __init__(self, rolls: str):
        self.rolls = rolls
        self.frames = self._parse_frames()

 
    def _parse_frames(self):
        frames = []
        i = 0

        while len(frames) < 9:
            if self.rolls[i] == 'X':
                frames.append(('X',))
                i += 1
            else:
                frames.append((self.rolls[i], self.rolls[i+1]))
                i += 2

        # Frame 10: todo lo que queda
        frames.append(tuple(self.rolls[i:]))
        return frames


    def _value(self, roll):
        return self.VALUES[roll]

    def _is_strike(self, frame):
        return frame[0] == 'X'

    def _is_spare(self, frame):
        return len(frame) > 1 and frame[1] == '/'

    def _next_rolls(self, frame_index, n):
        """Devuelve los próximos n lanzamientos reales."""
        rolls = []
        for f in self.frames[frame_index+1:]:
            for r in f:
                rolls.append(r)
        return rolls[:n]

  
    def score(self):
        total = 0

        for i, frame in enumerate(self.frames):
            # Último frame
            if i == 9:
                total += sum(self._value(r) for r in frame)
                continue

            # Strike
            if self._is_strike(frame):
                total += 10
                bonus = self._next_rolls(i, 2)
                total += sum(self._value(r) for r in bonus)
                continue

            # Spare
            if self._is_spare(frame):
                total += 10
                bonus = self._next_rolls(i, 1)[0]
                total += self._value(bonus)
                continue

            # Open frame
            total += self._value(frame[0]) + self._value(frame[1])

        return total
  