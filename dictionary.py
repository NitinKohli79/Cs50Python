
english_french = {'paper':'papier', 'pen':'stylo', 'car':'voiture', 'table':'table','door':'porte'}
french_spanish = {'papier':'papel', 'stylo':'pluma', 'voiture':'coche', 'table':'mesa', 'porte':'puerta'}



#print(french_spanish[english_french ['pen']])

#len
#del
#copy
#print(f"Translation Available {'money' in english_french}" )

for word in english_french:
    print(
        f"English :{word} : French : {english_french[word]}  Spanish : {french_spanish[english_french[word]]}"
        
        )
    
    
   # print (f"English : {word} *  French : {english_french[word]}"
