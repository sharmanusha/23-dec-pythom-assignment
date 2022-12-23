Exercise1
l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
odd_index_list = [num for index, num in enumerate(l1) if index % 2]
print(odd_index_list)

even_index_list = [num for index , num in enumerate(l2) if not index % 2]
print("Element at even-index positions from list two")
print(even_index_list)

final_index_list = odd_index_list+even_index_list
print("printing final third list")
print("final_list")

output:
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
printing final third list
final_list
-------------------------------------------------------------

Exercise2
sample_list = [34, 54, 67, 89, 100, 43, 94]

print("Original list" ,sample_list)
element = sample_list.pop(4)
print("List after removing element at index 4", sample_list)

sample_list.insert(2, element)
print("List after adding element at index 2", sample_list)

sample_list.append(element)
print("List after adding element at last", sample_list)

output:
Original list [34, 54, 67, 89, 100, 43, 94]
List after removing element at index 4 [34, 54, 67, 89, 43, 94]
List after adding element at index 2 [34, 54, 100, 67, 89, 43, 94]
List after adding element at last [34, 54, 100, 67, 89, 43, 94, 100]
--------------------------------------------------------------------------

Exercise3
lst = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("list: ",lst)
chunk1 = lst[0:3]
chunk2 = lst[3:6]
chunk3 = lst[6:10]
print("Chunk 1 ",chunk1)
chunk1.reverse()
print("After reversing chunk 1",chunk1)
print ("Chunk 2 ",chunk2) 
chunk2.reverse()
print("After reversing chunk 2",chunk2)
print ("Chunk 3 ",chunk3)
chunk3.reverse()
print("After reversing chunk 3",chunk3)

output:
list:  [11, 45, 8, 23, 14, 12, 78, 45, 89]
Chunk 1  [11, 45, 8]
After reversing chunk 1 [8, 45, 11]
Chunk 2  [23, 14, 12]
After reversing chunk 2 [12, 14, 23]
Chunk 3  [78, 45, 89]
After reversing chunk 3 [89, 45, 78]
-----------------------------------------------------

4xercise4
# Python code to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count


# Driver Code
lst = [11,45,8,23,45,23,45,89]
x = 8
print('{} has occurred {} times'.format(x,
										countX(lst, x)))


output:
8 has occurred 1 times
45 has occurred 3 times
11 has occurred 1 times
23 has occurred 2 times
89 has occurred 1 times
-------------------------------------------------

Exercise9
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}
print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)

output:
Dictionary's values -  dict_values([47, 52, 47, 44, 52, 53, 54, 44, 54])
unique list [47, 52, 44, 53, 54]
---------------------------------------------------------------------------------------

Exercise10
sample_list =[87,45,41,65,94,41,99,94]
# Python code to remove duplicate elements
def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
# Driver Code
duplicate = (87,45,41,65,94,41,99)
print(Remove(duplicate))

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))

output:
[87, 45, 41, 65, 94, 99]
tuple  (87, 45, 41, 65, 94, 41, 99, 94)
Minimum number is:  41
Maximum number is:  99
-----------------------------------------------------------

PROBLEMS ON DICTIONARY

Exercise1
test_keys = ['Ten','Twenty','Thirty']
test_values = [10,20,30]

print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

res = {}
for key in test_keys:
	for value in test_values:
		res[key] = value
		test_values.remove(value)
		break

print("Resultant dictionary is : " + str(res))

output:
Original key list is : ['Ten', 'Twenty', 'Thirty']
Original value list is : [10, 20, 30]
Resultant dictionary is : {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
-----------------------------------------------------------------------------

Exercise2
def Merge(dict1, dict2):
	return(dict2.update(dict1))

dict1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
dict2 = {'Thirty':30, 'Fourty':40, 'Fifty':50}

print(Merge(dict1, dict2))

print(dict2)

output:
{'Thirty': 30, 'Fourty': 40, 'Fifty': 50, 'Ten': 10, 'Twenty': 20}
----------------------------------------------------------------------------
Exercise3
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
#now we have to access the "history" element from above dictionary

print(sampleDict['class']['student']['marks']['history'])

output:
80
---------------------------------------------------------------------------------------

