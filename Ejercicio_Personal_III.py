#remove_chars("juanpy",4)
#remove_chars("pynative",2)

def remove_chars (word,n):
	print("Original String: ",word)
	x = word [n:]
	return x

print("Remove Characters from a String")
print(remove_chars("pynative", 4))
print(remove_chars ("pynative",2))



