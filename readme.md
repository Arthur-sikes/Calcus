Here is a clean, professional README.md for your calculator project. I’ve included a "How it Works" section and a "Styling" breakdown based on the specific KivyMD properties you’ve implemented.
​KivyMD Calculator
​A modern, Material Design calculator built using KivyMD 1.2.0. This application features a responsive grid layout, custom-colored operation buttons, and a clean user interface.
​🚀 Features
​Dynamic UI: Built with MDGridLayout for a perfectly aligned button pad.
​Custom Styling:
​Numbers use a #CD853F (Peru/Brown) theme with zero elevation.
​Operators use a #FFD700 (Gold) theme for visual distinction.
​Smart Logic: Uses Python's eval() to process mathematical expressions.
​Responsive Input: Utilizes MDTextFieldRect with large font sizes for better readability.
​🛠️ Requirements
​Python 3.x
​Kivy
​KivyMD 1.2.0
​Install the dependencies via pip:
     pip install kivy kivymd
📂 Code Structure
​1. Calc(MDGridLayout)
​The main widget container.
​Input Panel: An MDTextFieldRect for displaying the current expression and results.
​Button Pad: A nested MDGridLayout (4 columns) that dynamically generates buttons from a list.
​Process Method: Handles the button logic:
​=: Calculates the result.
​del: Deletes the last character (backspace).
​Numbers/Ops: Appends text to the display.
​2. CalcusApp(MDApp)
​The application class that initializes the ScreenManager and sets up the "home" screen.
​🎨 Button Configuration
​The buttons are styled specifically to avoid the "raised" shadow look while maintaining high contrast.
Property Value Purpose
md_bg_color Hex Codes Custom branding for ops vs numbers.
elevation 0 Removes the shadow for a flat, modern look.
size_hint (0.01, 0.049) Controls how buttons scale within the grid.
font_size 32sp Large, accessible text.
📝 Usage
python main.py
