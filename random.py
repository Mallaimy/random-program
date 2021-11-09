import random
ma_list =["abakar","oumar","nassir","idriss","clotilde","hissen","djalabi","mariam","sonia","yves","korom","grene","kevin"]
#this list will contain our random list
random_list = None
groupe = 0
#for each element in ma_list, we randome and put into our variable
for i in ma_list:
    random_list = random.sample(ma_list, 2)
    #then we remove data already randomize in our list, but the complexity is high for this little program
    for element in random_list:
        ma_list.remove(element)
    print("===Goupe N°:",groupe,"===")
    #and we finally print our randomized list 
    print(random_list)
    groupe += 1