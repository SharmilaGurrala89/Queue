import queue



def main():

  # Step 1: Create a Queue from Python's import library

  q = queue.Queue()



  # Step 2: Create an object for that queue

  # (In this case, the object is 'q' itself created above.)



  # Step 3: Add an element to that queue

  q.put('element1')



  # Step 4: Pop an element from the queue

  removed_element = q.get()



  # Step 5: Show the output

  print("Removed element from the queue:", removed_element)



if __name__ == "__main__":

  main()

