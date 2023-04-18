start_list=["1","2","3","4"]
new_list=[]
output_list=["0"]

for x in start_list:
    new_list.append(x)
    m=start_list.index(x)+1
    for y in start_list[m:]:
        result= x+y
        new_list.append(result)


for x in new_list:
    output_list.append(x)
    if len(x)>=2:
        index=x[-1]
        m=start_list.index(index)+1
        for y in start_list[m:]:
            result= x+y
            output_list.append(result)

def all_button():
    result=""
    for x in start_list:
        result=result+x
output_list.append(result)
print(f"Number of probabilities:",len(output_list))
print(f"probability:",output_list)
