##### IMPORT STATEMENTS
from tkinter import *
import time

##### CONSTANTS AND VARIABLES
BACKGROUND_COLOR = "#B1DDC6"
TARGET_TEXT = "Every great journey begins with a small step. So, be courageous and take your first step towards your " \
              "dream!"
# Split the text for convenience
TARGET_TEXT_LIST = TARGET_TEXT.split()
# Global variables
start_timer = [True]
i = [0]

# Main function
def start_test():
    start_time = [0]

    # Checks the typed word
    def check_word(e):

        # Start the timer if already not started
        if start_timer[0]:
            start_time[0] = time.time()
            start_timer[0] = False

        # Checking algorithm
        if e.keysym != 'Shift_L' and e.keysym != 'Shift_R':
            # For keys other than "Shift" get the last typed letter from the text field
            input_text_field.tag_add("new_let", "end-2c")
            all_text = input_text_field.get('1.0', 'end-1c')
            new_let = input_text_field.get('end-2c')

            # Check if the target text is typed all, calculate the speed and display it.
            if len(all_text) == len(TARGET_TEXT):
                print('End of the test.')
                wpm = len(TARGET_TEXT_LIST) / ((time.time() - start_time[0]) / 60)
                input_text_field['state'] = 'disabled'
                print(f'Your speed is {int(wpm)} words per minute!')
                instruction_text_label.destroy()
                sample_text_label.destroy()
                input_text_field.destroy()
                input_text_field.unbind_all('<Key>')
                canvas_final = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
                canvas_final.create_text(400, 263, text=f"End of the test.\nYour speed is {int(wpm)} words per "
                                                        "minute!", font=('Arial', 30, 'bold'))
                canvas_final.grid(row=0, column=0, columnspan=1)

            # Delete last character if it is not equal to the target one
            if new_let != TARGET_TEXT[len(all_text)-1]:
                input_text_field.delete('end-2c')

    # --- Typing space --- #
    canvas.destroy()
    load_image_but.destroy()

    instruction_text_label = Label(window, text="In the bottom field, type the following:", font=('Arial', 15, 'bold'),
                                   wraplength=300)
    instruction_text_label.grid(row=0, column=1)

    sample_text_label = Label(window, text=TARGET_TEXT, width=100, height=1, pady=50, wraplength=500)
    sample_text_label.grid(row=1, column=0, columnspan=3)

    # When key is released call check_word function
    input_text_field = Text(window, height=15, width=100)
    input_text_field.grid(row=2, column=0, columnspan=3)
    input_text_field.bind('<KeyRelease>', check_word)


# ---------------------- UI SETUP --------------------#
window = Tk()
window.title('Typing Speed Test')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
word_text = canvas.create_text(400, 263, text="Test your typing speed!", font=('Arial', 30, 'bold'))

canvas.grid(row=0, column=0, columnspan=1)
load_image_but = Button(text='Click here to begin', command=start_test)
load_image_but.grid(row=1, column=0)

window.mainloop()
#
# for w in TARGET_TEXT.split():
#     print(w)
