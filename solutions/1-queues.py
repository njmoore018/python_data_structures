def assign_rep(call_queue, reps_queue):
    # Check if there are any callers.
    if len(call_queue) < 1:
        print("No callers right now.")

    # If there are callers, check if there are any representatives.
    elif len(reps_queue) < 1:
        print("No available representatives right now.")

    # Since there are both callers and reps, assign each caller to a 
    # rep in the order the calls came in and the reps became available.
    while len(call_queue) > 0 and len(reps_queue) > 0:
           # Using the pop() function allows us to accomplish two things
           # at once, obtaining the person and removing them from the queue.
           rep = reps_queue.pop(0)
           caller = call_queue.pop(0)
           print(f"{rep} is assigned to help {caller}.")
        

def main():
    # Create an empty queue for incoming calls and one for 
    # representatives as they become available.
    call_queue = []
    reps_queue = []

    reps_queue.append("Rep1")
    assign_rep(call_queue, reps_queue) # Output: No callers right now.
    call_queue.append("Caller1")
    call_queue.append("Caller2")
    call_queue.append("Caller3")
    assign_rep(call_queue, reps_queue) # Output: Rep1 -> Caller1
    assign_rep(call_queue, reps_queue) # Output: No reps right now.
    reps_queue.append("Rep2")
    reps_queue.append("Rep3")
    assign_rep(call_queue, reps_queue) # Output: Rep2 -> Caller2
                                       #         Rep3 -> Caller3

if __name__ == "__main__":
    main()