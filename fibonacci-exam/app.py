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
  amount = 100
  mem = ['' for _ in range(amount)]
  file_name = "./correct.txt"
  # file_name = "./wrong.txt"

  fib_list = [fib(i, mem) for i in range(amount)]

  with open(file_name) as f:
    line = f.readline().strip().split(", ")
    seq = [int(i) for i in line]

  for i in range(0, len(seq), 2):
    for j in range(0, len(fib_list), 2):
      if seq[i] == fib_list[j]:
        try:
          if seq[i+1] != fib_list[j+1]:
            return print("No")
        except:
          return print("Yes")
  return print("No")

if __name__ == "__main__":
  main()
