# from langchain_community.document_loaders import CSVLoader

# loader = CSVLoader(file_path='Social_Network_Ads.csv')

# docs = loader.load()

# print(len(docs))
# print(docs[3])



from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

DOCS = loader.load()

print("Total Documents:", len(DOCS))


print("\nFirst Document:\n", DOCS[0])

print("\nLast Document:\n", DOCS[-1])