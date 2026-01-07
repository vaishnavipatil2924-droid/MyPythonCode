# List of top 4 IPL teams in 2025 
PBSK=[
        "Shreyas Iyer (Captain)",
        "Priyansh Arya",
        "Pyla Avinash",
        "Xavier Bartlett",
        "Harpreet Brar",
        "Yuzvendra Chahal",
        "Praveen Dubey",
        "Lockie Ferguson",
        "Aaron Hardie",
        "Josh Inglis",
        "Marco Jansen"
    ]


RCB= [
  "Rajat Patidar (Captain)",
  "Virat Kohli",
  "Jacob Bethell",
  "Manoj Bhandage",
  "Swastik Chikara",
  "Rasikh Salam Dar",
  "Tim David",
  "Yash Dayal",
  "Josh Hazlewood",
  "Bhuvneshwar Kumar",
  "Liam Livingstone"
]


GT= [
        "Shubman Gill (Captain)",
        "Gurnoor Brar",
        "Jos Buttler",
        "Gerald Coetzee",
        "Karim Janat",
        "Arshad Khan",
        "Rashid Khan",
        "Shahrukh Khan",
        "Kulwant Khejroliya",
        "Sai Kishore",
        "Prasidh Krishna"
    ]


MI=[
    "Hardik Pandya (Captain)",
    "Rohit sharma",
    "Raj Bawa",
    "Trent Boult",
    "Jasprit Bumrah",
    "Deepak Chahar",
    "Naman Dhir",
    "Mujeeb Ur Rahman",
    "Will Jacks",
    "Bevon Jacobs",
    "Ashwani Kumar",
    "Robin Minz"
    ]

SuperFours=[PBSK,GT,MI,RCB]
# for team in SuperFours:
    # print(team)

#Iterate IPL superfours list using range data type to dispay mi team players .
for team in SuperFours[2]:
    print(team)  

# print name Rohit sharma from mi team 
for team in SuperFours[2][1]:
    print(team) 

for player in SuperFours[3][1][0:6]:
    print(player)      #  V i r a t

# Iterate a tupke using range and create two lists
# even and odd index
t=(1,2,3,4,5,6,7,8,9)

list1=[]
list2=[]

for index in range(len(t)):
    if index %2==0:
        list1.append(t[index])
    else :
        list2.append(t[index])

print("List 1 :",list1)
print("List 2 :",list2)

# first half-> one list and second half ->another list

t = (1, 2, 3, 4, 5, 6)

mid = len(t) // 2  
list1 = []
list2 = []

for i in range(len(t)):
    if i < mid:
        list1.append(t[i])
    else:
        list2.append(t[i])

print("List 1:", list1) #List 1: [1, 2, 3]
print("List 2:", list2) #List 2: [4, 5, 6]