from crud import CRUDCategory

category = CRUDCategory.all()
for category in category:
    print(category.id, category.name)
