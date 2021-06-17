f=open('fileone.txt','w+')
>>> f.write('one file')
8
>>> f.close()
>>> f=open('filetwo.txt','w+')
>>> f.write('two file')
8
>>> f.close()
>>> import zipfile
>>> comp_file=zipfile.ZipFile('comp_file.zip','w')
>>> comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
>>> comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
>>> comp_file.close()
>>> zip_obj=zipfile.ZipFile('comp_file.zip','r')
>>> zip_obj.extractall('extracted_content')
>>> import shutil
>>> dir_to_zip=/home/akarsh/MYPackage
  File "<stdin>", line 1
    dir_to_zip=/home/akarsh/MYPackage
               ^
SyntaxError: invalid syntax
>>> dir_to_zip='/home/akarsh/MYPackage'
>>> output_filename='example'  
>>> shutil.make_archive(output_filename,'zip',dir_to_zip)
'/home/akarsh/MYPackage/example.zip'
>>> shutil.unpack_archive('example.zip','file_unzip','zip')#extract
>>> 

