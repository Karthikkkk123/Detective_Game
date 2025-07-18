import threading
import time
from typing import Callable, Optional

class GameTimer:
    def __init__(self, duration: int, callback: Optional[Callable] = None):
        self.duration = duration
        self.start_time = None
        self.callback = callback
        self.running = False
        self.thread = None
        self._stop_event = threading.Event()
    
    def start(self):
        """Start the timer"""
        if self.running:
            return
        
        self.running = True
        self.start_time = time.time()
        self._stop_event.clear()
        
        self.thread = threading.Thread(target=self._timer_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        """Stop the timer"""
        self.running = False
        self._stop_event.set()
        
        if self.thread:
            self.thread.join(timeout=1)
    
    def get_time_remaining(self) -> float:
        """Get remaining time in seconds"""
        if not self.running or not self.start_time:
            return 0
        
        elapsed = time.time() - self.start_time
        remaining = max(0, self.duration - elapsed)
        return remaining
    
    def is_running(self) -> bool:
        """Check if timer is running"""
        return self.running and self.get_time_remaining() > 0
    
    def _timer_loop(self):
        """Internal timer loop"""
        while self.running and not self._stop_event.is_set():
            remaining = self.get_time_remaining()
            
            if remaining <= 0:
                self.running = False
                if self.callback:
                    self.callback()
                break
            
            time.sleep(0.1)
