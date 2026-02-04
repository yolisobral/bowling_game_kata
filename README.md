
#  Bowling Game – Score Calculator

This project implements the core logic for scoring a **ten‑pin bowling game**.  
It parses a string of rolls, builds frames, and computes the final score following official bowling rules.

---

## Main Components

### **Automaton**
- Acts as the scoring engine.
- Receives a `ScoreCard` and returns the total score.

### **ScoreCard**
- Parses the input string of rolls.
- Builds the 10 frames (including extra rolls in the 10th frame).
- Converts symbols into pin values:
  - `X` = strike  
  - `/` = spare  
  - `-` = 0 pins  
  - `1–9` = pin count  

---

##  Bowling Rules Implemented

### **Frame**
- 10 frames per game.
- Frames 1–9:
  - Strike → one roll (`"X"`)
  - Spare → two rolls summing to 10 (`"5/"`)
  - Open frame → two rolls (`"34"`)

### **Strike**
- Worth:  
  `10 + next two rolls`

### **Spare**
- Worth:  
  `10 + next roll`

### **10th Frame Extras**
- Strike → 2 extra rolls  
- Spare → 1 extra roll  
- Supports perfect game (`"XXXXXXXXXXXX"` → 300)

---

## Testing

The project uses **pytest** and includes tests for:

- Regular scoring  
- Zero symbol (`-`)  
- Spares  
- Strikes, doubles, triples  
- Extra rolls in the 10th frame  
- Perfect game  

Run tests with:

```bash
pytest -v
```

