def findDataType(t):
    print("For the input", t, "the type is:", type(t).__name__)


findDataType(t="hello")
findDataType(t=20)
findDataType(t=20.5)
findDataType(t=1j)
findDataType(t=["apple", "banana", "cherry"])
findDataType(t=("apple", "banana", "cherry"))
findDataType(t={"name": "John", "age": 36})
findDataType(t={"apple", "banana", "cherry"})
findDataType(t=True)
findDataType(t=b"hello")
