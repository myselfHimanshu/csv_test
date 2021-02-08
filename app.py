import tracemalloc

tracemalloc.start()
with open("final.csv","wb") as fout:
    # write first file with header
    with open("data/0.csv", "rb") as f:
        fout.write(f.read())
    # write rest of the files    
    for num_file in range(1,100000):
        with open("data/"+str(num_file)+".csv", "rb") as f:
            next(f) # skip the header
            fout.write(f.read())

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
