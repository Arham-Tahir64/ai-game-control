import threading
import time
from .game_state import GameState
from .spotify import sp

def on_enemy_detected(boxes):
    """
    Called whenever model detects an enemy box
    """
    # Lower volume to 20%
    try:
        sp.volume(20)
    except Exception:
        pass

    # 2) Change combat state to true
    GameState.in_combat = True

    # 3) After 3s of no new calls, change combat to false and increase volume
    def exit_combat_later():
        time.sleep(3)
        GameState.in_combat = False
        try:
            sp.volume(75)
        except Exception:
            pass

    threading.Thread(target=exit_combat_later, daemon=True).start()
