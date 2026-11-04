import matplotlib.pyplot as plt

fig,ax=plt.subplots()

fruits=["apples","blueberry","cherry","orange"]
count=[40,65,24,77]
bar_labels=["red","blue","_red","ornage"]
bar_color=["tab:red","tab:blue","tab:red","tab:orange"]

ax.bar(fruits,count,label=bar_labels,color=bar_color)

ax.set_ylabel('fruit supply')
ax.set_title('fruit supply by kind and color')
ax.legend(title='fruit color')

plt.savefig("bars.png",bbox_inches="tight")

cat=["bored","happy","happy","bored","happy"]
dog=["happy","bored","bored","happy","bored"]
activities=["combing","drinking","feeding","napping","playing"]

fig,ax=plt.subplot()
ax.plot(activities,dog,label="dog")
ax.plot(activities,cat,label="cat")

ax.legend()
plt.savefig('lines.png',bbox_inches="tight")
