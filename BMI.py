
# coding: utf-8

# In[ ]:


name=input("ENTER YOUR NAME: ")
height=int(input("ENTER YOUR HEIGHT: "))
weight=int(input("ENTER YOUR WEIGHT: "))
BMI=weight*10000/(height*height)
print("YOUR BMI IS : ", BMI)
if BMI<25:
    print("MOTU NAHI HAI TUM ", name)
else:
    print("MOTU HAI TUM", name)
    
input("press enter to exit")

