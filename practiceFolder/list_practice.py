letters = ['a','b','c','d','f']
print(letters[0])
bicycles = ['trek','canon','redline','specialized']
print(bicycles[-1].title())
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('toyata')
motorcycles.insert(0,'ducati')
print(motorcycles[0].title())
first_motorcycle = motorcycles[0]
print(motorcycles)
print(f"My first bike is {first_motorcycle.title()}.")
