#! /usr/bin/enc python3


zero = [
       "  ***   ",
       " *   *  ",
       "*     * ",
       "*     * ",
       " *   *  ",
       "  ***   "
       ]


one = [
       "  *     ",
       " **     ",
       "* *     ",
       "  *     ",
       "  *     ",
       "  *     "
       ]

two = [
       " ***    ",
       "*   *   ",
       "   *    ",
       "  *     ",
       " *      ",
       "*****   "
       ]

three = [
       " ***    ",
       "*   *   ",
       "   *    ",
       "   *    ",
       "*   *   ",
       " ***    "
       ]

numbers = [zero, one, two, three]
seznam = []
cd = []
def napisCislo():
    try:
        
        cislo = input("Zadejte cisla 1 ... 3")
        rada = 0    
        
        for vl in cislo:
            c = int(vl)
            
            if c > 3 or c < 0:
                print("Cislo musim byt mezi 0 a 3")
                return
            cd.append(numbers[int(vl)])
        xx=0  
        
        while xx<6:
            seznam.insert(xx,"")
            for vl2 in cd:
                
                seznam.insert(xx, str(seznam[xx] + vl2[xx])) 
            xx = xx+1
        
        xx=0
        for vl in seznam:
            print(vl)
            xx = xx+1
            if xx>5:
                break  
    except ValueError as err:
        print(err)
        
napisCislo()