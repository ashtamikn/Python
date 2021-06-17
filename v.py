import csv
file_to_otput=open('to_save_file.csv',mode='w',newline='')
csv_writer=csv.writer(file_to_otput,delimiter=',')
csv_writer=csv.writer(file_to_otput,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_otput.close()
f=open('to_save_file.csv',mode='a',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()
