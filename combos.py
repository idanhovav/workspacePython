def findCombos(steps, lst, options):
  if (steps == 0):
    return [lst]
  if (len(options) == 0 or steps < 0):
    return []
  #biggest = options[0]
  results = []
  for option in options:
    results += findCombos(steps - option, lst + [option], options)
  return results

  #with_biggest = findCombos(steps - biggest, lst + [biggest], options)
  #without_biggest = findCombos(steps, lst, options[1:])
  #return with_biggest +  without_biggest

print(findCombos(3, [], [3,2,1])) 
