users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for role,roster in users.items():
    print role
    for idx, person in enumerate(roster):
        full = str(idx+1) + " - "
        justName = ''
        for name in person.values():
            justName += name + ' '
        full += justName.upper()
        full += " - " + str(len(justName)-1)
        print (full)
