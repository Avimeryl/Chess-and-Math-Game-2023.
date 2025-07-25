# 🏰 Chess + Math Quiz Game  

This is a **Python-based Chess game** built with **Pygame**, with a unique twist – before completing a move, players must answer a **Math Quiz** correctly. If they fail the quiz, the move is not executed!  

It also features:  
- Standard **drag-and-drop chess mechanics**  
- **Timers** for both White and Black players  
- **Sound effects** and customizable themes  
- **Math Quiz challenges** before a valid move  
- Reset & Theme switching  

---

## 🎮 Gameplay  

- Play classic Chess against another player on the same machine.  
- When you try to move a piece, a **Math Quiz popup** appears.  
- ✅ If you answer correctly, the move executes.  
- ❌ If you answer incorrectly, the move is canceled.  
- Each player has **10 minutes** before their timer runs out.  

---

## 🛠️ Installation  

1. **Clone the repository**  

   ```bash
   git clone https://github.com/your-username/chess-math-quiz.git
   cd chess-math-quiz

2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install dependencies

pip install -r requirements.txt


# ▶️ Running the Game

python main.py

Controls:

- Drag and drop to move pieces

- T – Change theme

- R – Reset the game

- Quit – Close the window

# 📂 Project Structure

chess-math-quiz/
│
├── main.py            # Main game loop
├── game.py            # Game logic, board, and move handling
├── square.py          # Square representation
├── move.py            # Move representation
├── MathQuiz.py        # Math quiz GUI & logic
├── const.py           # Constants (board size, colors, etc.)
├── assets/            # Sounds, images, themes
└── requirements.txt   # Dependencies

# 🧠 Math Quiz

- Each quiz is generated randomly.

- If you fail, the move is invalidated.

- Future updates could include difficulty scaling and score tracking.

# 🚀 Future Improvements

- Add AI opponent

- Add difficulty levels for Math Quizzes

- Online multiplayer mode

- Save/load game feature

# 👨‍💻 Author

1. Ibnu Ameerul bin Abdul Halim
2. Khoo Zi Yik
3. Lucas Chu Yen Feng

# 📜 License

MIT License – feel free to use and modify!