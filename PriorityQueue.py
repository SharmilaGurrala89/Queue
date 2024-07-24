import queue



def main():

  # Step 1: Create a Priority Queue from Python's import library

  pq = queue.PriorityQueue()



  # Step 2: Create an object for that priority queue

  # (In this case, the object is 'pq' itself created above.)



  # Step 3: Add an element to that priority queue

  pq.put((2, 'element2')) # Priority 2

  pq.put((1, 'element1')) # Priority 1



  # Step 4: Pop an element from the priority queue

  removed_element = pq.get()



  # Step 5: Show the output

  print("Removed element from the priority queue:", removed_element)



if __name__ == "__main__":

  main()

