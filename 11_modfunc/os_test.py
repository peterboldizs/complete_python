import os


def list_directories(s):
    def dir_list(di):
        nonlocal tab_stop
        files = os.listdir(di)
        for fi in files:
            current_dir = os.path.join(di, fi)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + fi)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + fi)

    tab_stop = 0
    if os.path.exists(s):
        print("*" * 40)
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + "does not exist")


list_directories('.')
list_directories('../10_io')

# the below does the same thing
# listing = os.walk('.')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for f in files:
#         print(f)
