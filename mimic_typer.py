import random
import time

import pyautogui
import schedule


def start_typing():
    with open("text_to_type.txt", "r", encoding="utf-8") as f:
        text = f.read()

    delay_before_start = 5

    print(f"Typing will start in {delay_before_start} seconds.")
    print("Quickly move your cursor to the input box where you want the text to appear...")
    time.sleep(delay_before_start)

    print("Typing now...")
    for char in text:
        pyautogui.typewrite(char)
        if char == " ":
            time.sleep(random.uniform(0.01, 0.2))
        if char in (".", "!", "?"):
            time.sleep(random.uniform(2.0, 3.0))
        if char == "\n":
            time.sleep(random.uniform(20.0, 30.0))

    pyautogui.press("enter")

    print("Done.")

    return schedule.CancelJob


def start():
    while True:
        ans = input("Do you want to schedule your typing? [Y/N] ").lower()
        if ans in ("y", "n"):
            break

    if ans == "y":
        scheduled_time = input("Enter the time to execute your typing: ")
        print("Scheduling...")
        schedule.every().day.at(scheduled_time).do(start_typing)
        while True:
            schedule.run_pending()
            jobs = schedule.get_jobs()
            if not jobs:
                break
            time.sleep(1)

    if ans == "n":
        start_typing()


if __name__ == "__main__":
    start()
