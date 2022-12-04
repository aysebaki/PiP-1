def create_train_test_splits(data: list, train_size: float)-> tuple:
   train_split = list()
   test_split = list()
   train_size = int(len(data)*train_size)

   for x in range(len(data)):
       if x < train_size:
           train_split.append(data[x])
       else:
           test_split.append(data[x])
   return (train_split, test_split)

print(create_train_test_splits([],0.5))
print(create_train_test_splits(list(range(10)), 0.5))
print(create_train_test_splits(list(range(10)), 0.67))