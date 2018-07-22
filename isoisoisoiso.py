def counter(word):
    count_list = []



    for char in "abcdefghijklmnopqrstuvwxyz":

        try:
            count_list.append(word.count(char))

            if max((count_list))==1:

                return(word,True)
            elif max(count_list)>1:
                return(word,False)


            elif word=="" or word==" ":

                return (word)
        except:
            raise TypeError('input a string')




        #except TypeError:
         #   print('its not a string')
          #  break

        #except AttributeError:
        #    print('thisisnotastring')
        #    break
    return


#print(counter("duck"))
#p#rint(counter(""))
#pr#int(counter(" "))
#pri#nt(counter("allofuscomeheredaily "))
#print(counter(45))
print(counter(3030))