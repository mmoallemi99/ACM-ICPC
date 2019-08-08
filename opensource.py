# https://open.kattis.com/problems/opensource

projects_dict = {}
all_students = set()
current_project = ''

line = input()

while line is not '0':

    if line == '1':
        projects_dict = sorted(projects_dict.items(), key=lambda x: (len(x[1]), len(x[0])), reverse=True)
        new_dict = {}
        for project_name, students in projects_dict:
            num = len(students)
            if num in new_dict.keys():
                new_dict[num].add(project_name)
            else:
                new_dict[num] = set()
                new_dict[num].add(project_name)

        for count, projects in new_dict.items():
            items = sorted(projects)
            for item in items:
                print(item, count)

        projects_dict = {}
        all_students = set()
        current_project = ''
    elif line.isupper():
        projects_dict[line] = set()
        current_project = line
    elif line.islower():
        if line not in projects_dict[current_project]:
            if line in all_students:
                for project_name in projects_dict.keys():
                    if line in projects_dict[project_name]:
                        projects_dict[project_name].remove(line)
            else:
                all_students.add(line)
                projects_dict[current_project].add(line)

    line = input()
