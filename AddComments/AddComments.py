import re
# input file
name = ["/translate_utils.c", "/translate.c", "/assembler.c", "/tables.c"]
a = name[3]
file = open("/home/st/p1.1_fubzh_ouyangkzh/part1"+a, mode='r', encoding='utf-8')
# output file
nfile = open("/home/st/Code/Python/submit"+a, mode='w')
p = file.readline()
search_comment_end = 0
while p:
    # set a flag that indicates whether the code is matched
    flag = 0
    if search_comment_end:
        match = re.search('(\*/)+', p)
    if search_comment_end and not match:
        nfile.write(p)
        p = file.readline()
        continue
    if search_comment_end and match:
        search_comment_end = 0
        nfile.write(p)
        p = file.readline()
        continue

    # The line already has had a comment
    match = re.search('(/\*)+', p)
    if match:
        flag = 1
        nfile.write(p)
        search_comment_end = 1
    match = re.search('(\*/)+', p)
    if match:
        search_comment_end = 0

    # 'if/else if' condition
    match = re.search('if', p)
    if match and not flag:
        nfile.write(p.strip('\n') + '  /* It judges the condition. */\n')
        flag = 1
    # 'while/for' loop
    match = re.search('while', p)
    if match and not flag:
        nfile.write(p.strip('\n') + '  /* It executes a "while" loop */\n')
        flag = 1
    match = re.search('for', p)
    if match and not flag:
        nfile.write(p.strip('\n') + '  /* It executes a "for" loop */\n')
        flag = 1
    # assigning value
    match = re.search('^ *([^ ]+) *= *([^ ]+) *;', p)
    if match and not flag:
        nfile.write(p.strip('\n') + f'  /* The value of {match.groups()[0]} is updated by {match.groups()[1]} */\n ')
        flag = 1
    # include .h file
    match = re.search('(include)+', p)
    if match and not flag:
        nfile.write(p.strip('\n') + '  /* include a header */\n')
        flag = 1
    # return value
    match = re.search('(return)+ *([^ ^;]+) *;', p)
    if match and not flag:
        nfile.write(p.strip('\n') + f'  /* The function returns {match.groups()[1]} */\n')
        flag = 1
    # does not match
    if not flag:
        # nfile.write(p.strip('\n') + f'  /* It is implemented on Mar 13th. */\n')
        nfile.write(p)
    p = file.readline()
print("Finished")
file.close()