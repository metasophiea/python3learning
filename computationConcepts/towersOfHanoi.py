def pegPrinter(*pegs,height=-1,width=-1):
    maxWidth = width if width > max(max(pegs)) else max(max(pegs))

    # dynamic height detection based on minimum needed height
    #maxHeight =  len(max(pegs,key=len))
    # dynamic height detection based on maximum needed height
    maxHeight = 0
    for peg in pegs: maxHeight += len(peg)
    # static height detection based input arguments
    maxHeight = height if height > maxHeight else maxHeight


    # top level printing
    for peg in range(len(pegs)):
        print("|" + " "*maxWidth, end="")
    print()
    
    #the rest of the printing
    for level in range(maxHeight):
        for peg in range(len(pegs)):
            outputString = ""
            if maxHeight-len(pegs[peg]) <= level:
                a = 0
                while a < pegs[peg][maxHeight-level-1]:
                    outputString += "#"
                    a += 1
                while a <= maxWidth:
                    outputString += " "
                    a += 1
            else:
                outputString = "|" + " "*maxWidth
            print(outputString, end="")
        print()
    print()




def hanoi(n, source, helper, target):
    if n > 0:
        pegPrinter(source, helper, target)
        hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        hanoi(n - 1, helper, source, target)
        pegPrinter(source, helper, target)
        



source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print(source, helper, target)
pegPrinter(source, helper, target)