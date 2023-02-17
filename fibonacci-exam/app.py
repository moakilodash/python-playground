def fib(num, mem):
  if mem[num] != '':
    return mem[num]
  if num < 2:
    result = 1
  else:
    result = fib(num - 1, mem) + fib(num - 2, mem)
  mem[num] = result
  return result

def main():
  amount = 5
  mem = ['' for _ in range(amount)]
  file_name = "./correct.txt"
  # file_name = "./wrong.txt"

  fib_list = [fib(i, mem) for i in range(amount)]

  with open(file_name) as f:
    line = f.readline().strip().split(", ")
    seq = [int(i) for i in line]
    

  index = list()
  for j in seq:
    for index_fib, n in enumerate(fib_list):
      if n == j:
        index.append(index_fib)
        break


  if index == list(range(index[0], index[-1] + 1)):
    print("True")
    return 0
  
  print("False")

if __name__ == "__main__":
  main()