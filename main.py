import bluetooth
import microphone
import time

# Loop every certain number of seconds
while True:
    counter = 1
    record_start = time.time()
    if (counter == 1 or time.ticks_diff(record_start, record_end) == 4): # Add in 4 secs
        
        microphone.record(seconds=4.0, bit_depth=8, sample_rate=8000)

        time.sleep(0.5)

        samples = bluetooth.max_length() // 2

        chunk1 = microphone.read(samples)
        chunk2 = microphone.read(samples)

        if chunk1 == None:
            break
        elif chunk2 == None:
            bluetooth.send(chunk1)
        else:
            bluetooth.send(chunk1 + chunk2)

        record_end = time.time()
    else:
        break
    counter +=1