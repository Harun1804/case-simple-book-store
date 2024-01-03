def formatArray(lists, transform):
  array = []
  for list in lists:
    array.append(transform(list))
  
  return array