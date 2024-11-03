open_file = open("Contoh_write_text.txt","w")
open_file.write("Ini contoh text yang akan di print")
open_file.close()

open_file = open("Contoh_write_text2.txt","r+")
open_file.write("Ini contoh text yang akan di print_2")
print(open_file.read())
open_file.close()