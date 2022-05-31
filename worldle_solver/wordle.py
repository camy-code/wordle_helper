# we are going to assume you have done the correct setup of in bulk_word.py

import bulk_word as b
class WORD:
    def __init__(self):
        self.ls = b.book() #this is the main list that we work with
        self.cor_placement = {} # key: position 
                                # value: name of letter
        self.wrong = set()
        self.contain = set()
        self.wrong_placement = {} # key: letter
                                  # value: places where the letter is not located


 #The follow are just the getters 
    def get_ls(self):
        return self.ls

    def get_ls_len(self):
        return len(self.ls)

    def get_corPos(self):
        return self.cor_placement

    def getWRONG_placement(self):
        return self.wrong_placement

    def getWrong(self):
        return self.wrong

    def getContain(self):
        return self.contain

    def get_fancy_ls(self):
        cou = 1
        for i in self.ls:
            print(f"{cou}: {i}")
            cou+=1
#----------END of Getters---------

    #the following adds a wrong character to the list
    def add_wrong(self,a):
        self.wrong.add(a)

    #the following adds a letter to a and has a list of all the times it doesnt occur
    def add_con(self, a):
        self.contain.add(a)        


    # Adds a correct letter our dictionary with its position 
    # [0,1,2,3,4] 
    def add_cor_placement(self,a, pos):
        self.cor_placement[pos] = a
        self.contain.add(a)

    def add_wrong_placement(self, letter, pos):
        if letter in self.wrong_placement:
            self.wrong_placement[letter].append(pos)
        else:
            self.wrong_placement[letter] = list()
            self.wrong_placement[letter].append(pos)
            self.add_con(letter)

#this method removes letters without that letter
    def update_wrong(self):
        #we need to make a shallow copy here
            x = self.ls[:]
            for i in x: #goes throuh all the letters
                for c in i: #we will first be checking for letters that are not present
                    if (c in self.wrong):
                        if (i in self.ls):
                            self.ls.remove(i)
   
    #this method looks at all the correct letters and removes accordingly
    def update_cor_placement(self):
            x = self.ls[:] #we need to make a shallow copy 
            for word in x:
                for letter in range(len(word)):
                    if (letter in self.cor_placement):
                        if word[letter] != self.cor_placement[letter] and word in self.ls:
                            self.ls.remove(word)         

    #removes things accordingly to whether it contains it                
    def update_contain(self):
            x = self.ls[:] # we need to make a shallow copy 
            for i in x:
                for let in self.contain:
                    if (not (let in i)) and i in self.ls:
                        self.ls.remove(i)

    #does the wrong placement and we dab
    def update_other_placement(self):
        x = self.ls[:]
        for word in x: #this is where we check for the word
            for letter in self.wrong_placement.keys(): #this now looks at the letter
                if type(self.wrong_placement[letter]) is list:
                    for pos in self.wrong_placement[letter]:
                        if word[pos] == letter and word in self.ls:
                            self.ls.remove(word)

    #this does all of the updates for easy use
    def updateLS(self):
        #word that contain a set letter
        self.update_wrong() 
        self.update_cor_placement()
        self.update_contain()
        self.update_other_placement()



# ---------- SANITIZERS ------------#
# This method checks if we can add a correct letter w/ placement
    def check_cor_placement(self, num, let):
        # ensure we are in contains
        if  let in self.wrong:
            return False
        # ensure we are not in the wrong placement
        if let in self.wrong_placement.keys():
            my_ls = self.wrong_placement[let]
            if num in my_ls:
                return False
        
        return True

    def check_contain(self,letter):
        #ensure we are not in wrong
        if letter in self.wrong:
            return False
        return True

    def check_wrong_letter(self, letter):

        #ensure we are not in contain
        if letter in self.contain:
            return False
        return True

    def check_wrong_placement(self, letter, pos):
        #ensure we not in wrong 
        if letter in self.wrong:
            return False
        if pos in self.cor_placement.keys():
            if self.cor_placement[pos] == letter:
                return False

        # ensure we are not in correct letter
        return True

    

#----------End of Sanitizers --------