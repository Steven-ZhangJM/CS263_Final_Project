

import sys

def main(args):
    passcode = ''
    count = 0;

    for line in open( "passcode.txt" ):
        passcode += line

    count = 0

    for counter in range( 1, len( passcode ) + 3 ):
        subset = passcode[ :counter ]
        #print "subset = " + subset
        test = 0
        for char in subset:
            #print "char : " + char,
                            
            for char1 in range( 1, len( passcode ) + 3 ):
                #print "char1 : " + char1

                for char2 in range( 1, len( passcode ) + 3 ):
                    test += 1

                    if char == passcode[char2]:
                        subset = subset[:char1-1] + passcode[char1:char2] + subset[char2:]
                        print subset
                        if subset == passcode:
                            print subset
                            print "FOUND ONE"
                            test = 1
                            break
                #if char == passcode[char1]:
                #     print "in here2"
                #     subset = subset[:char2-1] + passcode[char2:char1] + subset[char1:]
                #     if subset == passcode:
                #         test = 1
                #         #print subset
                #         break
            if test == 0:
                break

        #if test == 1:
        #    print "FOUND ONE",
        if len( subset ) == len( passcode ):
            count += 1

    print ""
    print count


if __name__ == "__main__":
    main( sys.argv )
