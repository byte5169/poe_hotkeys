import keyboard as k
import time as t


def use_bbbf(bf_key: str, bb_key: str) -> None:
    """
    It sends the keystrokes for the bladefall key and the bladeblast key

    Args:
      bf_key (str)
      bb_key (str)
    """
    k.send(bf_key)
    t.sleep(0.5)
    k.send(bb_key)


# A loop that will run forever until the user presses the "f10" key.
while True:
    if k.is_pressed("f10"):
        break

    # Press Q to start casting BB/BF sequence
    if k.is_pressed("q"):
        use_bbbf("t", "ctrl+t")
