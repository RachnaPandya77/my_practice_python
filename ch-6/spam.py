# detect spam

comment = input("Enter Comment: ")

if ("Make a  lot of money" in comment or "buy now" in comment or "click this" in comment):
    print("IT is spam")

else:
    print("Not spam")