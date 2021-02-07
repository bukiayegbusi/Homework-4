import matplotlib as matplotlib
import pandas as pd

family = {"Members": ["Aaron", "Nathan", "Mummy", "Daddy"],
          "Age": [11, 7, 40, 45]}
myframe = pd.DataFrame (family)
print(myframe)

myframe.index = ["FS","SS","MM","FF"]
print(myframe)

frame = pd.DataFrame([[2.22, 5.66], [80.10, 34.45], [2.30, 3.45]],
                     index =["Copper", "Iron", "Zinc"],
                     columns = ["Density g/cm3", "Melting point BC"])
print(frame)
print(frame.loc["Iron"])


#How many rows and columns are there in your file?
dst = pd.read_csv("/Users/bukiaiyegbusi/Desktop/Women In Data/Homework/Homework 4/dst.csv")
print(dst)

#Print row 3-8 ( using iloc/loc)
print(dst.iloc[3:9])

#Find the mean number of all-inclusive hotels across all destinations.
mean = dst["NAIH"].mean()
print(mean)

#Find the lowest scoring destination.
lowest_dst = dst["FS"].min()
print(lowest_dst)

#Find the highest scoring destination
highest_dst = dst["FS"].max()
print(highest_dst)

#Find all the destinations where there are more than 9 all-inclusive hotels.
my_filter = dst["NAIH"] > 9
filt_AIH = dst[my_filter]
print(filt_AIH)

#Filter the data by destination and score above 8.
dest_score = dst["FS"] > 8
filt_dst = dst[dest_score]
print(filt_dst)

#Filter the data by destination and score below 2
# ( I need to know if these destinations should be removed or there is a problem)
dest_score = dst["FS"] < 2
filt_dst = dst[dest_score]
print(filt_dst)

#Is there a correlation between number of all-inclusive hotels and score?
import matplotlib.pyplot as plt
dst.plot(x="NAIH", y="FS", kind="scatter")
plt.show()

#Create a data visualisation diagram to show destination and highest scores?
dst.plot(x="Destination", y="FS")
plt.show()

