import time
import pyautogui


def start_typing():
    with open("text_to_type.txt", "r", encoding="utf-8") as f:
        text = f.read()

    delay_before_start = 5
    char_interval = 0.2

    print(f"Typing will start in {delay_before_start} seconds.")
    print("Quickly move your cursor to the input box where you want the text to appear...")
    time.sleep(delay_before_start)

    print("Typing now...")
    pyautogui.typewrite(text, interval=char_interval)
    pyautogui.press("enter")

    print("Done.")


if __name__ == "__main__":
    try:
        start_typing()
    except KeyboardInterrupt:
        print("Stopped by user.")
