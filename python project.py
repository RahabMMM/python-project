def write_to_file(filename, content):
 
  try:
    with open(filename, 'w') as file:
      file.write(content)
      print(f"Successfully wrote to {filename}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Lack of permission to write to '{filename}'.")
  finally:
    
    print("File writing operation completed.")


  try:
    with open(filename, 'r') as file:
      content = file.read()
      print(f"Contents of {filename}:\n{content}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    
    print(f"Error: Lack of permission to read from '{filename}'.")
  finally:
    print("File reading operation completed.")

def append_to_file(filename, content):
 
  try:
    with open(filename, 'a') as file:
      file.write(content)
      print(f"Successfully appended to {filename}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Lack of permission to append to '{filename}'.")
  finally:
    print("File appending operation completed.")


write_to_file("my_file.txt", "Line 1: This is some text.\n")
write_to_file("my_file.txt", "Line 2: You can write numbers too: 42\n")
write_to_file("my_file.txt", "Line 3: And mix them up!\n")

read_from_file("my_file.txt")


append_to_file("my_file.txt", "\nLine 4: This is appended content.\n")
append_to_file("my_file.txt", "Line 5: You can append multiple lines.\n")
append_to_file("my_file.txt", "Line 6: And it gets added to the end.\n")

from django.db import models

class Benefit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

# ...

from django.shortcuts import render

def list_benefits(request):
    benefits = Benefit.objects.all()
    return render(request, 'benefits/list.html', {'benefits': benefits})