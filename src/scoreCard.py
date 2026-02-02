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


    