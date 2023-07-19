import json # imported json module


def gen_array():
    '''
    Although declared as an empty list,
    appending homogeneous datatype would
    suffice as an array in this case. 
    '''
    arr = []

    for x in range(1,101):
        '''
        The first if-statement condition ensures that only numbers
        divisible by primes 3 and 5 are replaced with 
        the string "BIG BANG". This avoids cases
        where a "BIG BANG" number may be mistakenly 
        replaced with a "BIG" or "BANG", for whichever
        condition is satisfied first. Therefore, the ordering
        of the conditions are imperative to the final resulting
        array output. Moreover, since the "BIG BANG" numbers 
        are divisible by both 3 and 5, there isn't an issue
        when it comes to short-circuit evaluation, whereby 
        the first condition "x % 3 == 0" will always 
        be satisfied by a "BIG BANG" number, and numbers that are
        divisible by 3 but not 5 will not satisfy the condition, vice versa. 
        '''
        if x % 3 == 0 and x % 5 == 0:
            arr.append("BIG BANG")
        elif x % 3 == 0:
            arr.append("BIG")
        elif x % 5 == 0:
            arr.append("BANG")
        else:
            # typecast integer number to string before appending to array
            arr.append(str(x))
    
        '''
        Notice that "BIG BANG" numbers occur at every 15
        number interval, and are divisible by 15, which 
        is a product of the primes 3 and 5. "BIG" numbers 
        occur at every 3, and "BANG" numbers 5 respectively.
        Thus, it's a given that the sequence of numbers 15,30,45,60,...
        at every 15 number increment results in a "BIG BANG".
        '''

        '''
        The time complexity of the program is O(1) provided that the 
        number of numbers that we iterate through is 100, a constant
        value that's not variable. Thus, if we take the number of operations
        performed into account, we would get O(100), which can be simplified to O(1). 
        Hypothetically, if the program was to be modified such that when a user
        runs the program, they will be required to enter any non-zero integer value, then the 
        program's corresponding time complexity will be O(n), where n denotes the
        non-zero numerical value that is entered by the user.  
        '''
    json_arr = json.dumps(arr)
    
    # writing json_arr to output.json
    with open("output.json","w") as output:
        output.write(json_arr)



def main():
    gen_array()

if __name__ == "__main__":
    main()