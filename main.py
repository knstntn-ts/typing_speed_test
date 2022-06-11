from tkinter import *
import time

BACKGROUND_COLOR = "#B1DDC6"
TARGET_TEXT = "Hello, my name is Kosta."
TARGET_TEXT_LIST = TARGET_TEXT.split()
start_timer = [True]

i = [0]


def start_test():
    start_time = [0]

    def check_word(e):

        if start_timer[0]:
            start_time[0] = time.time()
            start_timer[0] = False

        else:
            text_typed = input_text_field.get('1.0', 'end-1c')

            if e.keysym == 'space':

                last_typed_word = text_typed.split()[-1]

                if last_typed_word == TARGET_TEXT_LIST[i[0]]:
                    i[0] += 1

                else:
                    len_word = len(last_typed_word) + 2
                    input_text_field.delete(f'end-{len_word}c', 'end-1c')

            if len(text_typed) > 0 and len(text_typed) == len(TARGET_TEXT):
                print('End of the test.')
                wpm = (i[0] + 1) / ((time.time() - start_time[0]) / 60)
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

    canvas.destroy()
    load_image_but.destroy()

    instruction_text_label = Label(window, text="In the bottom field, type the following:", font=('Arial', 15, 'bold'),
                                   wraplength=300)
    instruction_text_label.grid(row=0, column=1)

    sample_text_label = Label(window, text=TARGET_TEXT, width=100, height=1, pady=50, wraplength=500)
    sample_text_label.grid(row=1, column=0, columnspan=3)

    input_text_field = Text(window, height=15, width=100)
    input_text_field.grid(row=2, column=0, columnspan=3)
    input_text_field.bind('<Key>', check_word)


# ---------------------- UI SETUP --------------------#
window = Tk()
window.title('Watermarker')
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