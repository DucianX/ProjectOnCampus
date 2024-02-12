from queue import Queue


class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        self.queue = Queue()

    def send_to_bench(self, player_name):
        # Put the player "onto the bench"
        self.queue.put(player_name)

    def get_from_bench(self):
        # Return the name of the player who has been on the bench longest.
        return self.queue.get()

    def display(self):
        temp_queue = Queue()
        if not self.queue.empty():
            print("The bench currently includes:")
            player = self.queue.get()
            print(player)
            temp_queue.put(player)
        else:
            print("The bench currently has nothing on it.")
        # Restore the original queue state
        self.queue = temp_queue

    def is_on_bench(self, player_name):
        # Temporary queue to hold players while we search
        temp_queue = Queue()
        found = False

        # Dequeue each player to check for the target player
        while not self.queue.empty():
            player = self.queue.get()
            if player == player_name:
                found = True
            # Enqueue the player onto the temporary queue
            temp_queue.put(player)

        # Restore the original queue from the temporary queue
        self.queue = temp_queue
        return found

    def is_bench_empty(self):
        if self.queue.empty():
            return True
        else:
            return False
