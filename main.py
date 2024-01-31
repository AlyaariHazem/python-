print("""
   1-add item
   2-delete item
   3-sort items
   4-edit item
   """)
def add():
    print("                            add projects")
    name_project=input('enter project name...')
    price_project=input("enter project price ")
    quantities_project=input('enter project quantities')
    print(f"""
                                successful 
name is {name_project}
price is {price_project}
quantities are {quantities_project}
""")

add()