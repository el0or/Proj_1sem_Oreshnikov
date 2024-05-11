#Даны имена девочек. Определить, какие из этих имен встречаются во всех группах
#какие есть только в некоторых группах и какие не встречаются ни в одной из групп

girls_names = ["Анна", "Мария", "Екатерина", "Алина", "Ольга", "Дарья", "Анастасия"]

group_1 = ["Анна", "Алина", "Мария"]
group_2 = ["Мария", "Екатерина", "Дарья"]
group_3 = ["Анна", "Ольга", "Мария"]

in_all_groups = set(group_1) & set(group_2) & set(group_3)  # имена, встречающиеся во всех группах
in_some_groups = set(girls_names) - set(in_all_groups)  # имена, встречающиеся только в некоторых группах
not_in_any_group = set(girls_names) - (set(group_1) | set(group_2) | set(group_3))  # имена, не встречающиеся вообще

print("Имена, встречающиеся во всех группах:", in_all_groups)
print("Имена, встречающиеся только в некоторых группах:", in_some_groups)
print("Имена, не встречающиеся ни в одной из групп:", not_in_any_group)