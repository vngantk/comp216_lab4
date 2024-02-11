import time
import threading


def long_delay(name: str):
    for i in range(100_000):
        time.sleep(0.000_1)
    print(f"{name}")


def execute_loops(times: int):
    print(f"execute_loops: {times} times - starting")
    initial_time: float = time.time()
    for i in range(times):
        long_delay("Hello World!")
    elapsed_time: float = time.time() - initial_time
    print(f"execute_loops: {times} times - completed in {elapsed_time:.2f} seconds")


def execute_threads(times: int):
    print(f"execute_threads: {times} times - starting")
    initial_time: float = time.time()
    threads = []
    for i in range(times):
        thread = threading.Thread(target=long_delay, args=("Hello World!",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    elapsed_time: float = time.time() - initial_time
    print(f"execute_threads: {times} times - completed in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    execute_loops(10)
    execute_threads(10)

