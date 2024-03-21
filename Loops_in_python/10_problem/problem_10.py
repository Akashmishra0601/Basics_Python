
import time

wait_time = 2

max_retrive = 5
attempts = 0

while attempts < max_retrive:
    print("Attempt" , attempts + 1, "wait time ",wait_time )

    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    