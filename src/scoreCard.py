class ScoreCard:
    # Diccionario que mapea símbolos de bolos a sus valores numéricos
    VALUES = {'-': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9, 'X': 10, '/': 10}

    def __init__(self, rolls: str):
        # Inicializa la tarjeta de puntuación con la cadena de lanzamientos
        self.rolls = rolls
        self.frames = self._parse_frames()

 
    def _parse_frames(self):
        # Método privado para analizar los frames a partir de la cadena de lanzamientos
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
        # Devuelve el valor numérico de un lanzamiento dado
        return self.VALUES[roll]

    def _frame_values(self, frame):
        # Calcula los valores numéricos reales de un frame, interpretando X y /
        values = []
        for r in frame:
            if r == 'X':
                values.append(10)
            elif r == '/':
                if len(values) == 0:
                    values.append(10)  # shouldn't happen
                else:
                    values.append(10 - values[-1])
            else:
                values.append(self._value(r))
        return values

    def _is_strike(self, frame):
        # Verifica si un frame es un strike
        return frame[0] == 'X'

    def _is_spare(self, frame):
        # Verifica si un frame es un spare
        return len(frame) > 1 and frame[1] == '/'

    def _next_rolls(self, frame_index, n):
        # Obtiene los próximos n valores de lanzamientos a partir del frame dado
        rolls = []
        for f in self.frames[frame_index+1:]:
            rolls.extend(self._frame_values(f))
            if len(rolls) >= n:
                break
        return rolls[:n]

  
    def score(self):
        # Calcula la puntuación total del juego
        total = 0

        for i, frame in enumerate(self.frames):
            if i == 9:
                total += sum(self._frame_values(frame))
                continue

            if self._is_strike(frame):
                total += 10
                bonus = self._next_rolls(i, 2)
                total += sum(bonus)
                continue

            if self._is_spare(frame):
                total += 10
                bonus = self._next_rolls(i, 1)
                total += bonus[0] if bonus else 0
                continue

            # Open frame
            total += sum(self._frame_values(frame))

        return total
  