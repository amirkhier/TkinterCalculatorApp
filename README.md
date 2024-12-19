# Simple GUI Calculator

This project is a simple calculator application built using Python's `tkinter` library for the graphical user interface and `sympy` for mathematical computations. The calculator supports basic arithmetic operations, parentheses, powers, and more.

---

## Features

- **Basic Arithmetic:** Addition, subtraction, multiplication, and division.
- **Advanced Operations:** Square (`**2`), cube (`*3.14` for π), and power functions.
- **Parentheses:** Grouping expressions for complex calculations.
- **Error Handling:** Displays "Error" for invalid expressions.
- **Reset Button:** Clear the current input.
- **Backspace Button:** Delete the last character in the input field.
- **Exit Button:** Close the application.

---

## Requirements

- Python 3.x
- Required libraries: `tkinter`, `sympy`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-gui-calculator.git
   cd simple-gui-calculator
   ```

2. Install dependencies:
   ```bash
   pip install sympy
   ```

---

## Usage

Run the calculator by executing the following command:
```bash
python calculator.py
```

---

## Code Overview

The calculator application consists of the following key components:

1. **Display Field**  
   An entry widget (`tkinter.Entry`) for displaying input and results.

2. **Number Buttons**  
   Buttons for digits (0-9), dynamically generated using nested loops.

3. **Operation Buttons**  
   Buttons for mathematical operations like `+`, `-`, `*`, `/`, and others.

4. **Special Buttons**
   - **C:** Clears the current input.
   - **=:** Evaluates the input and displays the result.
   - **Backspace:** Deletes the last character in the input.
   - **Exit:** Closes the application.

---

## How It Works

- **Input Handling:**  
  The numbers and operators are inserted into the display field in sequence when their respective buttons are clicked.

- **Evaluation:**  
  The `sympy.sympify()` function evaluates the input string as a mathematical expression.

- **Error Handling:**  
  If the input is invalid, an "Error" message is displayed in the input field.

---

## Preview

![Calculator Screenshot](https://via.placeholder.com/400x300.png?text=Calculator+Preview)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

