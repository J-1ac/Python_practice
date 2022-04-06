#subdir_search.py
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):                            #dir인 경우 재귀
                search(full_filename)
            else:                                                       #file인 경우 확장자 판단
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':                                        #.py인 경우 full_filename 출력
                    print(full_filename)
    except PermissionError:                                             #권한 없는 dir 접근시 pass
        pass

search("D:/")